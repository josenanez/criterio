[Español](DISENO.es.md) · [← The family](README.md)

# criterio-cmo · the family design

**Status: built and tested, in the lab (version 0.2.0).** The commands, the skills and the calculation engine
are built on the common core; the engine passes its deterministic test against the material in
`tests/criterio-cmo/`. In 0.2.0, the two agents ran on every entity in the material, with a key they never see: [the rounds](../../tests/evidencias/familias/cmo/RONDAS.md). Scope in [ADR 0036](../../docs/decisions/0036-la-familia-cmo.md).

**This is the family's design sheet**: the signals the code calculates, each command with its input,
process and report, and the decisions taken. What the family does, how it is installed, the folder
structure and the roadmap are on its [page](README.md).

The language model (LLM) extracts; the code calculates; the decision —approving a piece, extending a
budget, deciding which figure is right— is always legal's, the marketing office's and that of whoever signs
the report. **The agents process documents and exports**: they never connect to a platform or process a
person's data.

**Where this document comes from.** The tables of agents, signals, commands and figures are not written
here: they come from [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) and [`fuentes.json`](fuentes.json).

## One agent per role

<!-- cmo:agentes · generado por scripts/familias.py; no se edita a mano -->
| Role | Agent | Plugin | What it does |
|---|---|---|---|
| What is advertised | **Lucía** — from the Latin *lux*, light: each claim, in the light of its substantiation | `criterio-claims` | Each approved piece against its substantiation, each promotion against its published terms and each contact base against its consent: a claim with no substantiation, a comparison with no source, a promotion with no dates or terms, a piece paid to an influencer not identified as advertising, a piece published without legal's approval and a base used without marketing consent |
| What is invested | **Próspero** — from the Latin *prosperus*, the one who makes something yield: each unit of media spend against what it produced | `criterio-campaigns` | Each campaign's budget against the media invoiced and against its measured result: a campaign over budget, a media invoice with no campaign or order, a campaign with no goal or indicator, a reported result that does not match the platform and media invoiced after the end date |
<!-- /cmo:agentes -->

## The signals: what the code calculates

<!-- cmo:senales · generado por scripts/familias.py; no se edita a mano -->
**Lucía · What is advertised**

| Signal | Raised when |
|---|---|
| `claim_without_substantiation` | A claim in an approved piece has no substantiation in the substantiation folder |
| `comparative_claim_without_source` | A comparative claim does not cite its source or date |
| `promotion_terms_missing` | A promotion does not publish its dates or its terms of how and where |
| `sponsored_content_unidentified` | A piece paid to an influencer is not identified as advertising |
| `piece_published_unapproved` | A piece was published without the approval the policy requires, or before it |
| `contact_base_without_consent` | A contact base used in a campaign has no marketing consent |

**Próspero · What is invested**

| Signal | Raised when |
|---|---|
| `campaign_over_budget` | A campaign's invoiced media exceeds its budget plus the policy's tolerance |
| `media_invoice_unmatched` | A media invoice has no plan campaign or purchase order |
| `campaign_without_goal` | A campaign has no goal or measurement indicator |
| `result_differs_from_platform` | The reported result does not match the platform export for the same cut-off, beyond the tolerance |
| `campaign_ran_past_end` | Media was invoiced after the campaign's end date |
<!-- /cmo:senales -->

## Lucía's commands, in order of importance

<!-- cmo:comandos-lucia · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `claims-setup` | The root folder. Questions: entity and its tax ID, country and the period | Inventory of what is there; processes the piece register in `10-piezas/`, the contact base register in `40-bases/` and the plan in `50-campanas/`, and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `claims-scan` | The pieces in `10-piezas/`, the substantiation in `20-soportes/`, the terms in `30-promociones/` and the period's record | Brings into the record each claim in each piece with its substantiation, and each promotion with its dates and terms, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `claim-check` | The record —each piece's claims— and the substantiation folder in `20-soportes/` | Each claim against the substantiation in the folder, and each comparison against the source and date the piece cites | The claims with no substantiation and the comparisons with no source, with the piece |
| 3 | `promo-check` | The record —each promotion with its dates and terms— and the terms in `30-promociones/` | Each promotion against its start, its end and its terms of how and where, as its published terms state them | The promotions missing their dates or terms, with their published terms |
| 4 | `approval-check` | The piece register in `10-piezas/`, the base register in `40-bases/` and the plan in `50-campanas/` | Each published piece against its approval; each piece paid to an influencer against its identification as advertising; each base a campaign uses against its marketing consent | The pieces published without approval or before it, the paid ones not identified and the bases used without consent |
| 5 | `claims-wake` | The configuration and the run log | Decides whether the pieces need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cmo:comandos-lucia -->

## Próspero's commands, in order of importance

<!-- cmo:comandos-prospero · generado por scripts/familias.py; no se edita a mano -->
| # | Command | Input | Process (calculated by the code) | Report |
|---|---|---|---|---|
| 0 | `campaigns-setup` | The root folder. Questions: entity and its tax ID, country, the period and the policy's two tolerances: over budget and between a result and the platform | Inventory of what is there; processes the marketing plan, the media invoices and the platform export in `50-campanas/`, and says how many rows it recognises; compares the folder with the recommended structure; creates, moves or renames nothing | Configuration saved; inventory by folder; the recognised tables; the period's first record |
| 1 | `campaigns-scan` | The results report and the tables in `50-campanas/`, and the period's record | Brings into the record each result the report states —its campaign, indicator, value and cut-off—, with its citation; recalculates the signals | What went into the record; the documents not yet in it; the new signals; what could not be processed and why |
| 2 | `budget-check` | The marketing plan and the media invoices in `50-campanas/` | Each campaign's invoiced media against its budget and the policy's tolerance; each campaign against its goal and indicator; the media against the end date | The campaigns over budget, those with no goal and those that ran past their end, with the difference and the days |
| 3 | `invoice-check` | The media invoices and the marketing plan in `50-campanas/` | Each media invoice against the plan campaign it belongs to and its purchase order | The invoices with no campaign, with a campaign not in the plan or with no purchase order |
| 4 | `result-check` | The record —the report's results— and the platform export in `50-campanas/` | Each reported result against the platform's value for the same campaign, indicator and cut-off, with the policy's tolerance | The results that do not match the platform, with the difference |
| 5 | `campaigns-wake` | The configuration and the run log | Decides whether the campaigns need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | What ran and why, or nothing |
| 6 | `share-findings` | The trail of this agent's runs in this folder | Builds a summary with no data —which commands ran, how many signals, what could not be processed— and asks whether to share it; nothing is sent on its own | The summary and the question |
<!-- /cmo:comandos-prospero -->

## Third-party figures

<!-- cmo:cifras · generado por scripts/familias.py; no se edita a mano -->
Only verified figures go in, with their source, year and sample; they are in [`FUENTES.es.md`](FUENTES.es.md) (Spanish). Verified: C-01 (Gartner), C-02 (Gartner), C-03 (Association of National Advertisers (ANA)).
<!-- /cmo:cifras -->

## Closed decisions

- The names, Lucía and Próspero, and the structure: two agents, their eleven signals and their commands (decision 0036).
- Marketing comes in through what lives in documents —what is advertised and what is invested—; the ad and analytics platforms, only through their exports (decision 0036, following 0019).
- From a contact base only its register entry is processed: how many records, with what consent and since when; never a person's data.
- Whether a claim's substantiation is enough is legal's decision: the agent says whether there is one about the same thing.
- Colombia's Consumer Statute (F-10) is cited only for an entity in Colombia; Law 2300 of 2023, what Law 1581 requires for marketing and the advertising law of other countries stay out of 0.1.0 until verified.
