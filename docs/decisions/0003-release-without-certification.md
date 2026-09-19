# 0003 · Release without professional certification, with explicit acceptance

**Date:** 2026-09-18 · **Status:** accepted

## Context

An earlier draft of the governance made a package's `Reviewed` state depend on a licensed professional in that country signing each rule. That puts a lawyer and an accountant per country on the critical path of every release, for an open-source project with no budget, and it makes the launch hostage to eleven favours.

It also overstates what such a signature would mean. A lawyer reading a markdown file is not issuing a legal opinion, and presenting it as certification would be less honest than not having one.

## Decision

Design, build and release based on the law of each country, **with an explicit and unmissable disclaimer**, and record acceptance of the terms by whoever deploys or runs it. No professional certification is claimed or required.

Quality is held up by traceability instead: norm and article on every rule, a declared confidence level, a review date, and automatic surfacing of anything uncertain or stale at run time.

Each plugin is verified on its own terms, with its own acceptance criteria and its own graded test set. There is no single project-wide bar.

## Alternatives discarded

**Wait for a professional signature per country.** Blocks the launch, does not scale past Colombia, and claims more assurance than a markdown review provides.

**Ship with a disclaimer file and nothing else.** Nobody reads it. Without a gate and a footer on the output, the warning never reaches the person who receives the document.

## Consequences

Four acceptance layers must be implemented by every skill in every plugin: a gate in the local configuration, a footer on every generated report, a banner at the start of each run, and the terms file itself. Specified in [`docs/acceptance.md`](../acceptance.md).

The words *verified*, *certified* and *approved* are never used about content in this repository. Contributors are credited as authors, which records who wrote something rather than warranting it.

The project carries reputational exposure that a certification model would have transferred. That is accepted knowingly, and it is why the confidence levels must be honest.
