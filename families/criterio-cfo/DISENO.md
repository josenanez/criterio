[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cfo · the family design

**Status: built and tested on synthetic material.** The 22 commands, the thirteen skills and the calculation
engine are built; the engine passes its deterministic test against the material of four industries
and two control entities (`tests/criterio-cfo/`), and the agents passed the full round on the six entities ([the rounds](../../tests/evidencias/familias/cfo/RONDAS.md)).
Scope in [ADR 0006](../../docs/decisions/0006-scope-cfo.md); how the work is split between the
engine and the agent, in [ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md).

**This is the family's design sheet**: the documents it processes, the signals the code calculates, each command with its input, process and report, and the decisions taken. What the family does, how it is installed, its records and their invariants, the folder structure, Rostrum, the cadence, the tests and the roadmap are on its [page](README.md).

Three agents that extend the capacity of the finance function: they prepare the work of the close, the budget and
treasury, and check it against all of its evidence to flag what does not tie out, what has no
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

**Where this document comes from.** The tables of agents, signals, commands and figures
are not written here: they come from three sources, [`familia.json`](familia.json),
[`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json), which `scripts/familias.py`
writes into this design in both languages, into `FUENTES.es.md`, into the family page, into the
`criterio-finance` and `criterio-budget` READMEs and, with `scripts/criterio-familias.mjs`, into the portal. A gate in
`scripts/verificar.py` fails if any copy does not tie out, if a command cites a folder that is not
in the structure or if it relies on a source still to be verified.

**What people ask most** is in [`PREGUNTAS.md`](PREGUNTAS.md), and **where it is going**, in the [roadmap](README.md#roadmap).

## One agent per role

<!-- cfo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Controller | **Clara** — from *clarus*: the books say what the supporting documents say | `criterio-finance` | The monthly close with its checklist and evidence, bank and account reconciliations, e-invoices against the books, and the auditor's package |
| FP&A | **Tomás** — “the twin”: puts the budget next to its twin, actual spend | `criterio-budget` | The approved budget against actual and committed spend, the year-end forecast, budget transfers and the budget committee pack |
| Treasury | **Áurea** — from the Latin *aureus*, “golden”: the cash | `criterio-treasury` | Cash against its minimum and projection, each scheduled payment against who may approve it, currency exposure against its limit, and debt against its maturity and its covenants |
<!-- /cfo:agentes -->

As in the PMO family, the two never talk to each other: they talk through their records. The records and the invariants that govern them, on the [family page](README.md#the-agents-and-their-records).

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

The DIAN (F-01) and SRI (F-04) formats are taken from their official technical source and confirmed
field by field before the reader is written ([ADR 0006](../../docs/decisions/0006-scope-cfo.md),
rule 2). Where each document goes, in the [recommended folder structure](README.md#the-recommended-folder-structure).

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

**Áurea · Treasury**

| Signal | Raised when |
|---|---|
| `cash_below_minimum` | The balance of an account or of consolidated cash falls below the minimum the policy sets |
| `cash_vs_forecast` | An account's actual balance deviates from its projection by more than the threshold |
| `fx_exposure_over_limit` | The position in another currency, converted at the policy's rate, exceeds its limit |
| `payment_without_approval` | A scheduled payment lacks the approvals the policy requires for its amount |
| `signatory_without_authority` | Whoever approves a payment lacks the authority in the signing-authority matrix, or is not in it |
| `covenant_at_risk` | A debt-contract ratio, calculated from the trial balance Clara closes, crosses its limit or comes within the margin of it |
| `maturity_near` | A debt obligation or an investment matures within the configured days |
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
| 0 | `finance-setup` | The root folder. Questions: entity and NIT or RUC, country, IFRS group (F-05, F-06, F-15), ERP, currency, period, thresholds, who approves, chart of accounts | Inventory of what is there; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder (what is there, what is missing, what is out of place and where it would go); checklist loaded or recommended; the first close record |
| 1 | `close-scan` | The whole period | Extracts each document's text with its fingerprint; only reprocesses what changed; updates the record with the citation of every data point | What changed in the period; what was added to the record; the new signals; what could not be processed and why |
| 2 | `close-status` | `00-referencia/checklist-cierre.xlsx`, `40-soportes/` and the record | Matches each task with its evidence, its date and its dependencies; calculates evidenced progress weighted by criticality | Declared status against evidenced status; task table ordered by criticality and due date: done with evidence, done without evidence, overdue, on time, blocked by another; the close's critical path |
| 3 | `bank-reconcile` | Each folder in `20-bancos/`: statement and ledger, with date, description, reference, amount and balance | Matches by exact reference, then by amount and date within the configured window, then by amount; classifies every open item | Per account: balance per bank, deposits in transit, outstanding cheques, unrecorded bank notes and balance per books, with the unexplained difference (it must be zero); open items by age (0–30, 31–60, 61–90 and over 90 days) |
| 4 | `account-reconcile` | `10-contabilidad/`: the general ledger and `auxiliares/` for receivables, payables, inventory, fixed assets and intercompany | The logic of `bank-reconcile`: the general-ledger balance against the subledger balance of each account, and open items with their age | Per account: balance per general ledger, balance per subledger, the difference and the items that explain it by age; the accounts whose reconciliation was not updated in the period |
| 5 | `ledger-check` | `10-contabilidad/`: trial balance and general ledger; the chart of accounts in `00-referencia/` | Debits against credits; opening balance plus movements against closing balance; ledger against trial balance, account by account; balances contrary to the nature declared by the organisation's chart of accounts | The overall tie-out; differences by account with their amount; accounts with a balance contrary to their nature |
| 6 | `einvoice-check` | `30-facturacion/` and the accounting entries of the accounts the configuration links to sales and purchases | Processes each XML with its official structure (F-01, F-04, F-13); matches by number, NIT or RUC and amount, and finds duplicates by CUFE, access key or series and number | Invoices without an entry, entries without an invoice, differences in amount or tax, duplicates; no tax opinion: whatever is a tax judgement is left as a question for the person |
| 7 | `audit-pack` | `50-auditoria/` and the record | Matches each request with its answer and its supporting documents | The package index: request, answer, cited support and status (answered with support, answered without support, unanswered, overdue); moves or copies no files |
| 8 | `finance-wake` | The configuration and the record | Decides what is due by cadence: daily during the close window, weekly outside it | What ran and what it found; if nothing is due, it stays silent |
<!-- /cfo:comandos-clara -->

### Account reconciliation

Reconciling accounts against their subledgers —receivables, payables, inventory, fixed assets,
intercompany— is the controller's work, so it belongs to Clara and to this plugin, not to another:
it is `account-reconcile`, with the logic of `bank-reconcile`. Consolidating several entities is
outside the first version.

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

## Áurea's commands, in order of importance

Áurea shares the engine, the folder and the period with Clara ([ADR 0016](../../docs/decisions/0016-tesoreria-tercer-agente-cfo.md)): she takes the statements Clara reconciles and calculates the covenants from the trial balance Clara closes. She never moves money or logs into a bank portal.

<!-- cfo:comandos-aurea · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `treasury-setup` | The root folder, the same as Clara's and Tomás's. Questions: entity and period, the accounts in another currency, the thresholds for deviation, maturity and covenant margin, where the state is kept and the terms | Inventory of what is there: which accounts have a statement in `20-bancos`, whether there is a payment schedule and a projection in `60-tesoreria`, and whether `00-referencia` holds the policy, the signing-authority matrix, the debt register and the covenants; creates, moves or renames nothing | Configuration saved; inventory by folder; the first cash position |
| 1 | `treasury-scan` | The statements in `20-bancos`, the payment schedule and projection in `60-tesoreria`, the policy, matrix, debt register and covenants in `00-referencia`, and the trial balance in `10-contabilidad` | Processes each table with its fingerprint; reprocesses only what changed; calculates the seven signals | What changed; the new signals; what could not be processed and why |
| 2 | `cash-position` | The period's statements, the projection and the policy | The last balance of each account against its minimum and its projection; consolidated cash; the position in other currencies converted at the policy's rate | By account: balance, minimum, projected and deviation; consolidated cash; exposure by currency against its limit |
| 3 | `payment-check` | The payment schedule, the policy and the signing-authority matrix | Each payment against the approvals the policy requires for its amount and against the authority of each approver | By payment: amount, who approved and how many approvals it requires; those without them and who signed without authority |
| 4 | `debt-watch` | The debt register, the covenants and the trial balance of the period Clara closes | The days left on each obligation and investment; each covenant calculated from the trial balance, against its limit | The covenants with their value, limit and status; the obligations by maturity |
| 5 | `treasury-wake` | The configuration and the tables | Decides what is due: payments in the next five days, obligations entering their maturity window and a weekly review | What ran and what it found; if nothing is due, it stays silent |
<!-- /cfo:comandos-aurea -->

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
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Ventana Research / ISG), C-02 (KPMG), C-03 (APQC), C-04 (Gartner), C-05 (Association for Financial Professionals).
<!-- /cfo:cifras -->

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
