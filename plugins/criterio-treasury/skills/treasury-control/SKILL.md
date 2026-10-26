---
name: treasury-control
description: "La caja contra su mínimo y su proyección, los pagos contra sus aprobadores y la matriz de firmas, la exposición cambiaria contra su límite, y la deuda contra su vencimiento y sus covenants. Úsalo al revisar la posición de caja, el programa de pagos o la deuda. Treasury, cash position, payment approvals, covenants."
---

# La tesorería contra su política

Todo lo calcula el motor sobre tablas; nada se extrae a la ficha.

- **La caja:** el último saldo del extracto de cada cuenta en `<periodo>/20-bancos/`, contra el mínimo de la política (`caja_minima`, por cuenta y `consolidado`) y contra el saldo proyectado de `60-tesoreria/flujo-proyectado`. Una desviación mayor que `cash_forecast_pct` es `cash_vs_forecast`; un saldo bajo el mínimo, `cash_below_minimum`.
- **La exposición cambiaria:** las cuentas en otra moneda, según `treasury.currencies`, convertidas con la `tasa` de la política; sobre `limite_exposicion` es `fx_exposure_over_limit`. Sin tasa no se calcula y el reporte lo dice.
- **Los pagos:** cada pago de `60-tesoreria/programa-pagos` pide las aprobaciones que fija la política para su monto (`aprobadores`, desde un monto). Con menos es `payment_without_approval`. Quien aprueba por encima de su monto en `matriz-firmas`, o no está en ella, es `signatory_without_authority`.
- **La deuda:** cada obligación o inversión de `registro-deuda` que vence dentro de `maturity_days` es `maturity_near`. Cada covenant de `covenants` se calcula con los saldos del balance de comprobación del periodo —el que cierra Clara—: numerador y denominador por prefijos de cuenta, en valor absoluto. Cruzar el límite o quedar a menos de `covenant_margin_pct` de él es `covenant_at_risk`.

La política, la matriz y los covenants son de la organización. Áurea no los propone como norma, no mueve dinero ni recomienda una inversión, un financiamiento o una cobertura.
