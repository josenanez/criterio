# Samuel · one project's agent

**Samuel remembers what was promised in your meeting.** You go to the committee, negotiate and
unblock. He arrives with the week ready and with the list of what was said and not done.

[Español](README.es.md) · `criterio-project` · Apache 2.0 · One instance per project

**Status: the nine commands are built**, along with the eight skills of the method and the
arithmetic verified against a corpus with answers written by hand. **What has not been tested
yet: extraction over a real organisation's documentation** — the corpus seeds the record, so the
document → model → record chain has not been exercised. Nothing is announced as finished until
the [acceptance criteria](DISENO.es.md#criterios-de-aceptación) pass.

**This page reads on its own.** Samuel works without his siblings: if all you run is your
project, everything is here, tests included. The family — how he meets Vera and Alba — is in the
[criterio-pmo family](../../families/criterio-pmo/README.md).

---

## What it is

| | |
|---|---|
| **Whose hands it extends** | One project manager's |
| **What it works on** | **One project.** His own, and no other |
| **What it looks at** | His folder, and above all **what the meeting leaves written** |
| **Cadence** | The meeting's: the agenda before, the minutes after, the report once a week |
| **Instances** | One per project |

## What it does

**What it does that nobody else does: the commitment said and not kept.** Meetings are full of
*«I'll have it by Friday»*. It is not in the plan, because it is not a schedule task. It is not
in the minutes, because somebody wrote those from memory two days later. It was said, and it was
lost. **No tool a project manager uses today picks it up.**

**What it can answer that today nobody answers:** who promised what and by when, with the
citation from the minutes, what fell due with no evidence in the file, and **what keeps being
rescheduled meeting after meeting** — which is not a tracking problem, it is a blockage nobody
has named.

### The nine commands

| Command | What it does |
|---|---|
| `/pm-setup` | **The first thing you run.** Looks at your folder, asks four questions and reads your last minutes |
| `/pm-agenda` | The agenda with the items that need somebody in the room, and with what this meeting cannot move |
| `/pm-minutes` | The minutes over the transcript or the notes, with everything attributed to a person |
| `/pm-commitments` | Who promised what, what fell due with no evidence, and what keeps being rescheduled meeting after meeting |
| `/pm-report` | The full weekly report **except the status**, which you declare |
| `/pm-publish` | Publishes your record where the PMO can read it |
| `/pm-plan` | The first draft of the plan and the WBS from the charter, **without committing to any date** |
| `/pm-escalate` | What exceeds your authority, as a closed question, with who it reaches computed |
| `/pm-wake` | **The one you put on a clock.** Looks at what is due according to your meeting, and if nothing is due it stays quiet |

Three of them are a cycle, and that is why they are there: **the one that builds the agenda
before receives the minutes after.** Without the agenda the meeting inherits last week's order
of business; without the minutes, what was said is written from memory two days later and stops
being evidence of anything.

### The eight skills

They load on their own when the subject comes up. They are literal copies from `criterio-portfolio`,
because a risk is a risk whoever looks at it and the record is the whole family's data contract.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `project-record` | The record: schema, extraction, citation, field states, what to do when two documents contradict each other | Copy of Vera's · also in Alba |
| `document-intake` | Which document has to be re-read and which not, which formats can be read and with what | Copy of Vera's · also in Alba |
| `commitment-tracking` | **The central function.** Extraction, states, what counts as evidence, and the one that repeats with a new date every time | Copy of Vera's |
| `raid-taxonomy` | The four categories and how to tell them apart, assessment, escalation criteria | Copy of Vera's · also in Alba |
| `baseline-variance` | Append-only baseline, variance against the original and the current one, the budget's four figures | Copy of Vera's |
| `governance-artifacts` | Charter, committee, change control and closure: what each one contains and who decides what | Copy of Vera's · also in Alba |
| `vendor-control` | Contract against evidence of receipt against invoicing | Copy of Vera's |
| `project-diagnosis` | The diagnosis from scratch: in what order things are read and when it cannot be diagnosed | Copy of Vera's |

## What it is for

`/pm-commitments` extracts the commitment from the minutes with owner, date and source. And it
does one more thing, which is what separates useful tracking from a list that just grows: **the
same owner promising the same thing with a new date is a rescheduled commitment, not a new
one.**

> **Rubén** · Deliver the certification test plan
> Promised for 27 November, and before that for the 13th, and before that for 30 October.
> **Three times is not a tracking problem: it is a blockage nobody has named.**

Three loose entries are three overdue items chased separately. One entry with three
reschedulings is a conversation that has to be had.

That case comes from the synthetic corpus, with the answer written by hand **before** running
the calculation, and it is the reason Samuel exists: not to read your project better than you
do, but to pick up what the meeting left said and **nobody wrote into any system.**

### And what it is not for

- **It does not declare your project's status.** You declare that. Samuel shows you what
  against, and the difference between the two is the system's most valuable finding. It is not a
  recommendation: it is a restriction of the write path.
- **It does not attend your meeting.** It works on what the meeting leaves written, and produces
  what the meeting needs.
- **It does not write in your documentation folder.** The only thing it may ever put there is
  your record, and only when you run `/pm-publish`.
- **It does not write to anybody.** It produces the list; chasing a commitment is a
  conversation, not an automatic reminder.
- **It does not mark as done what nobody documented.** *«Rubén says he delivered it»* closes
  nothing: the acceptance note closes it.
- **It does not guess.** Every value carries the citation of the document it came from. *«It is
  not stated anywhere»* is a valid and expected answer.

**And one thing is deliberately absent: the portfolio view.** It carries neither
`portfolio-health` nor `portfolio-history`, because they only make sense looking at the whole
set and a project manager does not look at the whole set. It carries no regulatory content
either: project management is method, not regulation. If a regulatory obligation touches yours,
it records it as a constraint or as a risk and does not opine on it.

And one that has to be said out loud: **your documents are processed on the AI platform's
infrastructure**, not only on your machine. Confirm that this is admissible under your policies
before pointing it at confidential material. Full disclaimer in
[DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installing and configuring

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-project@criterio
/pm-setup
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from
GitHub → `josenanez-company/criterio`.

If you run the portfolio and not a project, yours is
[Vera](../criterio-portfolio/README.md). If you define a product,
[Alba](../criterio-product/README.md).

### The first result

`/pm-setup` does not ask you to tidy anything up before starting. It looks at your project's
folder, asks four questions — one at a time, each with a suggested answer — and **reads your
last minutes**. With that it shows you, in under ten minutes:

- **Who promised what and by when**, with the citation from the minutes where it was said.
- **What fell due with no evidence** in the file.
- **What was left with no date** — *«we'll look at it next week»*. It cannot be overdue, and
  **that is exactly why it disappears from every report.**

Then it tells you what your folder is missing for this to be better. As a finding, not as a
requirement: **it works with whatever is there.**

**What ends up configured** is written by `/pm-setup` from your answers, on your machine and in a
file of yours: where the project's folder is, which day you meet, where your record lives, the
thresholds, and the record that you accepted the terms, with your name and the date. All of that
is changed **by talking**.

### How often it runs

This is the difference between a command and an agent. A command waits. **This one is scheduled
and runs on its own.**

His cadence is your meeting's, and that is what produces what is due each day. The decision is
date arithmetic, so the code takes it and not the judgement of the moment:

```
python3 scripts/portafolio.py due --state <state> --config <file>
```

And `/pm-wake` is the command the clock invokes: the day before the meeting it prepares the
agenda, the day after it asks for the minutes, once a week it builds the report, and **if nothing
is due it produces nothing.** Staying quiet when nothing happened is not an omission — it is the
only reason an agent that runs every day is still installed the following month.

Putting it on a clock is on your organisation's side: a scheduled task in Cowork, or the
system's scheduler in Claude Code. **And if unattended runs are not welcome** — in a bank that
is a reasonable answer — the cadence still says what is due, run by hand. What you lose is being
told without anyone asking.

**And if you want your sponsor to see the report without asking you for it**, the family has a
server that publishes it with a section for projects, where whoever is looking can leave the
agent a written question. → **[Rostrum](../criterio-portfolio/SERVER.md)**

## Working with the others

Samuel works alone. If the other two are installed, **there is nothing to connect**: they
meet through the project record, which is one more document in the folder.

| With whom | What happens |
|---|---|
| **Alba** | Delivers the project charter, and the record is born with it. From that day the writer is Samuel: **one record, one writer** |
| **Vera** | Samuel publishes his record with `/pm-publish` and Vera reads it. She writes hers over the same documents and **the two never merge**. When they disagree, half the time the manager is right, because he was in the meeting where the thing changed that the charter never updated |
| **Rostrum** | Publishes the project's report on the portal, for whoever will not open a folder |

## Tests

### How it is built

The spine is the **project record**: a data contract every command reads and writes, with the
citation of the source document and its date on every field. No command reads raw documents on
its own. That is what makes it possible to build the report without reading anything again, to
**compute instead of opine**, and to compare one week against the previous one.

Two scripts, which are the only thing that does not opine.
[`scripts/texto.py`](scripts/texto.py) turns the document into text: `.docx`, `.xlsx` and
`.pptx` with the standard library — they are ZIPs with XML inside —, `.eml` with the email
parser, and PDF with `pdftotext`. What cannot be read is declared with the reason. And
[`scripts/portafolio.py`](scripts/portafolio.py) does the arithmetic: the cadence, the variance against both
baselines, and the commitment that repeats with a new date.

**Both are literal copies of Vera's, not imports**, and that is deliberate: an installed plugin
has to run on its own. In the repository, `scripts/sincronizar.py --check` fails if the copies
have drifted apart, because two copies computing differently over the same documents would leave
nobody knowing which to believe.

### How it is verified

```
python3 tests/criterio-project/grade.py      19 checks over two projects
python3 scripts/portafolio.py selftest         the arithmetic
python3 scripts/texto.py --selftest     document conversion
```

On the standard library, with nothing installed. Over a synthetic corpus with hand-written
answers read from the minutes — **including a negative control**: a project with meetings and
commitments that produces not one finding. An agent that finds something there is a noise
generator.

**How the last run came out, generated from the run itself:**
[`tests/criterio-project/RESULTADOS.md`](../../tests/criterio-project/RESULTADOS.md). What each piece of
the material proves and, in the same detail, **what it does not**, in
[`EVIDENCIA.md`](../../tests/criterio-project/EVIDENCIA.md).

The full design, with the acceptance criteria and what still belongs to the person, in
[`DISENO.es.md`](DISENO.es.md), which travels with the plugin.

And the family's tests — what no agent can answer alone — in the
[family README](../../families/criterio-pmo/README.md#the-familys-tests).

