# Criterio · catalogue 2.0.0 · 5 November 2026

All six families are now launched: the CLO, the CCO and the CISO join the PMO, the CFO and the EA. The
CCO and the CISO launch stable, so they open their 1.0.0 (decision 0021). Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| | |
|---|---|
| **Criterio CLO (1.4.0), launched** | Fidel, contracts, and Constanza, compliance, tested in 12 countries, with public procurement where its rule has a source |
| **Criterio CCO (1.0.0), launched** | Augusto, the forecast, and Valeria, from sale to invoice, with the Salesforce, HubSpot, Microsoft Dynamics and Zoho exports |
| **Criterio CISO (1.0.0), launched** | Alexis, governance and controls; Guillermo, vulnerabilities, with Tenable and Microsoft Defender; and Amparo, response and recovery |

## How it was tested

| Family | Rounds | Signals | Extracted fields |
|---|---|---|---|
| CLO | 2 to 13 | 262, with a floor of 98.5 % | 6,367, with a floor of 99.8 % |
| CCO | 1 and 2 | 197, with a floor of 98.0 % | 75, with a floor of 95.1 % |
| CISO | 1 and 2 | 148, with a floor of 97.4 % | 80, with a floor of 95.4 % |

The floor is the lower bound of the 95 % confidence interval. The material is synthetic and written by
the repository; the rounds do not replace the first use on a real organisation's documents.

## The versions in 2.0.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | **1.0.2** | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | **1.3.0** | Stable | Week of 26 October |
| CLO · Fidel and Constanza | **1.4.0** | Stable | Week of 5 November |
| EA · Ofelia | **1.0.2** | Stable | Week of 26 October |
| CCO · Augusto and Valeria | **1.0.0** | Stable | Week of 5 November |
| CISO · Alexis, Guillermo and Amparo | **1.0.0** | Stable | Week of 5 November |
| Rostrum | **1.0.2** | — | — |

## To update

```
/plugin marketplace update criterio
```

Each agent asks you to accept the terms of its version and leaves its receipt in `.criterio/terminos/`.
