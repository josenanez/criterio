# Acceptance criteria — criterio-revenue

Verified on synthetic material in `tests/criterio-cso/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every discount, contract, invoice and commission figure in a report comes from `ventas.py`; none is typed by the model.
- [ ] Contracts are taken from Fidel's records and invoices from Clara's; no contract or electronic invoice is processed again (ADR 0019).
- [ ] Every planted signal in each entity is raised, and the control entities raise none (`tests/criterio-cso/evaluar.py --agente valeria`).

## 2. People decide

- [ ] No output writes to the CRM, approves a discount, sets a target or settles a commission (ADR 0019).
- [ ] No output ranks or compares the people on the team; the forecast and the target are never shown by person.
- [ ] No record keeps a customer contact's email or phone; the engine flags a record that does.

## 3. Traceability

- [ ] Every signal cites the export, table or record row it came from, or the document for what was extracted.
- [ ] Committed and backed are kept apart; the difference is the signal.
- [ ] The period record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007). The only exception is the root marker, `_CRITERIO_<…>.txt`, written only with the person's explicit yes and never counted as a document (ADR 0011).

## 6. Privacy

- [ ] The commission report is not published in Rostrum unless `revenue.publish_commissions` says so.
