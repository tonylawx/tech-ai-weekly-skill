# Tech & AI Weekly Skill

Agent and Codex skill for curating, fact-checking, and drafting Sunday's **Tech & AI Weekly Digest (科技与 AI 周刊)**.

Rooted in institutional research discipline and industrial-grade content engineering:
1. **Event-Led Dissection (一段一事，事实先行)**: Every section opens with a clean, journalistic statement of a single real-world news event, followed by an uncompromising analytical breakdown.
2. **70% Familiarity + 30% Hardcore Increment (认知阶梯)**: Hooking general tech readers with macro events, then dissecting infrastructure, supply chain, and unit economics.
3. **Penetrating PR Smoke and Following the Cash Ledger (利益穿透与真实账本)**: Rejecting corporate marketing hype; calculating token unit costs, inference margins, hardware constraints, and ecosystem conflicts.
4. **Multi-Source Corroboration (孤证不立)**: Requiring two independent sources for technical claims and performance metrics.
5. **Seven-Day Review Window**: Record the date and authoritative source for each event in `source_notes.md` before drafting.

## Repository Layout

```text
tech-ai-weekly-skill/
├── tech-ai-weekly/
│   ├── SKILL.md                          # Primary agent skill instructions
│   ├── references/
│   │   ├── curation-standard.md          # Fact-checking & narrative standards
│   │   └── source-whitelist.md           # High-signal source catalog
│   ├── templates/
│   │   └── weekly-digest-template.md     # Fixed event-driven structural template
│   └── scripts/
│       └── validate_tech_weekly.py       # Structural & anti-PR validator
├── LICENSE                               # MIT License
└── README.md
```

## Usage

Read [tech-ai-weekly/SKILL.md](tech-ai-weekly/SKILL.md) and use its references and template.
Run the validator from the repository root with paths to your draft and source notes.

```bash
python3 tech-ai-weekly/scripts/validate_tech_weekly.py path/to/draft.md --source-notes path/to/source_notes.md
```

Run the validator tests with `python3 -m unittest discover -s tests -v`.

## License

MIT © 2026 Tony Law
