# /criterio-portfolio:budget-tracking PRY-204

## Presupuesto — PRY-204 Cajas de autopago al 2026-10-15

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar. Las cifras salen de `compute` y de la ficha de PRY-204. Todo es en COP; no hay otra moneda ni conversión.

| | Monto (COP) | % del aprobado |
|---|---|---|
| Aprobado | 1200000000 | — |
| Comprometido | 894302033 | 74.5 |
| Ejecutado | 501728889 | 41.8 |
| Proyección al cierre | 1342154042 | excede el aprobado en 11.8 |

- **Fuente de las cuatro cifras:** el informe de avance del 2026-09-26, que es una declaración del gerente. Ningún documento contable las respalda.
- **Disponible real** (aprobado menos comprometido): 305697967.
- **Contra la línea base:** el aprobado y la fecha de cierre (2027-02-16) no se han movido. Hay 0 replanificaciones y 0 solicitudes de cambio.
- **Ejecución frente a avance:**
  - Ejecutado 41.8%; hitos cumplidos 2 de 4, y solo 1 tiene evidencia.
  - El avance declarado es 32%, y el plan sostiene entre 50% y 75%.
  - El gasto no está muy por encima del avance de hitos; lo que no cuadra es que el avance va 18 puntos atrás.
- **Alertas:**
  - La proyección excede el aprobado en 11.8%, sobre el umbral de 10%.
  - El comprometido (74.5%) está bajo el umbral de 90%.
  - El informe declara "verde", pero ese mismo informe trae la proyección sobre el aprobado.
  - Hay dos incidencias abiertas sin dueño: un hallazgo de seguridad en los medios de pago y una prueba de carga que se repite. Ninguna trae estimación de costo.
- **Sin dato:**
  - El aprobado original del acta de constitución.
  - Evidencia contable.
  - Proveedores, porque la ficha no registra ninguno.
  - La autoridad que aprobó el presupuesto.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `change-control`. No ofrezco el detalle por proveedor porque no hay proveedores.

La salida completa quedó en `estado/corridas/salida-budget-tracking.md`. La corrida quedó registrada como `2026-10-15-budget-tracking-1`.