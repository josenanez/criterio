# Criterio · catalogue 1.8.0 · 30 October 2026

Honduras joins the CFO and the CLO; the CISO has its first round with the agents; and every agent
can share its findings, always asking. Open source under Apache 2.0.

**The catalogue number only orders the entries of the version register.** Each family carries its own version.

## What it brings

| | |
|---|---|
| **Honduras in the CFO (1.2.0)** | Honduras publishes no electronic invoice schema, so the invoice comes in as a document (decision 0024): the agent extracts from each PDF the CAI, the authorized range, the issue deadline and the sequential number, and the engine validates them against Agreement 481-2017 (F-37) and the 15 % sales tax (F-38). A new signal, `invoice_outside_authorization`: a received invoice outside its authorized range or issued after its deadline does not support the sales-tax credit |
| **Honduras in the CLO (1.3.0)** | The 15 % performance guarantee of the State Procurement Law (Decree 74-2001, art. 100), with contracts published in HonduCompras (F-14) |
| **The CISO, with its round (0.2.0)** | Alexis, Guillermo and Amparo on the six entities of the material: 100 of 100 signals and none extra. It stays in laboratory: the 48 extracted fields give a floor of 92.5 %, below 95 % |
| **Sharing findings (decision 0025)** | `/criterio-<plugin>:share-findings` in every agent —`/criterio-finance:share-findings` for Clara—: a summary with no data of what ran, built by the code from the local trail; always the question, and with a yes, the link to the finding template, which the person opens. Nothing is sent |
| **What the rounds fixed** | Document conversion no longer copies a credential the engine excludes (CISO-4); CCO and CISO runs leave their trail for Rostrum (CISO-2); `cuentas` proposes Honduras's accounts from the record (CFO-12) |

## How it was tested

| Round | | Signals | Fields |
|---|---|---|---|
| CFO · 12 | Honduras: banking, retail and control | 27 of 27 | 625 of 625 |
| CLO · 12 | Honduras: banking, retail, control and a public entity | 22 of 22 | 569 of 569 |
| CISO · 1 | Banking, retail, healthcare, technology and two controls | 100 of 100 | 48 of 48, with CISO-1 (the harness) and CISO-3 (the instructions) fixed and verified |

No extra signal. The material is synthetic and written by the repository; the rounds do not replace the
first use on a real organisation's documents.

## The versions in 1.8.0

| Family | Version | Quality | Launch |
|---|---|---|---|
| PMO · Vera, Samuel and Alba | **1.0.1** | Stable | Week of 19 October |
| CFO · Clara, Tomás and Áurea | **1.2.0** | Stable | Week of 26 October |
| CLO · Fidel and Constanza | **1.3.0** | Stable | Not launched |
| EA · Ofelia | **1.0.1** | Stable | Week of 26 October |
| CCO · Augusto and Valeria | **0.3.1** | Stable | Not launched |
| CISO · Alexis, Guillermo and Amparo | **0.2.0** | Laboratory | Not launched |
| Rostrum | **1.0.1** | — | — |

All of them move up: `share-findings` reaches every agent. The CFO and the CLO add Honduras, and the CISO its round.

## To update

```
/plugin marketplace update criterio
```

Each agent asks you to accept the terms of its version and leaves its receipt in `.criterio/terminos/`.
