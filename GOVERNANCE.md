# Governance

[Español](GOVERNANCE.es.md)

## Who maintains what

| Part | Owner |
|---|---|
| The method in the skills and commands, the record schemas, the acceptance criteria | The maintainer |
| Each organisation's own positions and thresholds | That organisation, in its own local configuration. These never enter this repository. |

**Maintainer:** José Francisco Ñáñez ([josenanez.com](https://josenanez.com)).

## Release model

Criterio builds and releases with an explicit disclaimer, and whoever deploys or runs it accepts the terms. No certification is claimed, and the words *verified*, *certified* and *approved* are not used about anything here. See [TERMS.md](TERMS.md) and [docs/acceptance.md](docs/acceptance.md).

What holds quality up is not a signature. It is that every statement in an output carries the document it came from, that arithmetic lives in code where it can be tested, and that anything uncertain or stale is surfaced at run time rather than smoothed over.

## Verification, plugin by plugin

Each plugin is verified on its own terms. There is no single bar across the project, because reading a portfolio and reviewing a contract fail in different ways.

Every plugin carries, in its own folder:

- `ACCEPTANCE.md` — what "working" means for this plugin, and the threshold it must hit.
- Synthetic material with known answers, under `tests/`.
- A grader that scores a run against those answers.

Nothing is released until its own criteria pass, and the result of that run is published with the release. A grader that only checks a report was produced is not a grader: it checks that every planted finding was found, and that nothing was invented.

## Versioning

`MAJOR.MINOR.PATCH`, shared by the marketplace and every plugin — there is no independent per-plugin versioning, and the validator enforces that they match.

- **Patch** — wording fixes, anything that does not change the output.
- **Minor** — a new skill or command, or changed behaviour.
- **Major** — a record schema changes, or the repository is restructured.

The terms are versioned separately. A change to `TERMS.md` bumps its version and triggers re-acceptance on the next run.

## Decisions

Architecture decisions are recorded in `docs/decisions/` as numbered ADRs: context, decision, discarded alternatives, consequences. A decision is not reversed in a conversation. It is superseded by a new ADR.
