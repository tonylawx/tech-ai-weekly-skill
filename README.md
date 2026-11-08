# Tech & AI Weekly Skill

Agent and Codex skill for curating, fact-checking, and drafting Sunday's **Tech & AI Weekly Digest (科技与 AI 周刊)**.

Rooted in institutional research discipline and **Industrial Content Engineering Methodology**:
1. **Event-Led Dissection**: Open each section with objective, ground-truth facts, explicit dates, entities, and critical metrics, completely eliminating corporate PR fluff.
2. **Follow the Capital Ledger & Real Costs**: Strip away vendor marketing spin to audit micro unit economics, token price trends, industrial power tariffs, and balance-sheet depreciation drag resulting from massive CapEx build-outs.
3. **Structure of Conflicts over Moralizing**: Examine structural incentive conflicts across the value chain (high foundry/hardware gross margins vs. downstream model margin bleeding, open-source parity vs. proprietary price defenses, compute cluster power draws vs. local community grid reliability).
4. **Cognitive Ladder & Two-Turn Logic**: 70% familiar headline on-ramp + 30% specialized industrial depth; strictly execute the golden two-turn sequence (Consensus Expectation A $\to$ Micro-Ledger Reality B $\to$ Systemic Institutional & Physical Deadlock C).
5. **Historical Mirroring**: Benchmark current trends against historical precedents such as the 1999 telecom dark fiber boom, early cloud price competition, and open-source Linux expansion.
6. **The Binder Protocol**: Reject vague speculative predictions; provide definitive 2–3 quarter deductions with explicit falsification criteria and observable milestones.

## Repository Layout

```text
tech-ai-weekly-skill/
├── tech-ai-weekly/
│   ├── SKILL.md                          # Primary agent skill instructions
│   ├── references/
│   │   ├── industrial-media-methodology.md # Industrial media methodology & content engineering standard
│   │   ├── curation-standard.md          # Fact-checking, accounting & narrative standards
│   │   └── source-whitelist.md           # High-signal source catalog
│   ├── templates/
│   │   └── weekly-digest-template.md     # Rich five-layer paragraph structural template
│   └── scripts/
│       └── validate_tech_weekly.py       # Richness, volume, attribution & format validator
├── tests/
│   └── test_tech_weekly.py               # Test suite for weekly validator
├── LICENSE                               # MIT License
└── README.md
```

## Validation

```bash
python3 tech-ai-weekly/scripts/validate_tech_weekly.py path/to/draft.md
```

## Running Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT © 2026 Tony Law
