# 0005 · Scope narrowed to project management; the jurisdiction layer is removed

**Date:** 2026-09-18 · **Status:** accepted · **Supersedes in part:** 0002, 0003

## Context

The project started with two lines of work under one repository: a normative line — adapting Anthropic's legal and finance plugins to reason with South American law, through per-country rule packages — and a project-management line, which had no upstream equivalent.

Work on the normative line produced a package for one country with 43 rules, a validator for it, and the documentation around it. None of those rules had been checked against the published text of the norms they cited; twenty-one carried `confidence: verify`.

In practice the two lines competed for attention and made the scope illegible: every status report mixed them, and work kept surfacing that nobody had asked for.

## Decision

**The scope is project management: `criterio-portfolio`, and `criterio-project` when it is built.**

The jurisdiction layer is removed from the repository: the country packages, their validator, their CI job, and the sections of the project documents that described how to contribute a country.

`criterio-legal` and `criterio-finance` stay declared in the marketplace with their acceptance criteria. They have no content, and nothing is built for them until the scope is deliberately widened again.

## Alternatives discarded

**Keep the rules and mark them as draft.** They were written without checking them against source. Unverified normative content published under the maintainer's name is the project's largest reputational exposure, and it was carrying that exposure for a line of work that was not being built.

**Keep the scaffolding without the content.** Structure with nothing in it still has to be maintained, still appears in every status report, and still invites the question of when it will be filled.

## Consequences

The repository is coherent: one marketplace, one plugin that works, two declared and empty.

What survives from the earlier decisions:

- **0002** — its rule holds in narrowed form: structure, file names and field names in English; the body of a skill in the language of its users.
- **0003** — its principle holds: release with an explicit disclaimer and recorded acceptance, claim no certification, and never use the words *verified*, *certified* or *approved* about anything here.
- **0001** and **0004** stand as the record of decisions taken for the legal and finance plugins, which remain declared.

Widening the scope again is a decision that needs its own ADR, not a conversation.
