# Criterio PMO · version 0.5.0 · 19 October 2026

The launch version of Criterio's project governance family: three agents and a server that process what the project office has already written, prepare its work and say what changed, what contradicts what and what no document supports. Open source under Apache 2.0.

## What it brings

| | For whom | Commands | What it does |
|---|---|---:|---|
| **Vera** · `criterio-portfolio` | The PMO | 17 | One record per project with the citation of every data point, variances and alerts across the portfolio, the report and the committee pack |
| **Samuel** · `criterio-project` | Each project manager | 9 | The commitments from each meeting with their date, their reschedules and whether they are met; agenda, minutes, report and the record he publishes to the PMO |
| **Alba** · `criterio-product` | Each product manager | 11 | The definition against the evidence of demand, the requirements register and the charter the project is born with |
| **Rostrum** · inside `criterio-portfolio` | Whoever never opens a folder | — | Publishes the report and receives requests; it never writes the record |

The 37 commands, one by one, in the [manual](manual.md).

## What is measured

Ten rounds since 14 October, on test data from four industries —financial institutions (banks and credit unions), retail and mining in South America— built to be more demanding than those organisations' usual documentation: over 500 documents per round in Markdown, Word, PDF, Excel and CSV, contradictions between documents, commitments moved up to six times, milestones met with no receipt, projects gone silent, vendor deliveries with no evidence, and in each industry one healthy project that must raise no alert. Each round brings new material and a key no agent sees.

Round 10, on version 0.5.0, on 18 October 2026: 52 projects and the 37 commands in PMO order, with the plugins installed from scratch.

| | Result | 95% margin |
|---|---|---|
| Commands that finished and kept their contract | 148 of 148 | — |
| Vera · correct alerts of those raised | 242 of 242 | 98.4–100% |
| Vera · alerts found of those there | 242 of 249 | 90.4–100% |
| Samuel · commitments and close date right | 108 of 108 | 96.6–100% |
| Alba · alerts found of those there | 131 of 131 | 97.2–100% |
| Alba · correct alerts of those raised | 131 of 132 | 95.8–99.9% |
| Rostrum · checks on what it shows | 2175 of 2175 | 99.8–100% |

No false alert from Vera. The seven she missed are one failure, in one mining project: at setup she left that project without commitments because they were in the record its manager published (D059). Alba's extra alert was right: the test data cited an interview the folder did not hold (D058). Both are fixed after 0.5.0.

60 defects registered with their origin, the commit that fixes them and the round that verified them, all under [`tests/evidencias/`](../tests/evidencias/). The FAQ is in [`families/criterio-pmo/PREGUNTAS.md`](../families/criterio-pmo/PREGUNTAS.md).

## What comes next

- **The first use on a specific organisation's documentation.** It is the step that decides version 1.0, when the record schema survives that use.
- **What is graded against a key:** Vera's alerts, Samuel's commitments and close date, and the alerts on Alba's product. The other commands are checked in every run against their contract —what they must write and must not—.
- **The model's writing** —minutes, reports, interview synthesis— is verified through the arithmetic its figures come from, not by a deterministic grader.
- **The field-by-field comparison of the whole record** (`grade.py --fichas` and `--registros`) is the next test to add to the rounds.

## Before using it

Every version is accepted again: the agent shows the terms, asks for an explicit yes and leaves a receipt in Markdown and PDF with the SHA-256 fingerprint of the terms. It produces working drafts, not decisions, and no agent writes a project's declared status.

Install: `/plugin marketplace add josenanez/criterio`, or in Claude Cowork, Customise → Explore plugins → Personal → + → `josenanez/criterio`.
