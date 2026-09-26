# criterio-pm

**Bevel**, the project manager's agent. One instance per project.

[Español](README.es.md) · Apache 2.0

**Status: under construction.** The design is settled, and the scripts and the eight
skills it shares with `criterio-pmo` are already here and verified. **There are no commands
yet**, so there is nothing to invoke — but the skills load on their own when the topic
appears. Nothing is announced as finished until the acceptance criteria pass.

## What it will do

The agent **does not attend the meeting** — the manager does. What it does is let the
manager arrive with the week prepared: the agenda built beforehand, the minutes drafted
afterwards, the plan current against the evidence, and the progress report ready except
for one line.

Its central function is one no tool a project manager uses today performs: **the
commitment said and not kept.** Meetings are full of *"I'll have it by Friday"* and nobody
records them.

## What is already decided

**The agent does not declare the project's status.** The manager does. The agent shows
them what against, and the gap between the two is the most valuable finding in the system.

**It writes its own record, and nobody else's.** Bevel and Plumb read the same
documents and write two separate records that **never merge**. Bevel publishes its own
into the project's governance folder, Plumb reads it like any other document, and **when
the two both cite a source and disagree, one of them saw a paper the other did not.** That
is the signal.

**It is distributed separately from `criterio-pmo`**, with the arithmetic copied from there
by a rule that fails if the two copies drift apart. A project manager does not need
seventeen portfolio commands.

## Where the design is

Complete, with the three classes of function, the flow, what stays with the person and
what is left to build in order:
[`docs/agents/project-manager.md`](../../docs/agents/project-manager.md) — in Spanish, as
working documents.

The family's frame, the seven invariants and the one-owner-per-thing rule:
[`docs/agents/README.md`](../../docs/agents/README.md).

## The eight skills it already ships

They load on their own when the topic appears, so **installing it today does do
something**: the method is there, even though no commands drive it yet. They are literal
copies from `criterio-pmo`, because a risk is a risk whoever is looking at it, and the
record is the whole family's data contract.

| Skill | What it encapsulates |
|---|---|
| `project-record` | The record: schema, extraction rules, citation, field states, what to do when two documents contradict each other |
| `document-intake` | Which document has to be re-read and which does not, which formats can be read and with what |
| `commitment-tracking` | **Bevel's central function.** Commitments said in meetings: extraction, states, what counts as evidence, and the one repeated with a new date each time |
| `raid-taxonomy` | The four categories and how to tell them apart, assessment, escalation criteria |
| `baseline-variance` | Append-only baseline, variance against the original and against the current one, the four budget figures |
| `governance-artifacts` | Charter, committee, change control and closure: what each contains and who decides what |
| `vendor-control` | Contract against evidence of receipt against invoicing, with an amount per deliverable |
| `project-diagnosis` | Diagnosis from zero: in what order you read, and when the answer is that it cannot be diagnosed |

What it does **not** ship, by scope and not by accident: `portfolio-health` and
`portfolio-history` only make sense looking at the whole, and a project manager does not
look at the whole. That is what [`criterio-pmo`](../criterio-pmo/README.md) is for.

## Acceptance criteria


See [ACCEPTANCE.md](ACCEPTANCE.md). Nothing ships until they pass.
