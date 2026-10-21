---
name: forecast-method
description: "Las dos proyecciones al cierre del año que calcula el motor —al ritmo y al plan—, sus supuestos, cómo se comparan con la proyección del área y cuándo una proyección está vencida. Úsalo al preparar la proyección o explicar por qué un área supera lo aprobado. Year-end forecast, run-rate, assumptions."
---

# La proyección al cierre del año

Tres cifras por área y línea, cada una con su supuesto escrito al lado:

| Proyección | Supuesto |
|---|---|
| **La del área** | La más reciente de `30-proyecciones/`, con su fecha en el nombre; la que entregó quien responde por la línea |
| **Al ritmo** | El ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido |
| **Al plan** | El ejecutado más lo que falta del aprobado según su distribución mensual |

**Ninguna es la correcta por definición.** El ritmo supone que el año sigue como va; el plan, que lo que falta se gasta como se aprobó. La decisión de cuál usar es de una persona; el reporte deja los supuestos escritos para que pueda tomarla.

## Las señales

- `forecast_over_approved`: la proyección del área —o, si el área no entregó la suya, la calculada al ritmo— supera lo aprobado en el año.
- `forecast_stale`: la proyección del área tiene más de `forecast_stale_days` (45 por defecto).
- `budget_version_mismatch`: una proyección o un informe usa una versión del presupuesto distinta de la aprobada.
