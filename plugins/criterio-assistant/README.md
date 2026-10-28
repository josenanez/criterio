<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-ea-oscuro.svg"><img src="../../docs/img/marca/en/criterio-ea-claro.svg" alt="Criterio EA · Executive office" height="48"></picture>

# Ofelia · the executive assistant

**Ofelia prepares the work of the executive's office.** You assist the president or the general
manager. She arrives with the week's calendar against its meetings and commitments, the pack for each
governing body's next meeting with the record of each decision, the draft minutes from the notes, the
status of the board's commitments and the correspondence that needs a reply. **She prepares; she does
not recommend or decide, and she never sends anything.**

<!-- agente:nombre · generado por scripts/familias.py; no se edita a mano -->
**The name.** Ofelia, from the Greek *ōphéleia*, «help»: she is the one who prepares.
<!-- /agente:nombre -->

[Español](README.es.md) · `criterio-assistant` · Apache 2.0 · One instance per executive

**Status:** built, with the engine tested against the test material of four offices —a president's
office and a general manager's office with seeded defects, and two control offices— and with the full
round with the agent on all four, in [the family's rounds](../../tests/evidencias/familias/ea/RONDAS.md).
Nothing has run yet on a specific executive's office. What remains before calling it done, in the
[acceptance criteria](ACCEPTANCE.md).

---

## What it is

The executive assistant as O*NET defines it (43-6011): the executive's calendar, the agenda and
logistics of boards and committees, the minutes, the correspondence and the information the executive
needs. The line with the chief of staff is the one practice draws: initiatives, coordinating the
leadership team and decisions about processes and resources belong to the other role
([ADR 0012](../../docs/decisions/0012-scope-asistente-ejecutivo.md)). Board secretary is a mode of
Ofelia, not a separate agent.

## What it does

<!-- ea:comandos · generado por scripts/familias.py; no se edita a mano -->
### The nine commands

> They are typed with the plugin prefix: `/criterio-assistant:` and autocomplete does the rest. It is the only form that resolves in a Claude Code session.

| Command | What it does |
|---|---|
| `/criterio-assistant:ea-setup` | The configuration, the inventory and the governing bodies with their meetings |
| `/criterio-assistant:ea-scan` | The records of the meetings, the correspondence and the calendar |
| `/criterio-assistant:ea-agenda` | The executive's week: conflicts, meetings without materials and meetings without minutes |
| `/criterio-assistant:ea-prep` | The meeting pack, with the record of each decision |
| `/criterio-assistant:ea-minutes` | The draft minutes, with each agreement and commitment cited |
| `/criterio-assistant:ea-commitments` | The status of the executive commitments, by governing body and by owner |
| `/criterio-assistant:ea-mail` | The correspondence that needs a reply, with its drafts |
| `/criterio-assistant:ea-weekly` | The weekly summary: what arrived, what is due and what still needs preparing |
| `/criterio-assistant:ea-wake` | What the office needs today; silent when nothing does |
<!-- /ea:comandos -->

<!-- ea:skills · generado por scripts/familias.py; no se edita a mano -->
### The six skills

They load on their own when the subject comes up. They are the knowledge the commands share, and they are consulted like a manual.

| Skill | What it encapsulates | Whose it is |
|---|---|---|
| `commitment-tracking` | The commitment overdue without evidence, the one nobody dated and the one moved again and again: Samuel's rules | Own |
| `correspondence-record` | An email record: whether it asks for a reply, what it asks and by when; and the draft of routine replies, never sent | Own |
| `decision-brief` | A decision brief: the options the documents carry with their evidence, what is still unknown and the deadline, without ranking or recommending | Own |
| `ea-intake` | Which documents Ofelia processes, where each one goes, what the code processes directly —the .ics calendar and email headers— and what the agent extracts to the record | Own |
| `meeting-record` | A meeting record: agenda, agreements with owner and date, commitments with their history and pending decisions, each item with its citation | Own |
| `minutes-draft` | Draft minutes from notes or a transcript, each agreement cited and «BORRADOR» in the name and text | Own |
<!-- /ea:skills -->

## What it is for

So that the executive reaches each meeting with what is open, the material and the decisions prepared,
and so that no agreement is left without an owner or a date and no commitment falls due without anyone
seeing it. What it processes:

| Document | Where |
|---|---|
| The calendar export in .ics, with the export date in the name | `10-agenda/` |
| Emails saved as files, one per message | `20-correspondencia/` |
| Each meeting's notice, material, notes and signed minutes | `organos/<body>/<YYYY-MM-DD>/` |
| The governing bodies followed and the office's sheet | `00-referencia/` |

**Exports, not accounts.** Ofelia does not connect to the mailbox or the calendar: she processes what
the office exports. A direct connection is a separate decision, with its privacy review.

### What it costs today

<!-- ea:cifras · generado por scripts/familias.py; no se edita a mano -->
| Figure | Source |
|---|---|
| **57%** of working time goes to communicating —meetings, email and chat— and 43% to creating | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?», 2023](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) — Aggregated Microsoft 365 usage data, not the survey; the report does not give the size of that sample |
| **55%** say the next steps at the end of a meeting are unclear | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?», 2023](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) — 31,000 full-time employed or self-employed workers in 31 markets |
| **68%** do not have enough uninterrupted focus time in their workday | [Microsoft, Work Trend Index 2023, «Will AI Fix Work?», 2023](https://www.microsoft.com/en-us/worklab/work-trend-index/will-ai-fix-work) — 31,000 full-time employed or self-employed workers in 31 markets |
<!-- /ea:cifras -->

### And what it is not for

- **It does not send, schedule, accept or move anything.** It writes drafts only in `90-borradores/`,
  with «BORRADOR» in the name and the text; a person sends.
- **It does not recommend an option or prioritise for the executive.** Each decision arrives with its
  options in the order the documents bring them, with their evidence and what is still unknown.
- **It does not edit original minutes, calendars or emails**, and never files a draft as minutes.
- **It does not declare a commitment done without a document that supports it**, and does not evaluate
  a person or a team.
- **It does not process what is excluded.** Excluded folders are named in every report.

And one to say out loud: **documents are processed on the AI platform's infrastructure**, not only on
your machine, and the executive's office is among the most sensitive things an organisation has. Her
report **is not published on Rostrum by default**. Full disclaimer in [DISCLAIMER.md](../../DISCLAIMER.md),
terms in [TERMS.md](../../TERMS.md).

## Installing and configuring

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-assistant@criterio
/criterio-assistant:ea-setup
```

**In Claude Cowork** — Customise → Explore plugins → Personal → **+** → Add marketplace from GitHub →
`josenanez/criterio`.

### The first result

`/criterio-assistant:ea-setup` does not ask you to tidy anything. It finds the office's folder, says
which calendar export there is and from what date, which governing bodies have meetings and how many
emails are saved, and asks what no document answers: the executive, the bodies, the excluded folders,
the office's email, the time zone and the thresholds. Within fifteen minutes it shows the next two
weeks of calendar with their overlaps, the meetings without material and the ones still without minutes.

**What stays configured** is written by the setup to `.criterio/direccion/<executive>/config.json`.
All of it is changed **by talking**.

### How often it runs

Every day it runs, with a single summary a week. The decision is date arithmetic:

```
python3 scripts/asistente.py despertar --config <file>
```

And `/criterio-assistant:ea-wake` is the command the clock calls: it does what is due —process what is
new, prepare a meeting entering its window, pending minutes, overdue correspondence— and, **if nothing
is, it stays quiet.**

## Working with the others

Ofelia works on her own. If the others are there, **there is nothing to connect**.

| With whom | What happens |
|---|---|
| **Samuel** | Project commitments are his: Ofelia cites them from his record and does not recalculate them. They share the commitment rules of the common core |
| **Rostrum** | Publishes her report only if the configuration says so; by default, it does not |

## Tests

### How it is built

[`scripts/asistente.py`](scripts/asistente.py), with the standard library, does everything that is
calculation: it reads the .ics calendar —recurrences, exceptions, moved occurrences and time zones, with
its self-test—, reads each email's headers, walks each body's meetings and calculates every signal with
the commitment rules it shares with Samuel (`nucleo.py`). The agent takes to each record only what a
written document carries: the agreements and commitments in the minutes, the decisions with their
options and what each email asks.

### How it is verified

```
python3 scripts/asistente.py selftest        the engine
python3 tests/criterio-ea/generar.py          the material of the four offices
python3 tests/criterio-ea/evaluar.py          each signal against the key, and the rules
```

On synthetic material with a key the engine never sees, including the control offices, where any
signal is a failure. The material also tests the rules of real operation: a meeting in another time
zone that only overlaps after the clock change, a free event and a cancelled one that do not overlap,
an old calendar that gives no overlaps, a draft placed in `40-acta/` and an excluded folder. The latest
run, in [`tests/criterio-assistant/RESULTADOS.md`](../../tests/criterio-assistant/RESULTADOS.md); what
the material tests and what it does not, in [`EVIDENCIA.md`](../../tests/criterio-ea/EVIDENCIA.md).
