[Español](DISENO.es.md) · [← The family](README.md)

# criterio-chro · the family design

**Status: stable, launched (version 1.0.0).** The commands, the skills and the calculation engine
are built on the common core; the engine passes its deterministic test and the bias test against the
material in `tests/criterio-chro/`, and both agents passed rounds 1 and 2 on the Colombian bank and its control. Scope in [ADR 0031](../../docs/decisions/0031-la-familia-chro.md).

**This is the family's design sheet**: the signals the code calculates, each command with its input,
process and report, and the decisions taken. What the family does, how it installs, the folder structure
and the roadmap are on its [page](README.md).

The language model (LLM) extracts; the code calculates; the decision —approving a profile, deciding who
moves on in a process— is always a person's. **The role is defined on occupational standards**, not on each
country's law: DANE's CUOC (F-03), adapted from ISCO-08 (F-01), and O*NET (F-02). Each country's data law
comes in through what a profile cannot ask for and what is not processed about a candidate.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json).

## One agent per role

<!-- chro:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Job profiles | **Norma** — from the Latin *norma*, the carpenter's square: every profile on a standard | `criterio-roles` | Every job profile against the occupation in its standard —DANE's CUOC or O*NET—: the skills and knowledge it leaves out, the requirements with no task, what the country's law and the policy do not allow asking for, the level of education against the skill level, the profiles that overlap and the ones past their review |
| Selection | **Cándido** — from the Latin *candidus*, “white”: hence *candidate*, the one who wore the white toga in Rome to seek office. Every claim in the CV against its supporting document | `criterio-talent` | Every CV against its supporting documents and every candidate against the profile, requirement by requirement and with its citation; the authorisation and retention of their data; every vacancy against its deadline, and the search the recruiter runs |
<!-- /chro:agentes -->

## The signals: what the code calculates

<!-- chro:senales · generado por scripts/familias.py; no se edita a mano -->
**Norma · Job profiles**

| Signal | Raised when |
|---|---|
| `profile_without_occupation` | A profile has no occupation code tying it to a standard, or its code is not in the standard |
| `essential_skill_missing` | A skill or knowledge of the occupation in the standard is not in the profile, and the profile does not say why it does not apply |
| `requirement_without_task` | A requirement in the profile is not backed by any of its tasks |
| `requirement_not_allowed` | A requirement asks for sensitive data under the country's law, or for something the selection policy forbids asking for |
| `education_level_inconsistent` | The level of education the profile asks for does not match its occupation's skill level |
| `profiles_overlap` | Two profiles share the occupation and most of their requirements |
| `profile_review_overdue` | A profile is past its review date |

**Cándido · Selection**

| Signal | Raised when |
|---|---|
| `claim_without_support` | The CV claims a degree, certification or job without the document that supports it |
| `certification_expired` | A certification the profile requires expired before the application |
| `employment_dates_differ` | The dates of a job in the CV are not those on its employment certificate |
| `requirement_not_evidenced` | An essential requirement of the profile has no evidence in the CV or its supporting documents |
| `protected_data_received` | Data that must not be processed arrived —photograph, age, ID document, health—, and it is excluded from the analysis |
| `consent_missing` | There is no data-processing authorisation for the candidate, or it postdates receiving their data |
| `retention_exceeded` | A candidate's data is past the policy's retention period and is still in the folder |
| `vacancy_past_target` | A vacancy is still open after the policy's time to fill |
<!-- /chro:senales -->

## Norma's commands, in order of importance

<!-- chro:comandos-norma · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `roles-setup` | The root folder. Questions: entity and its tax ID, country, the period, the occupational standard —CUOC or O*NET— and where its official download is in `00-referencia/`, with O*NET the importance threshold, how the organisation's levels of education map to ISCED, how often a profile is reviewed and what the policy forbids asking for | Inventory of what is there; reads the standard's download and says how many occupations it carries; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the standard and its occupations; the period's first record |
| 1 | `roles-scan` | The profiles in `10-perfiles/` and the period's record | Brings each new or changed profile into the record —its occupation, its tasks, its requirements with the task behind each, its education and its review—, with its citation; recalculates the signals | What went into the record; the profiles not yet in it; the new signals; what could not be processed and why |
| 2 | `profile-build` | The code of a CUOC or O*NET occupation, or the role's name to look it up | The engine brings the occupation from the standard —its description, duties, skills, knowledge and skill level—; the agent proposes the profile with each requirement tied to a task and to an element of the standard, and leaves it as a draft for a person to approve | The profile draft, with the source of each requirement and what the person has to decide |
| 3 | `profile-check` | The period's record and the standard's download in `00-referencia/` | Each profile against its occupation: whether it has a code, which skill or knowledge in the standard it leaves out without saying why, which requirement has no task behind it, whether the level of education matches the skill level (CUOC 2026, section 3.2, F-03) and whether it is past its review | Each profile with its occupation, level, education, what it lacks against the standard and its review; the signals with their citation |
| 4 | `profile-language` | The requirements in the period's record, the country's personal data law and the selection policy | Each requirement against the sensitive data in the country's law —F-10 to F-17, with its article— and against what the organisation's policy forbids asking for, such as age, sex or marital status | Each requirement that asks for something it cannot, with the law or policy that says so |
| 5 | `profile-map` | The period's record and the standard's download | Groups the profiles by occupation; says which share the occupation and most of their requirements, and which occupations related to the organisation's have no profile | The profiles by occupation, the ones that overlap with their share in common and the related occupations with no profile |
| 6 | `roles-wake` | The configuration, the run log and what changed in the folder | Decides whether new profiles or a report with open signals are due; if nothing is due, it stays quiet | What was due and what it did, or one line if nothing was due |
| 7 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /chro:comandos-norma -->

## Cándido's commands, in order of importance

<!-- chro:comandos-candido · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `talent-setup` | The root folder. Questions: entity and its tax ID, country, the period, the time to fill a vacancy and the days data is kept under the selection policy, the vacancy register in `20-vacantes/`, the authorisation register in `40-autorizaciones/` and the ATS export in `50-ats/` with its columns | Inventory of what is there; recognises each table's columns; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the missing columns; the period's first record |
| 1 | `talent-scan` | The folders in `30-candidatos/` and the period's record | Brings each new CV into the record: every degree, certification and job with its supporting document and dates, the evidence for each requirement of the profile and what arrived that must not be processed —only the kind of data and where, never its value—; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `talent-search` | A vacancy in the register in `20-vacantes/`, its profile from Norma, the standard and the internal base in `50-ats/` | Builds the strings for the recruiter's search engine from the occupation's job titles and the essential requirements, and matches the internal base on the same or a related occupation, in identifier order | The search strings and the people in the internal base with the occupation, in no numerical order |
| 3 | `cv-check` | The period's record and the supporting documents in `30-candidatos/` | Every degree, certification and job in the CV against its supporting document: the one without it, the dates of a job that are not those on its certificate and the certification the profile requires that expired before the application | Every claim with no support or that does not match, with its citation; none is called false |
| 4 | `candidate-fit` | The period's record and the vacancy's profile, from Norma | Each requirement in the profile with each candidate's evidence, from the CV or a supporting document, with its citation; an essential requirement with no evidence is a signal. No score and no numerical order: candidates go by their identifier | One table per candidate, requirement by requirement, with its evidence and where it is; the person selecting decides |
| 5 | `privacy-check` | The period's record, the register in `40-autorizaciones/`, the export in `50-ats/` and the policy's retention days | Each candidate against their data-processing authorisation —that it exists and predates receiving their data— and against the policy's retention once their process ended; what arrived and must not be processed is stated and excluded | Each candidate with their authorisation, how long their data is kept and what was excluded |
| 6 | `vacancy-status` | The register in `20-vacantes/` and the policy's time to fill | Each open vacancy against the policy's deadline, or its own if the register has one, counted from its opening | Each vacancy with its profile, opening, deadline, limit and days open; those past their deadline |
| 7 | `talent-wake` | The configuration, the run log and what changed in the folder | Decides whether new CVs, a vacancy falling due or a report with open signals are due; if nothing is due, it stays quiet | What was due and what it did, or one line if nothing was due |
| 8 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /chro:comandos-candido -->

## The bias test

Besides the material with its key, the family carries a test no other needs: **pairs of candidates
identical except for one protected attribute** —the photograph, the date of birth, sex, origin—. The engine
must deliver exactly the same for both members of each pair, except for the notice of what it excluded; any
difference is a defect that blocks the version. In the round, the same test is asked of the agent.

## Third-party figures

<!-- chro:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (ManpowerGroup), C-02 (HireRight), C-03 (SHRM).
<!-- /chro:cifras -->

## Decisions taken

- The names, Norma and Cándido, and the structure: two agents, their fifteen signals and their commands (decision 0031).
- The standards for 0.1.0: CUOC 2026 and O*NET 31.0, from their official download. ESCO comes in once its download and its terms are verified.
- SFIA stays out until the SFIA Foundation confirms whether an open-source tool that cites it needs its partner licence.
