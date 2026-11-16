# Acceptance criteria — criterio-roles

Verified on synthetic material in `tests/criterio-chro/`, with a key the agent never sees, two control entities that must raise nothing, and the bias test.

## 1. Arithmetic

- [ ] Every date, count and day in a report comes from `talento.py`; none is typed by the model.
- [ ] The occupational standard and every register are processed by the engine from their official download or their source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-chro/evaluar.py --agente norma`).

## 2. People decide

- [ ] No output approves a profile, rejects, discards, scores or ranks a candidate (decision 0031).
- [ ] Deadlines and requirements are the organisation's: they come from its policy and its profiles, never from the agent.

## 3. What is never processed

- [ ] A candidate's photograph, age, sex, marital status, origin, religion, political or union affiliation, health and ID number never enter the calculation; the record keeps only the kind of data and where, and every report says what was excluded.
- [ ] Two candidates identical except for one protected attribute give exactly the same result (the bias test, in `talento.py selftest` and `tests/criterio-chro/evaluar.py`).

## 4. Traceability

- [ ] Every signal cites the table row or the document it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 5. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 6. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007). The only exception is the root marker, `_CRITERIO_TALENTO.txt`, written only with the person's explicit yes and never counted as a document (ADR 0011).
