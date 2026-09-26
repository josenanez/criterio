# criterio-pm

**Samuel remembers what was promised in your meeting.** You run the committee, negotiate
and unblock. He arrives with the week prepared and with the list of what was said and
not done.

[Español](README.es.md) · Apache 2.0 · One instance per project

**Status: the seven commands are built**, along with the eight skills of the method and the
arithmetic verified against a corpus with answers written by hand. **What has not been
tested yet: extraction over a real organisation's documentation** — the corpus seeds the
record, so the document → model → record chain has not been exercised. Nothing is announced
as finished until the [acceptance criteria](ACCEPTANCE.md) pass.

---

## Install

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pm@criterio
/pm-setup
```

If you run the portfolio rather than a project, yours is
[`criterio-pmo`](../criterio-pmo/README.md).

## The first result

`/pm-setup` does not ask you to tidy anything up first. It looks at your project's
folder, asks four questions — one at a time, each with a suggested answer — and **reads
your latest minutes**. With that it shows you, in under ten minutes:

- **Who promised what and by when**, with the citation of the minutes where it was said.
- **What is overdue with no evidence** in the file.
- **What was left undated** — *"we'll look at it next week"*. It cannot be overdue, and
  **that is exactly why it disappears from every report.**

Then it tells you what your folder is missing for this to get better. As a finding, not
a requirement: **it works with whatever is there.**

## The commitment said and not kept

It is why Samuel exists, and **no tool you use today does it.**

Meetings are full of *"I'll have it by Friday"*. It is not in the plan, because it is not
a schedule task. It is not in the minutes, because someone wrote those from memory two
days later. It was said, and it was lost.

`/pm-commitments` extracts it from the minutes with owner, date and source. And it does
one more thing, which is what separates useful follow-up from a list that only grows:
**the same person promising the same thing with a new date is a rescheduled commitment,
not a new one.**

> **Rubén** · Deliver the certification test plan
> Promised for 27 November, and before that for the 13th, and before that for 30 October.
> **Three times is not a follow-up problem: it is a block nobody has named.**

Three loose entries are three overdue items chased separately. One entry with three
reschedules is a conversation that has to happen.

## What it never does

- **It does not declare your project's status.** You do. Samuel shows you what against,
  and the gap between the two is the most valuable finding in the system. Not a
  recommendation: a restriction of the write path.
- **It does not attend your meeting.** It works on what the meeting leaves written, and
  produces what the meeting needs.
- **It does not write in your documentation folder.** The only thing it can ever put
  there is your record, and only when you run `/pm-publish`.
- **It writes to nobody.** It produces the list; chasing a commitment is a conversation,
  not an automated reminder.
- **It does not mark as met what nobody documented.** *"Rubén says he delivered it"*
  closes nothing: the receipt note closes it.
- **It does not guess.** Every value carries the citation of the document it came from.
  *"Not stated anywhere"* is a valid and expected answer.

And one that has to be said out loud: **your documents are processed on the AI
platform's infrastructure**, not only on your machine. Confirm that is admissible under
your policies before pointing it at confidential material. Full disclaimer in
[DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

---

## You and the PMO read the same documents

Samuel writes your record. Vera, the PMO's agent, writes hers over the same documents.
**They never merge**, and that is deliberate: the comfortable way out — one record and
one owner — forces a bad choice in both directions.

`/pm-publish` puts your record in the project's governance folder, and Vera reads it
like any other document. **When both cite a source and disagree, one of them saw a paper
the other did not** — and half the time the one who is right is you, because you were in
the meeting where the sponsor changed and the charter was never updated.

What you have and the PMO does not — every meeting's commitments — **is not a
contradiction**: it is a difference of depth, and it is not reported as a finding.

## The seven commands

| Command | What it does |
|---|---|
| `/pm-setup` | **The first thing you run.** Looks at your folder, asks four questions and reads your latest minutes |
| `/pm-agenda` | The agenda with the items that need somebody in the room, and with what this meeting cannot move |
| `/pm-minutes` | The minutes from the transcript or the notes, with every item attributed to a person |
| `/pm-commitments` | Who promised what, what is overdue with no evidence, and what keeps being rescheduled meeting after meeting |
| `/pm-report` | The weekly report, complete **except for the status**, which you declare |
| `/pm-publish` | Publishes your record where the PMO can read it |
| `/pm-wake` | **The one you put on a clock.** Looks at what is due around your meeting, and stays quiet when nothing is |

Three of them are one cycle, and that is why they exist: **whoever builds the agenda
beforehand receives the minutes afterwards.** The seventh is of another kind: `/pm-wake` is
what makes this an agent rather than a box of commands — it does not wait to be called. Without the agenda the meeting inherits last
week's running order; without the minutes, what was said gets written from memory two days
later and stops being evidence of anything.

## The eight skills

They load on their own when the topic appears. They are literal copies from
`criterio-pmo`, because a risk is a risk whoever is looking at it and the record is the
whole family's data contract.

| Skill | What it encapsulates |
|---|---|
| `project-record` | The record: schema, extraction, citation, field states, what to do when two documents contradict each other |
| `document-intake` | Which document has to be re-read and which does not, which formats can be read and with what |
| `commitment-tracking` | **The central function.** Extraction, states, what counts as evidence, and the one repeated with a new date each time |
| `raid-taxonomy` | The four categories and how to tell them apart, assessment, escalation criteria |
| `baseline-variance` | Append-only baseline, variance against the original and the current one, the four budget figures |
| `governance-artifacts` | Charter, committee, change control and closure: what each contains and who decides what |
| `vendor-control` | Contract against evidence of receipt against invoicing |
| `project-diagnosis` | Diagnosis from zero: in what order you read, and when it cannot be diagnosed |

It does not ship `portfolio-health` or `portfolio-history`: they only make sense looking
at the whole, and a project manager does not look at the whole.

## How it is verified

```
python3 tests/criterio-pm/grade.py      19 checks over two projects
python3 scripts/pmo.py selftest         the arithmetic
python3 scripts/texto.py --selftest     document conversion
```

On the standard library, with nothing installed. Over a synthetic corpus with answers
written by hand from the minutes — **including a negative control**: a project with
meetings and commitments that produces not a single finding. An agent that finds
something there is a noise generator.

What that run proves and, in the same detail, **what it does not**, in
[`tests/criterio-pm/EVIDENCIA.md`](../../tests/criterio-pm/EVIDENCIA.md).

The full design, with the three classes of function and what stays with the person, in
[`DISENO.es.md`](DISENO.es.md), which ships with the plugin — in
Spanish, as working documents.

The three agents together, and how they meet, in [`FAMILIA.md`](../criterio-pmo/FAMILIA.md).
