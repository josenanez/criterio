<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cmo-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cmo-claro.svg" alt="Criterio CMO · Marketing" height="48"></picture>

# Próspero · what is invested

<img src="../../docs/img/en/robot-prospero.gif" alt="Próspero" width="220" align="right">

**Próspero puts each unit of media spend next to what it produced.**
You are responsible for the investment in campaigns. He comes with each campaign next to its budget, its invoice and its result: the campaign over budget, the media invoice with no campaign or order, the campaign with no goal or indicator, the one that ran past its end date and the report result that does not match the platform.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**The name.** Próspero, from the Latin *prosperus*, the one who makes something yield: each unit of media spend against what it produced.
<!-- /agente:nombre -->

[Español](README.es.md) · `criterio-campaigns` · Apache 2.0 · One instance per entity

**Status: built and tested, in the lab, with the CMO family.** The calculation engine, tested against all the family’s synthetic material with a key the agent never sees and control entities. In 0.2.0, the agent ran on every entity in the material, with a key it never sees; it has not been tested on a specific organisation’s documentation.

**This page stands on its own.** Próspero works without the family’s other agent. The family —how they meet each other and Rostrum— is in the [criterio-cmo family](../../families/criterio-cmo/README.md).

---

## What it is

| | |
|---|---|
| **Who it extends** | Whoever answers for marketing investment —the CMO or the media manager— and whoever builds the results report |
| **What it works on** | **An entity's marketing plan, media spend and results, period by period** |
| **What it looks at** | The marketing plan with each campaign's budget and goal, the media invoices, the platform export and the results report |
| **Cadence** | When an invoice, an export or a report arrives, and once a week |
| **Instances** | One per entity |

## What it does

**What it does that is not done by hand today: putting everything, not a sample, next to its source.**

**What it can answer:** which campaign went over budget, which media invoice has no campaign or order, which campaign has no goal or indicator, which ran past its end and which report result does not match the platform.

<!-- cmo:comandos · generado por scripts/familias.py; no se edita a mano -->
### The eight commands

> They are typed with the plugin prefix: `/criterio-campaigns:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-campaigns:campaigns-setup` | The configuration, the inventory and the recognised tables |
| `/criterio-campaigns:prospero` | Whatever you need, in your own words: Próspero picks the command that does it and runs it |
| `/criterio-campaigns:campaigns-scan` | The period's record up to date |
| `/criterio-campaigns:budget-check` | Which campaign overspent, overran or measures nothing |
| `/criterio-campaigns:invoice-check` | Which media was invoiced with no campaign or order |
| `/criterio-campaigns:result-check` | Which report result does not hold up against the platform |
| `/criterio-campaigns:campaigns-wake` | The campaigns up to date without anyone having to remember |
| `/criterio-campaigns:share-findings` | A summary with no data, only if the answer is yes |
<!-- /cmo:comandos -->

`campaigns-setup` goes first because the others need it, and `campaigns-wake` is the one you put on a clock.

<!-- cmo:skills · generado por scripts/familias.py; no se edita a mano -->
### The three skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `marketing-intake` | The recommended structure of the marketing folder, what goes in each folder and which agent uses it | Copy of Lucía's |
| `marketing-policy` | The advertising policy in the configuration: the tolerances, who approves and what is never decided | Copy of Lucía's |
| `result-record` | How each result in the marketing report goes into the record: its campaign, indicator, value and cut-off, with its citation | Own |
<!-- /cmo:skills -->

## What it costs today

<!-- cmo:cifras · generado por scripts/familias.py; no se edita a mano -->
<!-- /cmo:cifras -->

## What it is for

`/criterio-campaigns:budget-check` puts each case next to its source. **What is missing is said with its citation.**

### And what it is not for

- **It does not approve a budget or judge a campaign.** It says what overspent and what does not hold up; the decision is the marketing office's.
- **It does not decide which figure is right.** It says which one does not match the platform; whoever signs the report decides.
- **It does not connect to an ad or analytics platform.** It processes their exports.

And one that has to be said out loud: **your documents are processed on the AI platform’s infrastructure**, not only on your computer. A marketing plan or media invoices may contain confidential information: confirm it is admissible under your policy before pointing it at that folder. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installation and setup

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-campaigns@criterio
/criterio-campaigns:campaigns-setup
```

### The first result

`/criterio-campaigns:campaigns-setup` does not ask you to tidy anything before starting. It looks at the entity’s marketing folder, compares it with the [recommended structure](../../families/criterio-cmo/README.md#the-recommended-folder-structure), processes the advertising policy and asks the questions no document answers. Within the first fifteen minutes it shows the first result.

### How often it runs

`/criterio-campaigns:campaigns-wake` is the command the clock calls: it does what is due, first answers the questions someone left in Rostrum, and **if nothing is due it produces nothing.** Deciding what is due is date arithmetic, and the code does it:

```
python3 scripts/mercadeo.py despertar --config <file>
```

## Teamwork

| With whom | What happens |
|---|---|
| **Lucía** | They share the folder and the advertising policy; each writes only its own record |
| **Rostrum** | Only if the configuration says so (`publish_rostrum`): it publishes its reports, what is due and its signals for whoever does not open a folder, and returns the questions left by whoever views it. **It does not write to the state** |

## Tests

[`scripts/mercadeo.py`](scripts/mercadeo.py), with the standard library, does everything that is calculation: it processes each table with its source row, adds each campaign's invoiced media against its budget and tolerance, and compares each invoice with the end date and each result with the platform at the same cut-off, the same result every time. It lives in `criterio-claims` and is copied to Próspero; `scripts/sincronizar.py --check` fails if the copy drifts.

```
python3 scripts/mercadeo.py selftest
python3 tests/criterio-cmo/generar.py
python3 tests/criterio-cmo/evaluar.py
```

What is planted in each entity and **what the material does not test**, in [`EVIDENCIA.md`](../../tests/criterio-cmo/EVIDENCIA.md). The design, with the input, process and report of each command, in the [family design](../../families/criterio-cmo/DISENO.md).
