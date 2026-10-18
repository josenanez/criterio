# Criterio PMO · version 0.4.0 · 19 October 2026

The first public version of Criterio's project governance family: three agents and a server that process what the project office has already written, prepare its work and say what changed, what contradicts what and what no document supports. Open source under Apache 2.0.

## What it brings

| | For whom | Commands | What it does |
|---|---|---:|---|
| **Vera** · `criterio-portfolio` | The PMO | 17 | One record per project with the citation of every data point, variances and alerts across the portfolio, the report and the committee pack |
| **Samuel** · `criterio-project` | Each project manager | 9 | The commitments from each meeting with their date, their reschedules and whether they are met; agenda, minutes, report and the record he publishes to the PMO |
| **Alba** · `criterio-product` | Each product manager | 11 | The definition against the evidence of demand, the requirements register and the charter the project is born with |
| **Rostrum** · inside `criterio-portfolio` | Whoever never opens a folder | — | Publishes the report and receives requests; it never writes the record |

The 37 commands, one by one, in the [manual](manual.md).

## What is measured

Round 9, on version 0.4.0, on 17 October 2026: four industries —financial institutions (banks and credit unions), retail and mining in South America—, 52 projects, the 37 commands in PMO order, with the plugins installed from scratch and a key no agent sees.

| | Result | 95% margin |
|---|---|---|
| Commands that finished and kept their contract | 148 of 148 | — |
| Vera · alerts found of those there | 266 of 266 | 98.6–100% |
| Vera · correct alerts of those raised | 266 of 267 | 97.9–99.9% |
| Samuel · commitments and close date right | 108 of 108 | 96.6–100% |
| Alba · alerts on her product, found and right | 128 of 128 | 97.1–100% |
| Rostrum · checks on what it shows | 2170 of 2170 | 99.8–100% |

Vera's extra alert is a code defect this same round found: when the manager writes «No aplica» as the product, the contrast between the two records read it as a product (D056, fixed after 0.4.0).

Nine rounds since 14 October, 57 defects registered with their origin, the commit that fixes them and the round that verified them. All published under [`tests/evidencias/`](../tests/evidencias/).

## What is not known yet

- **Nothing has been run on an organisation's real documentation.** The test data is written by the repository.
- **Each industry has about a dozen projects:** the margins are wide, and they are published that way.
- **Graded against a key:** Vera's alerts, Samuel's commitments and close date, and the alerts on Alba's product. The other commands are checked against their contract —what they must write and must not—, not against a key.
- **The model's writing** —minutes, reports, interview synthesis— is not measured by a deterministic grader.
- **The field-by-field comparison of the whole record** (`grade.py --fichas` and `--registros`) has not yet been run on what the rounds produce.

## Before using it

Every version is accepted again: the agent shows the terms, asks for an explicit yes and leaves a receipt in Markdown and PDF with the SHA-256 fingerprint of the terms. It produces working drafts, not decisions, and no agent writes a project's declared status.

Install: `/plugin marketplace add josenanez/criterio`, or in Claude Cowork, Customise → Explore plugins → Personal → + → `josenanez/criterio`.
