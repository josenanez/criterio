<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cae-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cae-claro.svg" alt="Criterio CAE · Internal audit" height="48"></picture>

# Remedios · finding follow-up

<img src="../../docs/img/en/robot-remedios.gif" alt="Remedios" width="220" align="right">

**Remedios takes each finding to its remedy.**
You are responsible for following up findings. She comes with each action plan next to its date and its evidence: the finding with no plan, owner or date, the overdue plan with no evidence or explanation, the date pushed back again and again, the closure with no evidence or validation, the finding that comes back, the accepted risk that never reached senior management or the board and the external finding missing from the register.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**The name.** Remedios, from the Latin *remedium*, «what heals again»: every finding until its remedy.
<!-- /agente:nombre -->

[Español](README.es.md) · `criterio-remediation` · Apache 2.0 · One instance per entity

**Status: built, in testing, with the CAE family.** The calculation engine, tested against all the family's synthetic material with a key the agent never sees and control entities. The round with the agent comes in 0.2.0, and it has not been tested on a specific organisation's documentation.

**This page stands on its own.** Remedios works without the family's other agents. The family —how they meet each other and Rostrum— is in the [criterio-cae family](../../families/criterio-cae/README.md).

---

## What it is

| | |
|---|---|
| **Who it extends** | Whoever follows up findings and prepares the audit committee's material |
| **What it works on** | **An entity's findings and action-plan register, period by period** |
| **What it looks at** | The findings register, the evidence, the accepted-risk register and the reports of the statutory auditor, the external auditor and the supervisor |
| **Cadence** | When evidence arrives or a plan falls due, and once a week |
| **Instances** | One per entity |

## What it does

**What it does that is not done by hand today: putting everything, not a sample, next to its standard and its evidence.**

**What it can answer:** which plan expired with no evidence, which was pushed back more than allowed, which closure has no evidence or validation, which finding repeats, which accepted risk was not escalated and which external finding is missing from the register.

<!-- cae:comandos · generado por scripts/familias.py; no se edita a mano -->
### The eight commands

> They are typed with the plugin prefix: `/criterio-remediation:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-remediation:remediation-setup` | The configuration, the inventory and the recognised registers |
| `/criterio-remediation:remedios` | Whatever you need, in your own words: Remedios picks the command that does it and runs it |
| `/criterio-remediation:remediation-scan` | The period's record up to date |
| `/criterio-remediation:action-status` | Which plan is overdue and since when |
| `/criterio-remediation:closure-check` | Which closure does not hold and which finding repeats |
| `/criterio-remediation:committee-brief` | The committee material, for the chief audit executive to take |
| `/criterio-remediation:remediation-wake` | Follow-up up to date without anyone remembering |
| `/criterio-remediation:share-findings` | A summary with no data, only on a yes |
<!-- /cae:comandos -->

`remediation-setup` goes first because the others need it, and `remediation-wake` is the one you put on a clock.

<!-- cae:skills · generado por scripts/familias.py; no se edita a mano -->
### The three skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `audit-intake` | The recommended structure of the audit folder, what goes in each folder and which agent uses it, how engagements are named and what to do with what does not fit | Copy of Prudencia's · also in Justo |
| `audit-methodology` | The audit methodology in the configuration: the cycles by risk level, the priority scale with its impact and likelihood, who approves the plan, the program and the papers, and how many reschedules are allowed | Copy of Prudencia's · also in Justo |
| `follow-up-record` | How each piece of implementation evidence, each explanation of delay and each finding in an external report goes into the record, with the citation | Own |
<!-- /cae:skills -->

## What it costs today

<!-- cae:cifras · generado por scripts/familias.py; no se edita a mano -->
<!-- /cae:cifras -->

## What it is for

`/criterio-remediation:action-status` puts each case next to its standard and its evidence. **What is missing is stated with its citation.**

### And what it is not for

- **It does not close a finding or accept a risk.** It says what is missing and where; the opinion is the auditor's.
- **It does not go into the audited systems or the audit tool.** It processes what the organisation hands it.
- **It does not copy the text of the Standards.** The Global Internal Audit Standards are cited by number and title.

And one that needs saying out loud: **your documents are processed on the AI platform's infrastructure**, not only on your computer. A working paper may carry confidential information: confirm that this is acceptable under your policy before pointing it at that folder. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installation and setup

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-remediation@criterio
/criterio-remediation:remediation-setup
```

### The first result

`/criterio-remediation:remediation-setup` does not ask you to tidy anything before starting. It looks at the entity's audit folder, compares it with the [recommended structure](../../families/criterio-cae/README.md#the-recommended-folder-structure), processes the methodology and asks the questions no document answers. Within the first fifteen minutes it shows the first result.

### How often it runs

`/criterio-remediation:remediation-wake` is the command the clock calls: it does what is due, first answers the questions someone left in Rostrum, and **if nothing is due it produces nothing.** Deciding what is due is date arithmetic, and the code does it:

```
python3 scripts/auditoria.py despertar --config <file>
```

## Teamwork

| With whom | What happens |
|---|---|
| **Prudencia** | They share the folder and the methodology; each writes only its own record |
| **Justo** | They share the folder and the methodology; each writes only its own record |
| **Rostrum** | Only if the configuration says so (`publish_rostrum`; off by default, decision 0014): it publishes its reports, what falls due and its signals for whoever does not open a folder, and hands back the questions left by whoever reads it. **It does not write to the state** |

## Tests

[`scripts/auditoria.py`](scripts/auditoria.py), with the standard library, does everything that is calculation: it processes each table with its source row, counts days against the methodology's and the Standards' deadlines and matches each finding with its evidence, the same result every time. It lives in `criterio-audit-plan` and is copied to the other two agents; `scripts/sincronizar.py --check` fails if the copy drifts.

```
python3 scripts/auditoria.py selftest
python3 tests/criterio-cae/generar.py
python3 tests/criterio-cae/evaluar.py
```

What is planted in each entity and **what the material does not test**, in [`EVIDENCIA.md`](../../tests/criterio-cae/EVIDENCIA.md). The design, with each command's input, process and report, in the [family design](../../families/criterio-cae/DISENO.md).
