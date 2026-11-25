[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cro · the family design

**Status: built and tested, in the lab (version 0.2.0).** The commands, the skills and the calculation engine
are built on the common core; the engine passes its deterministic test against the material in
`tests/criterio-cro/`. In 0.2.0, the two agents ran on every entity in the material, with a key they never see: [the rounds](../../tests/evidencias/familias/cro/RONDAS.md). Scope in [ADR 0035](../../docs/decisions/0035-la-familia-cro.md).

**This is the family's design sheet**: the signals the code calculates, each command with its input,
process and report, and the decisions taken. What the family does, how it is installed, the folder
structure and the roadmap are on its [page](README.md).

The language model (LLM) extracts; the code calculates; the decision —approving a breach, setting a limit,
rating a risk— is always the board's, the risk committee's and the areas'. **The agents process exports**:
they never connect to a system or calculate capital, value at risk or expected loss.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json).

## One agent per role

<!-- cro:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Risk appetite | **Severo** — from the Latin *severus*, the one who makes no concessions: each exposure against its limit | `criterio-risk-appetite` | The appetite statement against its limits and each limit against the exposure the areas report: a limit breached with no plan or approval, a late report, a limit with no owner or past its review, a high risk in the register with no limit or indicator and a statement the board has not reviewed within the framework's period |
| Indicators and events | **Casandra** — the one who foretold what was coming: each indicator that warns ahead | `criterio-risk-events` | The key risk indicators against their thresholds and the loss event database against its records: an indicator on alert with no action, one not reported, an event with no cause, amount or process, one registered late, one repeating in the same process and one missing from the risk register |
<!-- /cro:agentes -->

## The signals: what the code calculates

<!-- cro:senales · generado por scripts/familias.py; no se edita a mano -->
**Severo · Risk appetite**

| Signal | Raised when |
|---|---|
| `limit_breached_without_plan` | An exposure exceeds its limit and has no action plan or approval of the breach |
| `limit_without_owner` | A limit in the framework has no owner |
| `limit_review_overdue` | A limit is past its review date |
| `exposure_report_late` | An area reported its exposure after the deadline the framework sets |
| `risk_without_limit` | A risk rated high or critical in the register has no limit or key indicator |
| `appetite_statement_outdated` | The appetite statement has not had the board's review within the period the framework sets |

**Casandra · Indicators and events**

| Signal | Raised when |
|---|---|
| `kri_alert_without_action` | A key indicator is at its alert or limit threshold and has no recorded action |
| `kri_not_reported` | A key indicator has no value for the period |
| `loss_event_incomplete` | A loss event has no cause, amount or process |
| `loss_event_registered_late` | An event was registered after the policy's deadline from its discovery |
| `loss_event_repeated` | The same type of event repeats in the same process within the policy's window |
| `loss_event_risk_unmapped` | An event does not belong to any risk in the register |
<!-- /cro:senales -->

## Severo's commands, in order of importance

<!-- cro:comandos-severo · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `appetite-setup` | The root folder. Questions: entity and its tax ID, country, the last closed period and the framework's deadlines: the days to report exposure and how often, in months, the board reviews the statement | Inventory of what is there; processes the risk register, the limits and the indicators in `00-marco/` and the exposure in `10-exposicion/`, and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `appetite-scan` | The statement and the framework in `00-marco/`, the minutes in `40-actas/`, the exposure in `10-exposicion/` and the period's record | Brings into the record the date the board reviewed the appetite statement and each breach the committee approved, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `limit-check` | The limits in `00-marco/`, the period's exposure and the action plans in `10-exposicion/`, and the approved breaches in the record | Each reported exposure against its maximum or minimum limit; the breach, against its action plan or its approval; each report, against the framework's deadline | The limits breached with no plan or approval and the late reports, with the difference and the days |
| 3 | `framework-check` | The limits in `00-marco/` and the record —the appetite statement with its last board review— | Each limit against its owner and its review date, and the statement against the period in which the board reviews it | The limits with no owner or past their review, and the overdue statement, with the days |
| 4 | `coverage-check` | The risk register, the limits and the indicators in `00-marco/` | Each risk rated high or critical in the register against the limits and key indicators that measure it | The high risks with no limit or indicator, with their row |
| 5 | `appetite-wake` | The configuration and the run log | Decides whether the limits need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cro:comandos-severo -->

## Casandra's commands, in order of importance

<!-- cro:comandos-casandra · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `events-setup` | The root folder. Questions: entity and its tax ID, country, the last closed period and the policy's deadlines: the days to register an event and the window in which two events count as repeated | Inventory of what is there; processes the indicators in `00-marco/`, their values in `20-indicadores/` and the event database in `30-eventos/`, and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `events-scan` | The minutes in `40-actas/`, the values and actions in `20-indicadores/`, the event database in `30-eventos/` and the period's record | Brings into the record each action on an indicator agreed in the minutes, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `kri-check` | The indicators in `00-marco/`, their values and actions in `20-indicadores/`, and the actions in the record | Each key indicator with its value for the period, against its alert and limit thresholds in the direction the framework sets; the one on alert, against its action | The indicators on alert with no action and those with no value for the period |
| 3 | `event-check` | The loss event database in `30-eventos/` | Each event against its cause, amount and process, and its registration date against the policy's deadline from discovery | The incomplete events and those registered late, with the days |
| 4 | `pattern-check` | The event database in `30-eventos/` and the risk register in `00-marco/` | Events of the same type in the same process within the policy's window, and each event against the register risk it belongs to | The repeated events, with their amount, and those missing from the register |
| 5 | `events-wake` | The configuration and the run log | Decides whether the events need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cro:comandos-casandra -->

## Third-party figures

<!-- cro:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte), C-02 (AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte), C-03 (AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte).
<!-- /cro:cifras -->

## Closed decisions

- The names, Severo and Casandra, and the structure: two agents, their twelve signals and their commands (decision 0035).
- Here CRO is Chief Risk Officer, the second line; the commercial function is the CCO family (decision 0022).
- It processes exports and never connects to a system; it does not calculate capital, value at risk or expected loss: it processes the figures the areas and the organisation's models report.
- The direction of each limit —maximum or minimum— and of each indicator —higher or lower is worse— is given by the framework's table: a liquidity indicator is breached from below.
- Supervisory regulation is cited only for a supervised entity in its country: the Financial Superintendency in Colombia (F-10), the SBS in Peru (F-11) and the National Monetary Council in Brazil (F-12).
- COSO ERM 2017 stays out of 0.1.0 until verified in its text.
