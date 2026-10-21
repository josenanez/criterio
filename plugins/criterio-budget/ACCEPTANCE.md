# Acceptance criteria — criterio-budget

Verified on synthetic material in `tests/criterio-cfo/`, with a key the agent never sees and a control entity that must raise nothing.

## 1. Arithmetic

- [ ] Every figure in a report comes from `finanzas.py`; none is typed by the model.
- [ ] Actual spend by line comes from the same books Clara closes (`10-contabilidad/`), mapped with the organisation's account mapping; spend the mapping does not cover is reported.
- [ ] Every planted signal in each industry is raised, and the control entity raises none (`tests/criterio-cfo/evaluar.py`).

## 2. Forecast and transfers

- [ ] Every forecast carries its assumption next to the figure; none is presented as the correct one.
- [ ] Every change between budget versions is matched to the minutes that approve it, or reported without them.

## 3. Traceability

- [ ] Every signal cites the file and, for tables, the row it came from.
- [ ] What an area declares is kept apart from what the numbers show.

## 4. Terms and acceptance

- [ ] No command produces anything without a current acceptance of the terms for the installed version.

## 5. Decisions

- [ ] The committee pack presents each decision with its figure, citation and who decides, and recommends none.
