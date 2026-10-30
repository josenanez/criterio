# Criterio · catalogue 1.6.0 · 30 October 2026

The **CISO · Information security** family comes in, in its laboratory 0.1.0: Alexis, Guillermo and Amparo, ordered by the six functions of the NIST Cybersecurity Framework 2.0. Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| | |
|---|---|
| **Alexis · governance and controls** | The statement of applicability against each control's evidence —the one with none, the one whose evidence lapsed, the one with no owner—, the access reviews and critical third-party assessments that lapsed, and the risk acceptances past their date |
| **Guillermo · vulnerabilities** | Every scanner finding against its severity's deadline in the policy, CISA's KEV catalog (F-06), expired exceptions, closures no scan proves and assets no scan covers. Any export in CSV or Excel, with its mapping; severity from CVSS v4.0 when the scanner only gives the score (F-05) |
| **Amparo · response and recovery** | Every incident against its severity's containment deadline, every notification in the matrix —to the supervisor, the data authority, the customers— against the one that was made, the post-incident review, and the continuity, recovery and restore tests against their calendar |
| **The deadlines are the organisation's** | They come from its policy, matrix and registers, with their citation. The only external one is the date the KEV catalog carries |
| **What is never opened** | Credentials, keys and backups are out by default, and every report says which it excluded. Vulnerability findings are not published in Rostrum unless the configuration says so |
| **CISO 0.1.0** | The engine, tested against synthetic banking, retail, healthcare and technology material with two control entities: 100 of 100 signals and none extra. **Laboratory**: the round with the three agents comes in 0.2.0 |

## The versions in 1.6.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | 1.0.0 | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | 1.0.0 | Stable | Week of 26 October |
| CLO · Fidel and Constanza | 1.1.0 | Stable | Not yet launched |
| EA · Ofelia | 1.0.0 | Stable | Week of 26 October |
| CCO · Augusto and Valeria | 0.3.0 | Stable | Not yet launched |
| CISO · Alexis, Guillermo and Amparo | **0.1.0** | Laboratory | Not yet launched |
| Rostrum | 1.0.0 | — | — |

This entry releases the CISO family.

## To install it

```
/plugin install criterio-security@criterio
/plugin install criterio-vulnerability@criterio
/plugin install criterio-resilience@criterio
```

Each agent asks you to accept the terms of its version and leaves its receipt in `.criterio/terminos/`.
