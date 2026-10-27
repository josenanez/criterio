# Criterio · version 0.11.0 · 27 October 2026

Chile joins the finance function, and Peru and Chile join contracts and compliance. Each country comes in with its round with the agents, on synthetic material no agent saw graded: what they found is measured against a key written before the run. Open source under Apache 2.0.

## What it brings

| Family | New in 0.11.0 |
|---|---|
| **Criterio CFO** · Clara, Tomás and Áurea | **Chile.** The SII electronic invoice (the DTE) processed from its official format, with the RUT and its check digit; the 19% VAT and the IFRS adopted by the Colegio de Contadores, each with its verified source |
| **Criterio CLO** · Fidel and Constanza | **Peru and Chile.** Contracts and compliance for banking, mining and retail with each country's tax ID. An obligation tied to termination —the final report, the settlement minutes— now falls due on the current end date, the one in the latest amendment |

The language model (LLM) extracts from the written documents; the code calculates the signals; a person always makes the decision.

## What is measured

Each new country has two industry entities with defects seeded on purpose and one control entity with none: any signal in it is a failure.

| | CFO · round 5, Chile | CLO · round 4, Peru and Chile |
|---|---|---|
| Entities | 3 | 6 |
| Seeded signals found | 26 of 26 (95% margin: 87.1–100%) | 37 of 37 (90.5–100%) |
| Extra signals | 0 | 0 |
| Data points extracted correctly | 24 of 24 | 812 of 813 |
| Control entities with no signal | 1 of 1 | 2 of 2 |
| Tokens | 12.7 million | 21.6 million, with the rerun |

In the CLO, the one data point missed was the final report date of a contract whose amendment moved the end date (CLO-10). Fidel's instruction was fixed, his run on that entity was repeated —128 of 128 data points— and the Chilean entities, already run with the fix, gave 132 of 132.

## Where each family is tested

| Family | Countries | Entities in the material |
|---|---|---|
| CFO | Colombia, Ecuador, Peru and Chile | 12 |
| CLO | Colombia, Ecuador, Peru and Chile | 12 |
| PMO | Six industries | — |

**What comes next:** Mexico and Brazil in both families, one at a time, by market size; in the PMO, telecommunications and logistics (0.12.0). None of this has been tested yet on a specific organisation's documentation: that is the step that decides version 1.0.

## If you already have it installed

Turn on auto-update once: in /plugin, Marketplaces → criterio → Enable auto-update. Each version asks you to accept the terms again, and leaves its receipt.

The rounds, every output and every defect with its origin, in [the CFO rounds](../tests/evidencias/familias/cfo/RONDAS.md) and [the CLO rounds](../tests/evidencias/familias/clo/RONDAS.md).
