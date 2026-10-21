[Español](DISENO.es.md)

# criterio-cfo · the finance function family

![Clara, Tomás and Rostrum](../../docs/img/en/robots-cfo.gif)

**Status: built and in testing.** The sixteen commands, the twelve skills and the calculation
engine are built; the engine passes its deterministic test against the material of four industries
and two control entities (`tests/criterio-cfo/`), and the test with the agent is the next step.
Scope in [ADR 0006](../../docs/decisions/0006-scope-cfo.md); how the work is split between the
engine and the agent, in [ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md).

Two agents that extend the capacity of the finance function: they prepare the work of the close and
the budget, and check it against all of its evidence to flag what does not tie out, what has no
support and what is reported differently from what the documents say. The large language model
(LLM) extracts; the code calculates; the status of the close and of the budget is always declared
by a person.

First version: IFRS as locally adopted in Colombia and Ecuador, with DIAN and SRI electronic
invoicing.

**How they work.** Automated: they process the documents, calculate the signals and prepare each
deliverable without intervention. Semi-automated when a data point no document carries is missing
—the entity, the period, the threshold, who approves—: then they ask the person, say what they
asked and carry on with the answer.

**Sources.** Every source used for processing —technical annexes, regulations, third-party
figures— is in [`FUENTES.es.md`](FUENTES.es.md) (Spanish) with its version, its link, the date it
was consulted and its status. The design, the documentation and the tests cite those sources by
their identifier.

**Where this document comes from.** The tables of agents, folders, signals, commands and figures
are not written here: they come from three sources, [`familia.json`](familia.json),
[`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json), which `scripts/familias.py`
writes into this design in both languages, into `FUENTES.es.md`, into the `criterio-finance`
READMEs and, with `scripts/criterio-familias.mjs`, into the portal. A gate in
`scripts/verificar.py` fails if any copy does not tie out, if a command cites a folder that is not
in the structure or if it relies on a source still to be verified.

**What people ask most** is in [`PREGUNTAS.md`](PREGUNTAS.md), and **where it is going**, in the
[roadmap](#roadmap).

## One agent per role

<!-- cfo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Controller | **Clara** — from *clarus*: the books say what the supporting documents say | `criterio-finance` | The monthly close with its checklist and evidence, bank and account reconciliations, e-invoices against the books, and the auditor's package |
| FP&A | **Tomás** — “the twin”: puts the budget next to its twin, actual spend | `criterio-budget` | The approved budget against actual and committed spend, the year-end forecast, budget transfers and the budget committee pack |
<!-- /cfo:agentes -->

As in the PMO family, the two never talk to each other: they talk through their records.

## The records: the only contract

| Record | One per | What it carries | Who writes it |
|---|---|---|---|
| Close record | Entity and period | The checklist tasks with owner, date and evidence; each reconciliation with its open items; the e-invoices against their entries; the declared status of the close | Clara; the status, the controller in person |
| Budget record | Area or cost centre and year | Approved, actual and committed by account; the area's forecast; the transfers with their minutes; the declared status | Tomás; the status, the head of the area |

Every data point cites the document it comes from and its date. Declared and evidenced go in
separate fields. «Not found» is a valid answer.

## The documents they process

| Document | Expected format | Agent |
|---|---|---|
| Trial balance and general ledger | ERP export in Excel or CSV | Both |
| Bank ledgers and bank statements | Excel, CSV or PDF with text | Clara |
| Electronic invoices issued and received, Colombia | DIAN XML (UBL 2.1, CUFE), per the technical annex in force | Clara |
| Electronic vouchers, Ecuador | SRI XML, offline scheme, 49-digit access key | Clara |
| Close checklist | Excel or Markdown, with owner and date | Clara |
| Auditor's requests and their answers | Word, PDF, email | Clara |
| Approved budget and its versions | Excel | Tomás |
| Purchase orders and commitments | ERP export | Tomás |
| Each area's forecasts | Excel | Tomás |
| Budget and transfer committee minutes | Word, PDF | Tomás |
| Project records from the PMO family | `ficha-pm.json` and Vera's records | Tomás, read only |

The DIAN (F-01) and SRI (F-04) formats are taken from their official technical source and verified
field by field before the reader is written ([ADR 0006](../../docs/decisions/0006-scope-cfo.md),
rule 2).

## The signals: what the code calculates

<!-- cfo:senales · generado por scripts/familias.py; no se edita a mano -->
**Clara · Controller**

| Signal | Raised when |
|---|---|
| `close_task_overdue` | A checklist task is past its date and has no evidence |
| `close_task_done_without_evidence` | A task is marked done and no document supports it |
| `trial_balance_unbalanced` | Debits and credits in the trial balance do not add up to the same amount |
| `ledger_vs_trial_balance` | An account's ledger balance differs from the trial balance |
| `bank_unreconciled` | There are statement movements with no entry, or entries with no movement |
| `reconciling_item_aged` | A reconciling item is older than the configured days |
| `reconciliation_stale` | An account's reconciliation was not updated in the period |
| `account_unreconciled` | An account's ledger balance differs from its sub-ledger (receivables, payables, inventory, fixed assets, intercompany) |
| `einvoice_not_recorded` | An issued or received e-invoice has no accounting entry |
| `recorded_without_einvoice` | An entry that needs an e-invoice has none to support it |
| `einvoice_amount_mismatch` | The XML amount or tax differs from the entry |
| `einvoice_duplicate` | The same CUFE or access key is recorded twice |
| `audit_request_unanswered` | An auditor request has no supported answer |
| `declared_close_vs_evidence` | The close is reported as closed and there are open signals that status does not explain |

**Tomás · FP&A**

| Signal | Raised when |
|---|---|
| `variance_over_threshold` | Actual spend at the cut-off departs from the budget by more than the configured percentage |
| `committed_near_approved` | Actual plus committed approaches the approved amount with no headroom |
| `forecast_over_approved` | The year-end forecast exceeds the approved amount |
| `forecast_stale` | The area's forecast was not updated within the configured days |
| `transfer_without_approval` | A transfer or change has no minutes approving it |
| `budget_version_mismatch` | The report uses a budget version other than the approved one |
| `spend_without_budget_line` | There is spend in an account or cost centre with no budget line |
| `declared_vs_evidence` | The area reports itself within budget and the numbers do not support it |
| `project_budget_mismatch` | A project's budget in its record differs from what the area has assigned |
<!-- /cfo:senales -->

Thresholds are each organisation's configuration, with a declared default value; none of them is a
regulation.

## The three classes, as in the PMO family

**A · What it does, and today takes someone's time:** building the close record, reconciling
statements against ledgers, matching each e-invoice with its entry, consolidating actual spend
against the budget, preparing the report and the committee material.

**B · What it does, and today nobody does:** matching every e-invoice of the period against the
books, not a sample; checking every close task against its evidence; comparing the budget version
each report uses with the approved one; matching each project's budget with the area's.

**C · What it does not do:** it does not post or correct entries; it does not file returns or
regulatory reports; in the first version it gives no opinion on deductibility, rates or IFRS
treatments, and it never states a rate, a deadline or the value of a tax unit from memory; it does
not sign; it does not declare the status of the close or the budget.

## The folder structure

Recommended, not required, as in the PMO family ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)):
the agents process the folder as it is. `finance-setup` and `budget-setup` compare what they find
with this structure and, on every run, say which file is out of place and where it would go; they
create, move or rename nothing among the organisation's documents. The numbering goes in tens, as
in the PMO family, in the order in which the close and the budget are worked. The folder names are
in Spanish: they are the names the agents look for.

Every document has a single place. The period's books live in `10-contabilidad/`: Clara closes them
and Tomás takes actual spend from there, with no copies between folders.

<!-- cfo:carpetas · generado por scripts/familias.py; no se edita a mano -->
One folder per entity, with its tax id at the start of the name: `900123456-andean-bank`. Inside it, what the organisation provides once, one folder per accounting period and one per budget year.

```
finanzas/
└── <entidad>/
    ├── 00-referencia/
    ├── <AAAA-MM>/
    │   ├── 10-contabilidad/
    │   ├── 20-bancos/
    │   ├── 30-facturacion/
    │   ├── 40-soportes/
    │   └── 50-auditoria/
    └── presupuesto-<AAAA>/
        ├── 10-aprobado/
        ├── 20-compromisos/
        ├── 30-proyecciones/
        └── 40-actas/
estado-finanzas/
```

**`<entidad>/`** · What the organisation provides once

| Folder | What goes in | Agent |
|---|---|---|
| `00-referencia/` | The chart of accounts with each account's nature, `checklist-cierre.xlsx` in the defined model, and the mapping of accounts to cost centres and budget lines | Clara, Tomás |

**`<AAAA-MM>/`** · One accounting period, numbered in the order the close is worked

| Folder | What goes in | Agent |
|---|---|---|
| `10-contabilidad/` | Trial balance and general ledger exported from the ERP, and `auxiliares/` with one file per account; budget execution comes from here too | Clara, Tomás |
| `20-bancos/` | One folder per account, `<bank>-<last 4 digits>`, with the statement and the book ledger | Clara |
| `30-facturacion/` | `emitidas/` and `recibidas/`, with the DIAN (F-01) or SRI (F-04) XML | Clara |
| `40-soportes/` | The evidence for each checklist task —minutes, emails, signed reconciliations—, with the task id at the start of the name | Clara |
| `50-auditoria/` | The auditor's `requerimientos/` (requests) and `respuestas/` (answers) | Clara |

**`presupuesto-<AAAA>/`** · One budget year

| Folder | What goes in | Agent |
|---|---|---|
| `10-aprobado/` | The approved budget and every version, with its date in the name | Tomás |
| `20-compromisos/` | Purchase orders and commitments exported from the ERP, with the cut-off date in the name | Tomás |
| `30-proyecciones/` | Each area's forecast, one per area and date | Tomás |
| `40-actas/` | Minutes of the budget committee, of approvals and of transfers | Tomás |

**`estado-finanzas/`** · What Clara and Tomás write: the configuration, the records, the reports and the indexes. No person edits it, and no agent writes anywhere else.
<!-- /cfo:carpetas -->

A file without the expected format is not guessed: it is reported with what it is missing.

## The close checklist

The checklist arrives in one of two ways, and the person chooses:

1. **The organisation loads it** in the defined model.
2. **Clara recommends one per industry** —banking, cooperatives, retail and mining, the four in the
   tests— as a draft. A person reviews and approves it before it is used; until then the close
   status is calculated, but the report says the checklist is not approved.

The model is a sheet with these columns:

| Column | What it carries | Required |
|---|---|---|
| `id` | Unique task identifier, for example `C-07` | Yes |
| `tarea` | What is done | Yes |
| `area` | Accounting, treasury, tax, payroll… | Yes |
| `responsable` | A person, not an area | Yes |
| `dia_limite` | Close working day on which it falls due (D+3) or a date | Yes |
| `depende_de` | Ids of the tasks that must come first | No |
| `evidencia_esperada` | Which document proves it: «signed reconciliation», «committee minutes» | Yes |
| `criticidad` | High, medium or low | Yes |

## The common report format

Every report by Clara and Tomás comes out in Markdown, and Rostrum publishes it, with the same
structure and in this order, from most to least important:

1. **Header:** entity, period, cut-off date, agent version.
2. **What needs attention:** the open signals ordered by importance (criticality, amount and age),
   each with its owner and its citation.
3. **The result:** each command's own table.
4. **What could not be processed:** each file with the reason and where it should be.
5. **The questions it asked** and the answer it took.
6. **Sources:** every document cited, with its path and its date, and the regulatory or technical
   sources by their identifier in [`FUENTES.es.md`](FUENTES.es.md).

## Clara's commands, in order of importance

`finance-setup` goes first because the others need it: it compares the folder with the recommended
structure, asks the questions no document answers and leaves the configuration.

<!-- cfo:comandos-clara · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `finance-setup` | The root folder. Questions: entity and NIT or RUC, country, IFRS group (F-05, F-06), ERP, currency, period, thresholds, who approves, chart of accounts | Inventory of what is there; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder (what is there, what is missing, what is out of place and where it would go); checklist loaded or recommended; the first close record |
| 1 | `close-scan` | The whole period | Extracts each document's text with its fingerprint; only reprocesses what changed; updates the record with the citation of every data point | What changed in the period; what was added to the record; the new signals; what could not be processed and why |
| 2 | `close-status` | `00-referencia/checklist-cierre.xlsx`, `40-soportes/` and the record | Matches each task with its evidence, its date and its dependencies; calculates evidenced progress weighted by criticality | Declared status against evidenced status; task table ordered by criticality and due date: done with evidence, done without evidence, overdue, on time, blocked by another; the close's critical path |
| 3 | `bank-reconcile` | Each folder in `20-bancos/`: statement and ledger, with date, description, reference, amount and balance | Matches by exact reference, then by amount and date within the configured window, then by amount; classifies every open item | Per account: balance per bank, deposits in transit, outstanding cheques, unrecorded bank notes and balance per books, with the unexplained difference (it must be zero); open items by age (0–30, 31–60, 61–90 and over 90 days) |
| 4 | `account-reconcile` | `10-contabilidad/`: the general ledger and `auxiliares/` for receivables, payables, inventory, fixed assets and intercompany | The logic of `bank-reconcile`: the general-ledger balance against the subledger balance of each account, and open items with their age | Per account: balance per general ledger, balance per subledger, the difference and the items that explain it by age; the accounts whose reconciliation was not updated in the period |
| 5 | `ledger-check` | `10-contabilidad/`: trial balance and general ledger; the chart of accounts in `00-referencia/` | Debits against credits; opening balance plus movements against closing balance; ledger against trial balance, account by account; balances contrary to the nature declared by the organisation's chart of accounts | The overall tie-out; differences by account with their amount; accounts with a balance contrary to their nature |
| 6 | `einvoice-check` | `30-facturacion/` and the accounting entries of the accounts the configuration links to sales and purchases | Processes each XML with its official structure (F-01, F-04); matches by CUFE or access key, number, NIT or RUC and amount | Invoices without an entry, entries without an invoice, differences in amount or tax, duplicates; no tax opinion: whatever is a tax judgement is left as a question for the person |
| 7 | `audit-pack` | `50-auditoria/` and the record | Matches each request with its answer and its supporting documents | The package index: request, answer, cited support and status (answered with support, answered without support, unanswered, overdue); moves or copies no files |
| 8 | `finance-wake` | The configuration and the record | Decides what is due by cadence: daily during the close window, weekly outside it | What ran and what it found; if nothing is due, it stays silent |
<!-- /cfo:comandos-clara -->

### Account reconciliation

Reconciling accounts against their subledgers —receivables, payables, inventory, fixed assets,
intercompany— is the controller's work, so it belongs to Clara and to this plugin, not to another:
it is `account-reconcile`, with the logic of `bank-reconcile`. Consolidating several entities is
outside the first version.

## In Rostrum

Rostrum is not duplicated: one portal, `criterio-server`, publishes what every family writes
([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)). The CFO enters like any other,
without the server knowing anything about finance.

**How it enters.** `/criterio-finance:finance-setup` and `/criterio-budget:budget-setup` leave
their configuration in `.criterio/finanzas/<entity>/` and `.criterio/presupuesto/<entity>/`, with
the entity's finance folder marked with `_CRITERIO_FINANZAS.txt`. Clara and Tomás share the
entity's state, and each one sees their own runs and reports in the portal, not the other's. Then
`/criterio-server:server-setup` finds both configurations and adds them to the map, and
`/criterio-server:server-start` raises the portal. A new entity enters by running `server-setup`
again.

**What the CFO has in Rostrum:**

| Where | What |
|---|---|
| Home | The **Criterio CFO** card with Clara and Tomás and their open signals |
| `/familia/cfo` | The latest each engine wrote —the close of a month, the budget of a year—, with its signals in words and the calculation date, and its reports as the engine left them |
| What falls due | Close tasks and auditor requests with a date, sorted with the other families' due dates |
| `/caso/<PRY>` | A budget signal on a PMO project shows up on that project's page |
| Where it works | The full path of the root folder, of the entity's documents with their marker, of the state and of each configuration |
| Ask an agent | A question for Clara or Tomás, taken on their next run |

Rostrum recalculates nothing and never writes to the state: it serves what the engine already wrote
and says when. The pages meet WCAG 2.2 level AA, checked with axe-core at four screen widths
(`tests/criterio-server/accesibilidad/`).

→ [Rostrum: install, configure and use it with every family](https://www.josenanez.com/agents/rostrum) ·
[its README](../../plugins/criterio-server/README.md)

## Tomás's commands, in order of importance

`budget-setup` goes first for the same reason as `finance-setup`. Tomás does not recalculate the
books: he takes actual spend from `10-contabilidad/`, brings it to each line with the
organisation's mapping and puts it next to the approved budget. The forecast always comes with its
written assumption, and the committee's decision is made by a person.

<!-- cfo:comandos-tomas · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `budget-setup` | The root folder. Questions: entity, budget year, areas or cost centres with their owner, the approved version and its minutes, the mapping of accounts to budget lines (in `00-referencia/`), the variance thresholds and, if the organisation uses the PMO family, where its records are | Inventory of `10-aprobado/` to `40-actas/` and of the periods with `10-contabilidad/`; identifies the approved version by its minutes; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder (what is there, what is missing, what is out of place and where it would go); the approved version it took and the minutes behind it; each area's first record |
| 1 | `budget-scan` | The whole `presupuesto-<AAAA>/` and `10-contabilidad/` for each period of the year | Extracts each document with its fingerprint; only reprocesses what changed; takes actual and committed spend to its line with the mapping in `00-referencia/`; updates each record with the citation of every data point | What changed; what was added to each record; the new signals; what could not be processed and why, including spend with no line in the mapping |
| 2 | `variance-report` | The records at cut-off and the approved version in force; if the organisation uses the PMO family, each project's budget in its record | By area, line and account: approved, actual, committed and available (approved minus actual minus committed); actual against approved accumulated to cut-off, with its monthly phasing if there is one, and saying so if there is not; each project's budget against the one assigned to the area | The table by area ordered by variance; lines over the threshold; spend with no budget line; projects whose budget does not tie out with the area's; status declared by the area against evidenced status |
| 3 | `forecast` | Actual at cut-off, `20-compromisos/` and each area's forecast in `30-proyecciones/` | Two calculated forecasts, each with its written assumption: at run rate (actual plus the greater of the monthly average times the remaining months and what is committed) and at plan (actual plus what is left of the approved budget by its monthly phasing); compares them with the forecast the area delivered | By area: approved, the area's forecast and the two calculated ones, with the difference of each; areas whose forecast exceeds what was approved; forecasts not updated within the configured days |
| 4 | `transfer-log` | The versions in `10-aprobado/` and the minutes in `40-actas/` | Compares each version with the previous one, line by line: every change in amount is a transfer, an addition or a reduction; matches it with the minutes that approve it by date, amount and source and destination lines | The log: date, source, destination, amount, minutes and status (with minutes, without minutes, minutes with no change applied); transfers leave the total unchanged, and additions and reductions are shown separately |
| 5 | `budget-committee-pack` | The records, `variance-report`, `forecast` and `transfer-log` at cut-off, and the previous committee's minutes in `40-actas/` | Builds the decision points: lines over the threshold, forecasts over what was approved, transfers without minutes and the previous committee's commitments with their evidence | The pack in the common format: each decision with its figure, its citation and who makes it; the previous minutes' commitments with their status; it does not recommend the decision |
| 6 | `budget-wake` | The configuration and the records | Decides what is due by cadence: when a new period appears in `10-contabilidad/`, before each committee and once a week for commitments | What ran and what it found; if nothing is due, it stays silent |
<!-- /cfo:comandos-tomas -->

## What is reused from the PMO family

- `texto.py` for Word, Excel, PowerPoint, PDF and email, and `terminos.py` for accepting the terms,
  copied between plugins by `scripts/sincronizar.py`, as today.
- The shape of the record: a citation per data point, declared against evidenced, «not found» as a
  valid answer.
- The terms per version with their receipt, the version register and the gates of
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, to publish the close and budget reports (ADR 0010).

What is new is the family's own engine, `finanzas.py`, on the standard library: it processes the
tables and the invoices directly, and the agent extracts to the record only what a written document
carries ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)). It lives in
`criterio-finance` and is copied to `criterio-budget`.

## How it is tested

As in the PMO family: synthetic material per industry with a key the agents never see, and control
entities that must not raise any signal. It is in `tests/criterio-cfo/`: four industries —banking
and retail in Colombia, cooperatives and mining in Ecuador— and one control per country, with the
invoices generated with each country's official structure. Every family signal is planted at least
once; what is planted and where, in [`tests/criterio-cfo/EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md)
(Spanish).

`tests/criterio-cfo/evaluar.py` runs the engine with the correct extraction and compares every signal
by its name and its key: an extra one counts the same as a missing one. The agent's extraction is
tested in the round, on the same material. The family is declared tested with a full round.

## Third-party figures

<!-- cfo:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Ventana Research / ISG), C-02 (KPMG), C-03 (APQC), C-04 (Gartner).
<!-- /cfo:cifras -->

## Roadmap

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->

The family grows in increments. Each one is a version with its full test and its statistical analysis published, with the same metrics, so the evolution can be compared.

| Version | Status | What goes in | Test |
|---|---|---|---|
| Increment 1 | In progress | **Built, with the engine tested**<br>· Clara and Tomás’s sixteen commands, their twelve skills and the calculation engine<br>· DIAN and SRI electronic invoicing, processed from its official technical source<br>· The root folder each agent searches for and, with permission, marks<br>· The family in Rostrum, with what falls due and where each agent works | The engine, against 4 industries and 2 control entities |
| Increment 2 | Next | **The round with the agent**<br>· Clara and Tomás run their commands on the material of the four industries, as the PMO does in every round<br>· What only minutes, emails and auditor letters carry, extracted and graded against the key<br>· With a full round, the family is declared tested | 4 industries and 2 control entities, with the key the agent never sees |
| Increment 3 | Reserved | **Deployment in an organisation**<br>· The first use on a specific organisation’s books and budget | That organisation’s documentation |

<!-- /hoja de ruta -->

## Closed decisions

- The agents' names: Clara (controller) and Tomás (FP&A). José, 2026-10-20.
- The plugins: `criterio-finance` for Clara, the one already declared, and `criterio-budget` for
  Tomás, within the `criterio-cfo` family. José, 2026-10-20.

## Construction decisions

Taken while building, with their reason; each one can be reversed by a new decision.

- **The export columns** are recognised by their name and its variants; one that is not recognised
  is asked about and stays in the configuration's `columns`. There is no template per ERP.
- **The default thresholds** are in each plugin's `config.example.json`, and setup offers them as
  configuration, not as a rule. In Colombia, the amount tolerance is the margin the DIAN annex
  allows: ±2.00 and ±5.00 for VAT (F-01, 5.2.1).
- **The budget version in force** is the most recent, unless the configuration sets another; that
  every change has its minutes is checked by `transfer-log`.
- **The recommended checklist per industry** is a draft from the plugin, with no regulatory source,
  and the report says it is not approved until a person approves it.
- **The folder structure** is suggested and never created among the organisation's documents
  ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)).

## Open decisions

1. ~~Moving Rostrum out of `criterio-portfolio` into a shared plugin of its own: the name and the
   timing.~~ Closed in [ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md):
   `criterio-server`, in 0.7.0.
2. Who reviews each industry's recommended checklist before offering it as anything more than a
   draft.
