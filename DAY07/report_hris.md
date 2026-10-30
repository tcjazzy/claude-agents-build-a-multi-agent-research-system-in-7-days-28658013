> Day 7 run on 2026-10-30 with the question in `day07_begin.py`. There was no `ANTHROPIC_API_KEY`, so the searches and grading were done by hand. This file was produced by the script's own `run_with_refinement`, `validate_report`, `prune_unused_references` and `render_markdown` functions. Pass 1 was the Day 6 report. The course sample is in `report.md`.
>
> **Refinement log**
> - Pass 1, score 6/10: only Colorado covered for the US. Follow-ups: state requirements, third-party posting liability, Washington litigation.
> - Pass 2, score 7/10: two gaps still searchable. Follow-ups: whether New Jersey's rules are final, and any 2026 Washington cure-period ruling.
> - Pass 3: both rounds used. The report passed validation and was saved without a further grade, as `day07_end.py` is designed. Remaining gaps can't be filled by searching (see Open gap lines).

# Pay Transparency Laws: Wage and Hiring Effects, Compliance Deadlines, Posting Liability, and HRIS Readiness for a Multi-State Hourly Employer

## Executive Summary

Pay transparency laws reliably change what employers post: Colorado's law raised the share of postings with salary data from roughly 35% to 70% or more, while wage effects are modest and disputed (about 1.3% to 3.6% in newer studies, none on realized wages in an earlier paper) and posting volume barely moves. There is no federal mandate; sources count 13 to 17 states plus DC with laws in effect in 2026, with Maine, Virginia and Connecticut changes landing in 2026 and Delaware in 2027. For high-volume hiring, the sharpest risk is litigation over postings: Washington saw more than 100 class actions in a year, its Supreme Court's 2025 Branson ruling held that anyone who applies counts as an applicant, and a five-business-day cure period now applies to postings after July 27, 2025. Liability generally follows the employer through recruiters and staffing firms, with California requiring employers to pass pay scales to third parties and Illinois requiring records of what was sent. In the EU, the 7 June 2026 deadline passed with only a handful of member states transposed and no extension; Workday supports requisition-level pay ranges and pay gap reporting, though those are vendor claims.

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
- There is no federal pay transparency posting mandate; every obligation comes from state or local law. [17, 19]
- Sources count between 13 and 17 states plus DC with pay transparency laws in effect or enacted in 2026, depending on date and definition. [17, 19, 20]
- New state requirements arrive through 2026 and 2027, including Virginia (July 1, 2026), Maine (July 29, 2026), a Connecticut amendment (October 1, 2026) and Delaware (2027). [19]
- For remote roles, the state where the candidate could work drives the obligation more than where the employer is based. [18, 19]
- California requires employers to provide the pay scale to any third party engaged to publish a posting, and the third party must include it. [23]
- Illinois can hold a third party liable for a noncompliant posting unless it shows the employer never supplied the pay and benefits information, and requires employers to keep records of what they sent and when. [24]
- New Jersey's proposed rules make employers liable for a vendor's noncompliant posting where the employer kept or delegated control of the content, but not for postings scraped by job aggregators. [21, 22]
- State and local laws differ on whether job sites and recruiters can be directly liable, and enforcers have pursued third-party job sites in some cases. [25]
- More than 100 class actions were filed under Washington's Equal Pay and Opportunities Act within its first year of posting enforcement. [26, 29]
- In Branson (September 4, 2025), the Washington Supreme Court held that a job applicant is anyone who applies to a posting, rejecting a bona fide intent requirement. [28, 29]
- Washington's SSB 5408, effective July 27, 2025 and not retroactive, gives employers five business days to cure a deficient posting after written notice and requires them to contact third-party sites hosting the posting. [26, 27]
- Statutory damages in Washington can reach $5,000, and commentators flag an open question whether that applies per posting or per applicant. [26, 29]
- New Jersey's pay transparency law took effect June 1, 2025, but its implementing regulations were still proposed, not final, as of the latest sources. [30, 31]
- A New Jersey notice dated October 19, 2026 proposes deleting the 60 percent cap on pay range spreads, with comments due December 18, 2026. [30]
- Under New Jersey's proposed rules, employers remain responsible when they give job details to a third-party site that creates the final posting. [30, 31]
- Branson was a 6-3 decision, and many pending Washington EPOA class actions had been stayed awaiting it. [32, 33]
- Washington's cure provision sunsets on July 27, 2027, and it remains unclear which damages rules apply to postings from January 1, 2023 to July 26, 2025. [32]

## Conflicting Evidence

- Size of the wage effect: 1.3% [3] vs. up to 3.6% [4, 5] vs. no realized-wage effect [2]. Unresolved: the studies use different data and methods, so the figures are reported side by side and not averaged. The newer studies [3, 4] lean toward a small positive effect.
- Effect on job postings: no decrease [1] vs. an 8.2% relative decline [6]. Resolved toward no meaningful decrease: two analyses agree [1], and the dissenting analysis's own author flags a confounder [6].
- Pre-law disclosure baseline: 35% [3] vs. under 10% [3]. Unresolved: the analyses use different posting datasets; both agree disclosure roughly doubled or more.
- Sweden's transposition status: one tracker reports the bill passed with entry into force on 1 July 2026, another reports postponement [9, 10]. Resolved provisionally toward the newer source, pending official Swedish confirmation.
- Number of states with pay transparency laws: 13 plus DC as of May 2026 [17] vs. 16 to 17 plus DC as of August 2026 [19, 20]. Partly resolved: the newer counts reflect laws that took effect mid-2026, but sources also define coverage differently, so a definitive count needs a check against state labor agencies.
- Washington cure period effect on litigation: commentators expect fewer new class actions [27], while pre-amendment postings remain exposed and Branson broadened who can sue [28, 29]. Both positions stand: exposure is falling for new postings but not for older ones.

## Confidence and Limitations

Confidence: high that transparency laws raise posting disclosure; medium that they have little effect on posting volume; low on the size of any wage effect; high on the EU deadline and no-extension position; low on any single EU country's status; low on HRIS capability, since sources are vendor material. Added in refinement: high confidence that employers remain responsible for postings made through recruiters and staffing firms, since several law firms agree; high that Washington is the highest-litigation US jurisdiction; medium on exact state counts and effective dates, since trackers disagree. New Jersey's third-party rules were proposed, not final, in the sources found. Massachusetts and Vermont posting details were not found. Round 2: no Washington decision applying the cure period was found as of October 2026, so how courts will treat cure notices is a live open question rather than a research gap. The October 2026 New Jersey notice comes from a single law-firm source and should be checked in the New Jersey Register.
- Open gap: hourly and seasonal workforce evidence on pay transparency effects (no studies found; inherent limitation)
- Open gap: court treatment of Washington's EPOA cure notices (no decisions yet)
- Open gap: final New Jersey pay transparency regulations (pending; comments close December 18, 2026)

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
17. Navigating 2026 Pay Transparency Laws and Employer Obligations (Jackson Lewis) (2026) - https://www.jacksonlewis.com/publication/navigating-2026-pay-transparency-laws-and-employer-obligations
18. Midyear Pay Transparency Update: Job Postings Lead Employer Responsibilities (Jackson Lewis) (2026) - https://www.jacksonlewis.com/insights/midyear-pay-transparency-update-job-postings-lead-employer-responsibilities
19. Pay Transparency Laws by State: Salary Range Posting Rules (Clockspot) (2026) - https://www.clockspot.com/articles/pay-transparency-laws-by-state
20. Several States Enact Pay Transparency Laws: What Employers Need to Know in 2026 (Hunton) (2026) - https://www.hunton.com/hunton-retail-law-resource/several-states-enact-pay-transparency-laws-what-employers-need-to-know-in-2026
21. Proposed Rules Clarify New Jersey's Pay Transparency Law (Saul Ewing) (2025) - https://www.saul.com/insights/blog/proposed-rules-new-jerseys-pay-transparency-law
22. New Jersey Proposes Rules to Clarify Far-Reaching Pay Transparency Law (Fisher Phillips via JD Supra) (2025) - https://www.jdsupra.com/legalnews/new-jersey-proposes-rules-to-clarify-9052180/
23. California Joins National Trend in Enacting Pay Transparency Laws (Winston & Strawn) - https://www.winston.com/print/v2/content/1053410/california-joins-national-trend-in-enacting-pay-transparency-laws.pdf
24. New Illinois Pay Transparency Rules: Compliance Blueprint for Employers (Fisher Phillips) - https://www.fisherphillips.com/print/v2/content/37417/new-illinois-pay-transparency-rules-compliance-blueprint-for-employers.pdf
25. Career Websites Face Emerging Role as Salary Transparency Cops (Bloomberg Law) - https://news.bloomberglaw.com/daily-labor-report/career-websites-face-emerging-role-as-salary-transparency-cops
26. Washington State Amends Equal Pay Law to Clarify Employer Requirements and Liability (Perkins Coie) (2025) - https://perkinscoie.com/insights/update/washington-state-amends-equal-pay-law-clarify-employer-requirements-and-liability
27. Washington Amends EPOA, Bringing More Balance to Employer Job Posting Obligations (Seyfarth) (2025) - https://www.seyfarth.com/news-insights/washington-amends-epoa-bringing-more-balance-to-employer-job-posting-obligations.html
28. Wash. Ruling Raises Pay Transparency Litigation Risk (Hunton, Law360) (2025) - https://www.hunton.com/insights/publications/wash-ruling-raises-pay-transparency-litigation-risk
29. Washington State Pay Transparency Class Actions: A Wild Ride (IADC Defense Counsel Journal) - https://www.iadclaw.org/defensecounseljournal/washington-state-pay-transparency-class-actions-a-wild-ride/
30. New Jersey pay transparency regulatory update (Ogletree Deakins) (2026-10) - https://ogletree.com/?p=94163
31. New Jersey Pay Transparency Regulations on the Way (National Law Review) (2025) - https://natlawreview.com/article/new-jersey-pay-transparency-regulations-way
32. Washington Supreme Court Clarifies Job Applicant Under EPOA, but July 27, 2025 Amendments Help Employers (Freeman Mathis & Gary) (2025) - https://www.fmglaw.com/insurance-4/washington-supreme-court-clarifies-job-applicant-under-epoa-but-july-27-2025-amendments-to-epoa-help-employers/
33. Washington Supreme Court Holds There Is No Good Faith Requirement for Job Applicants (Buchalter) (2025-09-12) - https://www.buchalter.com/insights/washington-supreme-court-holds-there-is-no-good-faith-requirement-for-job-applicants-who-bring-pay-transparency-claims/