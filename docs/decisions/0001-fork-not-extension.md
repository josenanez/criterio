# 0001 · Fork, not extension

**Date:** 2026-09-18 · **Status:** accepted

## Context

Anthropic's `knowledge-work-plugins` are Apache 2.0 and their method is sound. Their normative content is not: GDPR, CCPA, HIPAA, SOX, US GAAP, FCPA, Delaware and New York law are written **inside the text of the skills**, not in configuration.

A file-by-file review of the `legal` plugin (14 files: manifest, `.mcp.json`, CONNECTORS.md, LICENSE, README and 9 SKILL.md) found no executable code. Everything is markdown instructions. Inside those skills two different things live together:

| What | Where | Configurable? |
|---|---|---|
| Positions (liability caps, NDA criteria, templates) | `legal.local.md` | Yes, but only 3 skills read it |
| Law (GDPR, CCPA, DPA art. 28, FCPA, litigation hold, privilege, DocuSign flow) | Inside the skill text | No |
| Common-law reasoning (consequential damages, work-for-hire, non-compete) | Inside review-contract and triage-nda | No |
| Default behaviour with no playbook | Generic "commercial standards" | No |

Changing configuration localises 3 of 9 skills. The other 6, and the substantive legal reasoning, keep reasoning under US and EU law.

## Decision

Fork the plugins and modify them, rather than shipping a second plugin alongside the originals.

## Alternatives discarded

**A companion plugin installed next to the original.** Both would declare skills for the same task and compete for it, and the US content would still load. The user would get a blend of two jurisdictions with no way to tell which produced a given statement.

**Configuration only.** Covers a third of the skills. Silently leaves the rest wrong, which is worse than being obviously wrong.

## Consequences

Automatic upstream updates are lost. Mitigated by keeping the upstream repository as a reference and reviewing each release. Because the law is separated from the method, pulling a method improvement across is a bounded exercise.

Skill names must differ from the originals to avoid collision, and the README must tell users to disable the original plugin for the same function.
