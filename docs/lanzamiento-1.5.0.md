# Criterio · catalogue 1.5.0 · 30 October 2026

The CLO family moves to its 1.1.0 with public contracts. When the entity is public, Fidel checks each contract against its country's public procurement law: whether it was published on time and whether the performance guarantee meets what the law sets. Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| | |
|---|---|
| **The law, not an opinion** | Each rule comes from the country registry and has its verified source, F-03 to F-10 of the family. The engine compares the contract's record with the rule; it gives no opinion on the contract |
| **Publication** | Colombia: on SECOP, within 3 business days. Chile: direct awards, within 24 hours. Brazil: on PNCP, within 20 business days after a tender or 10 after a direct award |
| **The performance guarantee** | Colombia: at least 10 % of the value. Ecuador: 5 %, from the threshold. Peru: 10 % of the original amount. Chile: 5 %, from the threshold. Brazil: up to 5 %, or up to 10 % if justified. Mexico: delivered within 10 calendar days after signing |
| **CLO 1.1.0 · Fidel** | Round 7, on one public entity per country: 19 of 19 signals, none extra, and 909 of 912 data items. It found two defects: the key (CLO-13) and an instruction in the skill (CLO-14). Both were fixed and verified. With all its rounds, the 95 % margin floor is 97.0 % in signals and 99.7 % in data |

## The versions in 1.5.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | 1.0.0 | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | 1.0.0 | Stable | Week of 26 October |
| CLO · Fidel and Constanza | **1.1.0** | Stable | Not launched |
| EA · Ofelia | 1.0.0 | Stable | Week of 26 October |
| CCO · Augusto and Valeria | 0.3.0 | Stable | Not launched |
| Rostrum | 1.0.0 | — | — |

This entry releases the CLO.

## If you already have it installed

Update `criterio-legal` and `criterio-compliance`. Each agent asks you to accept the terms of its new version and leaves its receipt in `.criterio/terminos/`. If your entity is public, run `/criterio-legal:legal-setup` again: it asks whether it is and, in Ecuador and Chile, the guarantee threshold.
