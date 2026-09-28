# criterio-finance

Fork of Anthropic's `finance` plugin. The upstream closes the month against US GAAP and controls SOX; here the framework is locally adopted IFRS, and electronic invoicing is a first-class concern because it decides deductibility.

**Status:** declared, not built. No content, and no jurisdiction packages exist in this repository. Nothing is built here until the scope is deliberately widened — see [ADR 0005](../../docs/decisions/0005-scope-pmo-only.md).

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

| Figure | Source |
|---|---|
| **18%** of accountants make errors daily and **59%** several per month, due to capacity constraints | [Gartner, Feb 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) — 497 accountants, surveyed Jul 2023 |
| Annual close: **10 days** for top performers, **18** at the median, **35** for laggards | [APQC, Apr 2026](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-up-year-end-close) |
| The quarterly close got **worse**: 49% closed within six business days in 2019, 44% in 2023 | [Ventana Research / ISG, Dec 2023](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) |
| SOX programme hours rose **32% in two years**, to 15,580. **45% of controls remain fully manual** | [KPMG, *SOX Survey* 2025](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) — ~150 professionals |

The figure that should sting is the third: **the close did not improve in four years**, despite everything spent on technology.

→ CFO Agent: capability declared, not built

---

## Acceptance criteria

See [ACCEPTANCE.md](ACCEPTANCE.md).
