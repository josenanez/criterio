# Criterio · catalogue 1.2.0 · 29 October 2026

The EA family opens its 1.0.0: it has been launched since the week of 26 October and its round 2 left it stable. The CSO family moves to its 0.2.0 with its first round with the agents, as a laboratory version. Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| | |
|---|---|
| **EA 1.0.0 · Ofelia** | Travel: each flight in the itinerary against the calendar, with three new signals, the flight missing from the calendar, the meeting that falls during a flight and the in-person meeting in the executive's home city while they are travelling. The calendar as Outlook exports it —time zones with their Windows name and its own «free» status— and as Google Calendar does —the calendar's time zone and a cancelled occurrence of a series—, and Outlook's .msg email |
| **The EA's round 2** | Ofelia on the four offices, each with its provider: 85 of 85 seeded signals, none extra, and 144 of 146 data points on the first run. The two data points that failed were explained by the material, which was fixed and verified: 51 of 51 and 45 of 45. The lower bound of the 95% margin is 95.6% for signals and 97.4% for data |
| **CSO 0.2.0 · Augusto and Valeria** | The first round with the agents, on the material's six entities, from Colombia and Mexico, with Salesforce, HubSpot and generic exports: 72 of 80 signals on the first run, and 80 of 80 with none extra after verifying the three fixes. It stays laboratory: 30 data points are graded, and a 95% floor needs 73 or more |
| **Outlook's .msg in every family** | Email saved from Outlook is processed like an .eml, with no dependencies: what used to be declared as not processed now comes in |

## The versions in 1.2.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | 1.0.0 | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | 0.12.1 | Stable | Week of 26 October |
| CLO · Fidel and Constanza | 0.12.1 | Stable | Not launched |
| EA · Ofelia | **1.0.0** | Stable | Week of 26 October |
| CSO · Augusto and Valeria | **0.2.0** | Laboratory | Not launched |
| Rostrum | 1.0.0 | — | — |

This entry releases the EA and the CSO.

## If you already have it installed

Update `criterio-assistant`, `criterio-sales` and `criterio-revenue`. Each agent asks you to accept the terms of its new version and leaves its receipt in `.criterio/terminos/`. With HubSpot, the CSO configuration now asks for the associated-company column.
