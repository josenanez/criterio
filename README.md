# Criterio

**A marketplace of agents that accelerate organisational capabilities.**

[Español](README.es.md) · [Terms](TERMS.md) · [Disclaimer](DISCLAIMER.md) · [Contributing](CONTRIBUTING.md)

Apache 2.0 · Four clicks to install · Each agent produces its first result in fifteen minutes

---

## What it is

An organisation does not move by departments: it moves by **capabilities**. The capability to govern a portfolio of projects. To close a month and know what the numbers say. To review a contract before signing it.

Each of those has its own method, its own language and its own ways of failing. A generic assistant does not know what a baseline is, nor why rebaselining hides slippage, nor why a liability exclusion written in absolute terms does not hold.

**Criterio is a marketplace of agents, one per capability.** You install them, configure them by talking, and roll them out to the team that does that work.

---

## The capabilities

| Capability | Agents | State |
|---|---|---|
| **[PMO](capabilities/pmo.md)** — portfolio and project governance | PMO Agent · PM Agent | **PMO Agent available**, PM Agent under construction |
| **CFO** — close, control and financial reporting | — | Declared |
| **CLO** — contracts, compliance and legal risk | — | Declared |

The list is not closed. A capability joins when someone who practises it wants to build its agent.

---

## Installation

**Claude Cowork** — Customize → Browse plugins → Personal → **+** → Add marketplace from GitHub → `josenanez-company/criterio`

**Claude Code**

```
/plugin marketplace add josenanez-company/criterio
```

After installing, each agent has a setup command that looks at your folders, asks five questions and produces a first result on your own documents. **Nobody edits a configuration file by hand.**

---

## What every agent shares

This is not a collection of loose assistants. They are all built on the same four rules, and that is what makes their output survive a committee.

**They separate what is declared from what is evidenced.** What someone asserts goes in one column; what the documents support goes in another. They are never merged, and the gap between them is usually the highest-value finding.

**Nothing is overwritten.** A record keeps its history. When a new version silently replaces the previous one, what disappears is exactly what needed to be seen.

**The model extracts; code computes.** Reading a date is reading. Subtracting, projecting and adding is arithmetic, and arithmetic lives in code, where it is deterministic and testable. No number in a report comes from the model's estimate.

**Every data point carries its citation, or declares that it is missing.** *"Not stated anywhere"* is a valid and expected finding.

**And they know when to stay quiet.** They run on their own and speak only when something crosses a threshold. An agent that reports every week whether or not there is news is ignored within a month.

---

## Evidence

Each capability publishes the figures from its real runs: how many documents, how long it took, how many findings, and which of them nobody had seen. Together with the procedure for anyone to reproduce them.

**What has not been measured is not invented.** The whole project rests on a statement carrying its source; an unbacked marketing figure would contradict the one thing that makes it trustworthy. Until a capability has real runs, its page says so.

What can be verified today, by cloning the repository:

```
python3 plugins/criterio-pmo/scripts/pmo.py selftest    the arithmetic against 12 known results
python3 scripts/validate_plugins.py                     marketplace structure and consistency
```

---

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
