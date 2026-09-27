# The PMO family

**What each agent does, how the three operate together, how each one behaves and how you work
with it.** This is the family's page: what a director needs before deciding whether this comes
into their organisation, and what a manager needs before installing it.

[Español](FAMILIA.es.md) · The public promise, with the third-party figures, is in the
[marketplace README](../../README.md); each plugin's inventory of commands and skills is in its
own README.

Each agent's design sheet — the three classes of function, what is left to build, the closed
decisions and the open ones — ships with its plugin and is written in Spanish, because its use
is to argue about it:

- [**Vera** · PMO agent](DISENO.es.md) — portfolio governance
- [**Samuel** · Project Manager agent](../criterio-pm/DISENO.es.md) — one project
- [**Alba** · Product Manager agent](../criterio-product/DISENO.es.md) — before the project exists

---

## What each agent does

Three agents and a server. Every capability with the command that delivers it: if it has no
command it does not exist, and this table promises nothing you cannot run.

### Vera · the PMO's agent — `criterio-pmo`

| What it does | Command |
|---|---|
| Get the agent working over your own folders, in fifteen minutes | `/pmo-setup` |
| Read the documentation and produce one record per project, with a citation for every value | `/portfolio-scan` |
| Say which documents actually changed and which citations stopped resolving | `/document-index` |
| The consolidated report: what changed, what contradicts what, what has gone quiet | `/portfolio-report` |
| One project's status, separating what is declared from what the documents hold up | `/status-report` |
| Diagnose a project from zero, without believing its own progress report | `/health-check` |
| Reconstruct what happened, and when the evidence stopped supporting what was reported | `/project-history` |
| Risks, assumptions, issues and dependencies — including the ones said aloud and never registered | `/raid-log` |
| The four budget figures and what is really available | `/budget-tracking` |
| Assess a change and leave the new baseline without erasing the previous one | `/change-control` |
| Contracted against received against invoiced | `/vendor-tracking` |
| Review or draft the charter, and what follows from whatever is missing | `/project-charter` |
| Close against the success criterion agreed, with lessons that can be evidenced | `/project-closure` |
| The committee pack: a set of decisions, not a progress report | `/steering-pack` |
| A product's status across every project building it | `/product-view` |
| Publish the report where the team will read it, with nothing installed | `/pmo-server` |
| **Wake up on its own** and do whatever the cadence says is due | `/pmo-wake` |

### Samuel · the project manager's agent — `criterio-pm`

| What it does | Command |
|---|---|
| Get the agent working over your project, in ten minutes, reading your latest minutes | `/pm-setup` |
| **Who promised what and by when**, with the citation of the meeting where it was said | `/pm-commitments` |
| What is overdue with no evidence, and what keeps being rescheduled meeting after meeting | `/pm-commitments` |
| The agenda with the items that need somebody in the room, and what that room cannot move | `/pm-agenda` |
| The minutes, separating commitment, decision, intention with no owner, and risk said in passing | `/pm-minutes` |
| The weekly report, complete **except for the status**, which you declare | `/pm-report` |
| Publish your record where the PMO can read it | `/pm-publish` |
| The first draft of the plan and the WBS, **committing no date** | `/pm-plan` |
| What exceeds your authority as a closed question, with who it reaches **computed** | `/pm-escalate` |
| **Wake up on its own** around your meeting: the agenda before, the minutes after | `/pm-wake` |

### Alba · the product manager's agent — `criterio-product`

| What it does | Command |
|---|---|
| Get the agent working and contrast the definition you already have, in ten minutes | `/product-setup` |
| Interviews and tickets into themes **with the citation of who said it** | `/product-discovery` |
| The theme said for months that nobody has turned into anything | `/product-discovery` |
| The requirement register with its gaps: no owner, no criteria, no evidence | `/product-requirements` |
| **The definition against the evidence of demand**, and what is not stated anywhere | `/product-definition` |
| Where the business declares one number and the metric measures another, with both sources | `/product-definition` |
| What was decided and nobody is building, and the project whose record names another product | `/product-trace` |
| The specification draft with verifiable criteria and the gaps **marked, not filled** | `/product-spec` |
| The charter with which the project's record is born | `/product-charter` |
| The business case's structure with every figure cited, and the gaps with who produces them | `/product-business-case` |
| Publish your record where the other products can read it | `/product-publish` |
| **The same metric in two business cases**, the same project with two owners, the same segment | `/product-overlap` |
| **Wake up on its own** and say what crossed a threshold with nobody doing anything | `/product-wake` |

### Rostrum · the server — inside `criterio-pmo`

| What it does | How |
|---|---|
| Publish the portfolio report at an address the team will open | `/pmo-server` |
| Navigation across PMO, project and product reports, with the link between the last two | the portal |
| Take a request — *review, explain, correct* — and leave it in Vera's queue | the portal |
| **Never write the record.** A restriction of the code, verified on every run | by design |

---

## How the three operate

![How the three agents operate](../../docs/img/en/flujo.png)

The order in time is what makes them a system rather than three tools:

```
    THE DEFINITION           THE PROJECT             THE PORTFOLIO           THE TEAM
       Alba                     Samuel                    Vera                Rostrum
         │                         │                        │                     │
         │──── the charter ──────► │                        │                     │
         │     the record is born  │                        │                     │
         │                         │──── ficha-pm.json ───► │                     │
         │                         │     published          │                     │
         │                         │                        │──── the report ───► │
         │ ◄──── the record ───────┴────────────────────────┘                     │
         │       is my product being built?                                       │
         │                                                  │ ◄─── the request ───┘
         │                                                  │   review · explain · correct
```

**Two closed loops, and neither goes through a shared database.** The charter comes down once,
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

### And the people, in the same picture

```
   The product manager         The project manager        The PMO manager
   decides what gets built     declares the status        decides what escalates
   and signs the charter       and runs the meeting       and chases what the report asks for
         │                              │                           │
         └──────── each one gives their agent the input ────────────┘
                   no agent can produce on its own
```

**Each agent's input is produced by work its person cannot delegate.** Removing the person does
not leave the agent alone: it leaves it without food.

---

## How each one behaves, and how you work with it

All three share five behaviours. They are not style: they are what makes the output something
you can put in front of a committee.

1. **Every value carries the citation of the document it came from**, with its date. A value
   with no source is a defect, not a degraded case.
2. **"Not stated anywhere" is a valid answer**, and it is the most common one at the start.
3. **They go quiet when there is nothing.** None of them produces a report to say there is no
   news.
4. **None of them declares.** None writes a project's status or decides what gets built.
5. **None of them writes to anybody.** They produce the list; chasing someone is a conversation.

What changes between them is **the rhythm of the conversation**, and that is worth knowing
before you install them.

### With Vera you talk little and read a lot

Vera works over forty folders. The conversation is short — you name a project, or none — and
what comes back is long: a report somebody will take to a committee.

**How you work with her:** run `/pmo-setup` once, put `/pmo-wake` on a clock, and after that
ask by exception — *"diagnose PRY-014 from zero"*, *"reconstruct what happened"*, *"build the
committee pack"*.

**What she will ask of you:** confirm five fields per run, never forty. Ask about forty and
nobody answers. And **act on what the report asks for**: if nobody acts, the next report says
the same thing, and that is not a defect of the agent.

**What not to ask her:** what state a project is in. She tells you what its manager declares
and what the documents hold up, and **the difference between the two is the product.**

### With Samuel you talk every week

Samuel works over one project and his cycle is the meeting. The conversation is frequent and
short, and it almost always turns on a document that has just appeared.

**How you work with him:** `/pm-setup` once; then, the day before the meeting `/pm-agenda`, the
day after `/pm-minutes` with the transcript or the notes, and once a week `/pm-report`.

**What he will ask of you:** the minutes. They are his main input and without them he dries up
— a manager who does not keep what the meeting leaves written needs to know that on day one,
and `/pm-setup` says so. And **the status declaration**, which he always asks for **after**
showing you the evidence and never before: if he proposed a status, your declaration would stop
being independent information.

**What not to ask him:** to chase an overdue commitment. He gives you the name, the date and
the citation; you make the call, because chasing is a conversation.

### With Alba you talk in seasons

Alba works before the project exists, and that work is not weekly: it comes in bursts — a round
of interviews, a product committee, a definition about to be closed — with quiet weeks between.

**How you work with her:** `/product-setup` once; `/product-discovery` every time a round of
interviews ends; `/product-definition` when the definition is about to close or somebody is
about to argue with it; `/product-charter` the day it becomes a project.

**What she will ask of you:** to talk to the customer. It is the part of the craft no agent
will ever have, and without it there is nothing to synthesise. And **to decide**: what has gone
sixty days undecided is still undecided when Alba finishes; what changes is that it now has a
name, a number of days, and somebody to ask.

**What not to ask her:** whether something will land well. That is in no document.

### With Rostrum you do not talk

It is a server. You start it with `/pmo-server`, you open an address, and the report is there
for whoever is not going to open a folder. The only thing it sends back inward is a request
somebody left, and Vera attends to it on her next run.

---

## The common need: projects

All three agents exist around the same object, and that choice carries the whole weight of the
design: **a project has a plan, and without a plan there is nothing to compare against.**

The entire proposition rests on contrasting what somebody declares against what the documents
hold up. That comparison needs an approved reference. In a process or in a department there is
no *against what*; in a project there is, and it is called the baseline.

---

## The three agents and the single contract

Nothing talks to anything directly. **The project record is the only contract.**

```
   files ────┐
             ├──► extraction ──► RECORD ──► computation ──► projection ──► server
   database ─┘                    ▲ ▲ ▲
                                  │ │ └── PMO      writes findings, reads all of them
                                  │ └──── PM       writes the record, reads its own
                                  └────── Product  creates it, with the charter
```

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

---

## The three classes

Every function of every role falls into one of three. **Criterio's built scope is A and B.**

### A — What the agent does, and today takes somebody's time

Work the organisation already performs every week: reading, consolidating, cross-checking,
reporting. The agent does not speed it up, it replaces it. You recognise it by a simple test:
**if nobody does it, somebody notices.**

### B — What the agent does and today nobody does

Work the organisation does not perform, not out of negligence but because it would cost days
per project: the fourteen-month forensic, the contradiction across forty folders, the
assumption nobody verified. You recognise it by the inverse test: **if nobody does it, nobody
notices.**

The distinction matters for understanding the value. A saves time on work already being done,
and the team is grateful. B produces what today exists in no PMO, and a director buys it.

### C — What the agent does not do

A set of actions the agent **does not execute**. Nothing more.

This list does not assess risk or anybody's exposure: it describes the agent's boundary.
Whoever installs Criterio accepts the [terms](../../TERMS.md) — verification is theirs, §2;
it ships with no warranty and no liability, §5 — and the [disclaimer](../../DISCLAIMER.md). The
responsibility for use and execution belongs to the organisation deploying it, and if in their
context class C is larger than this list, bounding and documenting it is theirs to do, with
whatever additional disclaimer their internal governance requires.

Each row of C carries two things, and neither is a risk:

- **Requires** — why it is outside the agent's scope: *authority* (it commits the
  organisation), *information outside the documents*, or *judgement about people*.
- **What it hands the agent** — because almost every function in C produces the input of a
  function in A or B. That is the part that makes this a cycle and not two separate worlds.

---

## What they are called

**The capability is called PMO, CFO or CLO. The agent carries a person's name.** They are two
different things and it is worth not mixing them: the capability is the organisation's
function, and the agent is who extends it.

That they carry a person's name is not decoration: **they are capabilities that extend real
people**, and the whole product rests on the person still being there. A proper name says that
without having to explain it.

| Piece | Name | Where it comes from | The sentence |
|---|---|---|---|
| PMO agent | **Vera** | Latin *verus*, the true | *Vera says what the documents say, not what gets reported* |
| Project Manager agent | **Samuel** | "he who heard" | *Samuel heard what was said in the meeting, and remembers it on Friday* |
| Product Manager agent | **Alba** | daybreak, before there is light | *Alba works before the project exists* |
| The server | **Rostrum** | a speaker's platform | *It holds up what is already written, where others can read it* |

**The rule, which is what makes this scale rather than the list:** an agent's name is a
person's name **whose meaning points at the craft its family extends**, and it has to be able
to finish the sentence "X does this, and does not opine". If it cannot finish it, it is the
wrong name.

Samuel shows it best: that agent's central function is **the commitment said and not kept**,
and the name literally means "he who heard".

Families to come choose by the same rule and with their own guild's references — **CFO** with
Mateo, patron of accountants and bankers, or Luca after Pacioli; **CLO** with Ivo, patron of
lawyers. Whoever belongs to the guild recognises the reference without anyone explaining it,
and whoever does not just sees a name, which is fine too.

**The server is the only one without a person's name, and that is deliberate.** The agents
carry one because they make decisions about what they read; the server makes none. It is
infrastructure, and it keeps an object's name: a rostrum does not measure, does not correct and
does not opine — it holds up what is already written at the height of whoever is going to read
it. If it ever computed something, the name would stop being true, and that is exactly what we
want to be noticeable.

**The names are not translated** — they are proper nouns — and **they are not identifiers**:
the plugin is still called `criterio-pmo`, the commands and the skills do not change. The name
gives character to what the person sees, not to what the code imports.

---

## One owner per thing

Documentation is not duplicated. A table copied into three documents goes stale in the first
one nobody looks at, and that already happened: the signal list on the public page was once
five signals behind and promised one the code did not emit.

| Thing | Owner | Why there |
|---|---|---|
| The threshold values | `DEFAULT_THRESHOLDS` in `scripts/pmo.py` | It is what the code reads. Any other copy is an opinion |
| What each signal means and when it deserves an alarm | the `portfolio-health` skill | It is what the model loads at runtime, and it has to stand on its own |
| The inventory of commands and skills | the plugin's README | The plugin ships through the marketplace and its README travels with it |
| The public promise and the third-party figures | the marketplace README | It is the first page anybody opens, and the only one that decides an installation |
| Each agent's design | the `DISENO.es.md` of its plugin | Classes, flow, what belongs to people, what is missing |
| The result of the runs | `tests/<plugin>/EVIDENCIA.md` | The evidence lives with the material that produced it |

Two things verify it, and neither is a human remembering: `scripts/validate_plugins.py` demands
that the plugin's README list every command, and `tests/coherencia.py` demands that every signal
the code computes be documented in its skill and that every command appear on the public page.
**If something is added and not documented in its owner, it fails.**

---

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

---

## Status

**All three are built and can be installed today**, and all three carry the same debt, which is
better not hidden: **verified over a synthetic corpus, not tested against a real organisation's
documentation.**

| Agent | Installs as | Its A and B tables |
|---|---|---|
| Vera · PMO | `criterio-pmo` · 17 commands, 10 skills | **No open rows** |
| Samuel · Project Manager | `criterio-pm` · 9 commands, 8 skills | **No open rows** |
| Alba · Product Manager | `criterio-product` · 11 commands, 12 skills | **No open rows** |
| Rostrum · the server | Inside `criterio-pmo` | — |

**None of the three design sheets has a row left in "missing" or "partial".** What remains
is not construction.

And one debt that belongs to all three at once: **extraction has never been run.** The three
corpora seed the state from their reference answers, so the document → model → record chain has
not been exercised.

The run that supports these states, with what it proves and what it does not, is in the three
evidence pages under [`tests/`](../../tests/) and, drawn, in
[`docs/pruebas.html`](../../docs/pruebas.html).

---

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
