# criterio-pmo

**Vera, a second brain for the project management office.** It reads the documentation your PMO
already has and says what changed, what contradicts itself, and what has been silent for
weeks.

[Español](README.es.md) · Apache 2.0 · Four clicks to install · **The first result lands in
fifteen minutes, over your own documents**

---

## The PMO family

![The PMO family: three agents, one data contract](../../docs/img/en/familia-pmo.png)

The capability has more than one agent because the organisation has more than one role.
They carry people's names because **they are capabilities that extend people**, and each
name's meaning points at what it does: **Vera** — from *verus*, the true — says what the
documents say rather than what gets reported; **Samuel** — "he who heard" — remembers on
Friday what was said in the meeting; **Alba** — daybreak — works before the project
dawns.

**All three install today**, each with its own plugin, and they share the same data
contract. All three also carry the same debt, written on their own page: built and
verified over a synthetic corpus, **not yet tested against a real organisation's
documentation.**

**Samuel**, the project manager's agent, does not attend the meetings — the manager does. What it does is let the
manager arrive with the week prepared: the agenda built beforehand, the minutes drafted
afterwards, the plan current against the evidence, and the report ready except for one line.
Its central function is one no tool a project manager uses today performs: **the commitment
said and not kept.** Meetings are full of *"I'll have it by Friday"* and nobody records them.

**Alba** works before the project exists, and delivers the charter the project
is born from.

---

## How the three operate

![How the three agents operate](../../docs/img/en/flujo.png)

The order in time is what makes them a system rather than three tools. **Two closed loops, and neither goes through a shared database.** The charter comes down once,
and with it the record is born. The manager's record goes up published as one more document of
the project, and Vera reads it like everything else. The report goes out to the team, and from
the team a request comes back. And the loop at the top: Alba reads the project records to
confirm that whoever claims to be building her product actually is.

What is **not** in that picture matters as much as what is:

- **No arrow between two agents.** Every one of them passes through a document. Two agents
  talking directly are two agents you have to deploy together.
- **No arrow back from Rostrum into the record.** The server does not write.
- **No arrow that writes the declared status.** A person writes that, in all three places where
  it appears.

**And the people are in the same picture, at the bottom.** Each agent's input is produced by work its person cannot delegate.** Removing the person does
not leave the agent alone: it leaves it without food.

## Status

**All three are built and can be installed today**, and all three carry the same debt, which is
better not hidden: **verified over a synthetic corpus, not tested against a real organisation's
documentation.**

| Agent | Installs as | Its page | Its tests | A and B tables |
|---|---|---|---|---|
| **Vera** · PMO | `criterio-pmo` · 17 commands, 10 skills | this one | [results](../../tests/criterio-pmo/RESULTADOS.md) · [what they prove](../../tests/criterio-pmo/EVIDENCIA.md) | **no open rows** |
| **Samuel** · project | `criterio-pm` · 9 commands, 8 skills | [go](../criterio-pm/README.md) | [results](../../tests/criterio-pm/RESULTADOS.md) · [what they prove](../../tests/criterio-pm/EVIDENCIA.md) | **no open rows** |
| **Alba** · product | `criterio-product` · 11 commands, 12 skills | [go](../criterio-product/README.md) | [results](../../tests/criterio-product/RESULTADOS.md) · [what they prove](../../tests/criterio-product/EVIDENCIA.md) | **no open rows** |
| **Rostrum** · the server | inside `criterio-pmo` | [SERVER.md](SERVER.md) | inside Vera's | — |

**Each agent has its test analysis in markdown**, generated from the run: which gate ran,
what it proves, how many checks, how long it took, and — in the same file, not in an annex —
**what it does not cover**. They read on GitHub with nothing downloaded.

**None of the three design sheets has a row left in "missing" or "partial".** What remains
is not construction.

And one debt that belongs to all three at once: **extraction has never been run.** The three
corpora seed the state from their reference answers, so the document → model → record chain has
not been exercised.

The run that supports these states, with what it proves and what it does not, is in the three
evidence pages under [`tests/`](../../tests/) and the whole in
[`docs/pruebas.md`](../../docs/pruebas.md) — with charts, for a browser, in
[`pruebas.html`](../../docs/pruebas.html).

## Install

![Installation: four clicks, or two commands](../../docs/img/en/instalacion.png)

**Claude Code**

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pmo@criterio
/pmo-setup
```

## The first fifteen minutes

![The first fifteen minutes](../../docs/img/en/quince-minutos.png)

There is no configuration file to edit, no template to fill in, no folder to tidy before
starting. Setting it up **is a conversation**, and it ends with a result over your documents.

| | |
|---|---|
| **0 – 2 min** | **Install.** Two commands in Claude Code, or four clicks in Cowork |
| **2 – 4 min** | **It looks before it asks.** You point it at the folder where your project documentation lives, however it is. It lists what it found: how many projects it distinguishes, how many documents, which formats, which is the most recent, and which ones it will not be able to read. That is when you know it is actually looking at your things |
| **4 – 8 min** | **Five questions.** Who you are, when your committee meets, who receives the report and in what form, and the terms. One at a time, each with a suggested answer drawn from what it already saw. *"I don't know"* is a valid answer |
| **8 – 15 min** | **A first result.** It sweeps **three projects**, not the whole portfolio, so you see something real in minutes: what it knew about each one, what is not stated anywhere, and any contradiction or overdue commitment it found on the way |

At the end it tells you how long the full portfolio would take, and what your folder is
missing for the analysis to be better. But as a finding, not a requirement: **this works with
whatever is there.**

---

## The agent does not wait to be called

![The cadence: it wakes on its own, and almost always stays quiet](../../docs/img/en/cadencia.png)

This is the difference between a command and an agent. A command waits. **This one is
scheduled and runs on its own.**

The five questions at setup produce a cadence, and the cadence produces what is due each day.
The decision is date arithmetic, so the code makes it rather than judgement in the moment:

```
python3 scripts/pmo.py due --state <state> --config <file>
```

And `/pmo-wake` is the command the clock invokes: it looks at what is due, does it, and **if
nothing is due it produces nothing.** Staying quiet when nothing happened is not an omission —
it is the only reason an agent that runs every day is still installed a month later.

Three things can be due. The **sweep**, which looks at what changed in the folder and only
recomputes the projects it touched. The **committee report**, which lands with the lead time
you configured so you can react to what it finds. And the **confirmation**, five fields per
run — the ones that age worst: sponsor, manager, approved budget, committed end date and
scope.

Putting it on a clock is on your organisation's side: a scheduled task in Cowork, or the
operating system's scheduler in Claude Code. **And if they do not want unattended runs** — in
a bank that is a reasonable answer — the cadence still says what is due, run by hand. What is
lost is being told without anyone asking.

## Want your sponsor to see this without asking you for it?

![Rostrum: the report, for whoever does not open a folder](../../docs/img/en/servidor.png)

Up to here the report is files on your machine. **A sponsor does not open a folder of
files**: they open a link, or they open nothing. That is what **Rostrum** is for, this
family's server. A rostrum does not measure or correct: it holds up what is already
written, at the height of whoever is going to read it.

```
/pmo-server
```

It raises **a portal with three sections** — PMO reports, projects, products — and the
link between project and product runs **both ways**. That is where the thing no other
page can say lives: when a product is built by projects reporting to different
committees, each committee sees its project and **none of them sees the product**.

And it has one more thing, which is what changes how it gets used: **whoever is looking
can leave the agent a written question.** It does not answer on the spot — the agent is
not running — but the question stays in the queue, and the next time Vera wakes it
handles it. *"This does not match what I know"* is the most valuable request in the
system: it is a person telling you which document is missing.

**It authenticates nobody, and that is deliberate**: it is published behind the access
control your organisation already has. It listens only on your machine unless you say
otherwise.

→ **[Rostrum, with screenshots of every section and what to ask your organisation for](SERVER.md)**

## How each one is configured and how often it runs

| | Vera | Samuel | Alba |
|---|---|---|---|
| **Installs as** | `criterio-pmo` | `criterio-pm` | `criterio-product` |
| **Instances** | One per PMO | **One per project** | **One per product** |
| **Configured with** | `/pmo-setup` | `/pm-setup` | `/product-setup` |
| **How long that takes** | Fifteen minutes | Ten | Ten |
| **What you have to tell it** | Where the documentation is, when the committee meets, who you are | Where your project is, when your meeting is, who you are | Where the definition is, who decides what gets built, who you are |
| **Where it lands** | A file of the person's, written by the command | Same | Same |
| **The one you put on a clock** | `/pmo-wake` | `/pm-wake` | `/product-wake` |
| **Cadence that makes sense** | Daily if the sweep is on; and the report with its lead time before the committee | Daily with the sweep, or the day before and the day after the meeting | **Weekly is enough** |
| **What wakes it besides the clock** | A request somebody left in Rostrum | New minutes in the folder | Something crossing a threshold on its own |

**Nobody edits a configuration file by hand.** It is a rule of all three setup commands, not a
courtesy: if changing a threshold means opening a JSON, the threshold stays as it shipped and
the configuration stops describing the organisation. You say it in the conversation and the
command rewrites it.

Each plugin ships its `scripts/config.example.json` so you can see the full shape without
installing anything.

### Why the three cadences are different

It is not a preference: **each agent measures against something else.**

- **Vera** measures against the folder. A new document can change a project's state today, so a
  daily sweep makes sense and the report is delivered ahead of the committee — so the PMO
  manager has time to react to what it finds, not to learn about it once it has been sent.
- **Samuel** measures against the meeting. His cycle is not the calendar: it is *before the
  meeting* and *after the meeting*, which is why `/pm-wake` checks which side you are on before
  offering anything.
- **Alba** measures against the passing of time, and that changes everything. Her thresholds are
  counted in months, so a daily run over a register that barely moves is noise with punctuality.
  **But she is the only one of the three whose findings appear with nobody doing anything**: the
  requirement that had gone fifty-nine days undecided reaches sixty, and nobody is going to open
  a session to ask whether that has happened yet.

### All three go quiet when there is nothing

It is the rule that decides whether an agent is still installed a month later. The three clock
commands return `quiet` when nothing is due, and with `quiet` the output is one line: what was
reviewed and when it comes back.

An agent that produces a report to say there is no news teaches you to ignore it, and the day
there is news nobody opens it.

### What is **not** scheduled

Worth saying here and not in a footnote: **none of the three schedules itself.** All three ship
the command a clock invokes, and the clock lives outside the plugin — a Claude Cowork scheduled
task, or the operating system's scheduler invoking Claude non-interactively. Somebody has to
set it up, once, and each clock command explains how.

And for it to run with nobody watching, two things are needed that do not depend on this
repository: **that the session can run without approving each step**, and **that the folder is
mounted when the clock fires.**

**If the organisation does not want unattended runs** — and in a bank that is a reasonable
answer — all three commands work run by hand, and the cadence still says what is due. What is
lost is that they warn you without anybody asking, which is exactly what is hardest to see by
hand.

## What ends up configured

`/pmo-setup` writes it from your answers, on your machine and in a file of yours: where the
documents are, where the state lives, your committee cadence, the shape of the report, the
thresholds that make it speak, and the record that you accepted the terms, with your name and
the date.

All of it is changed **by talking**. If you want silence reported at ten days instead of
fifteen, you tell it.

## How you work with Vera

The family's three agents share five behaviours. They are not style: they are what makes the
output something you can put in front of a committee.

1. **Every value carries the citation of the document it came from**, with its date. A value
   with no source is a defect, not a degraded case.
2. **"Not stated anywhere" is a valid answer**, and it is the most common one at the start.
3. **They go quiet when there is nothing.** None produces a report to say there is no news.
4. **None of them declares.** None writes a project's status or decides what gets built.
5. **None of them writes to anybody.** They produce the list; chasing someone is a conversation.

What changes between them is **the rhythm of the conversation**, and that is worth knowing
before you install.

**With Vera you talk little and read a lot.** She works over forty folders: the conversation is
short — you name a project, or none — and what comes back is long, a report somebody will take
to a committee.

**The rhythm:** `/pmo-setup` once, `/pmo-wake` on a clock, and after that you ask by exception
— *"diagnose PRY-014 from zero"*, *"reconstruct what happened"*, *"build the committee pack"*.

**What she will ask of you:** to confirm **five fields per run**, never forty — ask about forty
and nobody answers. And **to act on what the report asks for**: if nobody acts, the next report
says the same thing, and that is not a defect of the agent.

**What not to ask her:** what state a project is in. She tells you what its manager declares
and what the documents hold up, and **the difference between the two is the product.**

## What it never does

This is what is worth being clear about before installing it, and it is not in small print:

- **It does not write in your folders.** It reads your documents; reports and records go to a
  state folder you choose.
- **It does not decide.** It produces working drafts. It frames the decision as a question
  with its options; who decides, and assuming what, belongs to whoever holds the authority.
- **It does not declare a project's status.** The manager does. The agent shows them what
  against, and the gap between the two is the most valuable finding in the system.
- **It does not know what is not written.** It does not know what was said in the corridor or
  decided in a call nobody minuted. Every finding of its own is *"according to the
  documents"*, and it says so.
- **It does not guess.** Every field carries the citation of the document it came from. *"Not
  stated anywhere"* is a valid and expected answer.

And one that has to be said out loud: **your documents are processed on the AI platform's
infrastructure**, not only on your machine. Confirm that is admissible under your policies
before pointing it at confidential material. Full disclaimer in
[DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

---

From here down is for whoever wants to audit it before installing it. **All of this can be
read without running anything**, and that is deliberate.

## How it works

![How it works: the model extracts, the code computes](../../docs/img/en/como-funciona.png)

The spine is the **project record**: a data contract every command reads and writes, with the
citation to the source document and its date in every field. No command reads raw documents on
its own. That is what allows consolidating forty projects without reading them again,
**computing instead of opining**, and comparing one run against the previous one.

Three scripts, which are the only things that do not opine. [`scripts/texto.py`](scripts/texto.py)
turns the document into text: `.docx`, `.xlsx` and `.pptx` with the standard library — they
are ZIP files with XML inside —, `.eml` with the email parser, and PDF with `pdftotext`. What
cannot be read is declared with the reason. [`scripts/pmo.py`](scripts/pmo.py) does the
arithmetic, and its `index` subcommand decides the cost of every run: two hashes per document,
one to know whether extracting is worth it and another to know whether re-reading is. And
[`scripts/informe.py`](scripts/informe.py) builds the printed report out of what the other two
produced, without reading a single document again.

## The three agents and the single contract

Nothing talks to anything directly. **The project record is the only contract.**

![The single contract: who writes the record and who only reads it](../../docs/img/en/contrato.png)

The Product Manager works before a plan exists: it does not write into the record, **it creates
it.** Its delivery closes with the charter, which is the record's birth certificate.

### The seven invariants

1. **The agents do not talk to each other.** They talk through the record.
2. **Rostrum, the server, does not write.**
3. **The source can change; the record cannot.** A new adapter fills the same fields.
4. **Declared and evidenced never merge**, whether they came from a file or a database.
5. **The model extracts, the code computes.**
6. **No agent writes the declaration.** A person writes the declared status.
7. **One record, one writer.** Two agents reading the same documents write two records, and
   they never merge. The difference between them is the finding.

The sixth is the easiest to break out of convenience and the one that takes the whole system
with it: if the agent declares, the comparison between declaration and evidence compares the
system against itself, and all of this becomes a generator of pretty reports. It is not a
documentation recommendation: it is a restriction of the write path, and it fails if attempted.

The seventh is the fourth one level up, and it appears the moment more than one agent looks at
the same project. The comfortable way out — one record and one owner — forces a bad choice in
both directions: if the manager owns it, the PMO cannot read for itself when it has doubts; if
the PMO owns it, it enters the critical path of seventy projects. Two records remove the
problem instead of arbitrating it, and **what was a write conflict becomes the signal.**

## What still belongs to the people

All three roles continue to exist in full. This extends capability; it does not replace
function. And the argument is not politeness, it is structural:

> **Each agent's input is produced by the non-delegable work of its person.**

The PM agent needs somebody to run the meeting, because that is where the minutes it feeds on
come from. The PMO agent needs somebody to chase what the report asks for, because if nobody
acts the next report says the same thing. The product agent needs somebody to talk to the
customer, because there is no synthesis without an interview.

Removing the person does not leave the agent alone: it leaves it without food. Each design
sheet documents what breaks first if you try, and in what order.

## The three agents' commands

Thirty-seven commands, and each one lives in its agent's plugin. This is the family's full list; the detail of each one is on its plugin's page.

### Vera · `criterio-pmo` · seventeen

| Command | What it does |
|---|---|
| `/pmo-setup` | **The first thing you run.** Looks at your folders, asks five questions and produces the first report over your own documents |
| `/pmo-wake` | **What the clock invokes.** Looks at what is due today, does it, and stays quiet if nothing is |
| `/pmo-server` | Raises **Rostrum**, the server: exposes the report for whoever does not open a folder, and says what to ask the organisation for |
| `/document-index` | Which documents actually changed, what has to be re-read, and which citations stopped resolving |
| `/portfolio-scan` | Reads the folder and produces or updates one record per project. The way in |
| `/portfolio-report` | Consolidated report: what changed, what contradicts itself, what is silent, what has no support |
| `/status-report` | A project's status, and the signals its declared light does not account for |
| `/health-check` | Diagnoses a project from zero against the evidence, assuming nothing from its own report |
| `/project-history` | What happened in a project, with the timeline and since when the declared status stopped holding |
| `/steering-pack` | Committee material as a package of decisions, not as a progress report |
| `/raid-log` | Risks, assumptions, issues and dependencies, including the ones said aloud that nobody recorded |
| `/change-control` | Assesses a change across scope, time and cost, and creates a new baseline without deleting the previous one |
| `/budget-tracking` | Approved, committed, executed and projection, with variance against both baselines |
| `/vendor-tracking` | Contractual deliverables against evidence of receipt and against invoicing |
| `/product-view` | The state of a product across every project that builds it |
| `/project-charter` | Reviews or drafts the charter, flagging what is missing and what the gap costs |
| `/project-closure` | Closes against the agreed success criteria, with lessons that can be supported |

### Samuel · [`criterio-pm`](../criterio-pm/README.md) · nine

| Command | What it does |
|---|---|
| `/pm-setup` | **The first thing you run.** Looks at your folder, asks four questions and reads your latest minutes |
| `/pm-agenda` | The agenda with the items that need somebody in the room, and with what this meeting cannot move |
| `/pm-minutes` | The minutes from the transcript or the notes, with every item attributed to a person |
| `/pm-commitments` | Who promised what, what is overdue with no evidence, and what keeps being rescheduled meeting after meeting |
| `/pm-report` | The weekly report, complete **except for the status**, which you declare |
| `/pm-publish` | Publishes your record where the PMO can read it |
| `/pm-plan` | The first draft of the plan and the WBS from the charter, **committing no date** |
| `/pm-escalate` | What exceeds your authority, as a closed question, with who it reaches computed |
| `/pm-wake` | **The one you put on a clock.** Looks at what is due around your meeting, and stays quiet when nothing is |

### Alba · [`criterio-product`](../criterio-product/README.md) · eleven

| Command | What it does |
|---|---|
| `/product-setup` | **The first thing you run.** Looks at your folder, asks four questions and contrasts the definition you already have |
| `/product-discovery` | Interviews and tickets into themes with the citation of who said it, and the theme said for months that nobody has turned into anything |
| `/product-requirements` | The register with its gaps: no owner, no acceptance criteria, accepted with nobody having asked for it, and what nobody decides |
| `/product-definition` | The definition against the evidence of demand, and where business and data disagree |
| `/product-trace` | Requirement → decision → project → deliverable, and the two gaps above |
| `/product-spec` | The specification draft with verifiable criteria and the gaps marked, not filled |
| `/product-charter` | The charter: where the record is born and the writer changes hands |
| `/product-business-case` | The business case's structure with every figure cited, and the gaps with who produces them |
| `/product-publish` | Publishes your record where the other products can read it |
| `/product-overlap` | Where you overlap another product: the same metric counted twice, the same project, the same segment |
| `/product-wake` | **The one you put on a clock.** What crossed a threshold with nobody doing anything |

**The only one that is not an agent's** is `/pmo-server`: Vera runs it, and what it starts is Rostrum, which decides nothing.

## Vera's ten skills

They load on their own when the topic appears. They are the knowledge the commands share, and
they can be read the way a manual is read.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `project-record` | The record: schema, extraction rules, citation, field states, what to do when two documents contradict each other | Its own · also in Samuel and Alba |
| `document-intake` | Which document has to be re-read and which does not, which formats can be read and with what, renaming, deletion, and the citation that stopped resolving | Its own · also in Samuel and Alba |
| `portfolio-health` | The nineteen signals with what each one means, the thresholds that govern them, and the three defences against data that stopped being true | Its own |
| `baseline-variance` | Append-only baseline, variance against the original and against the current one, the rebaseline against what the committee authorised, the four budget figures | Its own · also in Samuel |
| `raid-taxonomy` | The four categories and how to tell them apart, assessment, escalation criteria | Its own · also in Samuel and Alba |
| `commitment-tracking` | Commitments said in meetings: extraction, states, what counts as evidence, and the one repeated with a new date each time | Its own · also in Samuel |
| `governance-artifacts` | Charter, committee, change control and closure: what each contains and who decides what | Its own · also in Samuel and Alba |
| `vendor-control` | Contract against evidence of receipt against invoicing, with an amount per deliverable | Its own · also in Samuel |
| `project-diagnosis` | Diagnosis from zero: in what order you read, and when the answer is that it cannot be diagnosed | Its own · also in Samuel |
| `portfolio-history` | A project's history from its documents, and the point where the evidence separated from what was being reported | Its own |

## And the family's eighteen

Eighteen distinct skills across the three agents. **What they share are literal copies, not an imported module**: an installed plugin has to run on its own, and an `import` into the other one's path works here and fails on the machine of whoever installed it.

`scripts/sincronizar.py` copies them and `tests/coherencia.py` fails if they drift apart.

| Skill | Vera | Samuel | Alba |
|---|:--:|:--:|:--:|
| `assumption-tracking` | · | · | ● |
| `baseline-variance` | ● | ● | · |
| `commitment-tracking` | ● | ● | · |
| `demand-evidence` | · | · | ● |
| `discovery-synthesis` | · | · | ● |
| `document-intake` | ● | ● | ● |
| `governance-artifacts` | ● | ● | ● |
| `portfolio-health` | ● | · | · |
| `portfolio-history` | ● | · | · |
| `product-health` | · | · | ● |
| `product-metrics` | · | · | ● |
| `project-diagnosis` | ● | ● | · |
| `project-record` | ● | ● | ● |
| `raid-taxonomy` | ● | ● | ● |
| `regulatory-sweep` | · | · | ● |
| `requirement-record` | · | · | ● |
| `specification-draft` | · | · | ● |
| `vendor-control` | ● | ● | · |

## Out of scope, and why

**Capacity and resource allocation**, and **benefits realisation**. Not because they matter
little: because the data is not in the folder. Capacity requires real hours and benefits
require later measurement that almost no organisation has.

A skill that promises what the input does not allow burns the credibility of the whole plugin.

**No regulatory content.** Portfolio management is method, not regulation: it works the same
in Bogotá as in Santiago. If a regulatory obligation touches a project, this plugin records it
as a constraint or as a risk, and does not opine on it.

## How it is verified

All three run on the standard library, with nothing installed. Over synthetic material with known
answers there is a grader and the result of the last run, with what it proves and what it does
not: [`tests/criterio-pmo/`](../../tests/criterio-pmo/).

Acceptance criteria in [`DISENO.es.md`](DISENO.es.md#criterios-de-aceptación). The design of the capability, with what
the agent does not do and what remains the people's, in
[`DISENO.es.md`](DISENO.es.md) — in Spanish, as a working document.

**How the last run went, generated from the run itself:** [`tests/criterio-pmo/RESULTADOS.md`](../../tests/criterio-pmo/RESULTADOS.md).
