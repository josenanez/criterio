# Acceptance criteria — criterio-pmo

Verified on a synthetic documentation folder in `tests/`, built to contain the failures a real one contains.

## 1. Coverage

- [ ] Every document in the folder is either read or listed as unreadable with a reason. Nothing is silently skipped.
- [ ] Documents in mixed formats and mixed languages are handled, or declared.
- [ ] A project mentioned only inside another project's minutes is still surfaced.

## 2. Findings that must appear

- [ ] A project whose reported status contradicts its own dates.
- [ ] A project with no identifiable owner.
- [ ] A project with no update in the last quarter.
- [ ] Two documents that state different dates for the same milestone.
- [ ] A dependency named in one plan and absent from the plan it depends on.
- [ ] A project reporting green with at least one signal that green does not account for, listed by signal, and counted at portfolio level.
- [ ] A vendor deliverable past its date with no evidence of delivery, and an invoice declared against a vendor with no accepted deliverable.
- [ ] A rebaseline that moved more days than the approved changes authorised, reported as a documentation gap and not as an accusation.
- [ ] A change impact stated in months reported as unreadable rather than converted into a number.

## 3. Traceability

- [ ] Every statement in the portfolio report cites the document and the location it came from.
- [ ] No status is asserted that no document supports. "Not stated anywhere" is a valid and expected finding.

## 4. Terms and acceptance

- [ ] Same four layers as every plugin: gate, footer, banner, terms file.

## 5. Threshold

- [ ] Every planted finding is detected.
- [ ] Zero invented projects, dates or owners, checked by tracing a sample of statements back to source.
