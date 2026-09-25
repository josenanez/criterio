# PMO capability

**Portfolio and project governance.**

[Español](pmo.es.md) · [Back to the marketplace](../README.md)

State: **PMO Agent available** · PM Agent under construction

---

## What we attack

Not the lack of templates. There are plenty.

We attack the fact that **nobody has read together the documentation that already exists**. Forty projects, each with its charter, its schedule, its minutes, its emails and its spreadsheets. Each document was read by someone, once. Nobody has cross-read them.

And the crossing is what decides:

- The milestone whose date passed with **not a single document proving it was met**.
- The project reporting green that **has not produced a document in five weeks**.
- Last week's minutes **naming a sponsor different** from the one in the charter.
- The dependency one plan declares and **the other project's plan ignores**.
- The commitment someone made in **three consecutive meetings, with a new date each time**.
- The rebaseline that turned the light back to green and **erased a year of accumulated slippage**.

None of that shows up in a status report. The status report is written by the person being assessed.

This is not a suspicion: [Wellingtone](https://wellingtone.co.uk/publications/state-of-project-management-research/) found in 2026 that **a third of projects have no baseline** and that half of organisations have no real-time indicators. A third of projects have nothing to be measured against.

---

## What we improve

Three concrete things, and none of them is "visibility".

**Evidence outweighs declaration.** Today a project's status is whatever the person running it says. Here it is a comparison between what is declared and what the documents support, with both columns visible and the gap flagged — and the comparison is made by the code, not by judgement in the moment.

**Slippage cannot be erased.** Today a rebaseline replaces the previous baseline and the history disappears. We make it cumulative: every variance is reported against the original baseline **and** the current one, with the number of rebaselines beside it.

**Arithmetic stops being an opinion.** Days of silence, variance, real headroom, projection: all computed in code, not estimated. No number in a report comes from an estimate.

---

## This is what we do

Every line in this table is **something the agent does**, not something it promises. They are written down, they can be read in this repository, and they can be run today.

| What it does | Command |
|---|---|
| Looks at your folders, asks five questions and produces a first result on your documents | `/pmo-setup` |
| Reads the portfolio's documentation and builds a record per project, with a citation and a date on every data point | `/portfolio-scan` |
| Says what changed since the last run, what contradicts itself, what has gone silent and what no document supports | `/portfolio-report` |
| Compares a project against its plan and names the signals the declared status does not account for | `/status-report` |
| Builds the committee pack as a set of decisions, not as a status report | `/steering-pack` |
| Raises risks, assumptions, issues and dependencies — **including the ones said in a meeting that nobody recorded** | `/raid-log` |
| Assesses a change across scope, time and cost, and creates a new baseline without deleting the previous one | `/change-control` |
| Crosses contractual deliverables against evidence of receipt and against what was invoiced | `/vendor-tracking` |
| Shows approved, committed, executed and projection — all four, not two | `/budget-tracking` |
| Reviews the charter and says what is missing and what the gap costs | `/project-charter` |
| Closes against the success criteria agreed at the start, with lessons anchored to documented facts | `/project-closure` |

**Why this is a commitment and not a promise:** every command is written as readable instructions in [`plugins/criterio-pmo/`](../plugins/criterio-pmo/), under Apache 2.0. You can audit it before installing, change it if it does not match how you work, and measure it against the acceptance criteria that ship with it.

### Five design decisions you notice on day one

**The status light is checked, not repeated.** The declared status is compared against the computed signals, and the ones it does not account for are listed. When a project reports green and there is evidence that green does not cover, the report says so, and the portfolio carries the figure: how many greens do not hold. A light that repeats what the manager declared already exists, and it is called the weekly report.

**The baseline is append-only.** When a plan is rebaselined, the previous one is not deleted. That is exactly how slippage gets hidden: rebaseline, the light goes green, and nobody sees the project is a year late.

**Four budget figures, not two.** A project at 40% executed and 95% committed has no headroom: its budget is spent and not yet incurred. That is invisible if you look at executed against approved, which is how it is almost always looked at.

**Silence is measured.** Days since the last document and since the last meeting. A project with no documentation is not badly run: it is undocumented, and that is a different finding that also has to be said.

**"Not stated anywhere" is an answer.** The agent does not fill gaps with what would be reasonable. It declares them.

---

## The two agents

The capability has two because the organisation has two roles, and they need different things.

### PMO Agent — available

For the PMO lead and their analysts. **Forty projects, broad sweep, committee cadence.** It consolidates, crosses dependencies between projects, and prepares the committee.

### PM Agent — under construction

For each project manager, junior or senior. **One project, depth, daily or per-meeting cadence.**

Its core function is one no tool a project manager uses today performs: **the commitment that was made and not kept.** Meetings are full of *"I'll have it by Friday"* and nobody records them. The agent extracts them with an owner and a date, and on every run checks which ones passed their date with no evidence.

### How they relate

The project record is the interface: the PM Agent fills it as a by-product of its daily work, and the PMO Agent stops reverse-engineering status from messy folders.

With one rule that is not negotiable: **the PM's record is a declaration; the PMO's finding is evidence.** They stay two separate sources, and the gap between them is the most valuable signal in the system. *"The manager reports the milestone green; the last minutes say the vendor did not deliver"* is the conversation that cannot be had today.

Standards come down from the PMO: thresholds, conventions and the record schema are published to a shared folder, and each PM Agent checks itself against them before the PMO looks at anything. It works over a corporate file server, with no integration project.

---

## When it speaks

It runs on its own and raises its voice only when something crosses a threshold:

| Signal | Speaks when |
|---|---|
| Milestone overdue | The date passed and there is no evidence of completion |
| Project silent | 15 days with no new document |
| Variance against baseline | Above 10% in time or cost |
| Commitment overdue | The date passed and there is no evidence |
| Contradiction between documents | Always — no number attached |
| Budget | Executed above 90% of committed |
| Governance change | Always |
| Declaration the evidence does not account for | Reports green and at least one signal is not covered by that green |
| Stale declaration | The declaration is 30 days old or more |
| Vendor deliverable overdue | The date passed and there is no evidence of delivery |
| Invoiced without delivery | An invoice is declared and not one deliverable is accepted |
| Unauthorised rebaseline | The baseline moved more days than the approved changes authorised |

All configurable, and changed by talking, not by editing files. **Staying quiet when nothing happened is the feature, not the failure.**

---

## Evidence

**There are no real runs yet.** When there are, they go here: how many documents, how many projects, how long it took, how many findings and which of them nobody had seen — with the procedure to reproduce them.

What does exist is a run over **synthetic material with known answers**: six projects, twenty-six documents, built to contain the failures a real folder contains. All seventeen signals fire when they should, the healthy project produces no alert at all, and the set is scored by 69 checks. What that run proves, what it does not, and the six limits it surfaced are in [`tests/criterio-pmo/EVIDENCIA.md`](../tests/criterio-pmo/EVIDENCIA.md).

What is verified today is the machine, not the value:

```
python3 plugins/criterio-pmo/scripts/pmo.py selftest    the arithmetic
python3 tests/criterio-pmo/generar.py                   the synthetic portfolio
python3 tests/criterio-pmo/grade.py                     69 checks against the known answers
python3 tests/coherencia.py                             that the docs and the code say the same thing
```

30 known results, including the cases that get themselves wrong: slippage against the original baseline versus the current one with a rebaseline in between, the committed budget that looks healthy and is not, the rebaseline that moved sixty-one days when the committee authorised thirty, and the green light that fails to account for nine signals.

---

## Getting started

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-pmo@criterio
/pmo-setup
```

The setup command runs a first sweep over **three projects**, not the whole portfolio, so you see a result in minutes rather than a message saying "done, you can start now".

Before installing, read the [disclaimer](../DISCLAIMER.md). This produces working drafts, not decisions.
