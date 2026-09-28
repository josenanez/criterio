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

## The problem it will attack

**What it is.** The function that answers for what the company signed. Its components are contract review, the repository of what was executed, tracking obligations and expiries, regulatory compliance and disputes.

**What it costs today**

| Figure | Source |
|---|---|
| Poor contract management erodes an average of **8.6% of contract value** — 3% for the best, over 20% for the worst | [World Commerce & Contracting with Deloitte, 2023](https://info.worldcc.com/roi) — 1,236 organisations |
| Contracting teams spend **over 40% of their time and budget** on low-complexity contracts | [EY with Harvard Law School, 2021](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) — 1,000 professionals, 22 countries |
| A large organisation handles **19,000 contracts a year**, and **90% have difficulty locating their own** | EY / Harvard Law School, 2021 |
| Only **27%** keep all their executed contracts in a single repository | [Sirion and World Commerce & Contracting, 2026](https://www.sirion.ai/press/trusted-contract-data-world-cc-research-report/) — 170 companies |

A company that cannot find its own contracts cannot know what it signed, what expires, or what it committed to.

→ CLO Agent: capability declared, not built

---

The list is not closed. **A capability joins when someone who practises it wants to build its agent.**

---

## Acceptance criteria

See [ACCEPTANCE.md](ACCEPTANCE.md). Nothing ships until they pass.
