# Acceptance criteria — criterio-data-quality

Verified on synthetic material in `tests/criterio-cdo/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, count, difference and day in a report comes from `datos.py`; none is typed by the model.
- [ ] Every table is processed by the engine with its source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-cdo/evaluar.py --agente ariadna`).

## 2. The decision is the data office's

- [ ] No output assigns an owner, decides a classification, deletes data, corrects a figure or decides which of two figures is right (decision 0034).
- [ ] The tolerance, thresholds and periods are the organisation's: they come from its data policy, never from the agent.

## 3. Exports and metadata only

- [ ] No command connects to a database or a system.
- [ ] No personal data is processed: from a database with personal data, only its metadata.

## 4. Traceability

- [ ] Every signal cites the table row or the document it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 5. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 6. Folders

- [ ] The setup creates, moves and renames nothing in the documents, except the root mark when the person authorises it.
- [ ] The state never lives inside the documents folder.
