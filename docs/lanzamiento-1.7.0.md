# Criterio · catalogue 1.7.0 · 30 October 2026

The CFO and the CLO add **Argentina, Panama, Guatemala and Costa Rica**: the CFO moves to 1.1.0 and the CLO to 1.2.0, both stable. Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| Country | CFO · the electronic invoice | CLO · public procurement |
|---|---|---|
| **Argentina** | The ARCA voucher with its CAE (F-24) | The 10 % performance guarantee, lodged within five business days (Decree 1030/2016, arts. 77 and 78) |
| **Panama** | The DGI electronic invoice with its CUFE (F-27) | The performance bond, required in awards above B/.50,000 (Law 22, art. 123) |
| **Guatemala** | The SAT FEL with its authorization number (F-30) | Each counterparty's identification. **No public entity**: Law 57-92 leaves the guarantee percentage to its regulation, which is not among the verified sources |
| **Costa Rica** | The Hacienda 4.4 voucher with its fifty-position key (F-34), the 13 % VAT (F-35) and the IFRS profile (F-36) | The performance guarantee between 5 % and 10 % of the awarded amount (Law 9986, art. 44) |

Each country brings three test entities, one of them a control with no seeded defects. Argentina, Panama and Costa Rica also bring a public entity in the CLO.

## How it was tested

One round per country with the agents, over every entity in the material:

| Round | Country | CFO · signals | CFO · fields | CLO · signals | CLO · fields |
|---|---|---|---|---|---|
| 8 | Argentina | 24 of 24 | 25 of 25 | 25 of 25 | 548 of 548 |
| 9 | Panama | 27 of 27 | 24 of 24 | 24 of 24 | 569 of 569 |
| 10 | Guatemala | 24 of 24 | 25 of 25 | 20 of 20 | 396 of 396 |
| 11 | Costa Rica | 25 of 25 | 25 of 25 | 23 of 23 | 569 of 569 |

No extra signal and no defect in any of the four. The material is synthetic and written by the repository. The four rounds do not replace the first use on a real organisation's documents.

## The versions in 1.7.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | 1.0.0 | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | **1.1.0** | Stable | Week of 26 October |
| CLO · Fidel and Constanza | **1.2.0** | Stable | Not launched |
| EA · Ofelia | 1.0.0 | Stable | Week of 26 October |
| CCO · Augusto and Valeria | 0.3.0 | Stable | Not launched |
| CISO · Alexis, Guillermo and Amparo | 0.1.0 | Laboratory | Not launched |
| Rostrum | 1.0.0 | — | — |

This entry releases the CFO and the CLO.

## What comes next

Honduras, in CFO 1.2.0 and CLO 1.3.0. Honduras publishes no electronic invoice schema, so the invoice comes in as a document: the agent extracts its CAI, its authorized range and its issue deadline, and the engine validates them (decision 0024).

## To update

```
/plugin marketplace update criterio
```

Each agent asks you to accept the terms of its version and leaves its receipt in `.criterio/terminos/`.
