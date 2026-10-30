# Acceptance criteria — criterio-security

Verified on synthetic material in `tests/criterio-ciso/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, count and day in a report comes from `seguridad.py`; none is typed by the model.
- [ ] The statement of applicability, the systems table, the third-party register and the risk register are processed by the engine with their source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-ciso/evaluar.py --agente alexis`).

## 2. People decide

- [ ] No output accepts a risk, declares a control met, rates the organisation's maturity or certifies it against ISO/IEC 27001 (ADR 0023).
- [ ] The frequencies are the organisation's: they come from its statement and its registers, never from the agent.

## 3. Traceability

- [ ] Every signal cites the table row it came from, or the document for what was extracted.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007). The only exception is the root marker, `_CRITERIO_<…>.txt`, written only with the person's explicit yes and never counted as a document (ADR 0011).
- [ ] Credentials, keys and backups are never opened: the engine lists them as excluded and every report says which (ADR 0023).
