<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/en/criterio-cmo-oscuro.svg"><img src="../../docs/img/marca/en/criterio-cmo-claro.svg" alt="Criterio CMO · Marketing" height="48"></picture>

# criterio-cmo · the marketing family

**Two agents and a portal, around their records.** Each extends a different person in the marketing office
—whoever answers for what the brand advertises and whoever answers for what is invested in campaigns— and
they share the entity's folder and advertising policy: each writes only its own record.

[Español](README.es.md) · [← Criterio](../../README.md) · Apache 2.0

![Criterio CMO](../../docs/img/en/cmo.png)

---

## What the family does

A piece reaches the street after passing through the agency, the marketing office and legal. What it says
binds whoever advertises it, and what is paid to place it in a medium is invoiced separately, against a
campaign. When a claim has nothing to back it or a campaign goes over budget, it is rarely bad faith: it is
substantiation nobody filed, an approval that came late or an invoice nobody matched with its order. Today
that cross-check is done by hand, piece by piece and invoice by invoice. The family calculates it, on the
ICC Advertising and Marketing Communications Code (F-01) and the MRC outcomes standards (F-02)
([decision 0036](../../docs/decisions/0036-la-familia-cmo.md)).

- **Lucía** puts each claim in a piece next to its substantiation and each promotion next to its terms,
  and says which piece went out without approval or without being identified as advertising and which
  contact base was used without consent.
- **Próspero** puts each campaign next to its budget, goal, end date and media invoices, and each report
  result next to the platform.

## What remains with people

Approving a piece, judging the creative, saying whether a claim is true, approving or extending a budget and
deciding which of two figures is right. The agents say what is missing and where; the decision is always
legal's, the marketing office's and that of whoever signs the report.

## The recommended folder structure

<!-- cmo:carpetas · generado por scripts/familias.py; no se edita a mano -->
One folder per entity, with its tax id at the start of the name. Inside it, the advertising policy; the approved pieces with their register; the substantiation of the claims; each promotion's terms; the contact base register, and the marketing plan with the media invoices, the platform export and the results report.

```
mercadeo/
└── <entidad>/
    ├── 00-politica/
    ├── 10-piezas/
    ├── 20-soportes/
    ├── 30-promociones/
    ├── 40-bases/
    └── 50-campanas/
estado-mercadeo/
```

**`<entidad>/`** · What the marketing office keeps for the entity

| Folder | What goes in | Agent |
|---|---|---|
| `00-politica/` | The advertising and piece approval policy, with its tolerances | Lucía, Próspero |
| `10-piezas/` | Each approved piece with its text and the piece register: its channel, publication date, approval and whether it is paid to an influencer | Lucía |
| `20-soportes/` | The substantiation for each claim: studies, measurements, certificates and comparisons | Lucía |
| `30-promociones/` | Each promotion's terms, with its dates and its terms of how and where | Lucía |
| `40-bases/` | The contact base register: each base with its records, its marketing consent and its date. Never a person's data | Lucía |
| `50-campanas/` | The marketing plan with each campaign's budget, goal and base; the media invoices; the platform export and the results report | Próspero, Lucía |

**`estado-mercadeo/`** · What Lucía and Próspero write: the configuration, each period's record, the reports and the indexes. No person edits it, and no agent writes anywhere else.
<!-- /cmo:carpetas -->

A file without the expected format is not guessed: it is reported with what it lacks.

## Installing the family

It needs Claude Code 2.1.110 or later; if something fails, [the step-by-step installation](../../docs/instalacion.md).

**The family installs at once.** The `criterio-cmo` plugin brings its agents and Rostrum, and
`/criterio-cmo:cmo-setup` configures them in order, in a single conversation: what has already been
answered is not asked again.

```
/plugin marketplace add josenanez/criterio
/plugin install criterio-cmo@criterio
/criterio-cmo:cmo-setup
```

Then you ask each agent in your own words, without knowing each command's name:
`/criterio-claims:lucia` and `/criterio-campaigns:prospero`
([decision 0027](../../docs/decisions/0027-cada-agente-se-pide-en-palabras.md)).

## What each agent answers for, and where its detail is

<!-- cmo:familia-agentes · generado por scripts/familias.py; no se edita a mano -->
| | What it answers for | What it never does | Its page | Its tests |
|---|---|---|---|---|
| **Lucía** · what is advertised | Each approved piece against its substantiation, each promotion against its published terms and each contact base against its consent: a claim with no substantiation, a comparison with no source, a promotion with no dates or terms, a piece paid to an influencer not identified as advertising, a piece published without legal's approval and a base used without marketing consent | It does not approve a piece, judge the creative, say whether a claim is true, process a person's data or connect to a platform | [criterio-claims](../../plugins/criterio-claims/README.md) · 8 commands, 3 skills | [results](../../tests/criterio-claims/RESULTADOS.md) |
| **Próspero** · what is invested | Each campaign's budget against the media invoiced and against its measured result: a campaign over budget, a media invoice with no campaign or order, a campaign with no goal or indicator, a reported result that does not match the platform and media invoiced after the end date | It does not approve a budget, judge a campaign, decide which figure is right or connect to an ad or analytics platform | [criterio-campaigns](../../plugins/criterio-campaigns/README.md) · 8 commands, 3 skills | [results](../../tests/criterio-campaigns/RESULTADOS.md) |
| **Rostrum** · the portal | Publishing what the agents write where the team will see it, and taking the question from whoever will not open a folder | **Never writes the state or recalculates anything**, and decides nothing | [criterio-server](../../plugins/criterio-server/README.md) · 3 commands, one for every family | [results](../../tests/criterio-server/RESULTADOS.md) |
<!-- /cmo:familia-agentes -->

## How each one is configured and how often it runs

<!-- cmo:configuracion · generado por scripts/familias.py; no se edita a mano -->
| | Lucía | Próspero |
|---|---|---|
| **Installs as** | `criterio-claims` | `criterio-campaigns` |
| **Instances** | One per entity | One per entity |
| **Configured with** | `/criterio-claims:claims-setup` | `/criterio-campaigns:campaigns-setup` |
| **How long that takes** | Fifteen minutes | Fifteen minutes |
| **What you have to tell it** | Entity and its tax ID, country and the period | Entity and its tax ID, country, the period and the policy's two tolerances: over budget and between a result and the platform |
| **Where it lands** | `.criterio/piezas/<entity>/config.json`, written by the command | `.criterio/campanas/<entity>/config.json`, written by the command |
| **The one you put on a clock** | `/criterio-claims:claims-wake` | `/criterio-campaigns:campaigns-wake` |
| **What it does each day** | Decides whether the pieces need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet | Decides whether the campaigns need processing —new documents or the weekly review— or a report with open signals, and runs it; if nothing is due, it stays quiet |
| **What wakes it besides the clock** | A question somebody left in Rostrum | A question somebody left in Rostrum |
<!-- /cmo:configuracion -->

**Nobody edits a configuration file by hand.** You say it in the conversation and the command rewrites it.
The tolerances, goals and who approves each piece come from the organisation's advertising policy.

## The family's tests

**A single gate runs everything this repository checks**, for all families at once:

```
python3 scripts/verificar.py
```

What belongs to the CMO is in [`tests/criterio-cmo/`](../../tests/criterio-cmo/): synthetic material with
a key the engine never sees and two control entities, where any signal is a failure. **One signal too
many counts the same as one too few.** What is planted and what the material does not test, in
[`EVIDENCIA.md`](../../tests/criterio-cmo/EVIDENCIA.md).

## Roadmap

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->
<!-- /hoja de ruta -->

## The family's skills

<!-- cmo:skills-familia · generado por scripts/familias.py; no se edita a mano -->
Four distinct skills across the two agents. **The ones they share are literal copies, not an imported module**: an installed plugin has to run on its own. `scripts/sincronizar.py` copies them and `scripts/sincronizar.py --check` fails if they drift.

| Skill | Lucía | Próspero |
|---|:--:|:--:|
| `claim-record` | ● | · |
| `marketing-intake` | ● | ● |
| `marketing-policy` | ● | ● |
| `result-record` | · | ● |
<!-- /cmo:skills-familia -->

## Status

<!-- cmo:estado · generado por scripts/familias.py; no se edita a mano -->
| Agent | Installs as | Its test |
|---|---|---|
| **Lucía** · What is advertised | `criterio-claims` · 8 commands, 3 skills | The engine, tested; with the agent, every entitie in the material, up to round 3 · [results](../../tests/criterio-claims/RESULTADOS.md) |
| **Próspero** · What is invested | `criterio-campaigns` · 8 commands, 3 skills | The engine, tested; with the agent, every entitie in the material, up to round 3 · [results](../../tests/criterio-campaigns/RESULTADOS.md) |
| **Rostrum** · the portal | `criterio-server` · 3 commands, for every family | — |

Tests use synthetic material built on real company information, anonymised before processing: no name, identifier, figure or personal data that could identify a company or a person is kept or published. What is published from each test is its results, without data.
<!-- /cmo:estado -->
