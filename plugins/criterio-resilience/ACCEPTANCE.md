# Acceptance criteria — criterio-resilience

Verified on synthetic material in `tests/criterio-ciso/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every hour, day and count in a report comes from `seguridad.py`; none is typed by the model.
- [ ] The notification matrix and the continuity calendar are processed by the engine with their source row; an unrecognised condition is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-ciso/evaluar.py --agente amparo`).

## 2. People decide

- [ ] The containment and review deadlines come from the organisation's policy, with their citation, or from the person; the notification deadlines from its matrix.
- [ ] No output notifies anyone, declares or closes an incident, assigns its severity, or runs a test or a restore.

## 3. Traceability

- [ ] Every signal cites the incident report, the record of each notification, or the matrix or calendar row it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007). The only exception is the root marker, `_CRITERIO_<…>.txt`, written only with the person's explicit yes and never counted as a document (ADR 0011).
- [ ] Credentials, keys and backups are never opened: the engine lists them as excluded and every report says which (ADR 0023).
