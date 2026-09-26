# criterio-pm

**Escuadra**, the project manager's agent. One instance per project.

[Español](README.es.md) · Apache 2.0

**Status: declared, under construction.** The design is settled and the scripts it shares
with `criterio-pmo` are already here and verified. **There are no commands or skills yet**,
so installing it today does nothing. Nothing ships until the acceptance criteria pass.

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

**It writes its own record, and nobody else's.** Escuadra and Plomada read the same
documents and write two separate records that **never merge**. Escuadra publishes its own
into the project's governance folder, Plomada reads it like any other document, and **when
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

## Acceptance criteria

See [ACCEPTANCE.md](ACCEPTANCE.md). Nothing ships until they pass.
