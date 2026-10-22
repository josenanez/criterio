<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cfo-claro.svg" alt="Criterio CFO · Close, control and reporting" height="48"></picture>

# criterio-cfo · the finance function family

**Two agents and a portal, around two records.** Each one extends a different person in the
finance function — whoever closes the books and whoever runs the budget — and neither talks to
the other directly: they talk through their records.

[Español](README.es.md) · [← Criterio](../../README.md) · Apache 2.0

![Clara, Tomás and Rostrum](../../docs/img/en/robots-cfo.gif)

| | |
|---|---|
| **Scope** | The close, control and financial reporting of an entity: the books against their supporting documents, and the budget against its execution |
| **Objective** | That the close stops depending on someone remembering what is missing |
| **Made of** | [Clara](../../plugins/criterio-finance/README.md) · [Tomás](../../plugins/criterio-budget/README.md) · [Rostrum](../../plugins/criterio-server/README.md) |
| **State** | Built and in testing: the engine, tested against the material of four industries and two control entities. A first, small round with the agent —banking and the Colombian control— has [run](../../tests/evidencias/familias/cfo/RONDAS.md). **The full round is the next step**, and without it the family is not declared tested |
| **Approach** | Control and reporting |
| **Commitment** | Generating, sharing and preserving knowledge is a professional obligation |
| **What it is not** | It does not replace the controller or the financial planning team, and does not decide for them: it processes what the function already has and says what does not tie out |
| **Licence** | [Apache 2.0](../../LICENSE) |
| **What comes next** | The full round with the agent, and then deployment in an organisation: [the roadmap](#roadmap) |

---

## What the family does

The finance function has two roles that work on the same books and look at different things,
which is why the family has two agents. They carry a person's name because **they are extended
capabilities of people**, and what each name means points to what it does: **Clara** —from
*clarus*— makes sure the books say what the supporting documents say; **Tomás** —"the twin"— puts
the budget next to its twin, actual spend.

**Clara**, the controller's agent, prepares the monthly close: the checklist with its evidence,
bank and account reconciliations, every DIAN or SRI e-invoice against its entry, and the
auditor's package. What nobody does today and she does: **process every invoice of the period,
not a sample**, and every close task against its evidence.

**Tomás**, the financial planning (FP&A) agent, puts approved next to actual and committed,
forecasts the year-end with its stated assumption, matches each transfer with its minutes and
builds the committee material as a decision pack. He takes actuals from the same books Clara
closes, without copying them.

**Both install today**, each with its own plugin, and both carry the same debt, written on their
page: the engine is tested against synthetic material from four industries; **the agent's extraction passed a first, small round, and the full one is next; nothing has been tested yet on an
organisation's documents.**

First version: IFRS as locally adopted in Colombia and Ecuador, with DIAN and SRI electronic
invoicing processed from its official technical source.

---

## How the two work

The language model (LLM) extracts; the code calculates; the status of the close and of the
budget is always declared by a person. **The engine processes the tables directly** —the trial
balance, the ledger, the statements, the invoices, the budget—, and the agent takes to the record
only what a written document carries: what somebody declares, a request that arrived by email,
minutes ([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)).

**Automated**: they process the documents, calculate the signals and prepare each deliverable
without intervention. **Semi-automated** when a data point no document carries is missing —the
entity, the period, the threshold, who approves—: then they ask the person, say what they asked
and carry on with the answer.

## The two agents and their records

Nothing talks to anything directly. **Each agent writes its record, and the record is the
contract.**

| Record | One per | What it holds | Who writes it |
|---|---|---|---|
| Close record | Entity and period | The checklist tasks with owner, date and evidence; each reconciliation with its open items; the e-invoices against their entries; the declared status of the close | Clara; the status, the controller in person |
| Budget record | Area or cost centre and year | Approved, actual and committed by account; the area's forecast; the transfers with their minutes; the declared status | Tomás; the status, the area's owner |

Every data point cites the document it comes from and its date. "Not found" is a valid answer.

### The seven invariants

1. **The agents do not talk to each other.** They talk through their records.
2. **Rostrum, the portal, does not write.** It serves what the engine already wrote and says so
   with its date; it recalculates nothing.
3. **Each document has one place.** The period's books live in `10-contabilidad/`: Clara closes
   them and Tomás takes actuals from there, with no copies between folders.
4. **Declared and evidenced never merge.** They go in separate fields of the record.
5. **The model extracts, the code calculates.** Every figure in a report comes from
   `finanzas.py`, with all its digits; if the engine does not give it, it is not written.
6. **No agent declares the status.** The close's is declared by the controller; each area's, by
   its owner.
7. **One writer per file.** The agent writes the record and the engine writes the results;
   neither writes the other's.

The sixth is the easiest to break for convenience and the one that takes the whole system with
it: if the agent declares the close, the comparison between declared and evidenced compares the
system with itself. It is not a recommendation in the documentation: it is a restriction on the
write path.

## What still belongs to the people

Both roles continue to exist in full. This extends capability; it does not replace function. And
the argument is not politeness, it is structural:

> **Each agent's input is produced by the non-delegable work of its person.**

Clara needs somebody to do the close tasks and leave their evidence, because without support
there is nothing to contrast, and the controller to declare the status, because that is the line
everything is compared against. Tomás needs each area to deliver its forecast and the committee
to write down its decision, because a transfer without minutes is exactly what he flags.

Removing the person does not leave the agent alone: it leaves it without input. **And neither of
them posts an entry, approves a transfer, files a return or signs.**

## The recommended folder structure

Recommended, not mandatory ([ADR 0007](../../docs/decisions/0007-estructura-recomendada.md)):
the agents process the folder as it is. `finance-setup` and `budget-setup` compare what they find
with this structure and, on every run, say which file is out of place and where it would go; they
never create, move or rename anything in the organisation's documents. The numbering goes in
tens, as in the PMO family, in the order the close and the budget are worked.

<!-- cfo:carpetas · generado por scripts/familias.py; no se edita a mano -->
One folder per entity, with its tax id at the start of the name: `900123456-entity-name`. Inside it, what the organisation provides once, one folder per accounting period and one per budget year.

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

A file without the expected format is not guessed: it is reported with what it lacks.

## Installing the family

Each agent is a plugin and installs on its own. **You do not need both**: install the one that
covers the role you have.

```
/plugin marketplace add josenanez/criterio

/plugin install criterio-finance@criterio     if you close the books
/plugin install criterio-budget@criterio      if you run the budget
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from
GitHub → `josenanez/criterio`.

After installing, each agent has its own setup command that looks at the folder, asks the
questions no document answers and produces a first result over your own documents. **Nobody
edits a configuration file by hand.**

And if you install both, they find each other: **there is nothing to connect.** They share the
entity's state, and each one writes only its own.

## What each agent answers for, and where its detail lives

The same for each piece: what it answers for, what it does not do, and where all its detail
lives. **Each agent page stands on its own** — somebody can install one without the other.

<!-- cfo:familia-agentes · generado por scripts/familias.py; no se edita a mano -->
| | What it answers for | What it never does | Its page | Its tests |
|---|---|---|---|---|
| **Clara** · controller | The monthly close with its checklist and evidence, bank and account reconciliations, e-invoices against the books, and the auditor's package | It does not post entries, does not sign and does not declare the close status | [criterio-finance](../../plugins/criterio-finance/README.md) · 9 commands, 7 skills | [results](../../tests/criterio-finance/RESULTADOS.md) |
| **Tomás** · FP&A | The approved budget against actual and committed spend, the year-end forecast, budget transfers and the budget committee pack | It does not approve transfers, does not recommend the committee's decision and does not declare any area's status | [criterio-budget](../../plugins/criterio-budget/README.md) · 7 commands, 6 skills | [results](../../tests/criterio-budget/RESULTADOS.md) |
| **Rostrum** · the portal | Publishing what the agents write where the team will see it, and taking the question from whoever will not open a folder | **Never writes the state or recalculates anything**, and decides nothing | [criterio-server](../../plugins/criterio-server/README.md) · 2 commands, one for every family | [results](../../tests/criterio-server/RESULTADOS.md) |
<!-- /cfo:familia-agentes -->

The commands, one by one —what each does and which skills it uses—, are in the
[command manual](../../docs/manual.md); their input, process and report, with the signals the
engine calculates, in the [family design](DISENO.md); and the answers to what people ask most, in
the [FAQ](PREGUNTAS.md).

## In Rostrum, the portal for every family

Up to here the family's result is files on the machine of whoever ran the agents. **A CFO does
not open a folder of files**: they open a link, or they open nothing. That is what **Rostrum** is
for: a plugin of its own, `criterio-server`, that serves the CFO family together with the other
families, without the server knowing anything about finance
([ADR 0010](../../docs/decisions/0010-rostrum-plugin-propio.md)).

**How the CFO family enters the portal.** `/criterio-finance:finance-setup` and
`/criterio-budget:budget-setup` leave their configuration in `.criterio/finanzas/<entidad>/` and
`.criterio/presupuesto/<entidad>/`, with the entity's finance folder marked with
`_CRITERIO_FINANZAS.txt`. Clara and Tomás share the entity's state, and each one sees its own runs
and reports in the portal, not the other's. Then `/criterio-server:server-setup` finds both
configurations and adds them to the map, and `/criterio-server:server-start` raises the portal. A
new entity enters by running `server-setup` again.

**What the CFO family has in Rostrum:**

| Where | What |
|---|---|
| Home | The **Criterio CFO** card with Clara and Tomás and their open signals |
| `/familia/cfo` | The latest each one's engine wrote —the close of a month, the budget of a year—, with its signals in words and the calculation date, and its reports exactly as the engine left them |
| What falls due | The close tasks and the auditor's requests with a date, sorted with the other families' due dates |
| `/caso/<PRY>` | A budget signal on a PMO project appears on that project's page |
| Where it works | The full path of the root folder, of the entity's documents with their marker, of the state and of each configuration |
| Ask an agent | A question for Clara or for Tomás, taken on their next run |

**It authenticates nobody, and that is on purpose**: it is published behind the access control
the organisation already has. It recalculates nothing and does not write the state. The pages
meet WCAG 2.2 level AA, checked with axe-core at four screen widths
(`tests/criterio-server/accesibilidad/`).

→ **[Rostrum: install, configure and use it with every family](https://www.josenanez.com/agents/rostrum)** ·
[its README, with the routes and what to ask your organisation for](../../plugins/criterio-server/README.md)

## How each one is configured and how often it runs

This is the table that answers three questions at once: **where each agent lands, what it needs
configured, and how often it makes sense for it to run.**

<!-- cfo:configuracion · generado por scripts/familias.py; no se edita a mano -->
| | Clara | Tomás |
|---|---|---|
| **Installs as** | `criterio-finance` | `criterio-budget` |
| **Instances** | One per entity | One per entity |
| **Configured with** | `/criterio-finance:finance-setup` | `/criterio-budget:budget-setup` |
| **How long that takes** | Fifteen minutes | Fifteen minutes |
| **What you have to tell it** | Entity and NIT or RUC, country, IFRS group (F-05, F-06), ERP, currency, period, thresholds, who approves, chart of accounts | Entity, budget year, areas or cost centres with their owner, the approved version and its minutes, the mapping of accounts to budget lines (in `00-referencia/`), the variance thresholds and, if the organisation uses the PMO family, where its records are |
| **Where it lands** | `.criterio/finanzas/<entity>/config.json`, written by the command | `.criterio/presupuesto/<entity>/config.json`, written by the command |
| **The one you put on a clock** | `/criterio-finance:finance-wake` | `/criterio-budget:budget-wake` |
| **What it does each day** | Decides what is due by cadence: daily during the close window, weekly outside it | Decides what is due by cadence: when a new period appears in `10-contabilidad/`, before each committee and once a week for commitments |
| **What wakes it besides the clock** | A question somebody left in Rostrum | A question somebody left in Rostrum |
<!-- /cfo:configuracion -->

**Nobody edits a configuration file by hand.** If changing a threshold means opening a JSON, the
threshold stays as it came and the configuration stops describing the organisation. You say it
in the conversation and the command rewrites it. Each plugin ships its
`scripts/config.example.json` so you can see the full shape without installing anything; the
default thresholds are configuration, not a standard.

### Why the two cadences are different

It is not a preference: **each agent measures against something else.**

- **Clara** measures against the close window. While the close is open, an overdue task or a
  reconciliation not updated changes the status today, so she runs daily; outside the window,
  once a week is enough.
- **Tomás** measures against the books and the committee. His cycle is not the calendar: it is
  *when a new period arrives* in `10-contabilidad/` and *before each committee*, and once a week
  he reviews the commitments.

### Both go quiet when there is nothing

It is the rule that decides whether an agent is still installed a month later. The two clock
commands produce nothing when nothing is due, and then the output is one line: what was reviewed
and when it comes back. With an open question in Rostrum they never go quiet: they answer it
first.

An agent that produces a report to say there is no news teaches you to ignore it, and the day
there is news nobody opens it.

### What is **not** scheduled

**Neither of them schedules itself.** Both ship the command a clock invokes, and the clock lives
outside the plugin — a Claude Cowork scheduled task, or the operating system's scheduler invoking
Claude non-interactively. Somebody has to set it up, once.

And for it to run with nobody watching, two things are needed that do not depend on this
repository: **that the session can run without approving each step**, and **that the folder is
mounted when the clock fires.** If the organisation does not want unattended runs —and in a
finance function that is a reasonable answer—, the commands work run by hand and the cadence
still says what is due.

## The family's tests

**A single gate runs everything this repository checks**, across every family at once:

```
python3 scripts/verificar.py
```

What belongs to the CFO family is in [`tests/criterio-cfo/`](../../tests/criterio-cfo/): synthetic
material per industry with a key the engine never sees, and one control entity per country with no
defects at all, where any signal is a failure. Every family signal is planted at least once.
`evaluar.py` runs the engine and compares every signal by its name and its key: **an extra one
counts the same as a missing one.**

| What is checked across the family | Why it belongs to the family and not to one agent |
|---|---|
| That every planted signal is raised, and none in the controls | Clara's signals and Tomás's come from the same engine and the same material |
| **That the shared copies have not drifted apart** | `finanzas.py` and `finance-intake` travel copied in both plugins. Two copies that drift compute differently over the same documents, and nobody would know which to believe |
| That the design, the pages and the portal say what the sources say | The tables of agents, commands, signals, folders and skills come from `familia.json`, `carpetas.json` and `fuentes.json`; `scripts/familias.py --check` fails if a copy does not match |
| That every invoice field the engine processes is in its official source | A field that is not in the DIAN annex or the SRI technical sheet is not processed ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), rule 2) |

**Each agent's result, generated from the run**, on its own page:
[Clara](../../tests/criterio-finance/RESULTADOS.md) ·
[Tomás](../../tests/criterio-budget/RESULTADOS.md) (Spanish). What is planted in each entity and
the signal it has to raise, in the same detail, **and what the material does not test**, in
[`EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md) (Spanish). The whole set across every
family, in [`docs/pruebas.md`](../../docs/pruebas.md).

**The first round with the agent** ran on banking and the Colombian control: Clara and Tomás run their commands and what they extract from minutes, emails and auditor letters is graded against the same key. Every output, its cost, its grading and the commands repeated after a defect was fixed are in [the family's rounds](../../tests/evidencias/familias/cfo/RONDAS.md). The full round, with the four industries and the two controls, brings the family's statistical analysis, with the same metrics as the PMO.

## The test industries

Four South American industries and one control entity per country: **banking and retail in
Colombia**, with the DIAN XML, and **cooperatives and mining in Ecuador**, with the SRI's. Each
one carries the close of a month and the budget of the year. The entities, the planted defects
and the signals expected of each, in
[`tests/criterio-cfo/EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md) (Spanish).

## Roadmap

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->

The family grows in increments. Each one is a version with its full test and its statistical analysis published, with the same metrics, so the evolution can be compared.

| Version | Status | What goes in | Test |
|---|---|---|---|
| 0.8.0 | Released | **Built, with the engine tested and a first round with the agent**<br>· Clara and Tomás’s sixteen commands, their twelve skills and the calculation engine<br>· DIAN and SRI electronic invoicing, processed from its official technical source<br>· The root folder each agent searches for and, with permission, marks<br>· The family in Rostrum, with what falls due and where each agent works<br>· The first round with the agent: Clara and Tomás on banking and the Colombian control, with the defects it found fixed | The engine, against 4 industries and 2 control entities; the agent, on banking and the Colombian control |
| Increment 2 | Next | **The full round with the agent**<br>· Clara and Tomás run their commands on the material of the four industries, as the PMO does in every round<br>· What only minutes, emails and auditor letters carry, extracted and graded against the key<br>· With a full round, the family is declared tested | 4 industries and 2 control entities, with the key the agent never sees |
| Increment 3 | Reserved | **Deployment in an organisation**<br>· The first use on a specific organisation’s books and budget | That organisation’s documentation |

<!-- /hoja de ruta -->

## The family's twelve skills

<!-- cfo:skills-familia · generado por scripts/familias.py; no se edita a mano -->
Twelve distinct skills across the two agents. **The ones they share are literal copies, not an imported module**: an installed plugin has to run on its own. `scripts/sincronizar.py` copies them and `scripts/sincronizar.py --check` fails if they drift.

| Skill | Clara | Tomás |
|---|:--:|:--:|
| `audit-support` | ● | · |
| `budget-record` | · | ● |
| `close-checklist` | ● | · |
| `close-record` | ● | · |
| `committee-pack` | · | ● |
| `einvoice-matching` | ● | · |
| `finance-intake` | ● | ● |
| `forecast-method` | · | ● |
| `ledger-tieout` | ● | · |
| `reconciliation` | ● | · |
| `transfer-control` | · | ● |
| `variance-analysis` | · | ● |
<!-- /cfo:skills-familia -->

## Status

**Both are built and can be installed today**, and both carry the same debt, which is better not
hidden: **the engine is tested on synthetic material; the agent's extraction is not yet.**

<!-- cfo:estado · generado por scripts/familias.py; no se edita a mano -->
| Agent | Installs as | Its test |
|---|---|---|
| **Clara** · Controller | `criterio-finance` · 9 commands, 7 skills | The engine, tested; a first round with the agent; the full one, pending · [results](../../tests/criterio-finance/RESULTADOS.md) |
| **Tomás** · FP&A | `criterio-budget` · 7 commands, 6 skills | The engine, tested; a first round with the agent; the full one, pending · [results](../../tests/criterio-budget/RESULTADOS.md) |
| **Rostrum** · the portal | `criterio-server` · 2 commands, for every family | — |
<!-- /cfo:estado -->

The family is declared tested with a full round with the agent, and the first use on a specific
organisation's books is the increment after that. The decisions still open, in the
[design](DISENO.md#open-decisions).
