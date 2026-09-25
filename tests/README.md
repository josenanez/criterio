# Test material

Synthetic documentation with known answers, and the graders that score a run against it.

Nothing here is real. No client document, no employer data, no personal data, anonymised or not. Every file was built from scratch for testing. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Layout

```
tests/
├── coherencia.py        checks the documentation and the code say the same thing
└── <plugin>/
    ├── generar.py       builds input/ and expected/ from one declarative source
    ├── input/           the synthetic folder a command is pointed at
    ├── expected/
    │   ├── fichas/      the reference extraction: what a correct read of input/ produces
    │   └── hallazgos.json   the known answers, written by hand
    ├── grade.py         scores a run against them
    └── EVIDENCIA.md     what was run, what it proves, what it does not
```

`grade.py` has two modes. With no arguments it grades the **arithmetic**: it runs `compute`
over the reference records and checks every planted finding appears, that none appears that
was not declared, and that the numbers match. With `--fichas <dir>` it grades the
**extraction**: it compares, field by field, the records a model produced from `input/`
against the reference. The second mode needs the plugin running in a real session.

The reference records live under `expected/`, not `input/`, on purpose: they are an answer,
not an input.

## The bar

A plugin is not released until its own `ACCEPTANCE.md` passes over this material, and the result of that run is published with the release.

For `criterio-pmo` the input is a project documentation folder built to contain the failures a real one contains: a milestone that passed with no evidence, a project that has been silent for weeks, minutes naming a sponsor different from the charter, a dependency one plan declares and the other ignores, a commitment promised three times.

A grader that only checks the report was produced is not a grader. It checks that every planted finding was found, and that nothing was invented: a sample of statements is traced back to the document that supports them.
