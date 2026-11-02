# Criterio · catalogue 1.9.0 · 2 November 2026

Paraguay joins the CFO and the CLO; the CISO reads Tenable and Microsoft Defender exports and becomes
stable with its second round; and Rostrum says when it leaves signals out as private. Open source under
Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| | |
|---|---|
| **Paraguay in the CFO (1.3.0)** | The reader of the SIFEN electronic document by its forty-four-character CDC, with the fields of the DNIT's Technical Manual 150 (F-40) and the SET's XSD schema 150 (F-41). VAT is taken from the document at any of its rates, 10 % and 5 % (E734). A received invoice issued before its timbrado's validity starts, which SIFEN rejects (validation 1103), raises `invoice_outside_authorization`, no longer Honduras's alone. Each entity's accounting framework comes from Paraguay's IFRS profile (F-42) |
| **Paraguay in the CLO (1.4.0)** | Banking, retail and control, with no public entity: the guarantee rule of Paraguay's public procurement law is not among the verified sources |
| **The CISO, with its scanners (0.3.0)** | Guillermo reads the Tenable Vulnerability Management export in CSV (F-08) and the Microsoft Defender Vulnerability Management export in JSON, compressed too (F-09), each from its vendor's documentation. What a Defender export does not prove —asset coverage— he states as not processed, not as a finding. With the second round, the family becomes stable |
| **Rostrum (1.0.2)** | A family page no longer says «No open signals» for an agent whose signals are not published: it says there are some outside the portal and which configuration opens them, without saying how many or which (Guillermo, `vulnerability.publish`) |
| **The countries tested** | The CFO and CLO READMEs carry a table of each country with its entities, rounds, signals and fields, and the country's own rule with its source; the code writes it from the rounds' evidence |

## How it was tested

| Round | | Signals | Fields |
|---|---|---|---|
| CFO · 13 | Paraguay: banking, retail and control | 28 of 28 | 24 of 24 |
| CLO · 13 | Paraguay: banking, retail and control | 20 of 20 | 396 of 396 |
| CISO · 2 | Energy in Peru with Tenable, insurance in Chile with Defender and a control in each country | 48 of 48 | 32 of 32 |

No extra signal and no new defect. With its two rounds, the CISO adds up to 80 extracted fields and a
floor of 95.4 %. The material is synthetic and written by the repository; the rounds do not replace the
first use on a real organisation's documents.

## The versions in 1.9.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | **1.0.2** | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | **1.3.0** | Stable | Week of 26 October |
| CLO · Fidel and Constanza | **1.4.0** | Stable | Not launched |
| EA · Ofelia | **1.0.2** | Stable | Week of 26 October |
| CCO · Augusto and Valeria | **0.3.2** | Stable | Not launched |
| CISO · Alexis, Guillermo and Amparo | **0.3.0** | Stable | Not launched |
| Rostrum | **1.0.2** | — | — |

All of them move up: the country register, which every agent carries, adds Paraguay. The CFO and the CLO add Paraguay, the CISO its scanners and Rostrum its fix.

## To update

```
/plugin marketplace update criterio
```

Each agent asks you to accept the terms of its version and leaves its receipt in `.criterio/terminos/`.
