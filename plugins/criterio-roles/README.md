# Norma · job profiles

**Norma puts every job profile on a standard.**
You answer for job profiles and the duties manual. She comes with every profile next to the occupation in its standard —DANE's CUOC or O*NET—: the skills and knowledge it leaves out, the requirements no task supports, what it asks for that the law does not allow, the level of education that does not match the occupation and the profiles that overlap.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**The name.** Norma, from the Latin *norma*, the carpenter's square: every profile on a standard.
<!-- /agente:nombre -->

[Español](README.es.md) · `criterio-roles` · Apache 2.0 · One instance per entity

**Status: under construction, with the CHRO family.** The calculation engine, tested against the family's synthetic material with a key the agent never sees, control entities and the bias test with candidate pairs. **There is no round with the agent yet**, and it has not been tested on a specific organisation's documents.

**This page stands on its own.** Norma works without the family's other agent. The family —how they find each other and Rostrum— is in the [criterio-chro family](../../families/criterio-chro/README.md).

---

## What it is

| | |
|---|---|
| **Who it extends** | Whoever answers for people management —the CHRO, the head of compensation or organisational development— and whoever designs or updates job profiles |
| **What it works on** | **An entity's job profiles**, period by period |
| **What it looks at** | The job profiles, the duties manual and the official download of the occupational standard |
| **Cadence** | When a new or changed profile arrives, when a review falls due, and once a week |
| **Instances** | One per entity |

## What it does

**What it does that is not done today: put every profile, not a sample, next to the occupation in its standard**, with each requirement tied to a task.

**What it can answer:** which profile has no occupation, which skill of its occupation it leaves out, which requirement no task supports, which profile asks for age, marital status or sensitive data, which profile asks for a degree its occupation does not require and which profiles are the same one under another name.

<!-- chro:comandos · generado por scripts/familias.py; no se edita a mano -->
### The nine commands

> They are typed with the plugin prefix: `/criterio-roles:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-roles:roles-setup` | The configuration, the inventory and the recognised standard |
| `/criterio-roles:norma` | Whatever you need, in your own words: Norma picks the command that does it and runs it |
| `/criterio-roles:roles-scan` | The period's record up to date |
| `/criterio-roles:profile-build` | A profile draft on a standard |
| `/criterio-roles:profile-check` | Each profile against its standard |
| `/criterio-roles:profile-language` | The requirements that ask for what cannot be asked |
| `/criterio-roles:profile-map` | The map of the organisation's profiles |
| `/criterio-roles:roles-wake` | What is due today in the profiles |
| `/criterio-roles:share-findings` | A summary with no data, only on a yes |
<!-- /chro:comandos -->

`roles-setup` comes first because the others need it, and `roles-wake` is the one you put on a clock. Between them, the ones that prepare the work: what changed, a new profile from its occupation, profiles against their occupation, what cannot be asked for and the map.

<!-- chro:skills · generado por scripts/familias.py; no se edita a mano -->
### The three skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `occupation-standard` | The occupational standard: the official CUOC or O*NET download, each occupation's code, the O*NET importance threshold, the skill level and how the organisation's education maps to ISCED | Own |
| `profile-record` | How a job profile goes into the record: its occupation, its tasks, each requirement with the task and standard element behind it, its education, what does not apply with its reason, and its review | Own |
| `talent-intake` | The recommended structure of the talent folder, what goes in each folder and which agent uses it, how profiles, candidate folders and exports are named, and what is never asked for or processed | Own · also in Cándido |
<!-- /chro:skills -->

## What it costs today

<!-- chro:cifras · generado por scripts/familias.py; no se edita a mano -->
| Figure | Source |
|---|---|
| **72%** of employers say they struggle to fill their roles, down from 74% the year before | [ManpowerGroup, 2026 Global Talent Shortage Survey, comunicado del 26 de febrero de 2026, 2026](https://investor.manpowergroup.com/node/68796) — 39,063 employers in 41 countries, among them Argentina, Brazil, Chile, Colombia, Costa Rica, Guatemala, Mexico, Panama and Peru; fieldwork from 1 to 31 October 2025 |
| **Over 3 in 4** hiring professionals found discrepancies in what their candidates declared in the past twelve months | [HireRight, 2025 Global Benchmark Report, comunicado en Business Wire, 2025](https://www.businesswire.com/news/home/20250915364914/en) — Over 1,000 HR, risk and talent acquisition professionals worldwide; the report was released in June 2025 |
| **39 days** is the median time to fill a non-executive vacancy | [SHRM, 2026 Recruiting Executives Benchmarking, 2026](https://www.shrm.org/topics-tools/research/2025-recruiting-benchmarking) — Data from over 4,600 organisations; the page does not state the country or the collection dates |
<!-- /chro:cifras -->

## What it is for

`/criterio-roles:profile-check` puts every profile next to its occupation in the standard's download. **What it lacks, the requirement with no task and the mismatched level of education are stated with their citation.**

### And what it is not for

- **It does not approve a profile.** It says what is missing against its standard; the decision is a person's.
- **It does not set a salary, a position or a structure.**
- **It does not assess a person.** That belongs to selection, and there the agent does not decide either.
- **It does not copy the text of a paid standard.** ISO standards are cited by their number.

And one that has to be said out loud: **your documents are processed on the AI platform's infrastructure**, not only on your computer. A CV carries personal data: confirm this is acceptable under your data policy before pointing it at that folder. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installation and configuration

**It is in the marketplace**, under construction:

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-roles@criterio
/criterio-roles:roles-setup
```

### The first result

`/criterio-roles:roles-setup` does not ask you to tidy anything first. It looks at the entity's talent folder, compares it with the [recommended structure](../../families/criterio-chro/README.md#the-recommended-folder-structure), recognises the standard's download and asks what no document answers: which standard, from what importance a skill is required in O*NET and which ISCED level matches each way of naming education. Within the first fifteen minutes you see the first result: each profile against its occupation.

### How often it runs

`/criterio-roles:roles-wake` is the command the clock invokes: it does what is due, first answers the questions someone left in Rostrum, and **if nothing is due it produces nothing.** Deciding what is due is date arithmetic, and the code decides it:

```
python3 scripts/talento.py despertar --config <file>
```

## Teamwork

| With whom | What happens |
|---|---|
| **Cándido** | They share the folder and the reference. Cándido checks each candidate against the profiles Norma processed |
| **Rostrum** | Publishes her reports, what falls due and her signals for whoever does not open a folder, and hands back the questions people leave. **It does not write to the state** |

## Tests

[`scripts/talento.py`](scripts/talento.py), with the standard library, does everything that is calculation: it processes the standard's download and every table with its source row, counts days against the policy's deadlines, checks each requirement and each claim against its evidence and leaves out what is not processed, with the same result every time. It lives in `criterio-roles` and is copied to `criterio-talent`; `scripts/sincronizar.py --check` fails if the copy drifts.

```
python3 scripts/talento.py selftest                          the engine and the bias test
python3 tests/criterio-chro/generar.py                       the material
python3 tests/criterio-chro/evaluar.py --agente norma       each signal against the key
```

What is planted in each entity and **what the material does not test**, in [`EVIDENCIA.md`](../../tests/criterio-chro/EVIDENCIA.md). The design, with each command's input, process and report, in the [family design](../../families/criterio-chro/DISENO.md).
