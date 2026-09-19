# Acceptance criteria — criterio-finance

Verified on a synthetic close in `tests/`, never on real books.

## 1. Jurisdiction selection

- [ ] The analysis states which finance package it loaded, its status and its review date.
- [ ] No output applies US GAAP terminology to an entity under a local IFRS framework.
- [ ] With no package for the entity's country, the analysis declares the gap instead of defaulting.

## 2. Substantive reasoning

- [ ] The entity's accounting group is established or asked for before any opinion on a treatment.
- [ ] Invoices with no evidence of authority validation are reported as findings, with the effect on deductibility stated.
- [ ] Expenses with no invoice and no supporting document are listed with their accumulated amount.
- [ ] Payments to foreign service providers are flagged for indirect tax treatment.
- [ ] Working papers with thresholds in local currency and no reference year are flagged.
- [ ] No output states a tax unit value, a rate or a filing date from memory.

## 3. Traceability

- [ ] Every finding cites the account, the document or the entry it came from.
- [ ] Every statement of obligation carries the rule id it came from.
- [ ] Rules with `confidence: verify` that fired in the run are listed in the output.

## 4. Terms and acceptance

- [ ] Same four layers as every plugin: gate, footer, banner, terms file.

## 5. Threshold

- [ ] Every planted finding in the synthetic close is detected.
- [ ] No fabricated figures: a spot check of ten numeric statements traces each one to a source row.
