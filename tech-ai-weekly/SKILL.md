---
name: tech-ai-weekly
description: Curate, fact-check, and draft the Sunday Tech & AI Weekly Digest (科技与 AI 周刊). Use when the user requests generating a weekly tech/AI recap, summarizing major frontier model updates, investigating AI hardware and semiconductor supply chain dynamics, or drafting a Sunday tech newsletter following industrial media standards.
---

# Tech & AI Weekly (科技与 AI 周刊)

Use this skill to produce Sunday's **Tech & AI Weekly Digest**. The workflow transforms unstructured weekly industry noise into a high-signal, four-band analytical newsletter.

## Core Directives

1. **Cognitive Ladder (70% Familiarity + 30% Hardcore Increment)**:
   - Begin with the week's headline event that tech readers already recognize.
   - Deliver value in the second half through unit economics (token cost, cluster power, CoWoS packaging, HBM bandwidth), engineering trade-offs, and supply chain realities.
2. **Penetrate PR Smoke & Follow the Ledger**:
   - Never parrot corporate marketing claims, synthetic benchmark victories, or vague "AGI tomorrow" hype.
   - Interrogate the economic reality: Who pays? What is the inference cost? What is the hardware bottleneck?
3. **Corroboration (孤证不立)**:
   - Technical benchmark claims or unverified leak specs require at least two independent primary or secondary sources.
   - When a figure lacks independent verification, explicitly flag it as an unverified estimate.
4. **Welcome the Binder (欢迎合订本)**:
   - Maintain consistency across editions. If a prior judgment on a model family, architecture, or chip roadmap was disproven by reality, openly state the delta and update the analytical model.
5. **Rules & Boundary Discipline (在规则与边界中表达)**:
   - Write in neutral, measured, objective language. Avoid emotional fanboyism or apocalyptic doom-saying.
   - For WeChat distribution, follow platform compliance guidelines without sacrificing technical depth.

## Structural Template (Fixed Four-Part Architecture)

Do not alter the overarching narrative structure during drafting:

- **Draft Title**: Content-driven, conflict-oriented, ending with `YYYYMMDD` (e.g., `推理成本骤降十倍，但AI落地的死结还没解开 20261025`).
- **`## 0 本周焦点：热点现象与结构性矛盾`**:
  - The single most consequential tech/AI event of the week.
  - Frame the core tension: closed vs. open-source, cloud capex vs. enterprise revenue, speed vs. safety.
- **`## 1 芯片、算力与真实账本`**:
  - Hardware, semiconductor supply chain, datacenter power, and infrastructure unit economics.
  - Bold all stock/ETF symbols (e.g., `**NVDA**`, `**TSM**`, `**AMD**`, `**AVGO**`, `**MSFT**`, `**GOOGL**`).
- **`## 2 生态博弈与落地阻力`**:
  - Developer ecosystem, real-world deployment friction, agent workflow limitations, enterprise adoption barriers.
- **`## 3 长期合订本与推演`**:
  - 1–2 testable predictions or engineering takeaways.
  - Suitable for direct transformation into a standalone X (Twitter) post with an A-or-B question.

## Workflow

1. **Ingest & Filter**: Scan source feeds listed in `references/source-whitelist.md`. Reject PR announcements lacking architectural or economic substance.
2. **Cross-Check**: Verify benchmark numbers, funding figures, or technical specs against primary sources (GitHub repos, paper preprints, SEC filings).
3. **Drafting**: Write the complete Markdown following `templates/weekly-digest-template.md`.
4. **Validation**: Run `python3 tech-ai-weekly/scripts/validate_tech_weekly.py` on the draft.
5. **Handoff**: Pass the verified Chinese draft to downstream humanizers (`humanizer-zh`), translation editors (`financial-english-editor`), and renderers.
