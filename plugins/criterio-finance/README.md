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

## Acceptance criteria

See [ACCEPTANCE.md](ACCEPTANCE.md).
