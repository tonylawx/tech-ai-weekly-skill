# Tech & AI Weekly Skill

Agent and Codex skill for curating, fact-checking, and drafting Sunday's **Tech & AI Weekly Digest (科技与 AI 周刊)**.

Built on the industrial self-media methodology from 马督工 (Ma Dougong) and rigorous tech industry research standards, this skill emphasizes:
1. **70% familiarity + 30% incremental insight (认知阶梯)**: hooking general tech readers with macro events, then dissecting infrastructure, supply chain, and unit economics.
2. **Penetrating PR smoke and following the cash ledger (利益穿透)**: rejecting corporate marketing hype, analyzing token unit cost, inference margins, hardware constraints, and ecosystem conflicts.
3. **Multi-source corroboration (孤证不立)**: requiring two independent sources for technical claims and performance metrics.
4. **Long-term editorial accountability (欢迎合订本)**: tracking predictions across time and updating engineering models when falsified.

## Repository Layout

```text
tech-ai-weekly-skill/
├── tech-ai-weekly/
│   ├── SKILL.md                          # Primary agent skill instructions
│   ├── references/
│   │   ├── curation-standard.md          # Fact-checking & narrative standards
│   │   └── source-whitelist.md           # High-signal source catalog
│   ├── templates/
│   │   └── weekly-digest-template.md     # Fixed four-part structural template
│   └── scripts/
│       └── validate_tech_weekly.py       # Structural & anti-PR validator
├── LICENSE                               # MIT License
└── README.md
```

## Validation

```bash
python3 tech-ai-weekly/scripts/validate_tech_weekly.py path/to/draft.md
```

## License

MIT © 2026 Tony Law
