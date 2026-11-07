---
name: tech-ai-weekly
description: Curate, fact-check, and draft the Sunday Tech & AI Weekly Digest (科技与 AI 周刊). Use when the user requests generating a weekly tech/AI recap, summarizing major frontier model updates, investigating AI hardware and semiconductor supply chain dynamics, or drafting a Sunday tech newsletter following industrial media standards.
---

# Tech & AI Weekly (科技与 AI 周刊)

Use this skill to produce Sunday's **Tech & AI Weekly Digest**. The workflow transforms unstructured weekly industry news into a high-signal, event-driven analytical newsletter based strictly on verified facts from the preceding week.

## 核心原则：真实收集总结，严禁凭空捏造 (Strict News Gathering, Zero Hallucination)

周刊的核心价值是汇集并穿透**上一周真实发生的前沿科技与商业事实**，严禁任何形式的凭空捏造、估值杜撰或历史事件穿越：
1. **固定时间窗口边界 (Strict Time Window Boundary)**:
   - 周报发布于周日（基准日 $T$，如 `2026-10-25`）。
   - **事件时间窗口 (Review Window)**：严格限定在**前 7 天（$[T-6, T]$，即 10-19 至 10-25）**。入选的 3 起核心事件必须是在此 7 天内公开发生或官方披露的真实事件。
   - **检索纪律**：搜索背景资料时，**必须加上当期年份与月份（如 `2026年10月` 或 `October 2026`）**，严禁使用宽泛无年份限定的检索词，更严禁把历史旧闻（如 2024 年新闻）当作当下突破。
2. **一段一事，强制交代信源与具体日期 (Source & Date Attribution)**:
   - 正文 `## 0`、`## 1`、`## 2` 的首段新闻叙述中，**必须明确交代具体发生日期（如 `10月20日` 或 `当地时间10月21日`）及权威信源出处（如 `据彭博社报道`、`英伟达官方在 GTC Berlin 发布`、`根据公司提交的 SEC 文件`、`据 The Information 披露`）**。
   - 严禁出现“日前”、“最近”、“前段时间”、“据悉”、“坊间传闻”等无具体日期和无出处的模糊表述。
3. **研究底稿台账化 (`source_notes.md`)**:
   - 必须在运行目录中保留 `source_notes.md`，开头写清时间窗口（`复盘窗口: YYYY-MM-DD 至 YYYY-MM-DD`）。
   - 逐条罗列入选事件的名称、发生日期（YYYY-MM-DD）和权威信源出处链接/机构名。

## Core Directives

1. **One Event Per Section, Fact-Led (一段一事，事实先行)**:
   - Each major section centers on **one discrete news event** that took place in the past week.
   - **Opening Paragraph**: Provide a concise, objective journalistic account of the event (who, what, when, numbers, direct action) with exact date and source. No fluff, no speculation.
   - **Subsequent Breakdown**:
     - *Penetrate the PR (撕开公关包装)*: Discard company marketing talking points; inspect unit economics, pricing changes, and capital expenditure burdens.
     - *Follow the Cash Ledger & Incentives (算清楚账本与利益博弈)*: Who is monetizing? Who is subsidizing? What are the hardware, power, or gross margin constraints?
     - *Mechanisms & Structural Conflicts (结构性矛盾与深层机制)*: Contrast compute scaling vs. physical bottlenecks (grid, memory bandwidth, packaging yield, hallucination overhead).
     - *Testable Judgment (可检验的推演)*: Provide a clear, falsifiable conclusion with observation criteria over a 2–6 quarter horizon.
2. **Cognitive Ladder (70% Familiarity + 30% Hardcore Increment)**:
   - Start from an event the broader tech community already recognizes.
   - Deliver value through specific unit economics, packaging architecture (e.g., CoWoS, HBM), and power delivery realities.
3. **Corroboration (孤证不立)**:
   - Benchmark improvements, valuation cuts, or hardware leak specs require at least two independent primary or secondary sources.
4. **Welcome the Binder (欢迎合订本检验，但行文自然)**:
   - Maintain analytical consistency across editions. If new evidence changes a prior judgment, update the analysis and explain the current evidence in a way that stands on its own.
5. **Rules & Boundary Discipline (在规则与边界中表达)**:
   - Use neutral, measured, objective financial and engineering prose. Avoid sensationalism or emotional hype.

## Title & Structural Hard Rules (标题与结构硬性规范)

1. **Main Title (大标题 / H1)**:
   - **带有栏目标识 (Branded Column Prefix)**: 大标题开头必须带有栏目标识 `【科技周报】`，末尾附上出版日期（YYYYMMDD）。
   - **单点聚焦，选最重的一条 (Single Lead Event)**: 严禁将两三起不同事件用逗号并列拼接在主标题中。必须从全周事件中筛选出最具产业震荡力、颠覆性或认知差的**唯一起核心大事件**作为唯一主线。
   - **抓人眼球，突出硬核冲突 (Eye-Catching & Conflict-Driven)**: 标题必须极具吸引力，直击产业反差与核心痛点（例如揭示估值缩水、大模型算力成本反噬、电网物理死墙等真实账本代价），杜绝平铺直叙的公文式汇报。
   - **严禁使用冒号 (Strictly No Colons)**: **大标题严禁使用冒号（无论是全角 `：` 还是半角 `:`）**！杜绝 `A：B` 模板，采用一气呵成、自然抓人的叙事长句或逗号短语。
   - 归档与草稿末尾保留 `YYYYMMDD` 日期戳。

2. **Subheadings (小标题 / H2)**:
   - `## 0`, `## 1`, `## 2`, `## 3` 采用连贯自然的叙事实体短语，**严禁使用冒号（`:` 或 `：`）或 `xxx:xxx` 的套路化模板**。

3. **Natural Forward Outlook (自然前瞻，无内部黑话)**:
   - 最后一节（`## 3`）写自然的产业前瞻与业务闭环推演，**严禁在面向读者的正文中出现“长期合订本推演：”或“后续由事实合订本核对检验”等内部工程术语**。

4. **Numeral Formatting (数字规范)**:
   - 标题和小标题中的核心数据、百分比、日期一律使用阿拉伯数字。

## Structural Template (Fixed Four-Part Architecture)

- **Draft Title**: `【科技周报】[抓最重事件 + 强吸引力 + 无冒号自然标题] 2026MMDD`
- **`## 0 [事件一自然小标题，无冒号]`**:
  - *新闻段落*：写明发生具体日期与权威信源，交代核心事实与关键数据。
  - *深度剖析*：撕开公关表象，算清经济账本与利益冲突。
- **`## 1 [事件二自然小标题，无冒号]`**:
  - *新闻段落*：写明具体日期与信源，交代第二起关键事件（如基础设施、电网、芯片或交付延期）。
  - *深度剖析*：结合数据图表（```chart），剖析上中下游的实际成本与物理瓶颈。
  - Bold stock/ETF symbols (e.g., `**NVDA**`, `**TSM**`, `**AMZN**`, `**MSFT**`, `**GOOGL**`).
- **`## 2 [事件三自然小标题，无冒号]`**:
  - *新闻段落*：写明具体日期与信源，交代第三起事件（如企业落地摩擦、开源闭源交锋或商业模式变现）。
  - *深度剖析*：剖析真实业务流中的隐性工程开销与替代方案。
- **`## 3 [产业前瞻与推演，无冒号]`**:
  - 提炼 1–2 个中长期不可逆的产业判断，设立明确的时间窗口与证伪指标（用自然叙述呈现，不写内部字眼）。

## Workflow

1. **Lock Review Window**: Determine $T$ and anchor review period to $[T-6, T]$.
2. **Collect Real News & Build `source_notes.md`**: Use `references/source-whitelist.md` to find candidates. Check them against primary documents and follow `references/curation-standard.md`. Record each event date and source.
3. **Drafting**: Write complete Markdown according to `templates/weekly-digest-template.md`.
4. **Validation**: From this skill directory, run `python3 scripts/validate_tech_weekly.py <draft.md> --source-notes <source_notes.md>`.
5. **Handoff**: Pass the verified draft to humanizer, translation editor, and blog/WeChat renderers.
