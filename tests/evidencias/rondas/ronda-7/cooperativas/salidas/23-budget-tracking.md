# /criterio-portfolio:budget-tracking PRY-206

## Presupuesto — PRY-206 Pagos con QR, al 2026-10-17

El presupuesto está en riesgo: la proyección al cierre supera el aprobado en 26.9%. Los términos estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo.

**Moneda:** COP. Es la única, y no hubo conversiones.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 1.200.000.000 | 100% | acta de constitución | 2025-05-12 |
| Comprometido | 682.946.035 | 56.9% | informe de avance | 2026-10-16 |
| Ejecutado | 448.689.025 | 37.4% | informe de avance | 2026-10-16 |
| Proyección al cierre | 1.522.401.880 | 26.9% por encima del aprobado | informe de avance | 2026-10-16 |

**Disponible real** (aprobado menos comprometido): 517.053.965 COP.

La proyección es una declaración del gerente. Es posterior al último movimiento de presupuesto (CC-01, 2026-10-05), así que no está desfasada.

### Contra la línea base
- **Cambio CC-01:** declara 72.000.000 COP adicionales y dice "autorizada por el comité", sin nombrar quién.
- **Presupuesto vigente:** ningún documento deja una línea base nueva. El informe del 2026-10-16 sigue reportando 1.200.000.000 como aprobado. No calculé un presupuesto vigente porque el script no lo da y ningún documento lo declara.
- **Replanificaciones:** 0 de presupuesto. Sí hay una de cronograma (v2, +36 días).

### Ejecución frente a avance
Ejecutado 37.4%, hitos 5 de 5 declarados cumplidos (3 sin evidencia), avance reportado 45%. El plan sostendría 100% de avance, así que la brecha es de 55.0 puntos. El gasto cuadra con el 45% reportado; lo que no cuadra es el estado de los hitos.

### Alertas
- **Proyección sobre el aprobado:** 26.9% por encima, frente a un umbral de 10%.
- **Factura sin entrega:** el proveedor Integración Financiera del Sur (contrato CT-399) facturó 96.483.298 COP el 2026-09-18. Ninguno de sus 3 entregables está aceptado, y los 3 están vencidos (429, 344 y 260 días).
- **Hitos "cumplidos" sin evidencia:** Diseño funcional, Ambiente de pruebas y Salida a producción.
- **Desviación de tiempo:** 36 días, 11.7% contra la línea base original.
- **Comprometido:** 56.9%, bajo el umbral de 90%. Sin alerta.

### Sin dato
- Presupuesto vigente tras CC-01.
- Quién aprobó CC-01.
- Respaldo del comprometido y la proyección más allá del informe de avance.
- El presupuesto aprobado tiene 17 meses de antigüedad, por encima del límite de 12.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto con `/criterio-portfolio:change-control`.

La corrida quedó registrada como `2026-10-17-budget-tracking-1`. El informe completo está en `estado/corridas/salida-budget-tracking.md`.