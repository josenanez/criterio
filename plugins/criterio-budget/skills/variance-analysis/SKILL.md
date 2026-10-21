---
name: variance-analysis
description: "Cómo se calcula la ejecución contra el presupuesto: la versión aprobada, el aprobado al corte, lo ejecutado desde la contabilidad con el mapeo de cuentas, lo comprometido, lo disponible y la desviación. Úsalo al preparar el informe de ejecución o explicar una desviación. Budget vs actual, variance, commitments."
---

# La ejecución contra el presupuesto

## Las piezas

- **La versión vigente**: la más reciente de `presupuesto-<AAAA>/10-aprobado/`, salvo que la configuración fije otra en `budget.approved_version`. Cada versión lleva `v<N>` y su fecha en el nombre, y por fila `area`, `linea` y los doce meses (`ene` a `dic`) o un `total`. Que cada cambio respecto de la versión anterior tenga su acta lo revisa `transfer-log`.
- **Lo ejecutado** sale de `10-contabilidad/` de cada periodo del año hasta el corte: los movimientos de las cuentas de gasto (`budget.expense_prefixes`, 5, 6 y 7 por defecto), débito menos crédito, llevados a su línea con `00-referencia/mapeo-presupuesto` (cuenta, centro de costo, área, línea). Tomás no recalcula la contabilidad: usa la que cerró Clara.
- **Lo comprometido**: el saldo por ejecutar del archivo más reciente de `20-compromisos/`.

## Las cifras, por área y línea

| Cifra | Cómo |
|---|---|
| Aprobado al corte | La suma de los meses hasta el corte; sin distribución mensual, la proporción del año, y el reporte lo dice |
| Disponible | Aprobado del año menos ejecutado menos comprometido |
| Desviación | Ejecutado menos aprobado al corte, y su porcentaje |

## Las señales

- `variance_over_threshold`: la desviación pasa de `variance_pct` (10 % por defecto), por encima o por debajo.
- `committed_near_approved`: ejecutado más comprometido llega a `committed_pct` (95 %) de lo aprobado en el año.
- `spend_without_budget_line`: gasto que el mapeo no lleva a ninguna línea, o compromiso en una línea que el presupuesto no tiene.
- `declared_vs_evidence`: el área se declara dentro del presupuesto y alguna de sus líneas pasa el umbral o su proyección supera lo aprobado.
- `project_budget_mismatch`: si la organización usa la familia PMO, el presupuesto aprobado en la ficha de un proyecto (`money.approved`) no es el de la línea con su código.
