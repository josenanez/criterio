# Test material

Synthetic documentation with known answers, and the graders that score a run against it.

Nothing here is real. No client document, no employer data, no personal data, anonymised or not. Every file was built from scratch for testing. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Layout

```
tests/
└── <plugin>/
    ├── input/       the synthetic folder a command is pointed at
    ├── expected/    the known answers
    └── grade.py     scores a run against them
```

## The bar

A plugin is not released until its own `ACCEPTANCE.md` passes over this material, and the result of that run is published with the release.

For `criterio-pmo` the input is a project documentation folder built to contain the failures a real one contains: a milestone that passed with no evidence, a project that has been silent for weeks, minutes naming a sponsor different from the charter, a dependency one plan declares and the other ignores, a commitment promised three times.

A grader that only checks the report was produced is not a grader. It checks that every planted finding was found, and that nothing was invented: a sample of statements is traced back to the document that supports them.
