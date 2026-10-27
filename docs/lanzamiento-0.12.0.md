# Criterio · version 0.12.0 · 27 October 2026

Mexico joins the finance function and contracts and compliance, and a new family arrives: **Criterio EA**, with Ofelia, the executive assistant. Every country and the new agent come with their round with the agents, on synthetic material no agent saw graded: what they found is measured against a key written before the run. Open source under Apache 2.0.

## What it brings

| Family | New in 0.12.0 |
|---|---|
| **Criterio CFO** · Clara, Tomás and Áurea | **Mexico.** The SAT electronic invoice (CFDI 4.0) processed from its official filling guide, with the RFC; the 16% VAT from the guide's catalogue and each entity's framework, IFRS or NIF, each with its verified source |
| **Criterio CLO** · Fidel and Constanza | **Mexico.** Contracts and compliance for banking and retail with each counterparty's RFC. The date of an obligation tied to termination now comes from the latest amendment, and the engine checks it in the record (CLO-11) |
| **Criterio EA** · Ofelia | **New family.** The executive's office: the calendar against the meetings and commitments, each governing body's meeting pack with the record of each decision, the draft minutes, the follow-up of commitments and the correspondence that needs a reply. She prepares; she does not recommend, decide or send anything. Her report is not published in Rostrum unless the office decides so |

The language model (LLM) extracts from the written documents; the code calculates the signals; a person always makes the decision.

## What is measured

Each new country, and each of Ofelia's offices, has entities with defects seeded on purpose and one control with none: any signal in it is a failure.

| | CFO · round 6, Mexico | CLO · round 5, Mexico | EA · round 1, Ofelia |
|---|---|---|---|
| Entities | 3 | 3 | 4 offices |
| Seeded signals found | 27 of 27 (95% margin: 87.5–100%) | 20 of 20 (83.9–100%) | 14 of 14 (78.5–100%) |
| Extra signals | 0 | 0 | 1, in a control |
| Data points extracted correctly | 24 of 24 | 395 of 396 | 76 of 78 |
| Control entities with no signal | 1 of 1 | 1 of 1 | 1 of 2 |
| Tokens | 13.2 million | 12.1 million, with the rerun | 10.4 million, with the reruns |

In the CLO, the one data point missed repeated CLO-10: the final report of a contract whose amendment moved its end date. The cause was a contradiction in Fidel's instruction; it was fixed, the engine now flags it as a record issue, and Fidel's rerun on that entity gave 128 of 128.

Ofelia's first round found eight defects, each with its origin in [the EA rounds](../tests/evidencias/familias/ea/RONDAS.md). Two were code: the setup asked for a tax ID no office carries, and the inventory called the .ics calendar unsupported. One was in the answer key and one in the test harness. Four were instructions: how a citation points to a line and to the office folder, looking for a commitment's evidence before leaving it open —the extra signal in the Colombian control—, and what goes in what is still unknown about a decision. The reruns gave 17 of 17 on the credit union and no extra signal on the control; the last one was verified the same day, after the release: no extra signal and 22 of 22 data points on the Colombian control.

## Where each family is tested

| Family | Countries | Entities in the material |
|---|---|---|
| CFO | Colombia, Ecuador, Peru, Chile and Mexico | 15 |
| CLO | Colombia, Ecuador, Peru, Chile and Mexico | 15 |
| EA | Colombia and Ecuador | 4 offices |
| PMO | Six industries | — |

**What comes next:** Brazil in the CFO and the CLO; travel and the next countries for Ofelia; in the PMO, telecommunications and logistics (0.13.0). None of this has been tested yet on a specific organisation's documentation: that is the step that decides version 1.0.

## If you already have it installed

With auto-update on, the new version arrives by itself; Ofelia is a new plugin, `criterio-assistant`, and is installed on its own. Each version asks you to accept the terms again, and leaves its receipt.

The rounds, every output and every defect with its origin, in [the CFO rounds](../tests/evidencias/familias/cfo/RONDAS.md), [the CLO rounds](../tests/evidencias/familias/clo/RONDAS.md) and [the EA rounds](../tests/evidencias/familias/ea/RONDAS.md).
