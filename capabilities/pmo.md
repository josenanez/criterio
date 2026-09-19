# PMO capability

**Portfolio and project governance.**

[Español](pmo.es.md) · [Back to the marketplace](../README.md)

State: **PMO Agent available** · PM Agent under construction

---

## Where a PMO breaks

It is not short of templates. It has plenty.

What it lacks is someone reading together the documentation that already exists. Forty projects, each with its charter, its schedule, its minutes, its emails and its spreadsheets. Each document was read by someone, once. Nobody has cross-read them.

And the crossing is what decides:

- The milestone whose date passed with not a single document proving it was met.
- The project reporting green that has not produced a document in five weeks.
- Last week's minutes naming a sponsor different from the one in the charter.
- The dependency one plan declares and the other project's plan ignores.
- The commitment someone made in three consecutive meetings, with a new date each time.

None of that shows up in a status report, because the status report is written by the person being assessed.

---

## The two agents

The capability has two agents because the organisation has two roles, and they need different things.

### PMO Agent

For the PMO lead and their analysts. **Forty projects, broad sweep, weekly or committee cadence.**

It reads the whole portfolio's documentation, keeps a record per project, and on every run says what changed. It consolidates, crosses dependencies between projects, and prepares the committee.

### PM Agent

For each project manager, junior or senior. **One project, depth, daily or per-meeting cadence.**

It turns transcripts and minutes into decisions and commitments with an owner and a date. Its core function is one no tool a project manager uses today performs: **the commitment that was made and not kept.** Meetings are full of *"I'll have it by Friday"* and nobody records them. The agent extracts them and on every run checks which ones passed their date with no evidence.

### How they relate

The project record is the interface between them: the PM Agent fills it as a by-product of its daily work, and the PMO Agent stops reverse-engineering status from messy folders.

With one rule that is not negotiable: **the PM's record is a declaration; the PMO's finding is evidence.** They stay two separate sources, and the gap between them is the most valuable signal in the system. *"The manager reports the milestone green; the last minutes say the vendor did not deliver"* is the conversation that cannot be had today.

Standards come down from the PMO: thresholds, conventions and the record schema are published to a shared folder, and each PM Agent reads them and checks itself against them before the PMO looks at anything. It works over a corporate file server, with no integration project.

---

## What the PMO Agent does today

You install it, tell it where the documents live, and it works with whatever is there. It does not require the folder to be tidy.

| I want to… | Command |
|---|---|
| Set it up and see a first result | `/pmo-setup` |
| Have it read everything and build the record | `/portfolio-scan` |
| See the state of the portfolio | `/portfolio-report` |
| See the state of one project | `/status-report` |
| Prepare the steering committee | `/steering-pack` |
| Risks, assumptions, issues and dependencies | `/raid-log` |
| Assess a change in scope, time or cost | `/change-control` |
| Vendors: delivered against invoiced | `/vendor-tracking` |
| Budget | `/budget-tracking` |
| Review or draft the charter | `/project-charter` |
| Close a project | `/project-closure` |

### What makes it different from a report generator

**The baseline is append-only.** When a plan is rebaselined, the previous one is not deleted. That is exactly how slippage gets hidden: rebaseline, the light goes green, and nobody sees the project is a year late. Here every variance is reported against two references — the original and the current — with the number of rebaselines beside it.

**Four budget figures, not two.** Approved, committed, executed and projection. A project at 40% executed and 95% committed has no headroom: its budget is spent and not yet incurred. That is invisible if you look at executed against approved, which is how it is almost always looked at.

**Silence is measured.** Days since the last document and since the last meeting. A project with no documentation is not badly run: it is undocumented, and that is a different finding that also has to be said.

**No privilege for whoever reports.** The state it produces is a comparison between what is declared and what is evidenced. When no document backs the declaration, the state is *unsupported* — which is not the same as being wrong, and is the most common state in a real PMO.

### When it speaks

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

All configurable, and changed by talking, not by editing files.

---

## Evidence

**There are no real runs yet.** When there are, they go here: how many documents, how many projects, how long it took, how many findings and which of them nobody had seen — with the procedure to reproduce them.

What is verified today is the machine, not the value:

```
python3 ../plugins/criterio-pmo/scripts/pmo.py selftest
```

Twelve known results, including the cases that get themselves wrong: slippage against the original baseline versus the current one with a rebaseline in between, and the committed budget that looks healthy and is not.

---

## Getting started

```
/plugin marketplace add josenanez-company/criterio
/pmo-setup
```

The setup command looks at your folders, asks five questions and runs a first sweep over **three projects**, not the whole portfolio, so you see a result in minutes rather than a message saying "done, you can start now".

Before installing, read the [disclaimer](../DISCLAIMER.md). This produces working drafts, not decisions.
