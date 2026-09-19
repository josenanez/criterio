# criterio-legal

Planned fork of Anthropic's `legal` plugin, with the law separated out of the skills and held in per-jurisdiction packages.

**Status:** declared, not built. No content, and no jurisdiction packages exist in this repository. Nothing is built here until the scope is deliberately widened — see [ADR 0005](../../docs/decisions/0005-scope-pmo-only.md).

## What changes relative to the upstream plugin

| Skill | Upstream | Here |
|---|---|---|
| review-contract | Common law: consequential damages, work-for-hire, indemnities | Civil law: exclusions void for wilful misconduct and gross negligence, reducible penalty clauses, inalienable moral rights, commercial agency, interest ceilings, solemn contracts, amendments |
| triage-nda | US NDA criteria | Enforceability of non-compete and non-solicitation under local employment and competition law |
| compliance-check | GDPR, CCPA, HIPAA, DPA art. 28 | Local data protection statute and authority, consent as the general basis, cross-border transfer, database registration, incident reporting |
| legal-response | DSR, litigation hold, subpoena templates in English | Local templates: habeas data, document preservation under local procedure, responses to supervisors and prosecutors |
| brief | Attorney-client privilege, litigation hold | Professional secrecy, notification to the data authority and the sector supervisor |
| legal-risk-assessment | FCPA, escalation to outside counsel | Local anti-bribery regime, administrative liability of the legal person, money laundering controls |
| signature-request | DocuSign, Adobe Sign | Validity of electronic and digital signature, documents that require a notarial deed |
| vendor-check | NDA, MSA, DPA | Local agreements, restricted lists, tax registration and legal existence |
| meeting-briefing | Privilege | Professional secrecy |
| — | One jurisdiction, English | Jurisdiction selector, Spanish output, Portuguese for Brazil |

## Acceptance criteria

See [ACCEPTANCE.md](ACCEPTANCE.md). Nothing ships until they pass.
