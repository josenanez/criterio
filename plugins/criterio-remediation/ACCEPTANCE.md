# Acceptance criteria — criterio-remediation

Verified on synthetic material in `tests/criterio-cae/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, count, hour and day in a report comes from `auditoria.py`; none is typed by the model.
- [ ] Every table is processed by the engine with its source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-cae/evaluar.py --agente remedios`).

## 2. The opinion is the auditor's

- [ ] No output concludes on internal control, signs or approves a report, changes a finding's priority, closes a plan or accepts a risk (decision 0033).
- [ ] Cycles, deadlines, the priority scale and the number of reschedules are the organisation's: they come from its methodology, never from the agent.
- [ ] The Global Internal Audit Standards are cited by number and title, never by their text.

## 3. Traceability

- [ ] Every signal cites the table row or the document it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The setup creates, moves and renames nothing in the documents, except the root mark when the person authorises it.
- [ ] The state never lives inside the documents folder.
