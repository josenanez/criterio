# Criterio · catalogue 1.0.0 · 28 October 2026

The CSO family, the sales function, enters the marketplace in its version 0.1.0, as a laboratory version not yet launched. And from this entry on, three things about each family are said separately: its stage, by the code; its quality, laboratory or stable, by the evidence; and its launch, by a date (decisions 0020 and 0021). Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** It goes to 1.0.0 because, after 0.12, the next whole number comes (decision 0020). It says nothing about any family: each one carries its own version.

## What it brings

| | |
|---|---|
| **CSO 0.1.0** | Augusto, the forecast, and Valeria, from the sale to the invoice: twelve commands, their skills and the engine, with the nine signals. Salesforce and HubSpot exports, and any CSV or Excel with its column mapping. The engine passes its deterministic test against the key of all its material, six entities from Colombia and Mexico with their controls. The round with the agents comes in 0.2.0 |
| **Laboratory or stable** | Said by the evidence, not by the number: the lower bound of the 95% margin at 95% or more, for signals and for data, over the latest run of each entity in the material, and no control raising a signal. `scripts/calidad.py` calculates it and the register records it in this entry |
| **Ten versions per whole number** | From x.0 to x.9, then x+1.0. Fixes do not count among the ten. 0.10, 0.11 and 0.12 are the only exceptions |
| **Published from the first version, launched on a date** | A family enters the marketplace and the portal with its first release; it is marked «Runs today» the week of its launch. A launched family moves to 1.0.0 in its first stable version |

## The versions in 1.0.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | 0.12.1 | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | 0.12.1 | Stable | Week of 26 October |
| CLO · Fidel and Constanza | 0.12.1 | Stable | Not yet launched |
| EA · Ofelia | 0.12.1 | Laboratory | Not yet launched |
| CSO · Augusto and Valeria | 0.1.0 | Laboratory | Not yet launched |
| Rostrum | 0.12.1 | — | — |

Only the CSO is released in this entry. The next version of the PMO, the CFO, the CLO, the EA and Rostrum is their 1.0.0.

## If you already have it installed

Nothing changes for the families you already use: their version and their terms are the same. To try the CSO, install `criterio-sales` or `criterio-revenue`; each agent asks you to accept the terms and leaves its receipt in `.criterio/terminos/`.
