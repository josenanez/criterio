# Cándido · selection

**Cándido puts every claim in the CV next to its supporting document.**
You answer for selection. He comes with every CV against its supporting documents —the degree with no diploma, the job whose dates are not those on its certificate, the expired certification—, every candidate against the profile requirement by requirement and with its citation, the authorisation and retention of their data, and every vacancy against its deadline. No scores and no ranking: the person selecting decides.

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**The name.** Cándido, from the Latin *candidus*, “white”: hence *candidate*, the one who wore the white toga in Rome to seek office. Every claim in the CV against its supporting document.
<!-- /agente:nombre -->

[Español](README.es.md) · `criterio-talent` · Apache 2.0 · One instance per entity

**Status: under construction, with the CHRO family.** The calculation engine, tested against the family's synthetic material with a key the agent never sees, control entities and the bias test with candidate pairs. **There is no round with the agent yet**, and it has not been tested on a specific organisation's documents.

**This page stands on its own.** Cándido works without the family's other agent. The family —how they find each other and Rostrum— is in the [criterio-chro family](../../families/criterio-chro/README.md).

---

## What it is

| | |
|---|---|
| **Who it extends** | Whoever answers for selection —the head of recruitment, the recruiter— and whoever answers for candidates' personal data |
| **What it works on** | **An entity's vacancies and candidates**, period by period |
| **What it looks at** | The vacancy register, the CVs and their supporting documents, the authorisation register and the ATS export |
| **Cadence** | When new CVs arrive, when a vacancy nears its deadline, and once a week |
| **Instances** | One per entity |

## What it does

**What it does that is not done today: check every claim in every CV against its supporting document**, and every candidate against the profile, requirement by requirement, without the name, the photograph or the age entering the analysis.

**What it can answer:** which degree has no diploma, which job does not match its certificate, which required certification expired, which essential requirement has no evidence, which candidate did not authorise the processing of their data, whose data is kept longer than the policy says and which vacancy is past its deadline.

<!-- chro:comandos · generado por scripts/familias.py; no se edita a mano -->
### The ten commands

> They are typed with the plugin prefix: `/criterio-talent:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-talent:talent-setup` | The configuration and the inventory |
| `/criterio-talent:candido` | Whatever you need, in your own words: Cándido picks the command that does it and runs it |
| `/criterio-talent:talent-scan` | The period's record up to date |
| `/criterio-talent:talent-search` | The search the recruiter runs |
| `/criterio-talent:cv-check` | Every claim in the CV against its support |
| `/criterio-talent:candidate-fit` | Each candidate against the profile, requirement by requirement |
| `/criterio-talent:privacy-check` | Each candidate's authorisation and retention |
| `/criterio-talent:vacancy-status` | Each vacancy against its time to fill |
| `/criterio-talent:talent-wake` | What is due today in selection |
| `/criterio-talent:share-findings` | A summary with no data, only on a yes |
<!-- /chro:comandos -->

`talent-setup` comes first because the others need it, and `talent-wake` is the one you put on a clock. Between them, the ones that prepare the work: what changed, the search for a vacancy, CVs against their supporting documents, each candidate against the profile, candidate data and vacancies.

<!-- chro:skills · generado por scripts/familias.py; no se edita a mano -->
### The three skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `cv-record` | How a CV goes into the record: every degree, certification and job with its supporting document and dates, the evidence for each requirement, and what arrived that must not be processed, without copying its value | Own |
| `selection-policy` | The selection policy: the time to fill, how long data is kept, the authorisation register, the vacancy register and the ATS export with its columns | Own |
| `talent-intake` | The recommended structure of the talent folder, what goes in each folder and which agent uses it, how profiles, candidate folders and exports are named, and what is never asked for or processed | Copy of Norma's |
<!-- /chro:skills -->

## What it is for

`/criterio-talent:candidate-fit` puts each requirement of the profile next to each candidate's evidence, in identifier order. **What has no evidence is stated; who moves on in the process is decided by a person.**

### And what it is not for

- **It does not reject, discard, score or rank candidates.** No decision about a person belongs to the agent (decision 0031; Regulation (EU) 2024/1689, Annex III, point 4).
- **It does not use anyone's photograph, age, sex, marital status, origin or health.** If they arrive, they are excluded and it says so.
- **It does not go into LinkedIn or any network, buy databases or run background checks.** It prepares the search for the recruiter to run.
- **It does not infer personality, “culture” or potential**, or penalise a gap between two jobs.

And one that has to be said out loud: **your documents are processed on the AI platform's infrastructure**, not only on your computer. A CV carries personal data: confirm this is acceptable under your data policy before pointing it at that folder. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md), terms in [TERMS.md](../../TERMS.md).

## Installation and configuration

**It is in the marketplace**, under construction:

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-talent@criterio
/criterio-talent:talent-setup
```

### The first result

`/criterio-talent:talent-setup` does not ask you to tidy anything first. It looks at the entity's talent folder, compares it with the [recommended structure](../../families/criterio-chro/README.md#the-recommended-folder-structure), recognises the registers' columns and asks what no document answers: the time to fill a vacancy and how long a candidate's data is kept, from the selection policy. Within the first fifteen minutes you see the first result: each vacancy against its deadline.

### How often it runs

`/criterio-talent:talent-wake` is the command the clock invokes: it does what is due, first answers the questions someone left in Rostrum, and **if nothing is due it produces nothing.** Deciding what is due is date arithmetic, and the code decides it:

```
python3 scripts/talento.py despertar --config <file>
```

## Teamwork

| With whom | What happens |
|---|---|
| **Norma** | They share the folder and the reference. Cándido takes from Norma's records the profiles he checks each candidate against |
| **Rostrum** | Publishes the status of the vacancies. **Candidates do not appear there** unless the configuration says so, and then only by their identifier |

## Tests

[`scripts/talento.py`](scripts/talento.py), with the standard library, does everything that is calculation: it processes the standard's download and every table with its source row, counts days against the policy's deadlines, checks each requirement and each claim against its evidence and leaves out what is not processed, with the same result every time. It lives in `criterio-roles` and is copied to `criterio-talent`; `scripts/sincronizar.py --check` fails if the copy drifts.

```
python3 scripts/talento.py selftest                          the engine and the bias test
python3 tests/criterio-chro/generar.py                       the material
python3 tests/criterio-chro/evaluar.py --agente candido       each signal against the key
```

What is planted in each entity and **what the material does not test**, in [`EVIDENCIA.md`](../../tests/criterio-chro/EVIDENCIA.md). The design, with each command's input, process and report, in the [family design](../../families/criterio-chro/DISENO.md).
