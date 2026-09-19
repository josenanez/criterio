# Contributing

[Español](CONTRIBUTING.es.md)

## Before you start

Read [TERMS.md](TERMS.md). Contributions are licensed under Apache 2.0 by the act of submitting them, and by contributing you state that the content is yours to submit and contains no client or confidential material.

Open an issue first describing what you want to change, so two people do not write the same thing twice.

## The shape of the work

A plugin is markdown. There is no executable code in a skill or a command — only instructions — so a contribution is a text change that must survive being read literally by a model.

- **Skills are nouns.** Knowledge and frameworks the model loads on its own when the topic appears. A skill's `description` is what triggers it; write it with the words a user would actually type.
- **Commands are verbs.** Workflows the user invokes. They chain skills.
- **A command may only reference skills of its own plugin.** Plugins install independently; a cross-plugin reference breaks.
- A skill's `name` must match its directory name.
- Keep front matter lean — it is always loaded. Detail goes in the body, which loads only when the skill triggers.

## What makes a good contribution

The test is simple: **what would the output say differently because of this change?** If the answer is nothing, it is background reading, not a contribution.

Three shapes that do not work:

- *"Portfolio management is about delivering value."* True, changes nothing.
- *"Consider consulting a specialist."* Advice to the reader, not an instruction for the analysis.
- A three-paragraph framework transcribed from a book. Name it and say when to apply it.

And the shape that works: a concrete signal to look for in the material, what it means, and what the analysis must then state.

## The rules that are not negotiable

**Arithmetic goes in code.** If an instruction asks the model to compute days, percentages, projections or balances, it is in the wrong place. The model extracts; the script computes.

**Every statement carries its citation.** An output that asserts something no document supports is the failure this project exists to avoid. "Not stated anywhere" is a valid finding.

**No invented data.** Not a name, not a date, not a figure, not an owner. Where the material is silent, the output says so.

**Never write a figure that changes.** Thresholds and rates go in configuration, not in prose.

## Before opening the pull request

- [ ] `python3 scripts/validate_plugins.py` passes with no errors.
- [ ] A skill's name matches its directory; a command has `description` and `argument-hint`.
- [ ] The plugin README lists whatever you added — the validator checks this.
- [ ] Test material under `tests/` covers the new behaviour, and the grader catches it when it regresses.
- [ ] No real data from any company, client or person. Test material is synthetic, built from scratch. Do not anonymise a real document: anonymisation fails.
