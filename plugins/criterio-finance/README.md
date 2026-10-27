<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cfo-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cfo-claro.svg" alt="Criterio CFO · The finance function" height="48"></picture>

# Clara · the controller

<img src="../../docs/img/en/robot-clara.gif" alt="Clara" width="220" align="right">

**Clara puts the books next to their supporting documents.** You close the month and answer for
it. She arrives with the close prepared: every task against its evidence, every account
reconciled and every e-invoice against its entry.

[Español](README.es.md) · `criterio-finance` · Apache 2.0 · One instance per entity

**Status: the nine commands are built**, along with the seven skills and the calculation engine,
tested against synthetic material from four industries with a key the agent never sees and one
control entity per country. **The agent's extraction passed the [full round](../../tests/evidencias/familias/cfo/RONDAS.md)** on the six entities; nothing has been run yet on an organisation's documents. Nothing is announced as finished until the
[acceptance criteria](ACCEPTANCE.md) pass.

**This page stands on its own.** Clara works without Tomás: if you only close the books,
everything is here, including her tests. The family —how she meets Tomás and Rostrum— is in the
[criterio-cfo family](../../families/criterio-cfo/README.md).

---

## What it is

| | |
|---|---|
| **Whom it extends** | The controller and the accounting team |
| **What it works on** | **The close of one entity**, month after month |
| **What it looks at** | The entity's finance folder, as it is: the books, the banks, the invoices, the close support and what the auditor asks for |
| **Cadence** | Daily while the close window is open, and once a week outside it |
| **Instances** | One per entity |

## What it does

**What it does that is not done today: process every e-invoice of the period against the books,
not a sample, and every close task against its evidence.** A sample finds what falls in the
sample; the duplicate, the invoice with no entry or the entry with no invoice can be anywhere.

**What it can answer that today takes days:** which task is marked done with no document behind
it, which reconciling item has been open longer than acceptable, which DIAN, SRI or SUNAT invoice has no
entry —or which entry has no invoice—, which account does not tie out with its subledger and which
auditor request is still without a supported answer.

<!-- cfo:comandos · generado por scripts/familias.py; no se edita a mano -->
### The nine commands

> They are typed with the plugin prefix: `/criterio-finance:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-finance:finance-setup` | The configuration, the folder inventory and the first close record |
| `/criterio-finance:close-scan` | The close record up to date, with what changed and the new signals |
| `/criterio-finance:close-status` | The close status: declared against evidenced, task by task |
| `/criterio-finance:bank-reconcile` | Each bank account reconciled, with its open items by age |
| `/criterio-finance:account-reconcile` | Each account reconciled against its sub-ledger |
| `/criterio-finance:ledger-check` | The trial balance and ledger tie-out, account by account |
| `/criterio-finance:einvoice-check` | Every e-invoice in the period against the books, not a sample |
| `/criterio-finance:audit-pack` | The auditor's package index, with the status of every request |
| `/criterio-finance:finance-wake` | What the close needs today; silent when nothing does |
<!-- /cfo:comandos -->

`finance-setup` goes first because the others need it, and `finance-wake` is the one you put on a
clock. Between them, the six that prepare the close in the order it is worked: what changed, the
status, the banks, the accounts, the tie-out and the invoices, and at the end the auditor's
package.

<!-- cfo:skills · generado por scripts/familias.py; no se edita a mano -->
### The seven skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `audit-support` | The auditor's package: the request index, how each response is named and when a request is answered with support | Own |
| `close-checklist` | The close checklist: the column model, how each task is proven with its support, the business-day calendar and the recommended checklist per industry as a draft | Own |
| `close-record` | The close record: what the agent extracts from written documents —the declared status, the requests that arrived by email or in Word— with its citation | Own |
| `einvoice-matching` | The DIAN, SRI or SUNAT e-invoice against the books: the fields processed and their source, the matching rules, duplicates, and what is left without a tax opinion | Own |
| `finance-intake` | Which documents the family processes, where each one goes, what the engine processes directly and what the agent extracts to the record | Own · also in Tomás and Áurea |
| `ledger-tieout` | The trial balance and ledger tie-out: debits against credits, opening balance plus movements against closing balance, account by account, and balances contrary to their nature | Own |
| `reconciliation` | How the engine reconciles: the statement against the book ledger in three passes, how each open item is classified, its age, and the ledger against each account's subledger | Own |
<!-- /cfo:skills -->

## What it is for

`/criterio-finance:close-status` puts each checklist task next to its evidence. And it does
something more, which is what separates a useful checklist from a list of boxes: **a task marked
done without the document that proves it is not done**, and the report says so with the task and
its owner.

> **Test material · banking, Colombia** · September 2026 close
> A checklist task is marked done and there is nothing with its id in `40-soportes/`.
> **The checklist says it is done; the evidence does not.**

That case comes from the synthetic material, planted with its key **before** the engine runs,
and it is the reason Clara exists: not to close for you, but so that what is declared closed has
behind it what supports it.

### What it costs today

<!-- cfo:cifras · generado por scripts/familias.py; no se edita a mano -->
| Figure | Source |
|---|---|
| **44%** closed the quarter within six working days in 2023, down from 49% in 2019 | [Ventana Research / ISG, Smart Financial Close, 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) — Not stated in the note |
| **45%** of SOX controls are manual in the organisations surveyed; programme hours rose 32% in two years, from 11,800 to 15,580 | [KPMG, SOX Survey, 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — About 150 SOX professionals |
| **18 days** is the median annual close; top performers take 10 days or less and the slowest 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio, 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) — Not stated in the note; the benchmarking measure reports the 18.0-day median across 2,214 organisations |
| **18%** of people in the controllership function make errors at least daily, and 59% several per month, because of capacity constraints | [Gartner, comunicado del 21 de febrero de 2024, 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 people in the controllership function, surveyed in July 2023 |
| **79%** of organisations suffered attempted or actual payments fraud in 2024; 63% name business email compromise as the main channel | [Association for Financial Professionals, 2025 Payments Fraud and Control Survey, 2025](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/survey-79-percent-of-organizations-were-victims-of-attempted-or-actual-payments-fraud-activity-in-2024) — 521 corporate finance professionals |
<!-- /cfo:cifras -->

The figure that should sting is the first: **the close did not improve in four years**, despite
everything spent on technology.

### And what it is not for

- **It does not post or correct entries.** It flags the difference; a person posts the entry.
- **It does not file returns or supervisory reports, and it does not sign.**
- **It gives no opinion on deductibility, rates or IFRS treatment**, and states no rate, deadline
  or tax unit value from memory. Accounting or tax judgement is left as a question for the person.
- **It does not declare the close status.** The controller does. Clara shows what against, and
  the difference between the two is the most valuable finding.
- **It never moves, renames or creates anything inside the organisation's documents.** The only
  thing it leaves, if the person allows it, is the file that marks the root folder so it is
  recognised at a glance.
- **It does not guess.** Every data point carries the citation of the document and, for tables,
  the row it came from. A file without the expected format is reported with what it lacks.

**And one thing is deliberately absent: the budget.** Approved against actual is Tomás's, who
takes actuals from the same books Clara closes. Consolidating several entities is outside the
first version.

And one that has to be said out loud: **your documents are processed on the AI platform's
infrastructure**, not only on your machine. Confirm that this is admissible under your policies
before pointing it at confidential material. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md),
terms in [TERMS.md](../../TERMS.md).

## Installing and configuring

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-finance@criterio
/criterio-finance:finance-setup
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from
GitHub → `josenanez/criterio`.

If you run the budget and not the close, yours is [Tomás](../criterio-budget/README.md).

### The first result

`/criterio-finance:finance-setup` does not ask you to tidy anything up before starting. It looks
at the entity's folder, compares it with the
[recommended structure](../../families/criterio-cfo/README.md#the-recommended-folder-structure)
and asks the questions no document answers —the entity, the framework, the accounts the invoices
match against, who approves—. In the first fifteen minutes it shows the status of the period's
close: every checklist task with or without its evidence, and the signals the engine raised on
the tie-out, the banks, the accounts and the invoices.

From there, every command delivers its report in the same order: what needs attention, the
result, what could not be processed, the questions it asked and the sources. If the organisation
has no checklist, Clara recommends one for its industry **as a draft**, and the report says it is
not approved until a person approves it.

**What ends up configured** is written by `/criterio-finance:finance-setup` from your answers, in
`.criterio/finanzas/<entidad>/config.json`: the entity, the framework, the accounts, the
checklist, the thresholds and the record that you accepted the terms, with your name and the
date. All of that is changed **by talking**.

### How often it runs

A command waits. **This one is scheduled and runs on its own.** Its cadence is the close window:
daily while it is open, once a week outside it. The decision is date arithmetic, so the code takes
it:

```
python3 scripts/finanzas.py despertar --config <file>
```

And `/criterio-finance:finance-wake` is the command the clock invokes: it does what is due,
answers first the questions somebody left in Rostrum, and **if nothing is due it produces
nothing.** Putting it on a clock is on your organisation's side: a scheduled task in Cowork, or
the system's scheduler in Claude Code. If unattended runs are not welcome, the cadence still says
what is due, run by hand.

**And if you want the CFO to see the close without asking you for it**, the family has a portal
that publishes it, where whoever is looking can leave Clara a written question. →
**[Rostrum](../criterio-server/README.md)**

## Working with the others

Clara works alone. If the others are installed, **there is nothing to connect**: they meet
through the entity's state, which is a folder on the machine of whoever runs them.

| With whom | What happens |
|---|---|
| **Tomás** | They share the entity's state and the period's books: Clara closes them and Tomás takes the budget's actuals from there, without copying them. Each one writes only its own record |
| **Rostrum** | Publishes her reports, what falls due in the close and her signals, for whoever will not open a folder, and hands her the questions left by whoever is looking. **It does not write the state** |

## Tests

### How it is built

The spine is the **close record**, one per entity and period: the checklist tasks with their
evidence, each reconciliation with its open items, the invoices against their entries and the
declared status, each data point with the citation of its document and date. The agent writes
it; the engine writes the results.

[`scripts/finanzas.py`](scripts/finanzas.py), on the standard library, does everything that is
calculation: it processes the tables and the invoices directly —the trial balance, the ledger,
the statements, the subledgers, the DIAN, SRI, SUNAT, SII and SAT XML— and calculates each signal, the same result
every time. The agent takes to the record only what a written document carries: what somebody
declares, a request that arrived by email
([ADR 0008](../../docs/decisions/0008-cfo-motor-procesa-tablas.md)).
[`scripts/texto.py`](scripts/texto.py) turns Word, Excel, PowerPoint, PDF and email into text,
and is a literal copy of the PMO family's; `finanzas.py` travels copied in `criterio-budget`.
`scripts/sincronizar.py --check` fails if any copy drifts.

Every format and every regulation used is in
[`families/criterio-cfo/FUENTES.es.md`](../../families/criterio-cfo/FUENTES.es.md) (Spanish),
with its version, its link and its status; every invoice field the engine processes, with its
identifier in the technical annex.

### How it is verified

```
python3 scripts/finanzas.py selftest                 the engine
python3 tests/criterio-cfo/generar.py                 the material of the four industries
python3 tests/criterio-cfo/evaluar.py --agente clara  every signal against the key
```

On the standard library, with nothing installed. Over synthetic material with a key the engine
never sees — **including the controls**: one entity per country with no defects at all, where
any signal is a failure. An agent that finds something there is a noise generator.

**How the last run came out, generated from the run itself:**
[`tests/criterio-finance/RESULTADOS.md`](../../tests/criterio-finance/RESULTADOS.md) (Spanish).
What is planted in each entity and, in the same detail, **what the material does not test**, in
[`EVIDENCIA.md`](../../tests/criterio-cfo/EVIDENCIA.md) (Spanish).

The design, with the input, process and report of each command and the engine's signals, in the
[family design](../../families/criterio-cfo/DISENO.md); the acceptance criteria, in
[ACCEPTANCE.md](ACCEPTANCE.md).

And the family's tests — what no agent can answer alone — on the
[family page](../../families/criterio-cfo/README.md#the-familys-tests).
