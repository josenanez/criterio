[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cdo · the family's design

**Status: built and tested, in the lab (version 0.2.0).** The commands, the skills and the calculation engine
are built on the common core; the engine passes its deterministic test against the material in
`tests/criterio-cdo/`. In 0.2.0, the two agents ran on every entity in the material, with a key they never see: [the rounds](../../tests/evidencias/familias/cdo/RONDAS.md). Scope in [ADR 0034](../../docs/decisions/0034-la-familia-cdo.md).

**This is the family's design sheet**: the signals the code calculates, each command with its input,
process and report, and the decisions taken. What the family does, how it installs, the folder structure
and the roadmap are on its [page](README.md).

The language model (LLM) extracts; the code calculates; the decision —who owns a piece of data, which
figure is right— is always the data office's. **The agents process exports and metadata**: they never
connect to a database or process personal data.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json).

## One agent per role

<!-- cdo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| Data governance | **Custodia** — from the Latin *custodia*, safekeeping: each piece of data with whoever answers for it | `criterio-data-governance` | The data catalog against its owners, classification, retention and policies: a dataset with no owner or no classification, a policy past its review, data kept longer than the policy says, a report term missing from the glossary and a database with personal data missing from the organisation's register |
| Quality and lineage | **Ariadna** — the one whose thread leads back through the labyrinth: each figure back to its source | `criterio-data-quality` | Each figure in a management report against its source, cut-off and lineage, and each quality rule against its threshold: a figure with no source, one that does not match its source at the same cut-off, one taken from another cut-off, a broken lineage, a rule below its threshold, one that did not run and a critical data element with no rule |
<!-- /cdo:agentes -->

## The signals: what the code calculates

<!-- cdo:senales · generado por scripts/familias.py; no se edita a mano -->
**Custodia · Data governance**

| Signal | Raised when |
|---|---|
| `dataset_without_owner` | A dataset in the catalog has no business owner |
| `dataset_without_classification` | A dataset has no confidentiality classification |
| `policy_review_overdue` | A data or retention policy is past its review date |
| `retention_exceeded` | A dataset keeps records longer than the policy sets for its type |
| `term_not_in_glossary` | A term in a management report has no definition in the business glossary |
| `personal_data_unregistered` | A dataset with personal data is not in the organisation's register of personal databases |

**Ariadna · Quality and lineage**

| Signal | Raised when |
|---|---|
| `figure_without_source` | A figure in a management report has no source in the lineage or in the exported source figures |
| `figure_differs_from_source` | The report's figure does not match its source's at the same cut-off, beyond the tolerance the organisation sets |
| `cutoff_mismatch` | The report's figure is the source's at a cut-off other than the one the report states |
| `lineage_broken` | A step in a figure's lineage has no source system |
| `quality_rule_below_threshold` | A quality rule's result for the period is below its threshold |
| `quality_rule_not_run` | A quality rule on a critical data element has no result for the period |
| `critical_data_without_rule` | A data element marked critical has no quality rule |
<!-- /cdo:senales -->

## Custodia's commands, in order of importance

<!-- cdo:comandos-custodia · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `governance-setup` | The root folder. Questions: entity and its tax ID, country and the period | Inventory of what is there; processes the catalog export and the register of personal databases in `10-catalogo/` and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `governance-scan` | The policies and the glossary in `00-referencia/`, the catalog in `10-catalogo/`, the reports in `20-informes/` and the period's record | Brings into the record each policy with its review date, each retention period and each term in the reports, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `catalog-check` | The catalog export in `10-catalogo/` | Each dataset in the catalog against its business owner and its confidentiality classification | The datasets with no owner or no classification, with their row |
| 3 | `retention-check` | The record —the policies and the retention periods— and the catalog | Each policy against its review date and each dataset against its type's retention period | The policies past their review and the datasets keeping records beyond their period, with the days |
| 4 | `glossary-check` | The record —the terms in the reports—, the glossary in `00-referencia/` and the register of personal databases | Each term in the management reports against the business glossary, and each dataset with personal data against the organisation's database register | The undefined terms and the databases with personal data missing from the register, with their citation |
| 5 | `governance-wake` | The configuration and the run log | Decides whether governance needs processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cdo:comandos-custodia -->

## Ariadna's commands, in order of importance

<!-- cdo:comandos-ariadna · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `lineage-setup` | The root folder. Questions: entity and its tax ID, country, the period and the difference the data policy tolerates between a figure and its source | Inventory of what is there; processes the lineage, the source figures and the quality rules in `30-calidad/` and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `lineage-scan` | The reports in `20-informes/`, the lineage and the rules in `30-calidad/`, and the period's record | Brings into the record each figure in the reports —its indicator, value and cut-off—, with its citation; recalculates the signals | What went into the record; the reports not yet in it; the new signals; what could not be processed and why |
| 2 | `figure-check` | The record —the figures in the reports— and the source figures in `30-calidad/` | Each figure in a report against its source's at the same cut-off, with the policy's tolerance; if it matches another cut-off, it says so | The figures with no source, the ones that do not match and the ones taken from another cut-off, with both citations |
| 3 | `lineage-check` | The lineage export in `30-calidad/` | Each step in each indicator's lineage against its source system | The steps with no source system, with their row |
| 4 | `rule-check` | The rules, their results and the critical data in `30-calidad/` | Each rule against its threshold and the period's result, and each critical data element against the rules that measure it | The rules below threshold, the ones that did not run on a critical element and the critical elements with no rule |
| 5 | `lineage-wake` | The configuration and the run log | Decides whether quality needs processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cdo:comandos-ariadna -->

## Third-party figures

<!-- cdo:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Comité de Supervisión Bancaria de Basilea), C-02 (Nagle), C-03 (Nagle).
<!-- /cdo:cifras -->

## Closed decisions

- The names, Custodia and Ariadna, and the structure: two agents, their thirteen signals and their commands (decision 0034).
- It processes exports and never connects to a database; it does not process personal data, only its metadata (decision 0015, kept in 0034).
- What each country's law requires about the register of personal databases supports no signal until verified country by country: meanwhile, Custodia compares the catalog with the organisation's register.
- ISO 8000 stays out of 0.1.0 until its current parts are verified.
