# criterio-cae · the internal audit family

**Three agents and a portal, around their records.** Each one extends a different person in internal
audit —whoever is responsible for the plan, for the engagements and for following up the findings— and
they share the entity's folder and methodology: each one writes only its own record.

[Español](README.es.md) · [← Criterio](../../README.md) · Apache 2.0

| | |
|---|---|
| **Scope** | An entity's audit plan against its risk matrix, its audit universe and its capacity; each engagement against its program, its working papers and its report; and each finding until it is closed, with its evidence, on the Global Internal Audit Standards |
| **Goal** | That every high risk has an engagement, that every finding can be traced to the paper that supports it and that every action plan reaches its closure with evidence that it was implemented |
| **Made up of** | [Prudencia](../../plugins/criterio-audit-plan/README.md) · [Justo](../../plugins/criterio-audit-work/README.md) · [Remedios](../../plugins/criterio-remediation/README.md) · [Rostrum](../../plugins/criterio-server/README.md) |
| **The backing** | The Global Internal Audit Standards and their topical requirements, the Three Lines Model, COSO 2013 and the regulation of internal audit in the financial sector, with their source and status: [`FUENTES.es.md`](FUENTES.es.md) |
| **Status** | Built, in testing: the engine tested on all its material, with its key and its control entities. The round with the three agents comes in 0.2.0. **Not yet tested on a specific organisation's documentation** |
| **Approach** | Documents and exports, never systems: no agent goes into the audited systems or the audit tool |
| **Commitment** | Generating, sharing and preserving knowledge is a professional obligation |
| **What it is not** | It does not replace the auditor: it issues no opinions, signs no reports, changes no finding's priority, closes no plans and accepts no risks |
| **Licence** | [Apache 2.0](../../LICENSE) |
| **What comes next** | The round with the three agents: [the roadmap](#roadmap) |

---

## What the family does

Internal audit is the area that works most against documents, because its product is an opinion backed
by evidence: every finding has to be traceable to the working paper that supports it, and every action
plan to the evidence that it was implemented. Today that traceability is checked by hand, engagement by
engagement. The family calculates it, with the structure of The IIA's Global Internal Audit Standards
(F-01) —cited by number and title, never by their text— and the organisation's methodology
([decision 0033](../../docs/decisions/0033-la-familia-cae.md)).

- **Prudencia** puts the plan next to the risk matrix and the audit universe, and tells you which high
  risk has no engagement, which unit went past its cycle and which change has no minutes.
- **Justo** puts each finding next to its criteria and its paper, and each report next to its papers.
- **Remedios** takes each finding to its closure: the overdue plan, the date that keeps moving, the
  closure with no evidence and the accepted risk that never reached the board.

## What remains with people

Deciding what to audit, concluding on internal control, setting a finding's priority, validating
evidence, closing a plan, accepting a risk and reporting to the committee. The agents say what is missing
and where; the opinion is always the auditor's.

## The recommended folder structure

<!-- cae:carpetas · generado por scripts/familias.py; no se edita a mano -->
One folder per entity, with its tax id at the start of the name. Inside it, the audit charter and methodology with the team, the plan with the audit universe, the risk matrix and the committee minutes, one folder per engagement with its program, working papers and report, and the follow-up of findings with their evidence.

```
auditoria/
└── <entidad>/
    ├── 00-referencia/
    ├── 10-plan/
    ├── 20-trabajos/
    └── 30-seguimiento/
estado-auditoria/
```

**`<entidad>/`** · What internal audit keeps for the entity

| Folder | What goes in | Agent |
|---|---|---|
| `00-referencia/` | The audit charter and methodology —the cycles, the priority scale, the follow-up deadlines—, the report of the last external quality assessment and the team: each auditor with their available hours and the roles they held | Prudencia, Justo, Remedios |
| `10-plan/` | The audit universe, the second line's risk matrix, the annual plan with its engagements and hours, and the committee minutes that approve and change it | Prudencia |
| `20-trabajos/` | One folder per engagement with its code: the work program, the index of working papers, the working papers and the report | Justo |
| `30-seguimiento/` | The findings and action-plan register, one folder per finding with its evidence and explanations of delay, the accepted-risk register and the reports of the statutory auditor, the external auditor and the supervisor | Remedios |

**`estado-auditoria/`** · What Prudencia, Justo and Remedios write: the configuration, each period's record, the reports and the indexes. No person edits it, and no agent writes anywhere else.
<!-- /cae:carpetas -->

A file without the expected format is not guessed at: it is reported with what it lacks.

## Installing the family

It needs Claude Code 2.1.110 or later; if something fails, [the step-by-step installation](../../docs/instalacion.md).

**The family installs in one go.** The `criterio-cae` plugin brings its agents and Rostrum, and
`/criterio-cae:cae-setup` configures them in order, in a single conversation: what has already been
answered is not asked again.

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-cae@criterio
/criterio-cae:cae-setup
```

Afterwards you ask each agent in your own words, without knowing what each command is called:
`/criterio-audit-plan:prudencia`, `/criterio-audit-work:justo` and `/criterio-remediation:remedios`
([decision 0027](../../docs/decisions/0027-cada-agente-se-pide-en-palabras.md)).

## What each agent is responsible for, and where its detail is

<!-- cae:familia-agentes · generado por scripts/familias.py; no se edita a mano -->
| | What it answers for | What it never does | Its page | Its tests |
|---|---|---|---|---|
| **Prudencia** · the audit plan | The audit plan against the audit universe and the risk matrix: high risks with no engagement, units past their cycle, an outdated risk assessment, the areas the plan has to consider, unapproved changes, late engagements, hours that do not add up, a missing topical requirement and the external quality assessment | It does not approve the plan, decide what is audited, issue an opinion or copy the text of the Standards | [criterio-audit-plan](../../plugins/criterio-audit-plan/README.md) · 9 commands, 3 skills | [results](../../tests/criterio-audit-plan/RESULTADOS.md) |
| **Justo** · audit engagements | Each engagement against its program and its working papers: an unapproved program, a finding without its criteria, condition, cause, effect or priority, a finding with no working paper, an unexecuted step, an unreviewed paper, a report that does not say what the papers say, a priority the methodology does not give and an auditor reviewing what they were in charge of | It does not issue an opinion, sign or approve a report, change a finding's priority, edit a working paper or rate people | [criterio-audit-work](../../plugins/criterio-audit-work/README.md) · 9 commands, 3 skills | [results](../../tests/criterio-audit-work/RESULTADOS.md) |
| **Remedios** · finding follow-up | Each finding until it is closed: an action plan with no owner or date, an overdue one with no evidence or explanation, a date pushed back again and again, a closure with no evidence or validation, a finding that comes back, an accepted risk that did not reach senior management or the board and an external finding missing from the register | It does not close a finding, validate evidence on its own, accept a risk or communicate anything to the committee: it prepares what the chief audit executive takes there | [criterio-remediation](../../plugins/criterio-remediation/README.md) · 8 commands, 3 skills | [results](../../tests/criterio-remediation/RESULTADOS.md) |
| **Rostrum** · the portal | Publishing what the agents write where the team will see it, and taking the question from whoever will not open a folder | **Never writes the state or recalculates anything**, and decides nothing | [criterio-server](../../plugins/criterio-server/README.md) · 3 commands, one for every family | [results](../../tests/criterio-server/RESULTADOS.md) |
<!-- /cae:familia-agentes -->

## How it is configured and how often each one runs

<!-- cae:configuracion · generado por scripts/familias.py; no se edita a mano -->
| | Prudencia | Justo | Remedios |
|---|---|---|---|
| **Installs as** | `criterio-audit-plan` | `criterio-audit-work` | `criterio-remediation` |
| **Instances** | One per entity | One per entity | One per entity |
| **Configured with** | `/criterio-audit-plan:plan-setup` | `/criterio-audit-work:work-setup` | `/criterio-remediation:remediation-setup` |
| **How long that takes** | Fifteen minutes | Fifteen minutes | Fifteen minutes |
| **What you have to tell it** | Entity and its tax ID, country, the period, the rotation cycle of each risk level, from which rating a risk is high, who approves the plan under the charter, the date of the last risk assessment and of the last external quality assessment | Entity and its tax ID, country, the period, the methodology's priority scale —each level with its impact and likelihood— and who approves the program and the papers | Entity and its tax ID, country, the period, how many times the methodology allows a plan's date to be pushed back, who validates a closure and who senior management and the board are for escalation |
| **Where it lands** | `.criterio/plan/<entity>/config.json`, written by the command | `.criterio/trabajos/<entity>/config.json`, written by the command | `.criterio/seguimiento/<entity>/config.json`, written by the command |
| **The one you put on a clock** | `/criterio-audit-plan:plan-wake` | `/criterio-audit-work:work-wake` | `/criterio-remediation:remediation-wake` |
| **What it does each day** | Decides whether the plan needs processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | Decides whether the engagements need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | Decides whether follow-up needs processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet |
| **What wakes it besides the clock** | A question somebody left in Rostrum | A question somebody left in Rostrum | A question somebody left in Rostrum |
<!-- /cae:configuracion -->

**Nobody edits a configuration file by hand.** You say it in the conversation and the command rewrites it.
The cycles, the priority scale and the deadlines come from the organisation's audit methodology.

## The family's tests

**A single gate runs everything this repository checks**, for every family at once:

```
python3 scripts/verificar.py
```

What belongs to CAE is in [`tests/criterio-cae/`](../../tests/criterio-cae/): synthetic material with a
key the engine never sees and two control entities, where any signal is a failure. **One signal too many
counts the same as one too few.** What is planted and what the material does not test, in
[`EVIDENCIA.md`](../../tests/criterio-cae/EVIDENCIA.md).

## Roadmap

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->
<!-- /hoja de ruta -->

## The family's skills

<!-- cae:skills-familia · generado por scripts/familias.py; no se edita a mano -->
Five distinct skills across the three agents. **The ones they share are literal copies, not an imported module**: an installed plugin has to run on its own. `scripts/sincronizar.py` copies them and `scripts/sincronizar.py --check` fails if they drift.

| Skill | Prudencia | Justo | Remedios |
|---|:--:|:--:|:--:|
| `audit-intake` | ● | ● | ● |
| `audit-methodology` | ● | ● | ● |
| `finding-record` | · | ● | · |
| `follow-up-record` | · | · | ● |
| `plan-record` | ● | · | · |
<!-- /cae:skills-familia -->

## Status

<!-- cae:estado · generado por scripts/familias.py; no se edita a mano -->
| Agent | Installs as | Its test |
|---|---|---|
| **Prudencia** · The audit plan | `criterio-audit-plan` · 9 commands, 3 skills | The engine, tested; the round with the agent, pending · [results](../../tests/criterio-audit-plan/RESULTADOS.md) |
| **Justo** · Audit engagements | `criterio-audit-work` · 9 commands, 3 skills | The engine, tested; the round with the agent, pending · [results](../../tests/criterio-audit-work/RESULTADOS.md) |
| **Remedios** · Finding follow-up | `criterio-remediation` · 8 commands, 3 skills | The engine, tested; the round with the agent, pending · [results](../../tests/criterio-remediation/RESULTADOS.md) |
| **Rostrum** · the portal | `criterio-server` · 3 commands, for every family | — |

Tests use synthetic material built on real company information, anonymised before processing: no name, identifier, figure or personal data that could identify a company or a person is kept or published. What is published from each test is its results, without data.
<!-- /cae:estado -->
