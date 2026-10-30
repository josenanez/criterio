[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cco · the family's design

**Status: stable, not yet launched (version 0.3.0).** The twelve commands, the eight skills and the
calculation engine are built on the common core; the engine passes its deterministic test against the
material from Colombia, Mexico, Ecuador, Peru and Chile (`tests/criterio-cco/`), and the two agents
passed their two rounds: the 95% confidence floor is 98.0% on signals and 95.1% on data. Scope in
[ADR 0019](../../docs/decisions/0019-scope-comercial-cso.md) and its name in
[0022](../../docs/decisions/0022-la-familia-comercial-es-la-cco.md) (Spanish).

**This is the family's design sheet**: the documents it processes, the signals the code calculates, every command with its input, process and report, and the decisions taken. What the family does, how it installs, its records and invariants, the folder structure, Rostrum, the cadence, the tests and the roadmap are on its [page](README.md).

Two agents that extend the capacity of the commercial function: they process the CRM exports, each
opportunity's evidence, the quotes and the commission settlement, and contrast them against the
stage table, the discount matrix, the commission plan and Fidel's and Clara's records. The language
model (LLM) extracts; the code calculates; the decision —the forecast that is committed, the
discount that is approved, the target— is always a person's.

First version: Colombia and Mexico. **It does not rate people**: it says which opportunity has no
evidence and which commission is not the plan's, never who sells best.

**How they work.** Automated: they process the documents, calculate the signals and prepare every
deliverable without intervention. Semi-automated when a data point no document carries is missing
—which CRM the export comes from, which column carries each field, within how many days a contract
is invoiced—: then they ask the person, say what they asked and carry on with the answer.

**Sources.** Every source used to process —the role's framework, each export's format, third-party
figures— is in [`FUENTES.es.md`](FUENTES.es.md) (Spanish) with its version, link, date consulted
and status. The design, the documentation and the tests cite those sources by their identifier.

**Where this document comes from.** The tables of agents, signals, commands and figures are not
written here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and
[`fuentes.json`](fuentes.json), which `scripts/familias.py` writes into this design, into
`FUENTES.es.md`, into the family page, into the plugins' READMEs and, with `scripts/criterio-familias.mjs`, into the portal.

**The most frequent questions**, in [`PREGUNTAS.md`](PREGUNTAS.md) ([Español](PREGUNTAS.es.md)), and **where it is going**, in the [roadmap](README.md#roadmap).

## One agent per role

<!-- cco:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| The forecast | **Augusto** — from the Latin *augur*, the one who reads the signs before they happen: the forecast against what backs it | `criterio-sales` | The pipeline against its evidence and the forecast against what backs it: every opportunity against the document its stage requires, the stalled ones, the close dates that slip, what was committed against what is weighted with evidence, and the target against what closed |
| From sale to invoice | **Valeria** — from the Latin *valere*, to be worth: what a sale is worth once it is signed and invoiced | `criterio-revenue` | Price and discount against their policy, and what was won against what was signed and invoiced: every discount against the level that approves it, every won sale against its contract in Fidel's records, every signed contract against its invoice in Clara's, and every commission against the plan |
<!-- /cco:agentes -->

## The documents they process

| Document | Expected format | Agent |
|---|---|---|
| The CRM's opportunity export | CSV or Excel, with the export date in the name: Salesforce (F-02), HubSpot (F-04, F-05) or any other with its column mapping | Augusto, Valeria |
| The close-date history | Salesforce CSV or Excel (F-03), if the CRM exports it | Augusto |
| The stage table: the document each stage requires, its probability and whether it is open, won or lost | Excel or CSV | Augusto |
| The period's targets, by line if there are lines | Excel or CSV | Augusto |
| The sales committee's minutes or pack with the committed forecast | Word, PDF or email | Augusto |
| Each opportunity's proposal, purchase order and acceptance record | Any format, with the opportunity id at the start of the name | Augusto |
| The discount matrix: each level's cap and who approves it | Excel or CSV | Valeria |
| Each quote or order, with its discount and its approval | Word, PDF or email, with the quote id at the start of the name | Valeria |
| The accounts table: each CRM account with the customer's tax id | Excel or CSV | Valeria |
| The commission plan and each period's settlement | Excel or CSV | Valeria |
| Fidel's contract records and Clara's invoicing records | The ones they write in their state | Valeria |

The columns each table needs, and their variants, in the `sales-intake` skill; how each export is
processed, in the `crm-exports` skill. Where each document goes, in the
[recommended folder structure](README.md#the-recommended-folder-structure).

### What the engine processes and what the agent extracts

As in the CFO and CLO families ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)),
the engine processes the tables directly —the CRM exports, the history, the stages, the targets, the
discount matrix, the accounts table, the commission plan and settlement—, and the agent extracts to
the record what only a written document carries: **every evidence document** of an opportunity with
its type, amount and date; **the committed forecast** from the committee minutes; **every quote**
with its list price, discount and approval. Every data point with its citation.

**What crosses families goes through the records.** Fidel's record says the contract and Clara's
says the invoice: Valeria takes them from their state and never processes a contract or an
electronic invoice again. The cross is by the customer's tax id, which the accounts table puts next
to each CRM account.

## The signals: what the code calculates

<!-- cco:senales · generado por scripts/familias.py; no se edita a mano -->
**Augusto · The forecast**

| Signal | Raised when |
|---|---|
| `stage_without_evidence` | An opportunity is in a stage and does not have the document that stage requires: the proposal sent, the purchase order |
| `stalled_opportunity` | An open opportunity has no recorded activity within the configured days |
| `close_date_slipped` | An opportunity's close date moved more times than configured |
| `forecast_unsupported` | What was committed exceeds what the opportunities with evidence add up to, weighted by their stage, by more than the configured tolerance |
| `target_vs_closed` | What closed at the cut-off departs from the period's target, prorated by the days elapsed, by more than the threshold |

**Valeria · From sale to invoice**

| Signal | Raised when |
|---|---|
| `discount_outside_policy` | A discount exceeds its level's cap without the approval the matrix asks for, or no level covers it |
| `won_without_contract` | A won opportunity has no signed contract in Fidel's record |
| `signed_without_invoice` | A signed contract has no invoice in Clara's record within the invoicing period |
| `commission_differs_from_plan` | The settled commission is not the one the plan gives on what was closed and invoiced |
<!-- /cco:senales -->

The days without activity, the times a close date may slip, the forecast tolerance, the target
threshold, the invoicing period and the commission tolerance are each organisation's configuration,
with a declared default; none of them is a rule.

## The three classes, as in the PMO family

**A · What it does, and today takes someone's time:** preparing the sales committee with a clean
pipeline, checking which opportunity lacks its proposal or its purchase order, building the weighted
forecast, checking discounts against the matrix, reconciling what was won with what was invoiced and
reviewing the commission settlement.

**B · What it does, and today does not get done:** checking every opportunity, not a sample,
against its stage's evidence; counting how many times each close date slipped; separating the
committed forecast that has evidence from what does not; crossing every won sale with its contract
and every contract with its invoice; recalculating every commission with the plan.

**C · What it does not do:** it does not write or change anything in the CRM; it does not contact a
customer; it does not approve a discount or a price exception; it does not set or change a target;
it does not settle or correct a commission; it does not rate or compare the people on the team.

## Augusto's commands, in order of importance

<!-- cco:comandos-augusto · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `sales-setup` | The root folder. Questions: entity and its tax ID, country, the period, which CRM the export in `10-crm/` comes from —Salesforce, HubSpot, Dynamics 365, Zoho or another, in CSV or Excel— and, if another, which column carries each field, the stage table in `00-referencia/` with the document each stage requires and its probability, how many days without activity stall an opportunity and how many times a close date may slip | Inventory of what is there; recognises each export's format by its columns (F-02, F-04); compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; each export with its format, its date and its opportunities; the missing columns; the period's first record |
| 1 | `pipeline-scan` | The whole `10-crm/`, `20-comite/` and `30-evidencia/` | The code processes each export with its date and compares every opportunity with the previous export: stage, amount and close date; the agent takes to the period record every document in `30-evidencia/` —the proposal, the purchase order, the acceptance record— with its opportunity, type, amount and date, and the committed forecast from the committee minutes, every data point with its citation; the engine validates the record | What changed between the previous export and the latest; new, won and lost opportunities; the new signals; what could not be processed and why |
| 2 | `pipeline-check` | The latest export in `10-crm/`, the earlier ones, the stage table in `00-referencia/` and the period record | Every open opportunity against the document its stage requires; the days since its last activity; the times its close date slipped from one export to the next, or in the field history if it arrives | The opportunities without their stage's document, the stalled ones and the ones whose close date slipped, each with its citation; without rating whoever owns it |
| 3 | `forecast-check` | The committed forecast in the record, the latest export in `10-crm/` and the stage table in `00-referencia/` | What closed in the period plus the open opportunities closing in it with their stage's evidence, each at its amount and its stage's probability, against what was committed; the difference against the configured tolerance | What was committed, what closed, what is weighted with evidence and what is weighted without it; the difference; the opportunities that back it and those that do not |
| 4 | `target-check` | The targets in `00-referencia/` and the latest export in `10-crm/` | What was won with a close date in the period up to the cut-off date against the period's target prorated by the days elapsed, by line if the target has one; the difference against the configured threshold | The target, what was expected at the cut-off, what closed and the difference by line; never by person |
| 5 | `sales-wake` | The configuration and the record | Decides what is due: a new export in `10-crm/`, new committee minutes, the period's end coming up and a weekly review | What ran and what it found; if nothing is due, it stays quiet |
<!-- /cco:comandos-augusto -->

## Valeria's commands, in order of importance

<!-- cco:comandos-valeria · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `revenue-setup` | The root folder. Questions: entity and its tax ID, country, the period, the discount matrix, the commission plan and the accounts table in `00-referencia/`, where Fidel's contract records and Clara's invoicing records are, and within how many days a signed contract is invoiced | Inventory of what is there; compares the folder with the recommended structure; checks that every won account has its tax id in the accounts table; creates, moves or renames nothing | Configuration saved; inventory by folder; the accounts without a tax id; whether it found Fidel's and Clara's records; the period's first record |
| 1 | `deal-scan` | The whole `40-cotizaciones/` and the latest export in `10-crm/` | Only reprocesses what changed; the agent takes to the period record every quote or order with its opportunity, list price, discount and who approved it, in what role and on what date, every data point with its citation; the engine validates the record | What changed; which quotes are new; the new signals; what could not be processed and why |
| 2 | `discount-check` | The discount matrix in `00-referencia/` and the period record | Every discount against the level of the matrix that covers it and the approval that level asks for; a discount no level covers is always flagged | Every quote with its discount, its level, the approval it asks for and the one it has; those outside the policy, with their citation |
| 3 | `won-to-invoice` | The latest export in `10-crm/`, the accounts table in `00-referencia/`, Fidel's contract records and Clara's invoicing records | Every won opportunity against a signed contract with its customer in Fidel's records; every contract signed with a customer against an invoice issued to that customer in Clara's records, within the invoicing period | What was won without a contract and what was signed without an invoice, each with its citation in the CRM and in the other agent's record; contracts are not processed again |
| 4 | `commission-check` | The commission plan in `00-referencia/`, the period's settlement in `50-comisiones/`, the latest export in `10-crm/` and Clara's invoicing records | What the plan gives on what was won in the period and already invoiced, by opportunity owner and by line, against what was settled; the difference against the configured tolerance | By owner: what the plan gives, what was settled and the difference, with the opportunities that make up the base; not published in Rostrum unless the configuration says so |
| 5 | `revenue-wake` | The configuration and the record | Decides what is due: new quotes, a won opportunity without a contract or an invoice when its deadline arrives, the period's settlement when it arrives and a weekly review | What ran and what it found; if nothing is due, it stays quiet |
<!-- /cco:comandos-valeria -->

## The common report format

The same as the other families, and the engine writes it: header, what needs attention, the
command's own result, what could not be processed, the questions it asked and the sources.

## What is reused from the other families

- `texto.py` for Word, Excel, PowerPoint, PDF and email, `terminos.py` for accepting the terms,
  `rastro.py` for each run's trace and `raiz.py` for the root folder, copied from the PMO family by
  `scripts/sincronizar.py`.
- `nucleo.py` —tables, dates, inventory, signals and report—, copied from `criterio-finance`.
- The record's shape: a citation per data point, declared against evidenced, "not found" valid.
- Fidel's contract records and Clara's issued invoicing, which Valeria reads from their state.
- The versioned terms with their receipt, the version register and the gates in
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, to publish the pipeline and sale-to-invoice reports
  ([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

What is new is its own engine, `ventas.py`, standard library only: it processes the CRM exports
directly, and the agent extracts to the record only what a written document carries. It lives in
`criterio-sales` and is copied to `criterio-revenue`, with the `sales-intake` and `crm-exports`
skills.

## How it is tested

Synthetic material in `tests/criterio-cco/`: two industries per country —Colombia and Mexico—, with
a Salesforce export, a HubSpot export and a CSV export with its mapping, and one control per
country, with a key the engine never sees. Every signal in the family is seeded at least once; what
is seeded and where, in [`tests/criterio-cco/EVIDENCIA.md`](../../tests/criterio-cco/EVIDENCIA.md).
The agent's extraction is tested in the round, on the same material. The family is declared tested
with a full round.

## Third-party figures

<!-- cco:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Xactly con Regina Corso Consulting), C-02 (Salesforce), C-03 (Gartner).
<!-- /cco:cifras -->

## Closed decisions

- The scope: the commercial function, with two agents, their nine signals and what they never do (ADR
  0019). José, 2026-10-28.
- The names, Augusto and Valeria. José, 2026-10-28.
- The exports: Salesforce and HubSpot with their reader, and any CSV or Excel with its column
  mapping. José, 2026-10-28.
- Commissions go in the first increment: all nine signals from the first one. José, 2026-10-28.
- The countries: Colombia and Mexico first. José, 2026-10-28.
- The plugins: `criterio-sales` for Augusto and `criterio-revenue` for Valeria.

## Open decisions

1. Microsoft Dynamics and Zoho, each with its verified source, in increment 2.
2. The price list against each quote's price, as one more signal.
