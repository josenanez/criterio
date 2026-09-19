# 0002 · English field names, jurisdiction language for content

**Date:** 2026-09-18 · **Status:** accepted

## Context

The repository holds three kinds of text with different readers: the structure (paths, field names, scripts, project documents), read by contributors and by GitHub; the normative content (what the norm says, what signal to look for, what to state), read by the model producing an analysis for a local professional; and the output, always in the language of the jurisdiction.

The project deliberately carries no region in its name, and extension beyond Latin America is expected.

## Decision

**English for the structure. The language of the jurisdiction for rule content.** `country: co`, `signal: cláusula que exonera de "toda" responsabilidad`.

## Alternatives discarded

**Everything in Spanish.** Consistent for the current contributor base, but a repository with `paises/` and `señal:` reads as a regional project rather than infrastructure that covers South America first. It also walls out Brazil and anywhere beyond the region, and ties the validator to one language.

**Everything in English, including rule text.** `culpa grave` is not `gross negligence`; `otrosí`, `agencia comercial` and `cesantía comercial` have no clean equivalents. Translating the rules imports the common-law reasoning this project exists to remove, and the analysis has to be read by a lawyer in the local language anyway.

## Consequences

The validator is language agnostic and the same schema serves a European package without renaming anything. A contributing lawyer meets nine English field names, documented once in the template — acceptable friction.

Project documents are maintained in English with a Spanish version alongside. `DISCLAIMER` and `TERMS` are maintained in both because they are what users accept.
