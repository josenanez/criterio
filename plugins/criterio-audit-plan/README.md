<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cae-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cae-claro.svg" alt="Criterio CAE · Internal audit" height="48"></picture>

# Prudencia · the audit plan

<img src="../../docs/img/en/robot-prudencia.gif" alt="Prudencia" width="220" align="right">

**Prudencia puts the audit plan next to the risks.**
You are responsible for the internal audit plan. She comes with the plan next to the risk matrix and the audit universe: the high risk no engagement covers, the unit past its cycle, the risk assessment that is over a year old, the area the plan does not consider, the change with no minutes, the late engagement, the hours that do not add up, the missing topical requirement and the overdue external quality assessment.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**The name.** Prudencia, from the Latin *prudentia*, a contraction of *providentia*, «seeing ahead»: the plan that looks at risk before it happens.
<!-- /agente:nombre -->

[Español](README.es.md) · `criterio-audit-plan` · Apache 2.0 · One instance per entity

**Status: built and tested, in the lab, with the CAE family.** The calculation engine, tested against all the family's synthetic material with a key the agent never sees and control entities. In 0.2.0, the agent ran on every entity in the material, with a key it never sees; it has not been tested on a specific organisation's documentation.

**This page stands on its own.** Prudencia works without the family's other agents. The family —how they meet each other and Rostrum— is in the [criterio-cae family](../../families/criterio-cae/README.md).

---

## What it is

| | |
|---|---|
| **Who it extends** | Whoever leads internal audit —the CAE or chief auditor— and whoever builds and follows the plan |
| **What it works on** | **An entity's audit plan, period by period** |
| **What it looks at** | The audit universe, the risk matrix, the annual plan, the committee minutes and the team with its hours |
| **Cadence** | When minutes arrive or the plan changes, and once a week |
| **Instances** | One per entity |

## What it does

**What it does that is not done by hand today: putting everything, not a sample, next to its standard and its evidence.**

**What it can answer:** which high risk has no engagement, which unit has gone longer than its cycle allows without an audit, whether the plan considers IT governance, fraud and compliance, which added or cancelled engagement has no minutes, which engagement is late, whether the hours add up and when the external assessment is due.

<!-- cae:comandos · generado por scripts/familias.py; no se edita a mano -->
### The nine commands

> They are typed with the plugin prefix: `/criterio-audit-plan:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-audit-plan:plan-setup` | The configuration, the inventory and the recognised tables |
| `/criterio-audit-plan:prudencia` | Whatever you need, in your own words: Prudencia picks the command that does it and runs it |
| `/criterio-audit-plan:plan-scan` | The period's record up to date |
| `/criterio-audit-plan:plan-coverage` | Which risk and which unit are left uncovered, with their citation |
| `/criterio-audit-plan:plan-status` | The plan's status for the committee |
| `/criterio-audit-plan:plan-capacity` | Whether the hours add up, with the arithmetic |
| `/criterio-audit-plan:quality-status` | When the next one is due |
| `/criterio-audit-plan:plan-wake` | The plan up to date without anyone remembering |
| `/criterio-audit-plan:share-findings` | A summary with no data, only on a yes |
<!-- /cae:comandos -->

`plan-setup` goes first because the others need it, and `plan-wake` is the one you put on a clock.

<!-- cae:skills · generado por scripts/familias.py; no se edita a mano -->
### The three skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `audit-intake` | The recommended structure of the audit folder, what goes in each folder and which agent uses it, how engagements are named and what to do with what does not fit | Own · also in Justo and Remedios |
| `audit-methodology` | The audit methodology in the configuration: the cycles by risk level, the priority scale with its impact and likelihood, who approves the plan, the program and the papers, and how many reschedules are allowed | Own · also in Justo and Remedios |
| `plan-record` | How each committee minute goes into the record: which engagement it adds, cancels or postpones, who approved it and the citation | Own |
<!-- /cae:skills -->

## What it costs today

<!-- cae:cifras · generado por scripts/familias.py; no se edita a mano -->
| Figure | Source |
|---|---|
| **5%** of revenue is what organisations lose to fraud each year, according to fraud examiners' estimate | [ACFE, Occupational Fraud 2026: A Report to the Nations, 2026](https://acfe.com/RTTN) — 2,402 cases from 143 countries and territories, investigated between January 2024 and September 2025 |
| **43%** of frauds are detected by a tip, nearly three times more than the next method | [ACFE, Occupational Fraud 2026: A Report to the Nations, 2026](https://acfe.com/RTTN) — 2,402 cases from 143 countries and territories, investigated between January 2024 and September 2025 |
| **12 months** is how long a fraud lasts, at the median, before it is detected | [ACFE, Occupational Fraud 2026: A Report to the Nations, 2026](https://acfe.com/RTTN) — 2,402 cases from 143 countries and territories, investigated between January 2024 and September 2025 |
<!-- /cae:cifras -->

## What it is for

`/criterio-audit-plan:plan-coverage` puts each case next to its standard and its evidence. **What is missing is stated with its citation.**

### And what it is not for

- **It does not approve the plan or decide what is audited.** It says what is missing and where; the opinion is the auditor's.
- **It does not go into the audited systems or the audit tool.** It processes what the organisation hands it.
- **It does not copy the text of the Standards.** The Global Internal Audit Standards are cited by number and title.

And one that needs saying out loud: **your documents are processed on the AI platform's infrastructure**, not only on your computer. A working paper may carry confidential information: confirm that this is acceptable under your policy before pointing it at that folder. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installation and setup

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-audit-plan@criterio
/criterio-audit-plan:plan-setup
```

### The first result

`/criterio-audit-plan:plan-setup` does not ask you to tidy anything before starting. It looks at the entity's audit folder, compares it with the [recommended structure](../../families/criterio-cae/README.md#the-recommended-folder-structure), processes the methodology and asks the questions no document answers. Within the first fifteen minutes it shows the first result.

### How often it runs

`/criterio-audit-plan:plan-wake` is the command the clock calls: it does what is due, first answers the questions someone left in Rostrum, and **if nothing is due it produces nothing.** Deciding what is due is date arithmetic, and the code does it:

```
python3 scripts/auditoria.py despertar --config <file>
```

## Teamwork

| With whom | What happens |
|---|---|
| **Justo** | They share the folder and the methodology; each writes only its own record |
| **Remedios** | They share the folder and the methodology; each writes only its own record |
| **Rostrum** | Only if the configuration says so (`publish_rostrum`; off by default, decision 0014): it publishes its reports, what falls due and its signals for whoever does not open a folder, and hands back the questions left by whoever reads it. **It does not write to the state** |

## Tests

[`scripts/auditoria.py`](scripts/auditoria.py), with the standard library, does everything that is calculation: it processes each table with its source row, counts days against the methodology's and the Standards' deadlines and matches each finding with its evidence, the same result every time. It lives in `criterio-audit-plan` and is copied to the other two agents; `scripts/sincronizar.py --check` fails if the copy drifts.

```
python3 scripts/auditoria.py selftest
python3 tests/criterio-cae/generar.py
python3 tests/criterio-cae/evaluar.py
```

What is planted in each entity and **what the material does not test**, in [`EVIDENCIA.md`](../../tests/criterio-cae/EVIDENCIA.md). The design, with each command's input, process and report, in the [family design](../../families/criterio-cae/DISENO.md).
