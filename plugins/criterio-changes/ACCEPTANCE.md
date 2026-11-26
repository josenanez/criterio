# Acceptance criteria — criterio-changes

Verified on synthetic material in `tests/criterio-cto/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, count, difference and day in a report comes from `tecnologia.py`; none is typed by the model.
- [ ] Every table is processed by the engine with its source row; an unrecognised column is reported, not guessed.
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-cto/evaluar.py --agente fausto`).

## 2. The decision is the change board's and the technology office's

- [ ] No output approves a change, decides an architecture or rates an incident (decision 0037).
- [ ] The deadlines and service levels are the organisation's: they come from its change and service level policy and its service catalogue, never from the agent.

## 3. Exports only

- [ ] No command connects to a service management tool or a server.
- [ ] No security is processed: vulnerabilities, controls and security incidents belong to the CISO family.

## 4. Traceability

- [ ] Every signal cites the table row or the document it came from.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 5. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 6. Folders

- [ ] The setup creates, moves and renames nothing in the documents, except the root mark when the person authorises it.
- [ ] The state never lives inside the documents folder.
