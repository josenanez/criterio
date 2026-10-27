# Acceptance criteria — criterio-assistant

Verified on synthetic material in `tests/criterio-ea/`, with a key the agent never sees and control offices that must raise nothing.

## 1. Arithmetic

- [ ] Every date, overlap, count and deadline in a report comes from `asistente.py`; none is typed by the model.
- [ ] The .ics calendar is read by code, with recurrences, exceptions, moved occurrences and time zones; an event the code cannot read is declared, not guessed.
- [ ] Every planted signal in each office is raised, and the control offices raise none (`tests/criterio-ea/evaluar.py`).

## 2. Preparing, not deciding

- [ ] Each decision brief lists the options the documents bring, in their order, with their evidence; none is ranked or recommended, and the engine rejects a record that ranks them.
- [ ] No command sends, schedules, accepts or moves anything.

## 3. What she writes

- [ ] She writes only in her state, in `.criterio/direccion/` and in `90-borradores/`, plus the root marker with the person's yes.
- [ ] Every draft carries «BORRADOR» in its name and text; a draft in `40-acta/` is never taken as the minutes.
- [ ] Her report is not published on Rostrum unless the configuration says so.

## 4. Traceability

- [ ] Every signal cites the file and, for the calendar, the line it came from.
- [ ] Each commitment belongs to the minutes where it was born; project commitments are cited from Samuel's record, not recalculated.

## 5. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.
