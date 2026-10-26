# Criterio CFO · version 0.10.0 · 26 October 2026

Criterio's finance function: three agents that process what the finance function already produces —the ledger, bank statements, electronic invoices, the budget, the treasury policy and the minutes— and check it against the evidence to say what is done, what has no support and what is off plan. Locally adopted IFRS in Colombia, Ecuador and Peru. Open source under Apache 2.0.

## What it brings

| | For whom | Commands | What it does |
|---|---|---:|---|
| **Clara** · `criterio-finance` | The controller's office | 9 | The monthly close with its checklist and evidence, bank and account reconciliations, DIAN, SRI and SUNAT electronic invoices against the ledger, and the auditor's package |
| **Tomás** · `criterio-budget` | Financial planning (FP&A) | 7 | The approved budget against actuals and commitments, the year-end forecast, budget transfers and the budget committee's materials |
| **Áurea** · `criterio-treasury` | Treasury | 6 | Cash against its minimum and its forecast, each payment against who may approve it, FX exposure, and debt against its maturity and its covenants |

The language model (LLM) extracts from written documents; the code calculates the 30 signals; a person always takes the decision. None of the three posts entries, signs, approves transfers, moves money or declares the status of the close.

**New in 0.10.0:** Áurea; Peru, with the SUNAT electronic invoice processed from its official guide; and the material in the formats of a real finance function —Excel, Word and PDF—, including the bank statement in PDF, which the engine processes directly.

## What is measured

Test data from four industries in three countries —banking and retail in Colombia, credit unions and mining in Ecuador, banking and mining in Peru— and one control entity per country with no seeded defect: any signal there is a failure. A key no agent sees.

**Round 4, with the three agents, complete on the nine entities.** Each agent ran its setup and its scan, which is where it raises its signals and extracts what the written documents carry:

| | Result | 95% margin |
|---|---|---|
| Seeded signals found | 80 of 80 | 95.4–100% |
| Extra signals | 0 | — |
| Data extracted correctly | 74 of 74 | 95–100% |
| Control entities with no signal | 3 of 3 | — |

The first pass scored 79 of 80 with 2 extra signals. All three misses were in setup, not in the calculation: Clara took a financial-expense account as purchases (CFO-8) and added an account to reconcile with no subledger (CFO-9), and Áurea inferred the functional currency from a test rate set wrong (CFO-10). The engine now proposes the accounts from the data, the material carries what was missing to decide, and the repeated runs gave the expected result. The round used 43.5 million tokens, reruns included.

Before it, round 3 —partial, on four entities— found CFO-5, CFO-6 and CFO-7, and round 2, with Clara and Tomás on the six Colombian and Ecuadorian entities, scored 45 of 45 signals.

The ten recorded defects carry their origin, the commit that fixes them and the round that verified them, in [`tests/evidencias/familias/cfo/`](../tests/evidencias/familias/cfo/RONDAS.md). The full statistical analysis is in [`families/criterio-cfo/analisis/`](../families/criterio-cfo/analisis/ANALISIS.md).

## What it costs today

Third-party figures, verified against the publisher's text, in [`FUENTES.es.md`](../families/criterio-cfo/FUENTES.es.md):

- **18%** of controllership staff make errors at least daily, and 59% several a month, because of capacity constraints. Gartner, 2024; 497 people.
- **45%** of SOX controls are manual, and program hours rose 32% in two years. KPMG, SOX Survey 2025; about 150 professionals.
- **18 days** is the median annual close; the slowest take 35. APQC, 2026; 2,214 organisations.
- **79%** of organisations suffered attempted or actual payments fraud in 2024. Association for Financial Professionals, 2025; 521 corporate finance professionals.

## What comes next

- **The three agents' round on the rest of the material:** Ecuadorian credit unions and mining, Colombian retail and the Colombian and Ecuadorian controls, in the new formats.
- **More countries, by market size:** Chile, Mexico and Brazil, each with its electronic-invoice reader and verified sources. A country is announced when it passes its round.
- **The first use on a specific organisation's documentation**, the step that takes the family to version 1.0. Before the first one in Peru, the reader is checked against SUNAT's current validation rules.

## Before you use it

Each version is accepted again: the agent shows the terms, asks for an explicit yes and leaves a receipt with the terms' SHA-256 fingerprint. It produces working drafts, not decisions.

Installation: `/plugin marketplace add josenanez/criterio`, then `criterio-finance` for Clara, `criterio-budget` for Tomás and `criterio-treasury` for Áurea. In Claude Cowork: Customise → Explore plugins → Personal → + → `josenanez/criterio`.
