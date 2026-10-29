# Criterio · catalogue 1.1.0 · 29 October 2026

The PMO family opens its 1.0.0: it has been launched since the week of 19 October and it is stable, and a launched, stable family moves to 1.0.0 in its next version (decision 0021). Rostrum, the server for every family, moves to its 1.0.0 with it. Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** It goes to 1.1.0 because it is the entry after 1.0.0. Each family carries its own version.

## What it brings

| | |
|---|---|
| **PMO 1.0.0** | Two new industries, telecommunications and logistics, tested with all 38 commands of Vera, Samuel, Alba and Rostrum: 38 of 38 contracts kept in each, Vera 119 of 119 signals and none extra, Samuel 52 of 52 commitments, Alba 61 of 61 alerts. The family is now tested in eight industries |
| **The PMO is measured like the other families** | Its quality comes from each industry's latest run, whatever round it came from: the six earlier industries with their round 11 run and the two new ones with round 12. Over 500 signals, the lower bound of Vera's 95% margin is 99.2% for precision and for coverage; Samuel, 98.2%; Alba, 98.5% |
| **Rostrum 1.0.0 · the schedule** | On every project page, the Gantt of each approved baseline against the current plan, each milestone with its baseline date, its current date and its status in words, and the progress curve by milestones with the declared progress as a separate point. The engine calculates the schedule and the report only draws it, with the same information in a table |
| **The schedule, tested in all eight industries** | `tests/cronograma.py` draws every project from the records the agents wrote in each industry's latest run, without running any agent: 104 projects, 130 baselines and 365 milestones, and no difference between what is drawn and what is calculated. It is a gate in `scripts/verificar.py`. Rostrum passed 1,072 of 1,072 checks in round 12 |

## The versions in 1.1.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | **1.0.0** | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | 0.12.1 | Stable | Week of 26 October |
| CLO · Fidel and Constanza | 0.12.1 | Stable | Not launched |
| EA · Ofelia | 0.12.1 | Laboratory | Week of 26 October |
| CSO · Augusto and Valeria | 0.1.0 | Laboratory | Not launched |
| Rostrum | **1.0.0** | — | — |

This entry releases the PMO and Rostrum.

## If you already have it installed

Update `criterio-portfolio`, `criterio-project`, `criterio-product` and `criterio-server`. Each agent asks you to accept the terms of its new version and leaves its receipt in `.criterio/terminos/`. The records you already have work as they are: the schedule is calculated from them.
