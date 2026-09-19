# Acceptance criteria — criterio-legal

What "working" means for this plugin, and the threshold it must hit before release. Verified on the synthetic set in `tests/`, never on real documents.

## 1. Jurisdiction selection

- [ ] With `jurisdictions:` set in the local file, the analysis loads that package and says so in the opening banner.
- [ ] With no `jurisdictions:` set, the skill lists the available packages and asks. It does not guess.
- [ ] With a document governed by a law that has no package, the analysis **declares the gap** and applies only the regional baseline.
- [ ] No output in any of the above cases cites GDPR, CCPA, HIPAA, SOX, FCPA or US state law unless the document itself is governed by that law.

## 2. Substantive reasoning

- [ ] A liability cap written in absolute terms is reported *and* flagged as not reaching wilful misconduct or gross negligence.
- [ ] A distribution agreement with agency features is flagged for the termination payment.
- [ ] A post-termination non-compete on an employee is flagged as ineffective, not as a negotiation point.
- [ ] A clause assigning "all rights, moral and economic" is reported as ineffective in its moral part.
- [ ] An amendment that changes term or value overrides the main agreement, and the citation points at the amendment.

## 3. Traceability

- [ ] Every extracted data point carries a citation to the source document, or declares `not_found`.
- [ ] Every statement of law carries the rule id it came from.
- [ ] Rules with `confidence: verify` that fired in the run are listed in the output.

## 4. Terms and acceptance

- [ ] With no acceptance recorded, the skill shows the short disclaimer and does not produce a full analysis.
- [ ] Every generated report carries the footer: version, packages applied with status and review date, rules marked verify, link to the terms.
- [ ] A stale package is flagged in the opening banner.

## 5. Threshold

- [ ] 100% on critical fields of the synthetic set (parties, governing law, term, renewal, notice period, value).
- [ ] 90% or better on general fields.
- [ ] Zero differences against the expected alert list.
- [ ] With three typical errors injected, the grader detects all three and blocks.
