# Criterio

**A marketplace of agent families that accelerate organisational capabilities.**

[Español](README.es.md) · [Terms](TERMS.md) · [Disclaimer](DISCLAIMER.md) · [Contributing](CONTRIBUTING.md)

Apache 2.0 · Four clicks to install · Each agent produces its first result in fifteen minutes

**Status: in testing (0.3).** The agents are being tested command by command against seeded cases; reliability figures are published when they are measured, not before. [Security](SECURITY.md)

---

| | | |
|:--:|:--:|:--:|
| ![Portfolio, project and product](docs/img/en/pmo.png) | ![CFO](docs/img/en/cfo.png) | ![CLO](docs/img/en/clo.png) |
| **[criterio-pmo →](families/criterio-pmo/README.md)**<br>three agents and a server | criterio-cfo<br>not built | criterio-clo<br>not built |

---

## The problem was never a missing tool

An organisation does not move by departments: it moves by **capabilities**. The capability to govern a portfolio of projects. To close a month and answer for the numbers. To review a contract before signing it.

Each has its own method, its own language and its own ways of failing. And they all share the same bottleneck: **hundreds of documents nobody has read together.** Charters, schedules, minutes, reconciliations, contracts. Each was read by someone, once. Nobody has cross-read them.

Work tools help you produce one more document. The problem was never a missing template.

**Criterio is a marketplace of agents, one per capability.** They read what already exists, keep a record of what they found with a citation for every data point, and on the next run say what changed.

---

## The families

A **family** groups the agents that need each other to cover one whole capability. It is
not a catalogue category: the agents in a family share a data contract and hand work to
one another. Agents from different families do not.

| Family | Scope | Objective | State |
|---|---|---|---|
| **[criterio-pmo](families/criterio-pmo/README.md)** | The governance of a portfolio, of each project and of each product | That what is declared and what the documents support can be compared, every day and across the whole | **Three agents and a server, installable today** |
| **criterio-cfo** | Close, control and financial reporting | That closing the books stops depending on somebody remembering what is missing | [Declared, not built](plugins/criterio-finance/README.md) |
| **criterio-clo** | Contracts, compliance and legal risk | That a company knows what it signed, what expires and what it committed to | [Declared, not built](plugins/criterio-legal/README.md) |

**The list is not closed.** A family joins when somebody who performs that capability
wants to build it, and the format is in [CONTRIBUTING.md](CONTRIBUTING.md).

## What every agent shares

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

## Installation

The marketplace is added once, and after that you install what you need.

```
/plugin marketplace add josenanez/criterio
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace
from GitHub → `josenanez/criterio`.

**What to install depends on the role you have, and each family explains that.** For the
project governance one, see [criterio-pmo](families/criterio-pmo/README.md#installing-the-family).

## Apache 2.0 — what we give and what we invite

**We give, in full and with no conditions,** each agent's method, its record schemas, the code that computes, its acceptance criteria and the way to measure them.

**What we invite**

- Use it inside your organisation without asking, and adapt it to how you work.
- Change the criteria: thresholds are configuration, not code.
- **Build the capability you are missing.** If you practise a function that is not on the list, its agent should be written by someone who knows the work, not by someone who knows how to code. The format is in [CONTRIBUTING.md](CONTRIBUTING.md).
- If you find it wrong, open an issue with the document that proves it. That is worth more than a star.

**What we do not claim**

This produces working drafts, not decisions. Nothing here has been certified by anyone. The agents know what was written, not what was said outside the documents. Read the [disclaimer](DISCLAIMER.md) before installing: using it means accepting the [terms](TERMS.md).

---

Maintained by [José Francisco Ñáñez](https://josenanez.com).

---

Maintained by [José Francisco Ñáñez](https://josenanez.com).

---

Maintained by [José Francisco Ñáñez](https://josenanez.com).
