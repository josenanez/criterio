[Español](DISENO.es.md) · [← The family](README.md)

# criterio-clo · the family design

**Status: built and tested on synthetic material.** The fourteen commands, the ten skills and the calculation engine are
built; the engine passes its deterministic test against the material of four industries and two
control entities (`tests/criterio-clo/`), and the agents passed the full round on the six entities ([the rounds](../../tests/evidencias/familias/clo/RONDAS.md)). Scope in
[ADR 0009](../../docs/decisions/0009-scope-clo.md).

**This is the family's design sheet**: the documents it processes, the signals the code calculates, each command with its input, process and report, and the decisions taken. What the family does, how it is installed, its records and their invariants, the folder structure, Rostrum, the cadence, the tests and the roadmap are on its [page](README.md).

Two agents that extend the capacity of the legal function: they process what the company signed and
what it committed to comply with, and check it against all of its evidence to flag what falls due,
what has no evidence, who signed without authority and what was paid outside what was agreed. The
large language model (LLM) extracts; the code calculates; the decision —to renew, to terminate, how
a clause or a regulation is read— is always made by a person.

First version: Colombia and Ecuador. **No legal opinion**: neither of them interprets a clause,
rules on the validity of a contract or says what a regulation requires. What an obligation requires
is defined by the organisation in its matrix, citing its source.

**How they work.** Automated: they process the documents, calculate the signals and prepare each
deliverable without intervention. Semi-automated when a data point no document carries is missing
—the entity, the notice days, who decides to renew—: then they ask the person, say what they asked
and carry on with the answer.

**Sources.** Every source used for processing —frameworks, regulations, third-party figures— is in
[`FUENTES.es.md`](FUENTES.es.md) (Spanish) with its version, its link, the date it was consulted and its
status. The design, the documentation and the tests cite those sources by their identifier.

**Where this document comes from.** The tables of agents, signals, commands and figures
are not written here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json)
and [`fuentes.json`](fuentes.json), which `scripts/familias.py` writes into this design in both
languages, into `FUENTES.es.md`, into the family page, into the plugins' READMEs and, with
`scripts/criterio-familias.mjs`, into the portal.

**What people ask most** is in [`PREGUNTAS.md`](PREGUNTAS.md), and **where it is going**, in the
[roadmap](README.md#roadmap).

## One agent per role

<!-- clo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Contracts | **Fidel** — from the Latin *fides*, the word given: what was signed is kept | `criterio-legal` | What was signed and on what terms: the contract register against its documents, expiries and renewal notices, obligations with their evidence, who signed with what authority, and what was paid against what was agreed and its guarantees |
| Compliance | **Constanza** — from the Latin *constantia*, “constancy”: compliance every day, not only on audit day | `criterio-compliance` | The organisation's obligations matrix against its evidence, policy reviews, new rules with their assessment, the whistleblowing channel with its deadlines, and the compliance obligations that contracts carry |
<!-- /clo:agentes -->

As in the PMO and CFO families, the two never talk to each other: they talk through their records.
Constanza takes from Fidel's records the compliance obligations that the contracts bring. The records and the
invariants that govern them, on the [family page](README.md#the-two-agents-and-their-records).

## The documents they process

| Document | Expected format | Agent |
|---|---|---|
| Contract register and payments export by contract | Excel or CSV, with the cut-off date in the name | Fidel |
| Signing-authority matrix: who signs what and up to what amount | Excel or CSV | Fidel |
| The signed contract and each amendment | Word or PDF with text | Fidel |
| Insurance policies and guarantees provided | PDF with text | Fidel |
| Counterparty's certificate of existence and legal representation | PDF with text | Fidel |
| Minutes or email in which someone decides to renew or terminate | Word, PDF, email | Fidel |
| Delivery records, reports and the evidence of each obligation | Any format, with the obligation's id at the start of the name | Fidel, Constanza |
| Compliance obligations matrix | Excel or CSV, in the defined model | Constanza |
| Policy index, and each policy | Excel or CSV; the policy, Word or PDF | Constanza |
| Regulatory register, bulletins and impact assessments | Excel or CSV; the bulletin, PDF or email | Constanza |
| Whistleblowing case register | Excel or CSV, with its dates only | Constanza |
| The period's compliance report | Word or PDF | Constanza |

The columns each table needs, and their variants, in the `legal-intake` skill. Where each document
goes, in the [recommended folder structure](README.md#the-recommended-folder-structure).

### What the engine processes and what the agent extracts

As in the CFO family ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)), the engine
processes the tables directly —the contract register, the payments, the signing-authority matrix,
the obligations matrix, the policy index, the regulatory register and the case register—, and the
agent extracts to the record what only a written document carries: **each contract**, with its
parties, value, dates, renewal, notice period, signatories, amendments, guarantees and obligations;
each insurance policy with its validity; the counterparty's certificate with its date; what the
compliance report declares and the new regulations in a bulletin. Every data point with its
citation.

## The signals: what the code calculates

<!-- clo:senales · generado por scripts/familias.py; no se edita a mano -->
**Fidel · Contracts**

| Signal | Raised when |
|---|---|
| `contract_expiring` | A contract expires within the configured days with no recorded decision to renew or terminate |
| `notice_deadline_near` | The non-renewal notice deadline of an auto-renewing contract falls within the configured days |
| `renewal_notice_missed` | The notice deadline of an auto-renewing contract passed with no recorded decision |
| `contract_expired_active` | The register reports as active a contract whose end date has passed |
| `register_mismatch` | A contract in the folder is not in the register, or a register row has no document |
| `register_differs_from_contract` | The register's value or dates differ from the document's |
| `contract_obligation_overdue` | A contract obligation is past its date with no evidence |
| `signed_without_authority` | The entity's signatory had no authority for the type or amount under the authority matrix |
| `unsigned_contract` | The document lacks both parties' signatures and the contract has already started |
| `counterparty_certificate_stale` | The counterparty's certificate was older than the configured days at signing |
| `payments_over_value` | Payments exceed the contract value plus its amendments |
| `payment_after_termination` | There are payments dated after the contract's end |
| `guarantee_missing` | The contract requires a guarantee and none was provided |
| `guarantee_expires_early` | The policy provided expires earlier than the contract requires |

**Constanza · Compliance**

| Signal | Raised when |
|---|---|
| `compliance_obligation_overdue` | A matrix obligation is past its deadline with no evidence |
| `compliance_done_without_evidence` | An obligation is marked done and no evidence supports it |
| `compliance_evidence_stale` | The latest evidence of a periodic obligation predates its window |
| `obligation_without_owner` | A matrix obligation has no owner |
| `obligation_without_source` | A matrix obligation cites no rule, contract or policy it comes from |
| `declared_compliance_vs_evidence` | The report declares the period compliant and there are open signals that status does not explain |
| `policy_review_overdue` | A policy is past its review date |
| `regulatory_change_unassessed` | A registered rule has gone longer than the configured days without an impact assessment |
| `applicable_norm_not_in_matrix` | An applicable rule has no obligation in the matrix |
| `report_case_overdue` | A whistleblowing case is past the configured response time |
| `contract_obligation_not_in_matrix` | A contract's compliance obligation is not in the matrix |
<!-- /clo:senales -->

The notice days, the maximum age of the certificate, the channel's deadline and the days to assess a
regulation are each organisation's configuration, with a declared default value; none of them is a
regulation.

## The three classes, as in the PMO family

**A · What it does, and today takes someone's time:** building the contract register, keeping the
calendar of expiries and notice periods, checking who signed each contract, matching payments
against what was agreed, preparing the compliance status against its evidence.

**B · What it does, and today nobody does:** checking every contract, not a sample, against the
signing-authority matrix; matching every payment against its contract's value and end date;
verifying each insurance policy against the validity the contract requires; keeping the obligations
matrix up to date with what the contracts oblige.

**C · What it does not do:** it does not interpret clauses or regulations; it does not rule on the
validity of a contract or a signature; it does not decide to renew or terminate; it does not draft
or negotiate; it does not answer whistleblowing cases or process data about who reported; it does
not declare the compliance status.

## Fidel's commands, in order of importance

<!-- clo:comandos-fidel · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `legal-setup` | The root folder. Questions: entity and NIT or RUC, country, the signing-authority matrix in `00-referencia/`, how many days ahead an expiry or a notice period is flagged, the maximum age of the counterparty's certificate and who decides to renew | Inventory of what is there; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the contracts in `contratos/` against those in the register; the first records |
| 1 | `contract-scan` | The whole `contratos/` and `10-registro/` | Extracts each document's text with its fingerprint and only reprocesses what changed; the agent takes to each contract's record its parties, value, dates, renewal, notice period, signatories, amendments, guarantees and obligations, every data point with its citation; the engine validates the record | What changed; which contracts are new; the new signals; what could not be processed and why |
| 2 | `contract-register` | `10-registro/registro-contratos` and the records | Matches the register with the folders and the records: contract with no register entry, register entry with no document, declared status against the end date, and the register's value and dates against what the document says | Per contract: declared status and status by its dates, and every difference between the register and the document |
| 3 | `obligations-calendar` | The records and each contract's `40-ejecucion/` | End date, deadline for the non-renewal notice (end date minus the notice days) and every dated obligation against its evidence in `40-ejecucion/`, with its id at the start of the name | The calendar for the coming days: expiries, notice periods and obligations; what is overdue without evidence and the notice periods that passed without a decision |
| 4 | `authority-check` | The records, `00-referencia/matriz-atribuciones` and `30-contraparte/` | Each of the entity's signatories against their authority on the signing date, by type and amount, amendments included; documents without both parties' signatures; the counterparty's certificate against the configured age on the signing date | Per contract: who signed, their authority and the amount; those without both parties' signatures; expired certificates; no opinion on the contract's validity |
| 5 | `contract-execution` | `10-registro/pagos`, the records and `20-garantias/` | What was paid against the value plus amendments; payments after the end date; the guarantees required against those provided, and their validity against what the contract requires | Per contract: value, paid, balance and last payment; each required guarantee with the one provided and its validity |
| 6 | `legal-wake` | The configuration and the records | Decides what is due: the expiries and notice periods entering the window, new documents and a weekly review | What ran and what it found; if nothing is due, it stays silent |
<!-- /clo:comandos-fidel -->

## Constanza's commands, in order of importance

<!-- clo:comandos-constanza · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `compliance-setup` | The root folder. Questions: entity, country, the obligations matrix in `00-referencia/` in the defined model (F-01), the period, the channel's response deadline, the days to assess a new regulation and, if the organisation uses Fidel, where his records are | Inventory of what is there; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; the matrix loaded and what each obligation is missing —owner, source—; the period's first status |
| 1 | `compliance-scan` | The entity's whole folder | Only reprocesses what changed; the agent takes to the record what the report in `20-reportes/` declares and the new regulations in the bulletins in `30-normativa/`, with their citation | What changed; what was added to the record; the new signals; what could not be processed |
| 2 | `compliance-status` | `00-referencia/matriz-obligaciones`, `10-evidencias/` for the period and earlier ones, and Fidel's records if there are any | Each obligation against its evidence within the window of its frequency and its deadline; those with no owner or source; the contracts' compliance obligations that the matrix does not have; declared against evidenced | Declared status against evidenced; table of obligations ordered by criticality and due date: done with evidence, done without evidence, overdue, on time |
| 3 | `policy-review` | `20-politicas/indice-politicas` | Each policy against its review date and its owner | Policies with an overdue review or no owner, and those coming up for review |
| 4 | `regulatory-watch` | `30-normativa/registro-normativo` and the new regulations in the record | Each registered regulation against its impact assessment within the configured days; those that apply without an obligation in the matrix | Regulations not yet assessed and those that apply without an obligation in the matrix; no opinion on the scope of any regulation |
| 5 | `reports-cases` | `40-canal/casos` | Each case against the configured response deadline | Open cases by age and those past their deadline; no data about who reported |
| 6 | `compliance-wake` | The configuration and the record | Decides what is due: obligations falling due within the window, new documents and a weekly review | What ran and what it found; if nothing is due, it stays silent |
<!-- /clo:comandos-constanza -->

## The common report format

The same as in the PMO and CFO families, and the engine writes it: header, what needs attention, the
command's own result, what could not be processed, the questions it asked and the sources.

## What is reused from the PMO and CFO families

- `texto.py` for Word, Excel, PowerPoint, PDF and email, `terminos.py` for accepting the terms,
  `rastro.py` for the trail of each run and `raiz.py` for the root folder, copied from the PMO
  family by `scripts/sincronizar.py`.
- `nucleo.py` —tables, dates, inventory, signals and report—, copied from `criterio-finance`.
- The shape of the record: a citation per data point, declared against evidenced, "not found" valid.
- Terms per version with their receipt, the version register and the gates of
  `scripts/verificar.py`.
- Rostrum, `criterio-server`, to publish the contract and compliance reports
  ([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

What is new is its own engine, `legal.py`, on the standard library: it processes the tables
directly, and the agent extracts to the record only what a written document carries. It lives in
`criterio-legal` and is copied to `criterio-compliance`, together with the `legal-intake` skill.

## How it is tested

Synthetic material in `tests/criterio-clo/`: four industries —banking and retail in Colombia,
cooperatives and mining in Ecuador— and one control per country, with a key the engine never sees.
Every family signal is planted at least once; what is planted and where, in
[`tests/criterio-clo/EVIDENCIA.md`](../../tests/criterio-clo/EVIDENCIA.md) (Spanish). The agent's
extraction is tested in the round, on the same material. The family is declared tested with a full
round.

## Third-party figures

<!-- clo:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (World Commerce & Contracting con Deloitte), C-02 (EY Law y Harvard Law School Center on the Legal Profession), C-03 (EY Law y Harvard Law School Center on the Legal Profession), C-04 (NAVEX).
<!-- /clo:cifras -->

## Closed decisions

- The roles —contracts and compliance— and the names, Fidel and Constanza. José, 2026-10-20.
- The plugins: `criterio-legal` for Fidel, the one already declared, and `criterio-compliance` for
  Constanza. José, 2026-10-20.
- No legal opinion in the first version. José, 2026-10-20.

## Open decisions

1. A recommended obligations matrix per industry, and who reviews it before offering it as anything
   more than a draft.
2. Public contracts, with their own rules on publication and guarantees, are left for another
   version.
