# Test material

Synthetic documentation with known answers, and the graders that score a run against it.

Nothing here is real. No client document, no employer data, no personal data, anonymised or not. Every file was built from scratch for testing. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Layout

```
tests/
├── coherencia.py        checks the documentation and the code say the same thing
├── sintetico/
│   ├── corpus.py        the engine: the reference structure, the Proyecto and
│   │                    Producto classes, and the four layouts
│   └── disposiciones.py proves discovery does not depend on the layout
└── <plugin>/
    ├── generar.py       builds input/ and expected/ from one declarative source
    ├── input/           the synthetic folder a command is pointed at
    ├── expected/
    │   ├── fichas/      the reference extraction: what a correct read of input/ produces
    │   └── hallazgos.json   the known answers, written by hand
    ├── grade.py         scores a run against them
    └── EVIDENCIA.md     what was run, what it proves, what it does not
```

## The engine, and the reference structure

The three corpora are declarations; `sintetico/corpus.py` is the only thing that writes
them. It holds the folder structure the material uses — `00-gobierno`, `10-plan`,
`20-seguimiento`, `30-reuniones` for a project, and `00-definicion`,
`10-descubrimiento`, `20-metricas`, `30-decisiones` for a product — declared once
instead of repeated by habit in three places. The numeric prefix is there so folders
sort by lifecycle stage rather than alphabetically, and for no other reason.

**That structure is test material, not a requirement of the agent, and it is not
proposed to whoever adopts it.** The agents walk the folder recursively and are told to
propose a structure when there is none, never to impose one.

Because a `Proyecto` holds its documents as data and only reaches disk at the end, the
same declaration can be written out four ways:

| Layout | What it looks like |
|---|---|
| `referencia` | the numbered folders above |
| `plana` | every document in the project's folder, no subfolders |
| `revuelta` | folders named the way a person names them — with spaces, an accent, one level deeper, and some documents loose at the project root |
| `sin_carpeta` | no project has a folder of its own; everything sits together |

`disposiciones.py` emits Vera's corpus in all four and checks `index()` finds the same
documents with the same content hashes in each. That promise — *«it works with whatever
is there»* — is on all six agent pages and had no check behind it: all three corpora
used the same tidy tree, so a regression that made the walk depend on the structure
would have passed every gate green. What it still does **not** prove is that the model
groups documents into projects correctly when no folder groups them; that is
extraction, and it stays on the list of what has not been tested.

`grade.py` has two modes. With no arguments it grades the **arithmetic**: it runs `compute`
over the reference records and checks every planted finding appears, that none appears that
was not declared, and that the numbers match. With `--fichas <dir>` it grades the
**extraction**: it compares, field by field, the records a model produced from `input/`
against the reference. The second mode needs the plugin running in a real session.

The reference records live under `expected/`, not `input/`, on purpose: they are an answer,
not an input.

## The bar

A plugin is not released until the acceptance criteria at the end of its own `DISENO.es.md` pass over this material, and the result of that run is published with the release.

For `criterio-pmo` the input is a project documentation folder built to contain the failures a real one contains: a milestone that passed with no evidence, a project that has been silent for weeks, minutes naming a sponsor different from the charter, a dependency one plan declares and the other ignores, a commitment promised three times.

A grader that only checks the report was produced is not a grader. It checks that every planted finding was found, and that nothing was invented: a sample of statements is traced back to the document that supports them.
