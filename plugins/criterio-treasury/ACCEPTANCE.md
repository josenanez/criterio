# Acceptance criteria — criterio-treasury

Verified on synthetic material in `tests/criterio-cfo/`, with a key the agent never sees and a control entity that must raise nothing.

## 1. Arithmetic

- [ ] Every figure in a report comes from `finanzas.py`; none is typed by the model.
- [ ] Covenants are calculated from the same trial balance Clara closes; the engine does not recalculate the books.
- [ ] Every planted signal in each industry is raised, and the control entity raises none (`tests/criterio-cfo/evaluar.py`).

## 2. Policy and authority

- [ ] Every scheduled payment is checked against the approvals the organisation's policy requires for its amount and against the signing-authority matrix.
- [ ] The policy, the matrix and the covenants are the organisation's; none is proposed as a rule.

## 3. Traceability

- [ ] Every signal cites the file and, for tables, the row it came from.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Decisions and money

- [ ] Áurea never moves money, makes a payment, logs into a bank portal, or recommends an investment, a financing or a hedge.
