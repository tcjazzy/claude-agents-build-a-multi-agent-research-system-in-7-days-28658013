import asyncio
import json
from claude_agent_sdk import (
    query,
    ClaudeAgentOptions,
    AgentDefinition,
    AssistantMessage,
    ToolUseBlock,
    ResultMessage,
    HookMatcher,
)

REPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "executive_summary": {"type": "string"},
        "findings": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "citations": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["claim", "citations"],
            },
        },
        "conflicts": {"type": "array", "items": {"type": "string"}},
        "limitations": {"type": "string"},
        "open_gaps": {"type": "array", "items": {"type": "string"}},
        "references": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "date": {"type": "string"},
                },
                "required": ["id", "title", "url"],
            },
        },
    },
    "required": ["title", "executive_summary", "findings", "references"],
}

SEARCH_AGENT = AgentDefinition(
    description=(
        "Searches the web for credible sources on one specific topic. "
        "Use whenever a task requires finding new information."
    ),
    prompt="""You are a research search agent.
Search the web for the topic you are given.
Find five to seven distinct, credible sources.
For each source report the title, URL, publication date if available,
and a two-sentence summary.
Do not analyze or draw conclusions. Just search and report.
If you cannot search, report that you could not search and stop.
Do not attempt workarounds.""",
    tools=["WebSearch"],
    maxTurns=10,
)

ANALYSIS_AGENT = AgentDefinition(
    description=(
        "Analyzes ONE set of sources on ONE topic and extracts key "
        "findings. Use once per search result set. Cannot search the web."
    ),
    prompt="""You are a research analysis agent.
You receive sources found by a search agent on a single topic.
Extract the key findings:
- The main claims, each tagged with the title AND URL of every
  source that supports it
- Points where sources disagree, with each position attributed
  by title and URL
- Gaps the sources do not cover
Be complete but compact: every claim, disagreement, and gap
survives, but no filler prose. Your output accumulates in the
coordinator's context and travels to the synthesis agent
alongside every other analysis.
Never mention a claim without its source URLs.
Do not resolve disagreements. Do not search the web.""",
    tools=[],
    maxTurns=5,
)

SYNTHESIS_AGENT = AgentDefinition(
    description=(
        "Combines multiple analyses into one unified picture and "
        "resolves conflicts between them. Use exactly once per research "
        "pass, after all analyses are complete. Cannot search the web."
    ),
    prompt="""You are a research synthesis agent.
You receive analyses of several topics, each containing claims,
disagreements, and gaps, all with source URLs attached. You may
also receive findings from an earlier research report to merge in.
Produce one unified synthesis:

1. State the overall picture that emerges across all analyses.
2. For every conflict between sources, resolve it explicitly:
   - Prefer claims corroborated by multiple independent sources.
   - Prefer more recent sources when facts change over time.
   - Prefer primary sources over secondary reporting.
   - If the conflict cannot be resolved, say so and present
     both positions with their support. Never split the
     difference or average competing numbers.
3. Attach a confidence level (high, medium, low) to each major
   conclusion, with one line explaining why.
4. Carry forward every unresolved gap. Do not let gaps disappear.

Preserve the source URLs on every claim and conclusion.
Work only from the analyses and prior findings you are given.""",
    tools=[],
    maxTurns=5,
)

REPORT_AGENT = AgentDefinition(
    description=(
        "Turns a completed synthesis into a structured, cited research "
        "report. Use exactly once per research pass, as the final step. "
        "Cannot search."
    ),
    prompt="""You are a research report agent.
You receive a synthesis containing conclusions, confidence levels,
conflicts, gaps, and source URLs. Produce a report with these parts:

- title
- executive_summary: three to five sentences, the answer up front
- findings: a list of claims, each with the numeric ids of the
  references that support it
- conflicts: each conflict from the synthesis, including any left
  unresolved, described with its citations
- limitations: confidence levels and the gaps the research did
  not cover
- open_gaps: each gap from the synthesis as a short, searchable
  phrase
- references: a numbered list, each with id, title, url, and
  publication date if known

Citation rules, non-negotiable:
- Cite only sources present in the synthesis you received.
  Never add a source from your own knowledge.
- Every finding carries at least one reference id.
- If a claim in the synthesis has no source URL, exclude it or
  describe it in limitations as unsourced.

Do not search the web. Do not invent, infer, or complete URLs.""",
    tools=[],
    maxTurns=5,
)

COORDINATOR_PROMPT = """You are a research coordinator managing a team
of specialist agents.

When you receive a research request:
1. Break it into focused subtasks.
2. Delegate each search subtask to search-agent, one topic per
   delegation. Use at most three search delegations; prefer two.
   Fold smaller angles into the closest search rather than adding
   delegations.
3. Delegate each result set to analysis-agent, one analysis per topic.
4. Delegate ALL completed analyses to synthesis-agent in a single
   delegation. Include every analysis in full. If the request includes
   an earlier report to build on, include that report's findings and
   references in the same delegation so the synthesis merges old
   and new.
5. Delegate the complete synthesis to report-agent in a single
   delegation. Include the synthesis in full, with all URLs.
6. Return report-agent's output as your final answer, exactly as
   given. Do not edit, summarize, or reformat it.

Never search, analyze, synthesize, or write the report yourself.
Your job is delegation and assembly. Delegate only to the agents
named in this workflow: search-agent, analysis-agent,
synthesis-agent, report-agent. Never delegate to any other agent
type, including general-purpose."""

EVAL_SCHEMA = {
    "type": "object",
    "properties": {
        "meets_criteria": {"type": "boolean"},
        "score": {"type": "integer"},
        "assessment": {"type": "string"},
        "followup_queries": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["meets_criteria", "score", "assessment", "followup_queries"],
}

EVALUATOR_PROMPT = """You are a research quality evaluator. You receive
a research request and the report produced for it. Judge the report
against four criteria:

1. Coverage: does it answer every part of the request?
2. Source diversity: multiple independent sources per major finding?
3. Recency: are time-sensitive findings backed by current sources?
4. Gaps: which open_gaps could targeted follow-up research fill?

Score the report 1 to 10. Set meets_criteria true only if the score
is 8 or higher AND no fillable gaps remain.

For every fillable gap and coverage hole, write one focused,
searchable follow-up query. Distinguish fillable gaps from inherent
limitations: "no long-term studies exist yet" cannot be searched
away, so do not write a query for it. Limit yourself to the three
highest-value queries. Judge only. Do not rewrite the report."""

# Cap on how much of each WebSearch result enters the agent's context.
# Tune this and measure: too low starves the analysis, too high wastes tokens.
MAX_RESULT_CHARS = 4000


def _truncate_text(text: str) -> tuple[str, bool]:
    if len(text) <= MAX_RESULT_CHARS:
        return text, False
    return text[:MAX_RESULT_CHARS] + "\n[trimmed by hook]", True


async def trim_search_results(input_data, tool_use_id, context):
    """PostToolUse hook: shrink WebSearch output before it enters context.

    Runs at the system level, outside the model's reasoning. The agent
    never sees the untrimmed version, so the tokens are never spent."""
    response = input_data.get("tool_response")
    changed = False

    if isinstance(response, str):
        response, changed = _truncate_text(response)
    elif isinstance(response, dict) and isinstance(response.get("content"), list):
        for block in response["content"]:
            if isinstance(block, dict) and isinstance(block.get("text"), str):
                block["text"], block_changed = _truncate_text(block["text"])
                changed = changed or block_changed

    if not changed:
        return {}

    print("    [hook] trimmed a WebSearch result")
    return {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "updatedToolOutput": response,
        }
    }


def validate_report(report: dict) -> list[str]:
    """Mechanical checks no prompt can guarantee. Returns problems found."""
    problems = []
    ref_ids = {ref["id"] for ref in report.get("references", [])}

    if not report.get("findings"):
        problems.append("Report contains no findings.")

    for finding in report.get("findings", []):
        if not finding["citations"]:
            problems.append(f"Uncited finding: {finding['claim'][:60]}...")
        for cid in finding["citations"]:
            if cid not in ref_ids:
                problems.append(f"Citation [{cid}] has no matching reference.")

    for ref in report.get("references", []):
        if not ref["url"].startswith("http"):
            print(f"[warning] Reference [{ref['id']}] has a malformed URL: {ref['url']}")

    return problems


def prune_unused_references(report: dict) -> dict:
    """Remove references no finding cites. Mechanical cleanup, not a failure."""
    used = {c for f in report.get("findings", []) for c in f["citations"]}
    report["references"] = [
        ref for ref in report.get("references", []) if ref["id"] in used
    ]
    return report


def render_markdown(report: dict) -> str:
    """Turn the validated structure into the report.md deliverable."""
    lines = [f"# {report['title']}", "", "## Executive Summary", ""]
    lines.append(report["executive_summary"])
    lines += ["", "## Findings", ""]
    for finding in report["findings"]:
        cites = ", ".join(str(c) for c in finding["citations"])
        lines.append(f"- {finding['claim']} [{cites}]")
    if report.get("conflicts"):
        lines += ["", "## Conflicting Evidence", ""]
        for conflict in report["conflicts"]:
            lines.append(f"- {conflict}")
    if report.get("limitations") or report.get("open_gaps"):
        lines += ["", "## Confidence and Limitations", ""]
        if report.get("limitations"):
            lines.append(report["limitations"])
        for gap in report.get("open_gaps", []):
            lines.append(f"- Open gap: {gap}")
    lines += ["", "## References", ""]
    for ref in report["references"]:
        date = f" ({ref['date']})" if ref.get("date") else ""
        lines.append(f"{ref['id']}. {ref['title']}{date} - {ref['url']}")
    return "\n".join(lines)


async def run_research(request: str) -> dict | None:
    """One full pipeline pass. Last ResultMessage wins, so subagent
    results pass through."""
    options = ClaudeAgentOptions(
        system_prompt=COORDINATOR_PROMPT,
        agents={
            "search-agent": SEARCH_AGENT,
            "analysis-agent": ANALYSIS_AGENT,
            "synthesis-agent": SYNTHESIS_AGENT,
            "report-agent": REPORT_AGENT,
        },
        allowed_tools=["Agent", "WebSearch"],
        setting_sources=[],
        max_turns=35,
        max_budget_usd=4.00,
        model="claude-sonnet-5",
        fallback_model="claude-haiku-4-5",
        output_format={"type": "json_schema", "schema": REPORT_SCHEMA},
        hooks={
            "PostToolUse": [
                HookMatcher(matcher="WebSearch", hooks=[trim_search_results]),
            ],
        },
    )

    report = None
    async for message in query(prompt=request, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, ToolUseBlock) and block.name in ("Agent", "Task"):
                    agent = block.input.get("subagent_type", "unknown")
                    task = block.input.get("description", "")
                    print(f"--> Delegating to {agent}: {task}")
        elif isinstance(message, ResultMessage):
            print(f"\nRun ended: subtype={message.subtype}, "
                  f"is_error={message.is_error}, turns={message.num_turns}")
            print(f"Estimated cost: ${message.total_cost_usd:.4f}")
            if message.subtype == "success" and not message.is_error:
                report = message.structured_output
    return report


async def evaluate_report(request: str, report: dict) -> dict:
    """Grade the report. Standalone query, separate from the team."""
    options = ClaudeAgentOptions(
        system_prompt=EVALUATOR_PROMPT,
        setting_sources=[],
        max_turns=3,
        max_budget_usd=2.00,
        model="claude-sonnet-5",
        fallback_model="claude-haiku-4-5",
        output_format={"type": "json_schema", "schema": EVAL_SCHEMA},
    )
    prompt = f"Research request:\n{request}\n\nReport produced:\n{json.dumps(report)}"
    evaluation = None
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            evaluation = message.structured_output
    if evaluation is None:
        raise RuntimeError("Evaluator returned no structured output")
    return evaluation


async def run_with_refinement(request: str, max_rounds: int = 2) -> dict | None:
    """Research, grade, refine. Each pass is an independent query;
    the previous report travels forward in the prompt."""
    report = await run_research(request)

    for round_num in range(1, max_rounds + 1):
        if report is None:
            print("No report produced this pass. Stopping.")
            return None

        report = prune_unused_references(report)
        problems = validate_report(report)
        if problems:
            print("Report failed validation. Stopping.")
            for p in problems:
                print(f"  - {p}")
            return None

        evaluation = await evaluate_report(request, report)
        print(f"\n=== Evaluation: score {evaluation['score']}/10 ===")
        print(evaluation["assessment"])

        if evaluation["meets_criteria"] or not evaluation["followup_queries"]:
            print("Report meets criteria.")
            return report

        queries = evaluation["followup_queries"]
        print(f"\n=== Refinement round {round_num}: "
              f"{len(queries)} follow-up queries ===")
        for q in queries:
            print(f"  - {q}")

        refinement_request = (
            "An earlier research pass produced the report below. An "
            "evaluation found gaps. Search ONLY these follow-up topics, "
            "analyze the new results, then synthesize them together with "
            "the earlier report's findings into one updated, complete "
            "report:\n"
            "- " + "\n- ".join(queries) + "\n\n"
            "Earlier report:\n" + json.dumps(report)
        )
        new_report = await run_research(refinement_request)

        # If the refinement pass fails, keep the report we already have.
        if new_report is None:
            print("Refinement pass failed. Keeping the previous report.")
            return report
        report = new_report

    # Rounds exhausted: return the last report if it holds up.
    if report is not None:
        report = prune_unused_references(report)
        if validate_report(report):
            return None
    return report


# --- Sixth agent: HR compliance reviewer -----------------------------------
# Runs after refinement, before anything reaches leadership. It reads the
# finished report the way employment counsel would: it does not add research,
# it flags statements that could mislead a decision-maker or create risk if
# forwarded as-is.

COMPLIANCE_SCHEMA = {
    "type": "object",
    "properties": {
        "approved": {"type": "boolean"},
        "summary": {"type": "string"},
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "severity": {"type": "string", "enum": ["blocker", "advisory"]},
                    "category": {
                        "type": "string",
                        "enum": [
                            "pending_stated_as_final",
                            "missing_effective_date",
                            "legal_advice_tone",
                            "vendor_claim_as_fact",
                            "jurisdiction_overreach",
                            "sensitive_data",
                            "other",
                        ],
                    },
                    "problem": {"type": "string"},
                    "fix": {"type": "string"},
                },
                "required": ["location", "severity", "category", "problem", "fix"],
            },
        },
        "counsel_questions": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["approved", "summary", "issues", "counsel_questions"],
}

COMPLIANCE_PROMPT = """You are an HR compliance reviewer for an HRIS
leadership team at a multi-state employer with large hourly, seasonal
and event-day workforces. You receive a finished research report that
will be forwarded to HR, legal and finance leaders. Review it before
it is shared. Do not add research and do not rewrite the report.

Flag every statement that could mislead a decision-maker:

- pending_stated_as_final: a proposed rule, bill, pending case or
  preliminary ruling described as settled law. Always a blocker.
- missing_effective_date: a legal obligation with no effective date,
  sunset date, or "as of" date. Blocker when a deadline drives action.
- legal_advice_tone: wording that tells the reader what the law
  requires them to do, rather than what sources report. Advisory.
- vendor_claim_as_fact: a Workday, UKG, Oracle or other vendor
  capability stated as fact rather than as the vendor's claim. Advisory.
- jurisdiction_overreach: a rule from one state, city or country
  generalized to others. Blocker.
- sensitive_data: named individuals, employee data, or anything that
  should not circulate. Always a blocker.

For each issue give its location (the finding text, executive
summary, or conflicts), severity, category, the problem in one line,
and a fix in one line. Set approved true only if there are no
blockers. Then list up to five questions the HR team should put to
employment counsel before acting on the report."""

# Deliberately broad: a false flag costs counsel one glance, a missed
# legal claim can reach leadership unverified.
LEGAL_TERMS = (
    "law", "act ", "statute", "regulation", "rule", "court", "ruling",
    "liable", "liability", "class action", "directive", "amendment",
    "require", "propos", "mandate", "obligation", "effective", "transpos",
)


def check_legal_sourcing(report: dict) -> list[str]:
    """Mechanical check no reviewer prompt can guarantee: every legal
    claim needs two independent sources, or an explicit flag for counsel."""
    flags = []
    for finding in report.get("findings", []):
        claim = finding["claim"].lower()
        if any(term in claim for term in LEGAL_TERMS) and len(set(finding["citations"])) < 2:
            flags.append(f"Single-source legal claim: {finding['claim'][:80]}...")
    return flags


async def review_compliance(report: dict) -> dict:
    """Standalone query, like the evaluator: the reviewer is independent
    of the team that wrote the report."""
    options = ClaudeAgentOptions(
        system_prompt=COMPLIANCE_PROMPT,
        setting_sources=[],
        max_turns=3,
        max_budget_usd=1.00,
        model="claude-sonnet-5",
        fallback_model="claude-haiku-4-5",
        output_format={"type": "json_schema", "schema": COMPLIANCE_SCHEMA},
    )
    prompt = f"Report to review:\n{json.dumps(report)}"
    review = None
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, ResultMessage):
            review = message.structured_output
    if review is None:
        raise RuntimeError("Compliance reviewer returned no structured output")
    return review


async def run_with_compliance(request: str, max_revisions: int = 1) -> tuple[dict | None, dict | None]:
    """Refine, then review. Blockers get one revision pass through the
    report team; anything still blocked ships marked as held for counsel."""
    report = await run_with_refinement(request)
    if report is None:
        return None, None

    for revision in range(max_revisions + 1):
        review = await review_compliance(report)
        blockers = [i for i in review["issues"] if i["severity"] == "blocker"]
        print(f"\n=== Compliance review: {len(blockers)} blockers, "
              f"{len(review['issues']) - len(blockers)} advisories ===")
        print(review["summary"])

        if not blockers or revision == max_revisions:
            return report, review

        print(f"\n=== Compliance revision {revision + 1} ===")
        revision_request = (
            "A compliance review flagged the report below. Do not search. "
            "Delegate the report and these issues straight to synthesis-agent "
            "and then report-agent, and return a corrected report that fixes "
            "every blocker without dropping any finding or citation:\n"
            + "\n".join(f"- [{i['category']}] {i['location']}: {i['problem']} Fix: {i['fix']}"
                        for i in blockers)
            + "\n\nReport:\n" + json.dumps(report)
        )
        revised = await run_research(revision_request)
        if revised is not None:
            revised = prune_unused_references(revised)
        if revised is None or validate_report(revised):
            print("Revision failed or broke citations. Keeping the reviewed report.")
            return report, review
        report = revised

    return report, review


def render_compliance(review: dict, sourcing_flags: list[str]) -> str:
    blockers = [i for i in review["issues"] if i["severity"] == "blocker"]
    status = ("Approved for leadership distribution" if review["approved"] and not blockers
              else "HOLD: requires employment counsel review before distribution")
    lines = ["", "## Compliance Review", "", f"**Status:** {status}", "", review["summary"]]
    if review["issues"]:
        lines += ["", "| Severity | Category | Location | Problem | Fix |", "|---|---|---|---|---|"]
        for i in review["issues"]:
            cells = [i["severity"], i["category"], i["location"], i["problem"], i["fix"]]
            lines.append("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
    if sourcing_flags:
        lines += ["", "**Single-source legal claims (verify with counsel):**", ""]
        lines += [f"- {f}" for f in sourcing_flags]
    if review["counsel_questions"]:
        lines += ["", "**Questions for employment counsel:**", ""]
        lines += [f"{n}. {q}" for n, q in enumerate(review["counsel_questions"], 1)]
    return "\n".join(lines)


async def main():
    request = (
        "What does the evidence say about pay transparency laws in the US "
        "and EU: their effect on wages and hiring, where compliance deadlines "
        "stand, and what HRIS capabilities such as Workday need to support "
        "them for a multi-state employer with large hourly and seasonal staff?"
    )
    report, review = await run_with_compliance(request)

    if report is None:
        print("No valid report produced. Nothing saved.")
        return

    sourcing_flags = check_legal_sourcing(report)
    with open("report.md", "w", encoding="utf-8") as f:
        f.write(render_markdown(report) + "\n" + render_compliance(review, sourcing_flags))
    print("\nReport saved to report.md")


if __name__ == "__main__":
    asyncio.run(main())