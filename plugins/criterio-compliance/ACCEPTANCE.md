# Acceptance criteria — criterio-compliance

Verified on synthetic material in `tests/criterio-clo/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every due date, day count and percentage in a report comes from `legal.py`; none is typed by the model.
- [ ] Evidence is looked for within the window of each obligation's frequency, and progress is weighted by criticality.
- [ ] Every planted signal in each industry is raised, and the control entities raise none (`tests/criterio-clo/evaluar.py --agente constanza`).

## 2. The organisation defines the obligations

- [ ] No output adds, removes or rewrites an obligation of the matrix, or says what a rule requires or whether it applies (ADR 0009).
- [ ] An obligation without an owner or a source is reported, not completed.
- [ ] The whistleblowing channel is processed only by its deadlines: no output shows who reported, who was reported or what was reported.

## 3. Traceability

- [ ] Every signal cites the matrix, index or register row it came from, or the document for what was extracted.
- [ ] Declared and evidenced status are kept apart; an obligation declared met without evidence is reported as such.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007). The only exception is the root marker, `_CRITERIO_<…>.txt`, written only with the person's explicit yes and never counted as a document (ADR 0011).
