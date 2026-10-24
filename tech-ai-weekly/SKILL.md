---
name: tech-ai-weekly
description: Curate, fact-check, and draft the Sunday Tech & AI Weekly Digest (科技与 AI 周刊). Use when the user requests generating a weekly tech/AI recap, summarizing major frontier model updates, investigating AI hardware and semiconductor supply chain dynamics, or drafting a Sunday tech newsletter following industrial media standards.
---

# Tech & AI Weekly (科技与 AI 周刊)

Use this skill to produce Sunday's **Tech & AI Weekly Digest**. The workflow transforms unstructured weekly industry noise into a high-signal, event-driven analytical newsletter.

## Core Directives

1. **One Event Per Section, Fact-Led (一段一事，事实先行)**:
   - Each major section centers on **one discrete news event**.
   - **Opening Paragraph**: Provide a concise, objective journalistic account of the event (who, what, when, numbers, direct action). No fluff, no speculation.
   - **Subsequent Breakdown**:
     - *Penetrate the PR (撕开公关包装)*: Discard company marketing talking points; inspect unit economics, pricing changes, and capital expenditure burdens.
     - *Follow the Cash Ledger & Incentives (算清楚账本与利益博弈)*: Who is monetizing? Who is subsidizing? What are the hardware, power, or gross margin constraints?
     - *Mechanisms & Structural Conflicts (结构性矛盾与深层机制)*: Contrast compute scaling vs. physical bottlenecks (grid, memory bandwidth, packaging yield, hallucination overhead).
     - *Testable Judgment (合订本检验)*: Provide a clear, falsifiable conclusion with observation criteria over a 2–6 quarter horizon.
2. **Cognitive Ladder (70% Familiarity + 30% Hardcore Increment)**:
   - Start from an event the broader tech community already recognizes.
   - Deliver value through specific unit economics, packaging architecture (e.g., CoWoS, HBM), and power delivery realities.
3. **Corroboration (孤证不立)**:
   - Benchmark improvements, valuation cuts, or hardware leak specs require at least two independent primary or secondary sources.
4. **Welcome the Binder (欢迎合订本)**:
   - Maintain consistency across editions. If a prior judgment was disproven, openly acknowledge the delta and update the analytical model.
5. **Rules & Boundary Discipline (在规则与边界中表达)**:
   - Use neutral, measured, objective financial and engineering prose. Avoid sensationalism or emotional hype.

## Structural Template (Fixed Event-Driven Architecture)

- **Draft Title**: Content-driven, conflict-oriented, ending with `YYYYMMDD` (e.g., `OpenAI调降估值，亚马逊停建算力中心：AI狂飙背后的真实账本 20261025`).
- **`## 0 [事件一标题：核心事件与冲突点]`**:
  - *新闻段落*：简明交代第一起关键事件的核心事实与关键数据。
  - *深度剖析*：撕开公关表象，算清经济账本与利益冲突。
- **`## 1 [事件二标题：硬件/算力/供应链事件]`**:
  - *新闻段落*：简明交代第二起关键事件（如基础设施、电网、芯片或交付延期）。
  - *深度剖析*：结合数据图表（```chart），剖析上中下游的实际成本与物理瓶颈。
  - Bold stock/ETF symbols (e.g., `**NVDA**`, `**TSM**`, `**AMZN**`, `**MSFT**`, `**GOOGL**`).
- **`## 2 [事件三标题：落地障碍/生态路线事件]`**:
  - *新闻段落*：简明交代第三起事件（如企业落地摩擦、开源闭源交锋或商业模式变现）。
  - *深度剖析*：剖析真实业务流中的隐性工程开销与替代方案。
- **`## 3 [产业合订本推演与观察指标]`**:
  - 提炼 1–2 个中长期不可逆的产业判断，设立明确的时间窗口与证伪指标。
  - 提炼适合直接发布在 X 上的观点要点与 A-or-B 讨论问题。

## Workflow

1. **Ingest & Filter**: Scan source feeds listed in `references/source-whitelist.md`. Reject PR announcements lacking architectural or economic substance.
2. **Cross-Check**: Verify benchmark numbers, funding figures, or technical specs against primary sources (GitHub repos, paper preprints, SEC filings).
3. **Drafting**: Write the complete Markdown following `templates/weekly-digest-template.md`.
4. **Validation**: Run `python3 tech-ai-weekly/scripts/validate_tech_weekly.py` on the draft.
5. **Handoff**: Pass the verified Chinese draft to downstream humanizers (`humanizer-zh`), translation editors (`financial-english-editor`), and renderers.
