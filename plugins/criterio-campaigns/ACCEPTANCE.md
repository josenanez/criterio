# Acceptance criteria — criterio-campaigns

Verified on synthetic material in `tests/criterio-cmo/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, count, difference and day in a report comes from `mercadeo.py`; none is typed by the model.
- [ ] Every table is processed by the engine with its source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-cmo/evaluar.py --agente prospero`).

## 2. The decision is the marketing office's

- [ ] No output approves a piece or a budget, judges the creative, says whether a claim is true or decides which figure is right (decision 0036).
- [ ] The tolerances, goals and who approves are the organisation's: they come from its advertising policy, never from the agent.

## 3. Exports only

- [ ] No command connects to an ad or analytics platform.
- [ ] No person's data is processed: from a contact base, only its register entry.

## 4. Traceability

- [ ] Every signal cites the table row or the document it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 5. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 6. Folders

- [ ] The setup creates, moves and renames nothing in the documents, except the root mark when the person authorises it.
- [ ] The state never lives inside the documents folder.
