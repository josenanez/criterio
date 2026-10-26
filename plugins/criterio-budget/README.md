<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cfo-claro.svg" alt="Criterio CFO · The finance function" height="48"></picture>

# Tomás · FP&A

<img src="../../docs/img/en/robot-tomas.gif" alt="Tomás" width="220" align="right">

**Tomás puts the budget next to its twin, actual spend.** You run the budget and answer to the
committee. He arrives with approved against actual and committed, the year-end forecast with its
stated assumption and every transfer with its minutes.

[Español](README.es.md) · `criterio-budget` · Apache 2.0 · One instance per entity

**Status: the seven commands are built**, along with the six skills and the calculation engine,
tested against synthetic material from four industries with a key the agent never sees and one
control entity per country. **The agent's extraction passed the [full round](../../tests/evidencias/familias/cfo/RONDAS.md)** on the six entities; nothing has been run yet on an organisation's documents. Nothing is announced as finished until the
[acceptance criteria](ACCEPTANCE.md) pass.

**This page stands on its own.** Tomás works without Clara: if you only run the budget,
everything is here, including his tests. The family —how he meets Clara and Rostrum— is in the
[criterio-cfo family](../../families/criterio-cfo/README.md).

---

## What it is

| | |
|---|---|
| **Whom it extends** | The financial planning and analysis (FP&A) team, and each area owner before the budget committee |
| **What it works on** | **The budget of one entity**, year after year, by area, line and account |
| **What it looks at** | The approved budget and its versions, the commitments, each area's forecast and the committee minutes, next to each period's books |
| **Cadence** | When a new period reaches the books, before each committee, and once a week for the commitments |
| **Instances** | One per entity |

## What it does

**What it does that is not done today: compare the budget version each report uses with the
approved one, and match each project's budget with the area's.** A report built on the previous
version states correct figures of a budget that no longer exists.

**What it can answer that today takes days:** which line deviates beyond the threshold to date,
which area forecasts above what was approved, which transfer has no minutes approving it, which
spend landed on an account with no budget line and which project carries in its record a budget
other than the one assigned to the area.

<!-- cfo:comandos · generado por scripts/familias.py; no se edita a mano -->
### The seven commands

> They are typed with the plugin prefix: `/criterio-budget:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-budget:budget-setup` | The configuration, the inventory and each area's first budget record |
| `/criterio-budget:budget-scan` | The budget records up to date, with what changed and the new signals |
| `/criterio-budget:variance-report` | Approved, actual, committed, available and variance by area and account |
| `/criterio-budget:forecast` | The year-end forecast, with its stated assumption |
| `/criterio-budget:transfer-log` | Every transfer with its approval minutes, and those without |
| `/criterio-budget:budget-committee-pack` | The budget committee material as a decision pack |
| `/criterio-budget:budget-wake` | What the budget needs today; silent when nothing does |
<!-- /cfo:comandos -->

`budget-setup` goes first because the others need it, and `budget-wake` is the one you put on a
clock. Between them, the four that prepare the committee: what changed, actuals, the forecast and
the transfers, and at the end the pack with the decision points.

<!-- cfo:skills · generado por scripts/familias.py; no se edita a mano -->
### The six skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `budget-record` | The budget record: what the agent extracts from written documents —approval and transfer minutes, what each area declares, the committee's commitments— with its citation | Own |
| `committee-pack` | The budget committee material as a decision pack: what goes in, how each point is presented with its figure and citation, and the previous committee's commitments | Own |
| `finance-intake` | Which documents the family processes, where each one goes, what the engine processes directly and what the agent extracts to the record | Copy of Clara's · also in Áurea |
| `forecast-method` | The two year-end forecasts —at the current pace and to plan—, their assumptions, how they compare with the area's own and when a forecast is stale | Own |
| `transfer-control` | Transfers, additions and reductions: how they are found by comparing versions, how they are matched with the minutes that approve them and what minutes with no change applied are | Own |
| `variance-analysis` | Actuals against budget: the approved version, the approved amount to date, actuals from the books through the account mapping, committed, available and the variance | Own |
<!-- /cfo:skills -->

## What it is for

`/criterio-budget:transfer-log` compares each budget version with the previous one, line by line.
And it does something more, which is what separates a useful log from a list of changes: **every
movement between lines is matched with the minutes that approve it**, by date, amount and source
and destination lines.

> **Test material · banking, Colombia** · 2026 budget
> Between two versions of the budget, one line went down and another went up by the same amount, and
> there are no minutes approving it in `40-actas/`.
> **The budget changed; the decision is not written down anywhere.**

That case comes from the synthetic material, planted with its key **before** the engine runs, and
it is the reason Tomás exists: not to decide for the committee, but so that what the committee
decided is where it can be proven.

### And what it is not for

- **It does not approve or post transfers.** It shows each one with or without its minutes.
- **It does not recommend the committee's decision.** It presents each point with its figure, its
  citation and who decides it.
- **It does not declare any area's budget status.** The area's owner does. Tomás shows what
  against.
- **It does not present a forecast as the correct one.** It calculates two, at the current pace
  and to plan, each with its stated assumption, and puts them next to the one the area delivered.
- **It never moves, renames or creates anything inside the organisation's documents.** The only
  thing it leaves, if the person allows it, is the file that marks the root folder so it is
  recognised at a glance.
- **It does not guess.** Every data point carries the citation of the document and, for tables,
  the row it came from. Spend with no line in the mapping is reported, not spread.

**And one thing is deliberately absent: the close.** Tomás does not recalculate the books: he
takes them from `10-contabilidad/`, the same ones Clara closes, and carries them to each line with
the organisation's account mapping.

And one that has to be said out loud: **your documents are processed on the AI platform's
infrastructure**, not only on your machine. Confirm that this is admissible under your policies
before pointing it at confidential material. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md),
terms in [TERMS.md](../../TERMS.md).

## Installing and configuring

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-budget@criterio
/criterio-budget:budget-setup
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from
GitHub → `josenanez/criterio`.

If you close the books and do not run the budget, yours is [Clara](../criterio-finance/README.md).

### The first result

`/criterio-budget:budget-setup` does not ask you to tidy anything up before starting. It looks at
the budget folder and each period's folder with its books, compares them with the
[recommended structure](../../families/criterio-cfo/README.md#the-recommended-folder-structure),
identifies the approved version by its minutes and asks the questions no document answers —the
areas with their owner, the mapping of accounts to lines, the variance thresholds—. In the first
fifteen minutes it shows approved against actual and committed by area and line, with the budget
version in force and the signals the engine raised.

From there, every command delivers its report in the same order: what needs attention, the
result, what could not be processed, the questions it asked and the sources.

**What ends up configured** is written by `/criterio-budget:budget-setup` from your answers, in
`.criterio/presupuesto/<entidad>/config.json`: the entity, the year, the areas, the approved
version and its minutes, the mapping, the thresholds and the record that you accepted the terms,
with your name and the date. All of that is changed **by talking**.

### How often it runs

A command waits. **This one is scheduled and runs on its own.** Its cadence is not the calendar:
it is the books and the committee. It runs when a new period appears in `10-contabilidad/`, before
each committee and once a week for the commitments. The decision is date arithmetic, so the code
takes it:

```
python3 scripts/finanzas.py despertar --config <file>
```

And `/criterio-budget:budget-wake` is the command the clock invokes: it does what is due, answers
first the questions somebody left in Rostrum, and **if nothing is due it produces nothing.**
Putting it on a clock is on your organisation's side: a scheduled task in Cowork, or the system's
scheduler in Claude Code. If unattended runs are not welcome, the cadence still says what is due,
run by hand.

**And if you want each area owner to see their actuals without asking you for them**, the family
has a portal that publishes them, where whoever is looking can leave Tomás a written question. →
**[Rostrum](../criterio-server/README.md)**

## Working with the others

Tomás works alone. If the others are installed, **there is nothing to connect**: they meet
through the entity's state and the records, which are documents.

| With whom | What happens |
|---|---|
| **Clara** | They share the entity's state and the period's books: Clara closes them and Tomás takes actuals from there, without copying them. Each one writes only its own record |
| **The PMO family** | If the organisation uses it, Tomás processes its project records **without writing in them**, and matches each project's budget with the one assigned to the area. A difference shows up in Rostrum, on that project's page |
| **Rostrum** | Publishes his reports and signals, for whoever will not open a folder, and hands him the questions left by whoever is looking. **It does not write the state** |

## Tests

### How it is built

The spine is the **budget record**, one per area or cost centre and year: approved, actual and
committed by account, the area's forecast, the transfers with their minutes and the declared
status, each data point with the citation of its document and date. The agent writes it; the
engine writes the results.

[`scripts/finanzas.py`](scripts/finanzas.py), on the standard library, does everything that is
calculation: actuals by line from the books, available, variance, the two forecasts and the
matching of each transfer with its minutes, the same result every time. The agent takes to the
record only what minutes and declarations carry
([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)).

**`finanzas.py` and the `finance-intake` skill are literal copies of Clara's, not imports**, and
that is deliberate: an installed plugin has to run on its own. [`scripts/texto.py`](scripts/texto.py)
is a literal copy of the PMO family's. `scripts/sincronizar.py --check` fails if any copy drifts,
because two copies computing differently over the same books would leave nobody knowing which to
believe.

### How it is verified

```
python3 scripts/finanzas.py selftest                 the engine
python3 tests/criterio-cfo/generar.py                 the material of the four industries
python3 tests/criterio-cfo/evaluar.py --agente tomas  every signal against the key
```

On the standard library, with nothing installed. Over synthetic material with a key the engine
never sees — **including the controls**: one entity per country with no defects at all, with a
transfer approved with its minutes and areas that declare themselves within budget and are. Any
signal there is a failure.

**How the last run came out, generated from the run itself:**
[`tests/criterio-budget/RESULTADOS.md`](../../tests/criterio-budget/RESULTADOS.md) (Spanish).
What is planted in each entity and, in the same detail, **what the material does not test**, in
[`EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md) (Spanish).

The design, with the input, process and report of each command and the engine's signals, in the
[family design](../../families/criterio-cfo/DISENO.md); the acceptance criteria, in
[ACCEPTANCE.md](ACCEPTANCE.md).

And the family's tests — what no agent can answer alone — on the
[family page](../../families/criterio-cfo/README.md#the-familys-tests).
