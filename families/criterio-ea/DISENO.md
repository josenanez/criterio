[Español](DISENO.es.md)

# criterio-ea · the family design

**Status: in design.** Neither the engine nor the plugin exists yet; this sheet is what gets built.
Scope and rules in [ADR 0012](../../docs/decisions/0012-scope-asistente-ejecutivo.md).

**This is the family's design sheet**: the documents it processes, the signals the code calculates,
each command with its input, process and report, and the decisions taken. The family page is written
once the plugin exists.

One agent that extends the capacity of the executive office: she processes the executive's calendar,
the meetings of the governing bodies and the correspondence, and checks them against the executive's
commitments to flag what overlaps, which meeting has no materials or minutes, which agreement has no
owner and which email is waiting for a reply. The language model (LLM) extracts; the code calculates;
the decision is always taken by a person.

First version: the countries in the engine's registry. **She prepares; she does not recommend or
decide.** For each item that calls for a decision she builds its record —the options the documents
bring, the evidence for each, what is still unknown and the dates that set the deadline— and does not
rank them. The four reasons are in the ADR.

**How she works.** Automated: she processes the documents, calculates the signals and prepares each
deliverable without intervention. Semi-automated when a piece of data is in no document —who sits on
a governing body, the thresholds—: then she asks the person, says what she asked and carries on with
the answer.

**Sources.** Every source used to process —the role, the formats, third-party figures— is in
[`FUENTES.es.md`](FUENTES.es.md) with its version, link, consultation date and status.

**Where this document comes from.** The tables of the agent, signals, commands and figures are not
written here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and
[`fuentes.json`](fuentes.json), which `scripts/familias.py` writes into this design and into
`FUENTES.es.md`.

## One agent

<!-- ea:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Executive assistant | **Ofelia** — from the Greek *ōphéleia*, «help»: she is the one who prepares | `criterio-assistant` | The executive's day to day: the calendar against their commitments, the preparation of each governing-body meeting with the record of each decision, the draft minutes, the follow-up of commitments and the correspondence that needs a reply |
<!-- /ea:agentes -->

She is for whoever assists the executive: that person still owns the calendar and what gets sent.
The boundary with the chief of staff is O*NET's (F-01): initiatives, coordinating the leadership team
and decisions on processes and resources belong to the other role.

## The documents she processes

| Document | Where | Who processes it |
|---|---|---|
| The exported calendar, in .ics (F-02) | `10-agenda/` | The code: events, recurrences and time zones, with its self-test |
| Emails saved as files (F-03) | `20-correspondencia/` | The code processes the headers; the LLM extracts what is asked and by when |
| The notice of meeting and the agenda | `organos/<órgano>/<fecha>/10-convocatoria/` | The LLM, citing each item |
| The meeting materials | `20-material/` | The code counts what is there; nothing is summarised |
| The notes or transcript | `30-notas/` | The LLM extracts agreements and commitments, each with its citation |
| The signed minutes | `40-acta/` | The LLM extracts agreements and commitments; the code calculates their dates |

Ofelia processes exports, not accounts: she does not connect to the mailbox or the calendar. A direct
connection is a separate decision, with its own privacy review.

## The signals: what the code calculates

<!-- ea:senales · generado por scripts/familias.py; no se edita a mano -->
**Ofelia · Executive assistant**

| Signal | Raised when |
|---|---|
| `meeting_conflict` | Two of the executive's meetings overlap in the exported calendar |
| `meeting_without_material` | Within the configured days before a governing-body meeting, its materials are not in the folder |
| `meeting_without_minutes` | The configured days after a meeting have passed and its signed minutes are not there |
| `agreement_without_owner` | An agreement in the minutes has no owner |
| `agreement_without_date` | An agreement in the minutes has no date |
| `commitment_overdue` | A commitment is overdue and no document supports it as done |
| `commitment_rescheduled` | A commitment was moved more times than configured |
| `correspondence_unanswered` | A saved email asks for a reply and its deadline passed with no saved reply |
| `decision_deadline` | A pending decision has a date that sets it within the configured days |
<!-- /ea:senales -->

The days, the counts and the maximum age of the calendar are each office's configuration, with a
declared default. She stays silent when nothing crosses a threshold.

## The three classes, as in the PMO family

**A · What she does, and today takes someone's time:** checking the calendar against the meetings,
building the agenda with what is open, chasing the materials, drafting the minutes, keeping the list
of commitments, sorting the correspondence.

**B · What she does, and today is not done:** checking every agreement in every set of minutes against
its owner and date; counting how many times each commitment moved; preparing the record of each
decision with the evidence for each option cited.

**C · What she does not do:** she does not send, schedule, accept or move anything; she does not
recommend an option or prioritise for the executive; she does not declare a commitment done without
evidence; she does not edit original minutes, calendars or emails; she does not evaluate a person or
a team.

## Ofelia's commands, in order of importance

<!-- ea:comandos-ofelia · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `ea-setup` | The root folder. Questions: the executive and who assists them, the governing bodies in `00-referencia`, the excluded folders, the thresholds —days before a meeting for the materials, days for the minutes, date changes that count, maximum age of the calendar—, whether it publishes to Rostrum and the terms | Inventory of what is there; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the excluded folders; the governing bodies with the meetings found |
| 1 | `ea-scan` | The calendar in `10-agenda`, each meeting in `organos/` and the correspondence in `20-correspondencia` (F-02, F-03) | The code normalises the calendar —recurrences and time zones— and the emails; the language model (LLM) extracts from minutes, notes and emails the agreements, the commitments and what is being asked, each with its citation | The new records and those that changed; what could not be processed and why |
| 2 | `ea-agenda` | The calendar record and the meeting records | Checks the executive's week against their meetings and commitments; if the export is older than the threshold, it says so and computes no conflicts | The conflicts, the meetings without materials and those without minutes, with the export date |
| 3 | `ea-prep` | The governing body and the date of the next meeting; the record of the previous one | Builds the agenda with what was left open, lists the materials missing from `20-material` and prepares the record of each decision: the options the documents bring, the evidence for each with its citation, what is still unknown and the dates that set the deadline | The meeting pack. It does not rank the options or say which one is best |
| 4 | `ea-minutes` | The notes or the transcript in `30-notas` | The language model (LLM) extracts each agreement and commitment with its citation; the code flags those with no owner or no date | The draft in `90-borradores`, with «BORRADOR» in the name and in the text, and the list of what is missing to close it |
| 5 | `ea-commitments` | The meeting records; the project records, if Samuel has them | Using the commitment rules of the shared core, computes which are overdue without evidence, which have no date and which moved more than the threshold; project commitments are cited from Samuel's record, not recomputed | The status of the executive commitments, by governing body and by owner |
| 6 | `ea-mail` | The correspondence records | Computes what needs a reply and its deadline; for routine items, the language model (LLM) writes a draft reply | What needs a reply and by when; the drafts in `90-borradores`. It never sends |
| 7 | `ea-weekly` | The configuration and the records | Gathers what arrived, what is due and what still needs preparing | A single summary a week; not published to Rostrum unless the configuration says so |
| 8 | `ea-wake` | The configuration and the records | Decides what is due: the meetings entering the window, pending minutes, correspondence deadlines and a weekly review | What ran and what it found; if nothing is due, it stays silent |
<!-- /ea:comandos-ofelia -->

## Rules for real operation

They are those of ADR 0012, and each one has to be checkable in the test:

- She writes only in `estado-direccion/`, in `.criterio/direccion/` and in `90-borradores/`, plus the
  file that marks her root folder (ADR 0011).
- Every draft carries «BORRADOR» in its name and text; she never files it in `40-acta/`.
- Her report is not published to Rostrum by default.
- She processes only the folders she is given and honours the exclusion list, which she states in
  every report.
- Each commitment belongs to the minutes where it was born; project commitments are Samuel's and are
  cited from his record.
- If the calendar is older than the threshold, she says so and computes no conflicts.
- An ambiguous event is declared, not guessed.

## What is reused

- Samuel's commitment rules —overdue without evidence, undated, rescheduled—, which move from
  `portafolio.py` to the shared core (`nucleo.py`). Samuel's tests must give exactly the same before
  and after.
- `nucleo.py` —tables, dates, inventory, signals, report and the country registry—, and `texto.py`,
  `terminos.py`, `rastro.py` and `raiz.py`, copied by `scripts/sincronizar.py`.
- The `commitment-tracking` skill.
- Rostrum, for whoever decides to publish.

What is new is processing the .ics and the saved email, with the standard library and its self-test.

## How it is tested

Synthetic material by industry and one control office per country, with a key the engine does not
see, in `tests/criterio-ea/`. Every signal is seeded at least once, plus the rule cases: a stale
calendar, a recurring event that crosses a daylight-saving change, a draft placed in `40-acta/`. It
uses the same harness, `tests/ronda_familia.py`: first the engine against the key, then the round with
the agent. The family is declared tested after a complete round.

## Third-party figures

<!-- ea:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Microsoft), C-02 (Microsoft), C-03 (Microsoft). To be verified, and out of any publication until they are: C-04.
<!-- /ea:cifras -->

## Closed decisions

- The role, from O*NET 43-6011, and the name, Ofelia. José, 2026-10-23.
- The family acronym, EA. José, 2026-10-23.
- She prepares; she does not recommend or decide. José, 2026-10-23.
- The board secretariat is a mode of Ofelia, not a separate agent. José, 2026-10-23.
- The plugin, `criterio-assistant`, with the `ea-*` commands. José, 2026-10-23.
- The numbered folder structure —`10-agenda/`, `20-correspondencia/`, `90-borradores/` and
  `organos/<órgano>/<fecha>/`—, which adapts the ADR's to the ADR 0007 convention. José, 2026-10-23.

## Open decisions

None for building the first increment. Travel and the direct connection to the calendar or the
mailbox are left for the second (ADR 0012).
