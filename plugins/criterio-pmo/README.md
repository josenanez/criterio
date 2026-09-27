# criterio-pmo · the PMO family

**Three agents and a server, around a single data contract.** Each one extends a different
person in the chain — whoever defines the product, whoever runs the project, whoever watches the
portfolio — and none of them talks to another directly: they talk through the project record.

[Español](README.es.md) · Apache 2.0 · All three install today

**This is the family's page.** It explains what the family is, who is in it, how it installs,
what each agent answers for, and how the whole is verified. **Each agent's detail is on its own
page**, and each one reads alone: you can install one agent without the others.

- **[Vera](VERA.md)** · the PMO's agent — and **[Rostrum](SERVER.md)**, the server that publishes her report
- **[Samuel](../criterio-pm/README.md)** · the project manager's agent
- **[Alba](../criterio-product/README.md)** · the product manager's agent

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

## What the three share

This is not a collection of loose assistants. All three are built on the same five behaviours,
and they are not style: they are what makes their output something you can put in front of a
committee.

1. **Every value carries the citation of the document it came from**, with its date. A value
   with no source is a defect, not a degraded case.
2. **"Not stated anywhere" is a valid answer**, and it is the most common one at the start.
3. **They go quiet when there is nothing.** None produces a report to say there is no news. An
   agent that reports every week whether or not there is news gets ignored within a month.
4. **None of them declares.** None writes a project's status or decides what gets built.
5. **None of them writes to anybody.** They produce the list; chasing someone is a conversation.

What changes between them is **the rhythm of the conversation**, and that is on each one's page.

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

## Status

**All three are built and can be installed today**, and all three carry the same debt, which is
better not hidden: **verified over a synthetic corpus, not tested against a real organisation's
documentation.**

| Agent | Installs as | The A and B tables of its design |
|---|---|---|
| **Vera** · PMO | `criterio-pmo` · 17 commands, 10 skills | **no open rows** |
| **Samuel** · project | `criterio-pm` · 9 commands, 8 skills | **no open rows** |
| **Alba** · product | `criterio-product` · 11 commands, 12 skills | **no open rows** |
| **Rostrum** · the server | inside `criterio-pmo` | — |

**None of the three design sheets has a row left in "missing" or "partial".** What remains
is not construction.

And one debt that belongs to all three at once: **extraction has never been run.** The three
corpora seed the state from their reference answers, so the document → model → record chain has
not been exercised.

The run that supports these states, with what it proves and what it does not, is in the three
evidence pages under [`tests/`](../../tests/) and the whole in
[`docs/pruebas.md`](../../docs/pruebas.md) — with charts, for a browser, in
[`pruebas.html`](../../docs/pruebas.html).

## Installing the family

Each agent is a plugin and installs on its own. **You do not need all three**: install the one
that covers the role you have.

```
/plugin marketplace add josenanez-company/criterio

/plugin install criterio-pmo@criterio      if you run the portfolio
/plugin install criterio-pm@criterio       if you run a project
/plugin install criterio-product@criterio  if you define a product
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from
GitHub → `josenanez-company/criterio`.

After installing, each agent has its own setup command that looks at your folders, asks a few
questions and produces a first result over your own documents. **Nobody edits a configuration
file by hand.**

And if you install more than one, they find each other: **there is nothing to connect.** They
talk through the record, which is a document in the project's folder.

## What each agent answers for, and where its detail lives

The four pieces, with the same for each one: what it answers for, what it never does, and where
all its detail lives. **Each agent's page reads on its own** — somebody can install one without
the others.

| | What it answers for | What it never does | Its page | Its tests |
|---|---|---|---|---|
| **Vera** · the PMO | The whole portfolio: consolidating, contrasting what is declared against the evidence, and building the committee pack | Does not declare any project's status, and does not prioritise demand | [VERA.md](VERA.md) · 17 commands, 10 skills | [results](../../tests/criterio-pmo/RESULTADOS.md) |
| **Samuel** · one project | What the meeting leaves written: the commitment said and not kept, the plan against the evidence, and the report ready but for one line | Does not declare his project's status, and does not attend the meeting | [criterio-pm](../criterio-pm/README.md) · 9 commands, 8 skills | [results](../../tests/criterio-pm/RESULTADOS.md) |
| **Alba** · one product | What exists before the project: the definition against the evidence of demand, the requirement register, and the charter the record is born with | Does not decide what gets built, and does not talk to the customer | [criterio-product](../criterio-product/README.md) · 11 commands, 12 skills | [results](../../tests/criterio-product/RESULTADOS.md) |
| **Rostrum** · the server | Publishing the report where the team will read it, and taking the request from whoever will not open a folder | **Never writes the record**, and decides nothing | [SERVER.md](SERVER.md) | inside Vera's |

**The boundary is the same for all three, and it is not a recommendation: it is a restriction of
the write path.** None of them writes a project's declared status. A person writes that line,
and without it the comparison between declared and evidenced — which is what all of this lives
on — would be comparing the system against itself.

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

## The family's tests

**A single gate runs everything this repository verifies**, across the three agents at once:

```
python3 scripts/verificar.py
```

It is the equivalent of an integration test: it does not verify one agent, it verifies **that
the family is still a family.** What belongs to each agent — its arithmetic, its corpus, its
hand-written answers — is answered by its own page; here we verify what none of them can answer
alone:

| What is verified across the whole | Why it belongs to the family and not to one agent |
|---|---|
| That the documentation and the code say the same thing | A signal one agent computes and its skill does not explain breaks everyone's promise |
| That the marketplace and every plugin are complete | A plugin that installs without its README is an agent that arrives mute |
| **That the shared copies have not drifted apart** | The three share arithmetic by copy, not by import. Two copies that drift compute differently over the same documents, and nobody would know which to believe |
| That each agent has its test analysis and that it is linked | A result nobody can open is a result that does not exist |

**The whole run's result, generated from the run**, in
[`docs/pruebas.md`](../../docs/pruebas.md) — and with charts, to open in a browser, in
[`pruebas.html`](../../docs/pruebas.html).

**And each agent's, on its own page**, because each one answers for its own:
[Vera](../../tests/criterio-pmo/RESULTADOS.md) ·
[Samuel](../../tests/criterio-pm/RESULTADOS.md) ·
[Alba](../../tests/criterio-product/RESULTADOS.md).

Everything runs on the standard library with nothing installed. What each corpus proves and, in
the same detail, **what it does not**, in the three evidence pages under [`tests/`](../../tests/).

## The family's eighteen skills

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

