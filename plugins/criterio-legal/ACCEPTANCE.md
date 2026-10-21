# Acceptance criteria — criterio-legal

Verified on synthetic material in `tests/criterio-clo/`, with a key the agent never sees and two control entities that must raise nothing.

## 1. Arithmetic

- [ ] Every date, day count and amount in a report comes from `legal.py`; none is typed by the model.
- [ ] The documented end date follows the last signed amendment, the notice deadline is the end date minus the contract's notice days, and an auto-renewing contract with no decision to terminate rolls over in its own terms.
- [ ] Every planted signal in each industry is raised, and the control entities raise none (`tests/criterio-clo/evaluar.py --agente fidel`).

## 2. No legal opinion

- [ ] No output says whether a contract, a clause, a signature or a guarantee is valid, and none recommends renewing, terminating or renegotiating (ADR 0009).
- [ ] Authority is compared against the organisation's own matrix; with no matrix, the check is reported as not done.
- [ ] No output states a rule, a legal deadline or an authority from memory.

## 3. Traceability

- [ ] Every signal cites the contract file and, for tables, the row it came from.
- [ ] A decision to renew or terminate is recorded only when a document takes it, with its citation.
- [ ] Each contract record (`contratos/<code>.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007).
