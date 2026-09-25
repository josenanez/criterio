# Acceptance criteria — criterio-pmo

Verified on a synthetic documentation folder in `tests/`, built to contain the failures a real one contains.

That folder now exists: `tests/criterio-pmo/`, six projects and twenty-six documents, with
the known answers written by hand and a grader over them. The result of the run, including
what it does not cover, is in [`../../tests/criterio-pmo/EVIDENCIA.md`](../../tests/criterio-pmo/EVIDENCIA.md).
The boxes below that the arithmetic can decide are checked against that run; the ones that
depend on how a model reads the folder stay open until the plugin runs in a session.

## 1. Coverage

- [ ] Every document in the folder is either read or listed as unreadable with a reason. Nothing is silently skipped.
- [ ] Documents in mixed formats and mixed languages are handled, or declared.
- [ ] A project mentioned only inside another project's minutes is still surfaced.

## 2. Findings that must appear

- [x] A project whose reported status contradicts its own dates. — PRY-001 and PRY-004
- [ ] A project with no identifiable owner. — the synthetic set has authority missing, not the owner; add a project without one
- [x] A project with no update in the last quarter. — PRY-004, 153 days
- [x] Two documents that state different dates for the same milestone. — PRY-006: the charter says October, the committee minute says January, and nobody updated the plan
- [x] A dependency named in one plan and absent from the plan it depends on. — PRY-001 declares it of PRY-002, unconfirmed
- [x] A project reporting green with at least one signal that green does not account for, listed by signal, and counted at portfolio level. — three of six
- [x] A vendor deliverable past its date with no evidence of delivery. — PRY-003. The invoice case is **not** detected: it needs an amount per deliverable. See limit 1 of the evidence
- [x] A rebaseline that moved more days than the approved changes authorised. — PRY-001, 61 against 60 authorised
- [x] A change impact stated in months reported as unreadable rather than converted into a number. — PRY-006

## 3. Traceability

- [ ] Every statement in the portfolio report cites the document and the location it came from.
- [ ] No status is asserted that no document supports. "Not stated anywhere" is a valid and expected finding.

## 4. Terms and acceptance

- [ ] Same four layers as every plugin: gate, footer, banner, terms file.

## 5. Threshold

- [x] Every planted finding is detected. — 49 checks, no errors
- [x] **A healthy project produces no alert at all.** — PRY-005. This is the criterion that
  decides whether the plugin is usable: an agent that alerts on a sound project is a noise
  generator, and it gets silenced within a month
- [ ] Zero invented projects, dates or owners, checked by tracing a sample of statements back to source.
