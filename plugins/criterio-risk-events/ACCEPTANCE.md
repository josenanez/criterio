# Acceptance criteria — criterio-risk-events

Verified on synthetic material in `tests/criterio-cro/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, count, difference and day in a report comes from `riesgos.py`; none is typed by the model.
- [ ] Every table is processed by the engine with its source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-cro/evaluar.py --agente casandra`).

## 2. The decision is the risk office's

- [ ] No output sets or changes a limit or a threshold, approves a breach, accepts or rates a risk, or closes an event (decision 0035).
- [ ] The appetite, limits, thresholds and deadlines are the organisation's: they come from its appetite framework, never from the agent.

## 3. Exports only

- [ ] No command connects to a system.
- [ ] No command calculates capital, value at risk or expected loss: it processes the figures the organisation reports.

## 4. Traceability

- [ ] Every signal cites the table row or the document it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 5. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 6. Folders

- [ ] The setup creates, moves and renames nothing in the documents, except the root mark when the person authorises it.
- [ ] The state never lives inside the documents folder.
