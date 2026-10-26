# Criterio CFO · version 0.9.0 · 27 October 2026

Criterio's close, control and reporting family: two agents that process what the finance function already produces —the ledger, bank statements, electronic invoices, the budget and the minutes— and check it against the evidence to say what is done, what has no support and what is off plan. First version for locally adopted IFRS in Colombia and Ecuador. Open source under Apache 2.0.

## What it brings

| | For whom | Commands | What it does |
|---|---|---:|---|
| **Clara** · `criterio-finance` | The controller's office | 9 | The monthly close with its checklist and evidence, bank and account reconciliations, DIAN and SRI electronic invoices against the ledger, and the auditor's package |
| **Tomás** · `criterio-budget` | Financial planning (FP&A) | 7 | The approved budget against actuals and commitments, the year-end forecast, budget transfers and the budget committee's materials |

The language model (LLM) extracts from written documents; the code calculates the 23 signals; a person always takes the decision. Neither agent posts entries, signs, approves transfers or declares the status of the close.

## What is measured

Two rounds, on test data from four industries —banking and retail in Colombia, credit unions and mining in Ecuador— and one control entity per country with no seeded defect: any signal there is a failure. 340 documents in CSV, electronic-invoice XML and Markdown, plus the PMO's project records, with a key no agent sees.

Round 2, complete, on the six entities:

| | Result | 95% margin |
|---|---|---|
| Seeded signals found | 45 of 45 | 92.1–100% |
| Extra signals | 0 | — |
| Data extracted correctly | 48 of 49 (98%) | 89.3–99.7% |
| Control entities with no signal | 2 of 2 | — |

The missing item was in the grading, not the agent: in mining, Tomás wrote the committee commitment in more words than the key. It is fixed and verified (CFO-4). The four recorded defects carry their origin, the commit that fixes them and the round that verified them, in [`tests/evidencias/familias/cfo/`](../tests/evidencias/familias/cfo/RONDAS.md). The full statistical analysis is in [`families/criterio-cfo/analisis/`](../families/criterio-cfo/analisis/ANALISIS.md).

## What it costs today

Third-party figures, verified against the publisher's text, in [`FUENTES.es.md`](../families/criterio-cfo/FUENTES.es.md):

- **18%** of controllership staff make errors at least daily, and 59% several a month, because of capacity constraints. Gartner, 2024; 497 people.
- **45%** of SOX controls are manual, and program hours rose 32% in two years. KPMG, SOX Survey 2025; about 150 professionals.
- **18 days** is the median annual close; the slowest take 35. APQC, 2026; 2,214 organisations.

## What comes next

- **More countries, by market size:** Peru, Chile, Mexico and Brazil, each with its electronic-invoice reader and verified sources. A country is announced when it passes its round.
- **Áurea, treasury**, the family's third agent: cash, payments and debt against their policy. She is built and her engine matches the material's key exactly; her round with the agent is the next step, and she enters a version when she passes it.
- **The first use on a specific organisation's documentation**, the step that takes the family to version 1.0.

## Before you use it

Each version is accepted again: the agent shows the terms, asks for an explicit yes and leaves a receipt with the terms' SHA-256 fingerprint. It produces working drafts, not decisions.

Installation: `/plugin marketplace add josenanez/criterio`, then `criterio-finance` for Clara and `criterio-budget` for Tomás. In Claude Cowork: Customise → Explore plugins → Personal → + → `josenanez/criterio`.
