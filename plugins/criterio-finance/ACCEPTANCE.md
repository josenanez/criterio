# Acceptance criteria — criterio-finance

Verified on synthetic material in `tests/criterio-cfo/`, with a key the agent never sees and a control entity that must raise nothing.

## 1. Arithmetic

- [ ] Every figure in a report comes from `finanzas.py`; none is typed by the model.
- [ ] The trial balance, the ledger and every reconciliation tie out to the cent in the control entity, and the unexplained difference of every bank account is zero.
- [ ] Every planted signal in each industry is raised, and the control entity raises none (`tests/criterio-cfo/evaluar.py`).

## 2. Sources

- [ ] Every invoice field the engine reads is listed, verified, in `families/criterio-cfo/fuentes.json` with its id in the DIAN annex or the SRI technical sheet (`scripts/cfo.py --check`).
- [ ] An XML that is not a DIAN or SRI document, that the SRI did not authorise, or whose access key does not check out is reported, not guessed.
- [ ] No output states a tax rate, a deadline or a tax unit value from memory, and no output gives a tax or IFRS treatment opinion.

## 3. Traceability

- [ ] Every signal cites the file and, for tables, the row it came from.
- [ ] Declared and evidenced status are kept apart; a task marked done without support is reported as such.
- [ ] The record (`ficha.json`) has one writer, the agent; the results (`resultados.json`) have one writer, the engine.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Folders

- [ ] The agent never moves, renames or creates anything inside the organisation's documents; it suggests the recommended structure (ADR 0007).
