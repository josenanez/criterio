# Criterio

**Plugins that read the documentation an organisation already has, and say what it actually shows.**

[Español](README.es.md) · [Terms of use](TERMS.md) · [Disclaimer](DISCLAIMER.md) · [Contributing](CONTRIBUTING.md)

---

Most work tools help you produce another document. The problem in a real organisation is rarely a missing template: it is that nobody has read together the hundreds of documents that already exist.

Criterio reads them, keeps a record of what it found with a citation for every data point, and on the next run says what changed.

> **This produces working drafts, not decisions, and no professional has certified anything here.** Every output must be checked by someone qualified before it is acted on. Read [TERMS.md](TERMS.md) before installing. Using these plugins means accepting those terms.

---

## What ships today

| Plugin | State | What it does |
|---|---|---|
| `criterio-pmo` | **6 skills, 10 commands** | Project portfolio: reads a documentation folder, keeps a record per project, and reports what changed, what contradicts itself, what has gone silent and what no document supports |
| `criterio-legal` | Declared, not built | Contract review under civil-law reasoning |
| `criterio-finance` | Declared, not built | Monthly close and reporting |

---

## How it works

Two principles hold the whole thing up.

**The model extracts; the script computes.** Reading a date off a page is reading. Subtracting days, projecting variance and adding committed against executed is arithmetic, and arithmetic belongs in code, where it is deterministic and testable.

**Every data point carries its citation or declares that it is missing.** "Not stated anywhere" is a valid and expected finding. Without traceability nothing can be defended to a committee.

The spine is a **record per subject** — for `criterio-pmo`, one per project — that every command reads and writes. No command reads raw documents on its own. That is what allows consolidating forty projects without re-reading them, computing instead of opining, and comparing one run against the last.

---

## Installation

Criterio is a plugin marketplace. You add it once and the plugins come with it.

**Claude Cowork**

1. Open **Customize** (bottom left)
2. **Browse plugins** → **Personal** → **+**
3. **Add marketplace from GitHub**
4. Enter `josenanez-company/criterio`

**Claude Code**

```
claude plugins marketplace add josenanez-company/criterio
```

On first run the plugin shows the terms and does not produce a full analysis until acceptance is recorded in your local file. That is deliberate: see [docs/acceptance.md](docs/acceptance.md).

---

## Layout

```
criterio/
├── .claude-plugin/
│   └── marketplace.json     the marketplace manifest
├── plugins/
│   ├── criterio-pmo/        6 skills, 10 commands
│   ├── criterio-legal/
│   └── criterio-finance/
├── tests/                   synthetic material and graders
├── scripts/                 the validator
└── docs/
    └── decisions/           architecture decision records
```

---

## How to check that this works

Every plugin carries its own `ACCEPTANCE.md`: what "working" means for it and the bar it must clear. Nothing is released until its own criteria pass over the synthetic material in `tests/`, and the result of that run is published with the release.

```
python3 scripts/validate_plugins.py
```

---

## Licence

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

---

Maintained by [José Francisco Ñáñez](https://josenanez.com).
