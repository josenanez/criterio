[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cto · the family design

**Status: stable, at version 0.2.0, not yet launched.** The commands, the skills and the calculation engine
are built on the common core; the engine passes its deterministic test against the material in
`tests/criterio-cto/`. The engine passes its deterministic test against all the material; in 0.2.0, round 1 in Colombia, Mexico and Chile: 96 signals and 267 data items, with a floor of 96.1% on signals and 98.5% on data, and no control with a signal: [the rounds](../../tests/evidencias/familias/cto/RONDAS.md). Scope in [ADR 0037](../../docs/decisions/0037-la-familia-cto.md).

**This is the family's design sheet**: the signals the code calculates, each command with its input,
process and report, and the decisions taken. What the family does, how it is installed, the folder
structure and the roadmap are on its [page](README.md).

The language model (LLM) extracts; the code calculates; the decision —approving a change, granting an asset
exception, choosing a vendor— is always the change board's, the architecture board's, the technology office's
and legal's. **The agents process documents and exports**: they never connect to a tool, the cloud or a server,
and they do not process security, which belongs to the CISO family.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json).

## One agent per role

<!-- cto:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Changes and service | **Fausto** — from the Latin *faustus*, the one who brings good fortune: each change that goes well | `criterio-changes` | Each production change against its approval and review, each deployment against its change, each major incident against its problem and each service against its agreed level: a change not approved or approved afterwards, an emergency change with no review, a deployment with no change, a failed change with no review, a major incident with no cause and a service below its level |
| Assets and vendors | **Domingo** — from the Latin *dominicus*, the owner's: each asset with whoever answers for it | `criterio-assets` | The asset inventory against its owners and the manufacturer's support, the licences against their use, each vendor against its service level and the cloud against its budget: an asset with no owner, one past its end of support with no approved exception, a licence shortfall and a surplus, a vendor breach with no credit on the invoice and a cloud bill above its budget |
<!-- /cto:agentes -->

## The signals: what the code calculates

<!-- cto:senales · generado por scripts/familias.py; no se edita a mano -->
**Fausto · Changes and service**

| Signal | Raised when |
|---|---|
| `change_without_approval` | A normal change was implemented without its change authority's approval, or before it |
| `emergency_change_without_review` | An emergency change has no post-implementation review within the policy's deadline |
| `deployment_without_change` | A production deployment matches no registered change |
| `failed_change_without_review` | A failed or rolled-back change has no post-implementation review |
| `major_incident_without_problem` | A major incident has no problem record with its cause within the policy's deadline |
| `service_below_level` | A service's availability in the period fell below the level agreed in the catalogue |

**Domingo · Assets and vendors**

| Signal | Raised when |
|---|---|
| `asset_without_owner` | An asset in the inventory has no owner |
| `asset_out_of_support` | A production asset is past its manufacturer's end-of-support date with no current approved exception |
| `license_shortfall` | A software's licences in use exceed those purchased |
| `license_unused` | A software's unused paid licences exceed the policy's threshold |
| `vendor_breach_without_credit` | A vendor fell below its service level and its invoice for the period does not carry the credit the contract sets |
| `cloud_over_budget` | A cloud account's bill exceeds its budget plus the policy's tolerance |
<!-- /cto:senales -->

## Fausto's commands, in order of importance

<!-- cto:comandos-fausto · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `changes-setup` | The root folder. Questions: entity and its tax ID, country, the period and the policy's deadlines: the days to review an emergency change and to register a major incident's problem | Inventory of what is there; processes the service catalogue in `00-politica/`, the changes and deployments in `10-cambios/` and the incidents, problems and availability in `20-servicio/`, and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `changes-scan` | The change board minutes in `10-cambios/`, the tables in `10-cambios/` and `20-servicio/`, and the period's record | Brings into the record each change approval —its authority and date— and each post-implementation review recorded in the minutes, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `change-check` | The change export and the deployment log in `10-cambios/`, and the record —the approvals and reviews— | Each normal change implemented against its approval; each emergency change and each failed or rolled-back change against its review within the policy's deadline; each production deployment against the change that authorises it | The changes with no approval or approved afterwards, the emergency and failed ones with no review, and the deployments with no change, with the days |
| 3 | `incident-check` | The incidents and problems in `20-servicio/` | Each major incident in the period against the problem record that cites it and its cause, within the policy's deadline | The major incidents with no problem or with a problem with no cause, with the days |
| 4 | `service-check` | The service catalogue in `00-politica/` and the period's availability in `20-servicio/` | Each service's availability in the period against the level agreed in the catalogue | The services below their level, with the difference |
| 5 | `changes-wake` | The configuration and the run log | Decides whether the changes need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cto:comandos-fausto -->

## Domingo's commands, in order of importance

<!-- cto:comandos-domingo · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `assets-setup` | The root folder. Questions: entity and its tax ID, country, the period and the policy's thresholds: the share of unused licences it tolerates and the tolerance over the cloud budget | Inventory of what is there; processes the inventory and licences in `30-activos/`, the vendors' compliance and invoices in `40-proveedores/` and the bill and budget in `50-nube/`, and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `assets-scan` | The architecture board minutes in `30-activos/`, the contracts in `40-proveedores/`, the tables in `30-activos/`, `40-proveedores/` and `50-nube/`, and the period's record | Brings into the record each approved exception for an unsupported asset and each service level in a contract, with its credit, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `asset-check` | The asset inventory in `30-activos/` and the record —the approved exceptions— | Each asset against its owner, and each production asset against its manufacturer's end-of-support date and the exception that covers it | The assets with no owner and those past their end of support with no exception, with the days |
| 3 | `license-check` | The licences in `30-activos/` | Each software's purchased licences against those in use, and the surplus against the policy's threshold | The software with fewer licences than use and the software with unused paid licences above the threshold, with the difference |
| 4 | `vendor-check` | The record —each contract's service levels—, and the compliance and invoices in `40-proveedores/` | Each vendor's compliance in the period against its contract level; the breach, against the credit on its invoice | The vendors that breached with no credit on the invoice, with the level, the measured value and the amount |
| 5 | `cloud-check` | The bill and budget in `50-nube/` | The period's cloud bill, by account, against its budget and the policy's tolerance | The cloud accounts above their budget, with the difference |
| 6 | `assets-wake` | The configuration and the run log | Decides whether the assets need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 7 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cto:comandos-domingo -->

## Third-party figures

<!-- cto:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Flexera), C-02 (Uptime Institute), C-03 (Uptime Institute).
<!-- /cto:cifras -->

## Closed decisions

- The names, Fausto and Domingo, and the structure: two agents, their twelve signals and their commands (decision 0037).
- Technology comes in through what lives in documents —changes and service, assets and vendors—; the service management, inventory and cloud tools, only through their exports.
- Security is not this family's: vulnerabilities, controls and security incidents belong to the CISO (decision 0023).
- A standard change is pre-approved and needs no per-change approval; an emergency change is reviewed afterwards, within the policy's deadline.
- Availability is compared with the level agreed in the service catalogue: higher is better. A vendor's compliance, with its contract level, in the same direction.
- The Financial Superintendency's External Circular 005 of 2019 (F-10) is cited only for an entity in Colombia with agreed service levels; ITIL 4, COBIT 2019 and the regulation of Peru and Brazil stay out of 0.1.0 until verified.
- Each defect is planted more than once from the material's first version, so the family passes 73 signals (decision 0020).
