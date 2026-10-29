# Day 4 Research Results: Synthesis and Conflict Resolution

**Question (`day04_begin.py`):** A sports and entertainment employer runs Workday HCM and staffs stadium events with thousands of hourly and seasonal workers. Should it keep a best-of-breed UKG workforce management (WFM) system integrated with Workday, or consolidate onto Workday Time Tracking and Scheduling? Research hourly and event scheduling capability, predictive scheduling compliance, total cost, and implementation risk.

Run on 2026-10-29. The container has no `ANTHROPIC_API_KEY`, so the steps were done by hand: search (4 topics), then analysis per topic, then synthesis using `SYNTHESIS_AGENT`'s conflict policy:

1. Prefer claims backed by several independent sources.
2. Prefer newer sources when the facts change over time.
3. Prefer primary sources over secondary reporting.
4. If a conflict can't be resolved, show both positions. Never split the difference or average numbers.

---

## Overall picture

For a Workday shop whose hourly and event workforce is large, seasonal and shift-driven, the evidence favors **keeping a specialist WFM system (UKG) integrated with Workday**. Consolidating onto Workday alone looks better when hourly needs are moderate. Workday's advantage is one data model covering HR and finance. UKG's advantage is depth in scheduling, time and labor forecasting. No source gives independent, platform-specific cost or failure data, so the cost argument rests on advisory estimates, not measurements.

---

## Conflict log

| # | Conflict | Rule applied | Resolution |
|---|---|---|---|
| 1 | **WFM capability:** Workday markets one platform with scheduling tied to worker profiles and predictive analytics. Several comparisons (People Managing People, JitBase, TechVendorIndex) rate Workday WFM "adequate" and UKG's "strong", citing its Kronos roots | Several independent sources agree | **UKG is deeper for hourly WFM.** This is corroborated across independent comparisons. Workday's strength is real but sits elsewhere: HR, finance and position data in one model |
| 2 | **Cost:** one Workday-negotiation blog says complex WFM adds **25–40%** to Workday platform cost. A comparison site says UKG's bundled time and attendance is **"materially cheaper"** than Workday plus a separate WFM tool | Unresolvable: no primary pricing, and both claims are secondary | **Both stand. Not averaged.** Each claim comes from a single advisory source. The only reliable answer is quotes for actual headcount, peak event-day volume and pay rules |
| 3 | **Predictive scheduling compliance:** Workday's own admin guides document predictive scheduling calculations and penalties. A third-party vendor (Cloudapper) says Workday calculates the premium but **does not record whether the employee was actually notified in advance** | Primary over secondary, but the primary docs don't address notice tracking | **Partially resolved.** Premium calculation is confirmed by Workday's documentation. The notice-tracking gap is **plausible but unverified**, since it comes from a competitor. It should be tested in a proof of concept with the Fair Workweek rules for each city where events are held |
| 4 | **Implementation failure rates:** 32% over budget and 53% late (PeopleStrong, attributed to Gartner 2024), vs. 55% missing budget, schedule or goals (Clearbridge, attributed to Gartner), vs. 55–75% (HRMS World), vs. >75% for ERP | Primary over secondary; definitions differ | **No figure is citable.** None links to a Gartner document, and each defines "failure" differently (over budget vs. missed goals vs. abandoned). The most specific one, **32% over budget / 53% late**, can be used *as a direction* only, with its definition stated. Never quote "70% fail" |
| 5 | **Event and venue needs:** Humanforce, Shifton and Workforce.com list requirements such as per-zone scheduling, kiosk or GPS clock-ins, separate tracking of vendor and contractor hours, and FLSA blended-rate overtime for staff working several roles. No neutral source says whether Workday or UKG covers them | No independent source | **Kept as requirements, not findings.** These are competitors' marketing claims. They make a useful checklist for a proof of concept, but they are not evidence about either platform |

---

## Conclusions and confidence

| Conclusion | Confidence | Why |
|---|---|---|
| UKG offers deeper hourly scheduling, time and labor forecasting than Workday | **Medium–high** | Several independent comparisons agree; no primary benchmark |
| Workday-only is enough when hourly needs are moderate and a single data model is the priority | **Medium** | The same comparison sources support it |
| The best-of-breed route costs more, or less, than consolidation | **Low** | Conflicting single-source estimates; no published pricing |
| Workday handles predictive scheduling premiums | **High** | Workday's own documentation |
| Workday tracks advance-notice delivery for Fair Workweek | **Low / unverified** | Competitor claim only |
| HCM implementations carry material budget and schedule risk | **Medium** | Many sources agree on the direction; exact rates can't be traced |

## Gaps

- No independent pricing or 3–5 year TCO model for either option.
- No platform-specific (Workday or UKG) implementation outcome data.
- No source covers event-day surge volumes (thousands clocking in within hours) or per-event scheduling and labor costing on either platform.
- The cost of maintaining the Workday–UKG integration (middleware, payroll sync, failure handling) was not quantified.
- Union and collective bargaining rules, common for venue staff, are not covered.

**Recommended next step:** Run a scripted proof of concept on both options using a real event-day scenario: peak clock-ins, multi-role blended overtime, a last-minute schedule change in a Fair Workweek city, and contractor hours. Get 5-year quotes from both vendors.

## Sources

[People Managing People – UKG vs Workday](https://peoplemanagingpeople.com/tools/ukg-vs-workday) · [JitBase – UKG vs Workday WFM](https://www.jitbase.com/blog/ukg-vs-workday-workforce-management) · [TechVendorIndex](https://techvendorindex.pages.dev/compare/workday-vs-ukg-pro/) · [TrustRadius](https://trustradius.com/compare-products/ukg-pro-vs-workday-payroll-and-workforce-management) · [Workday – "unbiased review"](https://explore.workday.com/d52952/items/an-unbiased-review-of-workday-hcm-vs-ukg-pro) · [Workday Negotiations – cost](https://workdaynegotiations.pages.dev/blog/workday-vs-ukg-pro-cost/) · [Workday docs – predictive scheduling setup](https://doc.workday.com/admin-guide/en-us/human-capital-management/workday-scheduling/schedule-management-communications-and-productivit/steps--set-up-predictive-scheduling.html) · [Workday docs – predictive scheduling calculations](https://doc.workday.com/admin-guide/en-us/human-capital-management/time-tracking/time-calculations/create-predictive-scheduling-calculations.html) · [Cloudapper](https://www.cloudapper.ai/?p=174476) · [Workforce.com – predictive scheduling](https://www.workforce.com/buyers-guides/scheduling-software-for-predictive-scheduling-laws) · [Humanforce – stadium WFM](https://www.humanforce.com/us/stadium-workforce-management) · [Shifton – stadium operations](https://shifton.com/industries/stadium-operations/) · [PeopleStrong checklist](https://peoplestrong.com/?p=241719) · [Clearbridge](https://clearbridgetech.com/55-of-hr-technology-projects-miss-the-mark-and-its-almost-never-the-softwares-fault/) · [HRMS World](https://hrmsworld.com/hrms-failure-stats.html) · [HRM Asia](https://hrmasia.com/cloud-based-hcms-what-makes-for-successful-implementations/) · [Reliamag – failure-stat caution](https://reliamag.com/topics/articles/cmms-implementation-failure-rate/index.md)
