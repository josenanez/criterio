# Constanza · compliance

<img src="../../docs/img/en/robot-constanza.gif" alt="Constanza" width="220" align="right">

**Constanza puts every obligation of the organisation next to its evidence, every day and not only on audit day.** The obligations matrix period by period, the compliance obligations that come from contracts, policies due for review, new rules not yet assessed and the whistleblowing channel's deadlines. She says what is met with evidence, what is declared met without it and what is overdue.

[Español](README.es.md) · `criterio-compliance` · Apache 2.0 · One instance per entity

**Status: built and in testing.** The seven commands, the six skills and the calculation engine are built; the engine passes its deterministic test against synthetic material from four industries, with a key the agent never sees and two control entities. The end-to-end test with the agent is the next step. The family, with Fidel, is in [`families/criterio-clo/DISENO.es.md`](../../families/criterio-clo/DISENO.es.md) (Spanish).

---

## How it works

| | |
|---|---|
| **The large language model (LLM) extracts** | What only a written document carries: the status the period report declares, the new rule a bulletin announces |
| **The code calculates** | Every obligation against its evidence within the window of its frequency, progress weighted by criticality, overdue reviews, days without assessment and channel deadlines: `scripts/legal.py`, standard library, the same result every time |
| **The organisation defines** | The obligations, their source, owner and due date. Constanza brings no obligations and does not say what a rule requires |

The matrix model follows ISO 37301: every obligation with its source, owner and evidence. First version: Colombia and Ecuador.

## The commands

<!-- clo:comandos · generado por scripts/familias.py; no se edita a mano -->
| # | Command | What it delivers |
|---|---|---|
| 0 | `/criterio-compliance:compliance-setup` | The configuration, the reviewed matrix and the first compliance status |
| 1 | `/criterio-compliance:compliance-scan` | The compliance record up to date, with what changed and the new signals |
| 2 | `/criterio-compliance:compliance-status` | Compliance status: declared against evidenced, obligation by obligation |
| 3 | `/criterio-compliance:policy-review` | Every policy with its next review, and the overdue ones |
| 4 | `/criterio-compliance:regulatory-watch` | New rules with their assessment, and the applicable ones without an obligation |
| 5 | `/criterio-compliance:reports-cases` | Whistleblowing cases against their deadline |
| 6 | `/criterio-compliance:compliance-wake` | What compliance needs today; silent when nothing does |
<!-- /clo:comandos -->

## The skills

<!-- clo:skills · generado por scripts/familias.py; no se edita a mano -->
`compliance-record` · `legal-intake` · `obligations-matrix` · `policy-control` · `regulatory-change` · `whistleblowing-channel`
<!-- /clo:skills -->

## The first result

In the first fifteen minutes, `compliance-setup` shows the status of the period: every obligation in the matrix with or without its evidence, what is declared next to what is evidenced, and progress weighted by criticality. From there, every command delivers its report in the same order: what needs attention, the result, what could not be processed, the questions it asked and the sources.

## What it never does

- It does not add, remove or rewrite obligations in the matrix: the organisation defines them.
- It does not say whether a rule applies, what it requires or from when, and it states no rule or deadline from memory.
- It does not file reports with supervisors, and it does not sign.
- It does not read the content of a report or process who made it: only the deadlines in the case log.
- It does not declare the compliance status: the compliance officer does.
- It never moves, renames or creates anything inside the organisation's documents. The only thing it leaves, if the person allows it, is the file that marks the root folder so it is recognised at a glance.

## Installing and configuring

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-compliance@criterio
/criterio-compliance:compliance-setup
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from GitHub → `josenanez/criterio`.

`compliance-setup` looks at the folder, reviews the obligations matrix, asks what no document answers —the period, the channel deadline, the days to assess a new rule— and shows the first status. If the organisation uses Fidel, Constanza takes the contracts' compliance obligations from his records. The recommended folder structure is in the `legal-intake` skill.

**For whoever does not open a folder**, what Constanza writes —reports, what falls due, signals— is published by Rostrum, the portal for every family: [`criterio-server`](../criterio-server/README.md). Written questions can be left there too, and Constanza takes them in the `*-wake` command.

## Sources

Every framework used is in [`families/criterio-clo/FUENTES.es.md`](../../families/criterio-clo/FUENTES.es.md) (Spanish), with its version, link and status.

## How it is verified

```
python3 scripts/legal.py selftest
python3 tests/criterio-clo/generar.py
python3 tests/criterio-clo/evaluar.py --agente constanza
```

Standard library, nothing to install. **How the latest run went**, generated from the run itself: [`tests/criterio-compliance/RESULTADOS.md`](../../tests/criterio-compliance/RESULTADOS.md) (Spanish). Acceptance criteria in [ACCEPTANCE.md](ACCEPTANCE.md).
