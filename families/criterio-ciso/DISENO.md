[Español](DISENO.es.md) · [← The family](README.md)

# criterio-ciso · the family design

**Status: under construction (version 0.1.0).** The twenty commands, the seven skills and the calculation
engine are built on the common core; the engine passes its deterministic test against the banking,
retail, healthcare and technology material (`tests/criterio-ciso/`), and the round with the agents is the
next step, in 0.2.0. Scope in [ADR 0023](../../docs/decisions/0023-la-familia-ciso.md) (Spanish).

**This is the family's design sheet**: the documents it processes, the signals the code calculates, each
command with its input, process and report, and the decisions taken. What the family does, how it is
installed, its records and invariants, the folder structure, Rostrum, the cadence, the tests and the
roadmap are on its [page](README.md).

Three agents that extend the capacity of information security: they process the statement of
applicability, each control's evidence, the scanner exports, the incident and test reports, and contrast
them against the organisation's policy, notification matrix and registers. The language model (LLM)
extracts; the code calculates; the decision —accepting a risk, approving an exception, notifying— is
always a person's.

**Unlike the CFO or the CLO, the role is defined on international standards**, not on each country's law:
the NIST CSF 2.0 orders the family (F-02) and NIST SP 800-61 Rev. 3 the incident response (F-04). Each
country's regulation —the financial supervisor's circular, the data protection law— goes into the
organisation's notification matrix; the engine does not carry it.

**How they work.** Automated: they process the documents, calculate the signals and prepare each
deliverable without intervention. Semi-automated when a data point is missing that no document carries —a
deadline the policy does not state, which scanner column carries each field—: then they ask the person,
say what they asked and carry on with the answer.

**Sources.** Every source used to process —the role framework, the family's frameworks, the CVSS scale,
the KEV catalog format, third-party figures— is in [`FUENTES.es.md`](FUENTES.es.md) (Spanish) with its
version, link, consultation date and status.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and
[`fuentes.json`](fuentes.json), which `scripts/familias.py` writes into this design, `FUENTES.es.md`, the
family page, the plugin READMEs and, with `scripts/criterio-familias.mjs`, the portal.

**What is asked most**, in [`PREGUNTAS.md`](PREGUNTAS.md) ([Español](PREGUNTAS.es.md)), and **where it is
heading**, in the [roadmap](README.md#roadmap).

## One agent per role

<!-- ciso:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Governance and controls | **Alexis** — from the Greek *Aléxios*, “the one who defends”: every control against the evidence that it operated | `criterio-security` | The statement of applicability against the evidence: every applicable control with its owner and the evidence that it operated within its frequency, each system's access reviews, each critical third party's assessments and the risk acceptances past their date |
| Vulnerabilities | **Guillermo** — from the Germanic *Wilhelm*, “resolute protector”: every vulnerability against the deadline to fix it | `criterio-vulnerability` | Every vulnerability in the scanner exports against its severity's deadline in the policy, the KEV catalog, the approved exceptions, the closures no scan proves and the inventory assets no scan covers |
| Response and recovery | **Amparo** — from the Latin *ante parare*, “to prepare ahead, to protect”: every incident against the deadlines that were committed | `criterio-resilience` | Every incident against the policy's deadlines and the notification matrix: its severity's containment, each notification to the supervisor, the data authority or the customers, and its post-incident review; and the continuity, recovery and restore tests against their calendar |
<!-- /ciso:agentes -->

## The documents they process

| Document | Expected format | Agent |
|---|---|---|
| The statement of applicability: each control with whether it applies, its status, its owner and its frequency | Excel or CSV | Alexis |
| The systems table with how often their access is reviewed, and the third-party register with the critical ones and their assessment | Excel or CSV | Alexis |
| The risk register, with the decision on each risk and its review date | Excel or CSV | Alexis |
| Each control's evidence, each access review and each third-party assessment | Any format, with the control, system or third party in the name | Alexis |
| The vulnerability management policy, with each severity's deadline | Word or PDF | Guillermo |
| Each scanner export, with the scan date in the name | CSV or Excel, with its column mapping if not recognised | Guillermo |
| CISA's KEV catalog, as downloaded (F-06) | CSV | Guillermo |
| The asset inventory, the remediation tracker and the exceptions register | Excel or CSV | Guillermo |
| The incident response policy, with each severity's containment deadline and the post-incident review's | Word or PDF | Amparo |
| The notification matrix and the continuity calendar | Excel or CSV | Amparo |
| Each incident's report with its timeline and the record of each notification, its post-incident review and each test's report | Word, PDF or email, with the incident code at the start of the name | Amparo |

The columns each table needs, and their variants, are in the `security-intake` skill; how each scanner
export is processed, in `scanner-exports`. Where each document goes, in the
[recommended folder structure](README.md#the-recommended-folder-structure).

### What the engine processes and what the agent extracts

As in the other families ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)), the engine
processes the tables directly, and the agent extracts to the record what only a written document
carries: **a control's evidence** with the date it covers; **a system's access review** and **a third
party's assessment**; **an incident's timeline** with the time of detection, containment and closure, and
**each notification** with its record; **each test** with its date and result. In the setup, the agent
extracts each severity's deadlines from the policy, with their citation. Every data point with its
citation.

**What is never processed.** Credentials, keys and backups —by extension or by name— are out by default:
the engine lists them and every report says which it excluded.

## The signals: what the code calculates

<!-- ciso:senales · generado por scripts/familias.py; no se edita a mano -->
**Alexis · Governance and controls**

| Signal | Raised when |
|---|---|
| `control_without_evidence` | An applicable control in the statement is marked as implemented and has no evidence that it operated |
| `control_evidence_stale` | The latest evidence of a periodic control is older than its frequency |
| `soa_control_unassigned` | An applicable control has no owner |
| `access_review_overdue` | A system's access review is past its date, or there is none |
| `third_party_assessment_overdue` | A critical third party's security assessment is past its date, or there is none |
| `risk_acceptance_expired` | A risk acceptance is past its review date |

**Guillermo · Vulnerabilities**

| Signal | Raised when |
|---|---|
| `vuln_past_sla` | A vulnerability is still open past its severity's deadline in the policy, with no current exception |
| `kev_past_due` | A vulnerability in the KEV catalog is still open past its remediation date |
| `vuln_closed_without_rescan` | A vulnerability is marked closed and no later scan shows it fixed |
| `vuln_exception_expired` | A remediation exception is past its expiry and the vulnerability is still open |
| `asset_not_scanned` | An inventory asset does not appear in any scan within the configured window |

**Amparo · Response and recovery**

| Signal | Raised when |
|---|---|
| `incident_response_late` | An incident was contained after its severity's deadline in the policy, or is still not contained past it |
| `incident_notification_late` | A notification the matrix requires —to the supervisor, the data authority, the customers— was made late or not at all |
| `incident_without_review` | A closed incident has no post-incident review within the deadline |
| `continuity_test_overdue` | The continuity or recovery plan test is past its date, or there is none |
| `restore_test_overdue` | A critical backup's restore test is past its date, or there is none |
<!-- /ciso:senales -->

The remediation, containment and review deadlines, each notification's deadline and the frequency of each
review and test come from the organisation's policy, matrix and registers. The scan window is
configuration, with a declared default. The KEV catalog's remediation date comes with the catalog, and is
set by a directive for United States federal agencies (F-07): for the organisation it is a reference.

## The three classes, as in the PMO family

**A · What it does that takes someone's time today:** preparing the control evidence for the audit,
building the report of vulnerabilities past their deadline for the committee, reconstructing an
incident's timeline for the supervisor, and keeping the test calendar.

**B · What it does that is not done today:** checking every applicable control, not a sample, against its
evidence; crossing every finding of every scan with the catalog of what is exploited; proving every
closure with a later scan; putting every notification next to its deadline with the time of its record.

**C · What it does not do:** it does not run a scan or connect to a system; it does not accept a risk or
approve an exception; it does not declare a control met or rate maturity; it does not certify against
ISO/IEC 27001; it does not notify anyone or declare an incident; it does not run a test or a restore; it
does not open credentials, keys or backups.

## Alexis's commands, in order of importance

<!-- ciso:comandos-alexis · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `security-setup` | The root folder. Questions: entity and its tax ID, country, the period, where the statement of applicability in `00-referencia/` is and which column carries the control, whether it applies, its status, its owner and its frequency, the systems table with how often their access is reviewed, the third-party register with the critical ones and how often they are assessed, and the risk register in `40-riesgos/` | Inventory of what is there; lists what it excludes as a credential, key or backup; recognises each table's columns; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; what was excluded and why; the missing columns; the period's first record |
| 1 | `security-scan` | The whole `10-controles/`, `20-accesos/` and `30-terceros/` | The agent takes to the period record each piece of evidence in `10-controles/` with its control and the date it covers, each review in `20-accesos/` with its system, its date and who reviewed it, and each assessment in `30-terceros/` with its third party, its date and its result, every data point with its citation; the engine validates the record and says which document is not in it | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `soa-status` | The statement of applicability in `00-referencia/` | Each control in the statement with whether it applies, its status, its owner and its frequency; the engine does not rate maturity or declare a control met | The applicable controls without an owner, with their row; the full statement |
| 3 | `control-evidence` | The statement of applicability and the period record | Each applicable control marked as implemented against the evidence in the record: whether it has any, and whether the latest falls within its frequency | The controls without evidence and those whose evidence has lapsed, each with its citation and its owner |
| 4 | `access-reviews` | The systems table in `00-referencia/` and the period record | Each system against how often its access must be reviewed: the latest review in the record and when the next one was due | The systems with an overdue review or none at all, with their citation |
| 5 | `third-parties` | The third-party register in `00-referencia/` and the period record | Each critical third party against how often its security must be assessed: the latest assessment in the record, its result and when the next one was due | The critical third parties with an overdue assessment or none at all, with their citation |
| 6 | `risk-register` | The risk register in `40-riesgos/` | Each risk with its decision; the accepted ones against their review date. The agent never accepts or closes a risk | The acceptances past their review date, with who accepted them and their row |
| 7 | `security-wake` | The state and the new documents | If there are new documents or a week has passed, the full review; if there are open signals, their group's report; a question somebody left in Rostrum | What ran and why, or that nothing was due |
<!-- /ciso:comandos-alexis -->

## Guillermo's commands, in order of importance

<!-- ciso:comandos-guillermo · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `vuln-setup` | The root folder. Questions: entity and its tax ID, country, the period, the remediation deadline for each severity in the vulnerability management policy in `00-referencia/`, which scanner produces the exports in `50-escaneos/` and, if their columns are not recognised, which column carries the asset, the vulnerability, the severity or the CVSS score and the first detection, how many days without a scan leave an asset uncovered, and whether its reports are published in Rostrum | Inventory of what is there; lists what it excludes; recognises the columns of each scanner export and of the KEV catalog (F-06); the agent extracts each severity's deadline from the policy, with its citation; creates, moves or renames nothing | Configuration saved, with the deadlines and their citation; inventory by folder; each export with its date, its assets and its findings; the missing columns |
| 1 | `vuln-scan` | The whole `50-escaneos/` and `60-remediacion/` | The code processes each export with its date: what is open is what each asset's latest scan found, with the date it was first detected; the severity is the scanner's or, if it only gives the score, the CVSS scale's (F-05); it crosses the KEV catalog (F-06), the tracker and the exceptions | The scans with their assets and findings; what is open; the KEV catalog used; the new signals; what could not be processed and why |
| 2 | `vuln-sla` | The exports in `50-escaneos/`, the exceptions in `60-remediacion/` and the deadlines in the configuration | Each open vulnerability against its severity's deadline, counted from its first detection; a current exception suspends it; an expired exception on something still open is a signal | The vulnerabilities past their deadline and the expired exceptions, each with its asset, its severity, its days and its citation |
| 3 | `kev-check` | The exports in `50-escaneos/` and CISA's KEV catalog (F-06) | Each open vulnerability whose CVE is in the catalog, against the remediation date the catalog gives; says whether its use in ransomware is known | The catalog's vulnerabilities still open past their date, with their asset and their citation |
| 4 | `scan-coverage` | The asset inventory in `00-referencia/`, the exports in `50-escaneos/` and the tracker in `60-remediacion/` | Each in-scope inventory asset against the latest scan that includes it and the configured window; each vulnerability closed in the tracker against the scans after its closure | The assets with no scan in the window; the closures no later scan proves or that the scan still finds; what was scanned outside the inventory |
| 5 | `vuln-wake` | The state and the new documents | If a new export, catalog or tracker arrived, or a week has passed, the full review; if there are open signals, their group's report; a question somebody left in Rostrum | What ran and why, or that nothing was due |
<!-- /ciso:comandos-guillermo -->

Guillermo's reports are not published in Rostrum unless `vulnerability.publish` says so.

## Amparo's commands, in order of importance

<!-- ciso:comandos-amparo · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `resilience-setup` | The root folder. Questions: entity and its tax ID, country, the period, the containment deadline for each severity and the days for the post-incident review in the incident response policy in `00-referencia/`, the notification matrix with each recipient, when it applies and its deadline, and the continuity calendar with each test, its type and its frequency | Inventory of what is there; lists what it excludes; the agent extracts each severity's deadline and the post-incident review's from the policy, with their citation; recognises the matrix's and the calendar's columns; creates, moves or renames nothing | Configuration saved, with the deadlines and their citation; inventory by folder; the missing columns; the period's first record |
| 1 | `resilience-scan` | The whole `70-incidentes/`, `80-revisiones/` and `90-continuidad/` | The agent takes to the period record each incident in `70-incidentes/` with its severity, the detection, containment and closure with their time, whether personal data or customers were affected, and each notification with its recipient, its time and its record; each review in `80-revisiones/` and each test in `90-continuidad/` with its date and result; every data point with its citation (F-04); the engine validates the record | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `incident-timeline` | The period record and the deadlines in the configuration | Each incident: the hours from detection to containment against its severity's deadline, and its post-incident review against the policy's days from closure | The incidents contained late or not contained, and the closed ones without a review or reviewed late, with their citation |
| 3 | `notifications` | The notification matrix in `00-referencia/` and the period record | Each incident against every row of the matrix that applies to it —by its severity, personal data or affected customers—: the recorded notification and its time against the deadline from detection. The agent notifies no one | The late notifications and the ones never made, with their recipient, their rule and their citation |
| 4 | `continuity-tests` | The continuity calendar in `00-referencia/` and the period record | Each test in the calendar —the continuity plan, the recovery plan, each critical backup's restore— against its frequency: the latest in the record, its result and when the next one was due | The tests that are overdue or never done, with restores apart, with their citation |
| 5 | `resilience-wake` | The state and the new documents | If a new incident, review or test arrived, or a week has passed, the full review; if there are open signals, their group's report; a question somebody left in Rostrum | What ran and why, or that nothing was due |
<!-- /ciso:comandos-amparo -->

## The common report format

The same as the other families, and the engine writes it: header, what needs attention, the command's own
result, what could not be processed —including what was excluded—, the questions it asked and the
sources.

## What is reused from the other families

- `texto.py` for Word, Excel, PowerPoint, PDF and email, `terminos.py` for accepting the terms, `rastro.py`
  for each run's trace and `raiz.py` for the root folder, copied by `scripts/sincronizar.py`.
- `nucleo.py` —tables, dates, inventory, signals and report—, copied from `criterio-finance`.
- The record's shape: a citation per data point, “not found” is valid.
- Terms per version with their receipt, the version register and the gates in `scripts/verificar.py`.
- Rostrum, `criterio-server`, to publish the reports, with what is private left out by default
  ([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md), ADR 0019).

What is new is its own engine, `seguridad.py`, with the standard library. It lives in `criterio-security`
and is copied to `criterio-vulnerability` and `criterio-resilience`, with the `security-intake` skill.

## How it is tested

Synthetic material in `tests/criterio-ciso/`: one banking, one retail, one healthcare and one technology
entity, in Colombia, Mexico, Peru and Chile, and two controls, with a key the engine never sees. Each of
the family's signals is planted at least once, with cases that look like a defect and are not; what is
planted and where, in [`tests/criterio-ciso/EVIDENCIA.md`](../../tests/criterio-ciso/EVIDENCIA.md)
(Spanish). The agent's extraction is tested in the round, on the same material.

## Third-party figures

<!-- ciso:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Verizon), C-02 (Verizon), C-03 (Verizon).
<!-- /ciso:cifras -->

## Closed decisions

- The scope, the three agents, their sixteen signals and what they never do (ADR 0023). José, 2026-10-30.
- The names, Alexis, Guillermo and Amparo, and the family's structure. José, 2026-10-30.
- The plugins: `criterio-security`, `criterio-vulnerability` and `criterio-resilience`.
- The first version processes any scanner export with its mapping; each product comes later from its
  verified source.

## Open decisions

1. The export format of Tenable, Qualys, Rapid7 and Microsoft Defender, each from its source.
2. ISO/IEC 27001:2022 (F-03) remains to be verified: the engine does not need it, because it takes the
   controls from the organisation's statement; if it is ever cited, it is verified first.
3. CISA's BOD 26-04 (F-07) remains to be verified on CISA's page; the engine does not apply its deadlines.
