> Day 6 run on 2026-10-29 with the question in `day06_begin.py`. There was no `ANTHROPIC_API_KEY`, so the research was done by hand and this file was produced by the script's own `validate_report`, `prune_unused_references`, `render_markdown` and `run_with_retries` functions. The course sample is in `report.md`.

# Pay Transparency Laws: Wage and Hiring Effects, Compliance Deadlines, and HRIS Readiness for a Multi-State Hourly Employer

## Executive Summary

Pay transparency laws reliably change what employers post: Colorado's law raised the share of postings with salary data from roughly 35% to 70% or more, though about 1 in 5 Colorado postings are still estimated to be noncompliant. Wage effects are positive but modest and disputed: newer studies find pay about 1.3% higher, and up to 3.6% higher, while an earlier paper found posted wages rose about 5% with no change in realized wages, and a 2023 Econometrica study found transparency weakens individual bargaining power. Most studies find no meaningful drop in job postings. In the EU, the Pay Transparency Directive's 7 June 2026 deadline passed with only a handful of member states fully transposed and no extension, so obligations are arriving country by country. Workday supports location-specific pay ranges on requisitions and pay gap reporting natively, with third-party tools available, but these are vendor claims; for an employer posting thousands of hourly and seasonal requisitions, the operational risk is posting compliance at volume, not analytics.

## Findings

- Colorado's pay transparency law sharply increased salary disclosure in job postings, from roughly 35% to 70% in the following year by one NBER-cited estimate, and from under 10% to over 60% by another. [1, 3]
- Compliance remains incomplete: recent analyses estimate about 1 in 5 Colorado job postings are still noncompliant. [3]
- A November 2025 study found worker pay rose about 1.3% more in Colorado than in comparison states after the law. [3]
- A 2025 UC San Diego and USC study is reported to find wage increases of up to 3.6%. [4, 5]
- Earlier research found posted wages rose about 5% with no detectable effect on realized wages. [2]
- Employers did not respond by posting wider salary ranges. [1]
- Most studies find no decrease in the number of job postings, though an Indeed-based analysis reported an 8.2% relative decline versus Utah in the first year, which its author attributed partly to the broader hiring boom. [1, 6]
- A 2023 Econometrica study found transparency policies weaken individual workers' bargaining power, because raising one worker's pay can trigger costly renegotiations with others. [4]
- The EU Pay Transparency Directive's transposition deadline was 7 June 2026, and the Commission confirmed it would not grant postponements. [7, 8]
- Only a small group of member states, including Italy, Lithuania, Malta and Slovakia, had fully transposed the Directive by the deadline; others such as Poland and Estonia are partially transposed. [8, 9]
- The Netherlands and Denmark announced they would miss the deadline and target 1 January 2027, and Ireland's bill omits pay gap reporting. [9, 10]
- First pay gap reports are tiered by employer size, for example 7 June 2027 for Italian employers with 150 or more employees and 7 June 2031 for those with 100 to 149. [11]
- Workday states that its Pay Equity Hub provides pre-built unadjusted pay gap and joint pay assessment reports and supports location-specific pay ranges on job requisitions and adverts. [12, 13]
- Third-party pay equity platforms such as Trusaic PayParity and Deloitte's Pay Equity Platform offer two-way integrations with Workday. [14, 15]
- Practitioner checklists recommend reviewing salary ranges at least annually, auditing every posting channel for pay information, and documenting how ranges were set. [16]

## Conflicting Evidence

- Size of the wage effect: 1.3% [3] vs. up to 3.6% [4, 5] vs. no realized-wage effect [2]. Unresolved: the studies use different data and methods, so the figures are reported side by side and not averaged. The newer studies [3, 4] lean toward a small positive effect.
- Effect on job postings: no decrease [1] vs. an 8.2% relative decline [6]. Resolved toward no meaningful decrease: two analyses agree [1], and the dissenting analysis's own author flags a confounder [6].
- Pre-law disclosure baseline: 35% [3] vs. under 10% [3]. Unresolved: the analyses use different posting datasets; both agree disclosure roughly doubled or more.
- Sweden's transposition status: one tracker reports the bill passed with entry into force on 1 July 2026, another reports postponement [9, 10]. Resolved provisionally toward the newer source, pending official Swedish confirmation.

## Confidence and Limitations

Confidence: high that transparency laws raise posting disclosure; medium that they have little effect on posting volume; low on the size of any wage effect, since most of the evidence comes from working papers; high on the EU deadline and the no-extension position; low on any single country's status, since trackers disagree; low on HRIS capability, since the sources are vendor material. Gaps: no evidence specific to hourly, seasonal or event workforces; US state requirements beyond Colorado (for example California, New York, Washington, Illinois) were not researched in this run; no independent readiness survey of HRIS pay-transparency capability was found; and no source covers posting compliance through third-party job boards and staffing agencies, which matters for high-volume event hiring.

## References

1. Arnold, Quach and Taska: The Impact of Pay Transparency in Job Postings (ASU W. P. Carey working paper) (2023) - https://wpcarey.asu.edu/sites/default/files/2023-08/Arnold.pdf
2. Feng: pay transparency and posted vs. realized wages (IZA conference paper) (2023) - https://conference.iza.org/DATA_2023/feng_k34013.pdf
3. Colorado pay transparency study (Colorado Newsline) (2025-11-21) - https://coloradonewsline.com/2025/11/21/colorado-pay-transparency-study/
4. How Colorado Sparked a Global Push for Salary Transparency (Insurance Journal) (2026-01-14) - https://www.insurancejournal.com/news/west/2026/01/14/853971.htm
5. Colorado May Have Sparked a Push for Salary Transparency (CPA Practice Advisor) (2026-01-19) - https://www.cpapracticeadvisor.com/2026/01/19/colorado-may-have-sparked-a-push-for-salary-transparency/176542/
6. How Colorado's pay transparency law is impacting work in the state (CNBC) (2022-08-04) - https://www.cnbc.com/2022/08/04/how-colorados-pay-transparency-law-is-impacting-work-in-the-state.html
7. EU Pay Transparency Directive 2026: Employer Compliance (Lewis Silkin) (2026-07-01) - https://www.lewissilkin.com/insights/2026/07/01/eu-pay-transparency-directive-2026-employer-compliance
8. Just four Member States have transposed the Pay Transparency Directive (WageIndicator) (2026-06-30) - https://wageindicator.org/ai/work/collective-bargaining-agreement/updates/2026/eu-sources-just-four-member-states-have-transposed-the-pay-transparency-directive-june-30-2026/
9. Pay Transparency Directive country tracker (Assessio) (2026-06) - https://assessio.com/articles/pay-transparency-directive-country-tracker/
10. EU Pay Transparency Directive: Who Transposed, Who Delayed, the Risks (Trusaic) (2026) - https://trusaic.com/blog/eu-pay-transparency-directive-who-transposed-who-delayed-the-risks/
11. EU Pay Transparency Directive Deadlines 2026-2031: Timeline and Compliance Checklist (Mirro) (2026) - https://mirro.io/eu-pay-transparency/timeline-checklist/
12. Pay Transparency (Workday product page) - https://www.workday.com/en-us/products/human-resource-management/pay-transparency.html
13. Empower Your Pay Transparency Journey (Workday datasheet) - https://www.workday.com/content/dam/web/uk/documents/datasheets/empower-your-pay-transparency-journey-ds-engb.pdf
14. Trusaic Launches PayParity Available on Workday Marketplace (Trusaic) - https://trusaic.com/press-center/trusaic-launches-payparityavailable-on-workday-marketplace/
15. Pay Equity Platform (Deloitte) - https://www.deloitte.com/be/en/services/tax/services/pay-equity-platform.html
16. Pay Transparency Compliance Checklist (Hyring) - https://hyring.com/free-hr-toolkit/checklists/pay-transparency-compliance-checklist