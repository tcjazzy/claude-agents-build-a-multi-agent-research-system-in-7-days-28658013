# Day 3 Research Results

These topics were run on 2026-10-29 using the same search-then-analyze steps the Day 3 coordinator delegates.
The container had no `ANTHROPIC_API_KEY`, so the scripts could not be run here. Add a key and run them to get model-generated reports.

---

## 1. Running LLMs in production (`day03_end.py`)

| | Commercial APIs | Self-hosted open models | Cloud-managed (Bedrock, Azure, Vertex) |
|---|---|---|---|
| **Cost** | Pay per token. Cheapest at low or spiky volume | Can be up to 5x cheaper only at very high, steady volume (>500M tokens/day). GPUs often sit below 60% utilization, which pushes cost per token up | Same price as the direct API, or 10–30% more depending on the source. Reserved capacity breaks even at about 75–84% utilization |
| **Data privacy** | Data leaves your network. You rely on the vendor's terms | Full control. Data stays in your own environment | Data stays inside your existing cloud account and compliance boundary |
| **Operational burden** | Lowest | Highest: at least 10–20 hours a month of maintenance, plus GPU capacity planning | Low to moderate |

**Where sources agree:** Use APIs for experimental or variable workloads. Self-host only for high-volume, predictable workloads.
**Where sources disagree:** The Bedrock price premium (0% vs 10–30%).
**Gap:** Most figures come from vendors or bloggers with a stake in the answer.

Sources: [Marka](https://www.marka.net.ua/news/self-hosted-llm-vs-api-the-real-cost-and-security-trade-offs-for-enterprise-in-2026/), [TechSaaS/dev.to](https://dev.to/yash_pritwani_07a77613fd6/self-hosted-llms-vs-api-real-cost-comparison-at-production-scale-33kl), [Spheron – Bedrock pricing](https://www.spheron.network/blog/aws-bedrock-pricing-2026-managed-api-cost/), [Beri](https://www.beri.net/tag/LLM%20API%20pricing), [Petronella](https://petronellatech.com/blog/self-hosted-llm-deployment-a-technical-guide-for-ctos), [IntuitionLabs](https://intuitionlabs.ai/pdfs/hosted-ai-api-vs-self-hosted-llm-cost.pdf)

---

## 2. Solid-state vs sodium-ion EV batteries (`demo.py`)

- **Sodium-ion is shipping now, in small volumes.** CATL and Changan's Nevo A06 is the first mass-production passenger EV with a sodium-ion pack. CATL expects about 10,000–20,000 vehicles in 2026. Cells cost about $59/kWh, still above LFP at about $52/kWh. Sodium-ion has lower energy density but better cold-weather performance, and production is concentrated in China.
- **Solid-state is still in pilot.** CATL's chairman rates it level 4 of 9 for maturity. BYD targets small-batch sulfide cells in 2027, and Toyota targets 2027–28. Semi-solid-state is the bridge: MG claims mass production and plans to bring it to Europe in the MG4 by the end of 2026.

**Where sources agree:** Sodium-ion reaches the market first, in cheaper short-range cars. Full solid-state in passenger cars is a 2027+ story.
**Gap:** Some of the dates come from secondary sources and need checking against company announcements.

Sources: [MIT Technology Review](https://www.technologyreview.com/2026/02/02/1132042/whats-next-for-ev-batteries-in-2026/), [battery-news.de](https://battery-news.de/?p=39330), [CarNewsChina](https://carnewschina.com/2026/02/09/byd-breaks-ground-with-solid-state-battery-and-10000-cycle-sodium-tech-power-2027-evs/), [EV Magazine](https://evmagazine.com/news/semi-solid-state-sodium-ion-top-ev-news-this-week), [Eleport](https://eleport.com/new-battery-technologies/)

---

## 3. Day 3 challenge question: Workday vs UKG Pro vs Oracle HCM (`day03_begin.py`)

| | Workday HCM | UKG Pro | Oracle Fusion Cloud HCM |
|---|---|---|---|
| **Hourly / seasonal WFM** | Rated "adequate"; many customers add a separate WFM tool | Leads this category, building on Kronos time, attendance and scheduling | Workforce Scheduling plus the Workforce Operations Command Center agentic app (26C) |
| **AI** | Illuminate plus AI agents | UKG Bryte | Fusion Agentic Applications for HR (April 2026): Schedule Assistant, Scheduling Advisor, Time Assistant (one timecard at a time in 26B), Time-off Assistant |
| **TCO signal** | Higher if you need to add WFM | Bundled time and attendance can be materially cheaper for hourly-heavy organizations | Strongest when Oracle ERP is already in place. Pricing was not found |

**Where sources agree:** UKG is the strongest for hourly-heavy workforces. Workday is stronger for talent management, global HR and finance integration. AI from all three vendors is still maturing in production.
**Gaps:** No published pricing for any vendor. Most of the comparison sources are review aggregators.

Sources: [People Managing People](https://peoplemanagingpeople.com/tools/ukg-vs-workday), [TechVendorIndex](https://techvendorindex.pages.dev/compare/workday-vs-ukg-pro/), [G2](https://www.g2.com/compare/ukg-pro-vs-workday-hcm-vs-oracle-peoplesoft), [Oracle press release](https://www.oracle.com/es/news/announcement/oracle-introduces-fusion-agentic-applications-for-hr-2026-04-09/), [Oracle 26C readiness](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26c/wosc-26c/26C-workforce-scheduling-wn-f49778.htm), [Oracle 26B Time Assistant](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26b/tila-26b/26B-time-labor-wn-f45850.htm), [Oracle 26A Schedule Assistant](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26a/wosc-26a/26A-workforce-scheduling-wn-f43387.htm)
