# criterio-finance

Fork of Anthropic's `finance` plugin. The upstream closes the month against US GAAP and controls SOX; here the framework is locally adopted IFRS, and electronic invoicing is a first-class concern because it decides deductibility.

**Status:** in design. This is the plugin of **Clara**, the controller of the CFO family, designed for locally adopted IFRS in Colombia and Ecuador, with DIAN and SRI electronic invoicing ([ADR 0006](../../docs/decisions/0006-scope-cfo.md)). The full design, with its commands, signals and folder structure, is in [`families/criterio-cfo/DISENO.es.md`](../../families/criterio-cfo/DISENO.es.md) (Spanish).

## What changes relative to the upstream plugin

| Area | Upstream | Here |
|---|---|---|
| Accounting framework | US GAAP | Locally adopted IFRS, with the entity's group deciding which technical framework applies |
| Close | SOX controls | Book-to-tax reconciliation as a required control, functional currency analysis, inflation adjustment where a country requires it |
| Invoicing | Not covered | Electronic invoicing validated by the tax authority, supporting documents for purchases from non-issuers, electronic payroll, invoices circulating as negotiable instruments |
| Taxes | US federal and state | Withholding at source as a payer obligation, thresholds expressed in an indexed tax unit, VAT on services supplied from abroad |
| Reporting | SEC | Companies supervisor, commercial registry renewal, annual third-party information return |

## The problem it will attack

**What it is.** The function that closes the books and answers for what they say. Its components are the close and consolidation, reconciliations, book-to-tax, reporting to supervisors and audit preparation.

**What it costs today**

<!-- cfo:cifras · generado por scripts/cfo.py; no se edita a mano -->
| Figure | Source |
|---|---|
| **44%** closed the quarter within six working days in 2023, down from 49% in 2019 | [Ventana Research / ISG, investigación Smart Financial Close, 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) — Not stated in the note |
| **45%** of SOX controls are manual in the organisations surveyed; programme hours rose 32% in two years, from 11,800 to 15,580 | [KPMG, SOX Survey, 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — About 150 SOX professionals |
| **18 days** is the median annual close; top performers take 10 days or less and the slowest 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio, 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) — Not stated in the note; the benchmarking measure reports the 18.0-day median across 2,214 organisations |
| **18%** of people in the controllership function make errors at least daily, and 59% several per month, because of capacity constraints | [Gartner, comunicado del 21 de febrero de 2024, 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 people in the controllership function, surveyed in July 2023 |
<!-- /cfo:cifras -->

The figure that should sting is the first: **the close did not improve in four years**, despite everything spent on technology.

→ [The design of Clara and Tomás](../../families/criterio-cfo/DISENO.es.md)

---

## Acceptance criteria

See [ACCEPTANCE.md](ACCEPTANCE.md).
