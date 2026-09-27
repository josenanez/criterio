# 0004 · Plugin naming

**Date:** 2026-09-18 · **Status:** accepted

## Context

The plugins were working-titled `legal-latam`, `finanzas-latam` and `pmo-latam`, from when the project itself was called LatAm Knowledge Work. The project has since been named **Criterio**, deliberately without a region, because extension beyond Latin America is expected and the region belongs in the jurisdiction packages rather than in the name.

Skill names must also not collide with Anthropic's `legal` and `finance` plugins, which users may still have installed.

## Decision

`criterio-legal`, `criterio-finance`, `criterio-portfolio`.

## Alternatives discarded

**Keep the `-latam` suffix.** Contradicts the naming decision, and would have to be renamed the first time a package outside the region is contributed. Renaming a published plugin breaks every installation.

**Reuse `legal` and `finance`.** Guarantees collision with the upstream plugins.

## Consequences

The brand prefix carries across every plugin and makes the family obvious in a plugin list. The README must still tell users to disable the upstream plugin for the same function, because disabling is about competing skills, not about names.
