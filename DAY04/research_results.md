# Day 4 Research Results: Synthesis and Conflict Resolution

**Question (`day04_begin.py`):** Does a four-day work week improve outcomes for employers? Research the evidence on productivity, employee retention and wellbeing, and operating cost, including critiques of the pilots.

Run on 2026-10-29. The container has no `ANTHROPIC_API_KEY`, so the steps were done by hand: search (4 topics), then analysis per topic, then synthesis using `SYNTHESIS_AGENT`'s conflict policy:

1. Prefer claims backed by several independent sources.
2. Prefer newer sources when the facts change over time.
3. Prefer primary sources over secondary reporting.
4. If a conflict can't be resolved, show both positions. Never split the difference.

---

## Overall picture

For knowledge-work employers that **choose** to adopt a four-day week with no pay cut, the evidence for better **wellbeing and retention** is strong and consistent. The evidence for better **productivity** is weaker: it is mostly self-reported and comes from self-selected firms. For **operating cost**, the one well-documented case where coverage is required (Swedish elder care) shows real added cost, and that trial was ended. The policy pays for itself where output can be reorganized. It costs money where someone has to be physically present for every hour.

---

## Conflict log

| # | Conflict | Rule applied | Resolution |
|---|---|---|---|
| 1 | **Productivity:** blog coverage claims "40% productivity gains". The Nature Human Behaviour paper (Fan & Schor, 2025) reports only that workers *said* their ability to do their work improved, and outside economist Pedro Gomes says productivity still needs more analysis | Primary over secondary | **Reject the 40% figure.** It can't be traced to the paper. Productivity gains are *self-reported and unproven* |
| 2 | **How many firms kept the policy (UK 2022 pilot):** sources say 92%, 89%, "nine in ten", and 18 vs 31 made it permanent | Primary over secondary, plus more than one independent source | The best-supported count is **56 of 61 firms continued (≈92%) and 18 made it permanent**. 89% and 31 appear in only one secondary source each. Not averaged |
| 3 | **"Firms kept it, so it works" vs. "the sample was biased":** advocates point to 90%+ retention. Critics (Constangy, Sanders/KCL, Irish Times) point to volunteer firms, no randomized control, attrition (70 signed up, 44–51 supplied data), and researchers who are also advocates | Unresolvable from the evidence: both sides are factually correct | **Both positions stand.** Retention of the policy is a real result for *volunteer* firms. It does not show what would happen at a typical firm |
| 4 | **Gothenburg sick leave:** "10% reduction" vs "half the city average" (15 vs 31 days) | Primary/specific data over vague summary | The **specific figure, 15 vs 31 days**, is preferred. The "10%" claim has no source behind it. These measure different things: change over time vs. comparison with other care homes |
| 5 | **Gothenburg cost:** "+25% staff / +22% gross cost" vs. the trial leader saying the public cost was "half of what we thought" | Unresolvable: different baselines | **Both stand.** The direct cost rose by about 22%. The trial leader's claim counts offsetting savings such as lower sickness absence and unemployment costs. The city ended the trial, which suggests it judged the net cost too high |
| 6 | **Hours actually cut:** "one day off" vs. an average cut from 38 to 34 hours | Specific over headline | Many firms cut **about 4 hours, not 8**. Read the productivity results with that in mind |

---

## Conclusions and confidence

| Conclusion | Confidence | Why |
|---|---|---|
| Wellbeing improves: lower burnout, better sleep, less fatigue | **High** | Peer-reviewed study of about 2,900 workers in 141 orgs across 6 countries, consistent with the UK pilot, and includes a (small) comparison group |
| Retention improves: UK pilot reported 57% fewer staff departures and a 65% drop in sick days | **Medium** | Consistent across sources, but self-selected firms and a short trial window |
| Most volunteer firms keep the policy | **High** for volunteers, **low** for typical firms | Many sources agree, but there is a selection effect |
| Productivity holds or rises | **Low–medium** | Self-reported, no randomized controls, inflated figures in the press |
| Cost is neutral where full coverage is required | **Low** (evidence points the other way) | The one detailed coverage-based trial needed 25% more staff and was ended |

## Gaps

- No randomized controlled trial and no data on firms that dropped out or failed.
- Iceland's public-sector trials were searched for but not found in this run.
- Almost no evidence on hourly, shift or frontline workforces beyond Gothenburg. This matters for venue and event operations, where the Gothenburg result is the relevant one.
- No results beyond about 6–12 months.

## Sources

[Entrepreneur – Nature Human Behaviour coverage](https://www.entrepreneur.com/business-news/four-day-workweek-study-employees-happier-more-productive/495019) · [Euronews](https://www.euronews.com/2025/07/21/four-day-work-weeks-are-good-for-employees-mental-and-overall-health-pilots-in-6-countries) · [Nature supplementary material](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41562-025-02259-6/MediaObjects/41562_2025_2259_MOESM2_ESM.pdf) · [Interview Guys (40% claim)](https://blog.theinterviewguys.com/?p=7364) · [The Week](https://theweek.com/business-news/1021197/large-4-day-workweek-trial-was-so-successful-9-in-10-businesses-say-they) · [Time Doctor](https://www.timedoctor.com/blog/companies-retain-four-day-workweek/) · [Safety+Health](https://safetyandhealthmagazine.com/articles/23625-researchers-say-trial-of-4-day-workweeks-shows-positive-results) · [Business Desk](https://www.thebusinessdesk.com/south-west/?p=1695) · [Silicon Canals](https://siliconcanals.com/m-when-british-firms-trialled-a-four-day-week-for-the-same-pay-the-real-surprise-was-not-output-but-the-people-burnout-fell-for-71-percent-of-staff-and-nearly-nine-in-ten-companies-kept-the-shorter-w/) · [Constangy critique](https://constangy.com/employment-labor-insider/u-k-study-on-four-day-workweek-merits-scrutiny) · [Irish Times – Sanders](https://www.irishtimes.com/business/work/2023/07/28/four-day-week-expert-doesnt-want-everyone-working-that-regime-just-yet) · [What Works Wellbeing](https://whatworkswellbeing.org/blog/findings-from-four-day-work-week-trial/) · [Irish Times – Gothenburg](https://www.irishtimes.com/business/work/if-swedes-can-t-make-six-hour-day-work-who-can-1.2925485) · [McKnight's](https://www.mcknights.com/?p=56457) · [Stylist](https://www.stylist.co.uk/life/careers/sweden-employees-trial-experiment-shorter-days-svartedalens-nurses-gothenburg-benefits-productivity-happiness-health/45626)
