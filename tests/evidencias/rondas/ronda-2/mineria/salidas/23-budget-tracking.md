# /criterio-portfolio:budget-tracking PRY-211

## Presupuesto — PRY-211 Control de polvo en vías, al 2026-10-15

**Moneda:** COP, la única; no se convirtió nada. Salió de la ficha y de `compute`. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré una aceptación nueva.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 2.400.000.000 | 100 | acta de constitución | 2026-03-09 |
| Comprometido | 984.976.055 | 41.0 | informe de avance (declaración) | 2026-10-12 |
| Ejecutado | 1.403.798.497 | 58.5 | informe de avance (declaración) | 2026-10-12 |
| Proyección al cierre | 2.702.499.056 | 112.6 | informe de avance (declaración) | 2026-10-12 |

- **Disponible real** (aprobado menos comprometido): 1.415.023.945 COP.
- **Fuente única:** comprometido, ejecutado y proyección salen de una sola declaración del gerente, sin evidencia aparte.
- **Contra la línea base:** la fecha de fin pasó de 2027-07-22 a 2027-09-25, +65 días (13.3%) contra la original.
- **Cronograma sin autorizar:** esa replanificación no tiene aprobación documentada. CC-01 (+65 días, +130000000 COP) sigue pendiente.
- **Presupuesto:** no hay una línea base de presupuesto distinta del aprobado, así que no hay replanificaciones de presupuesto documentadas.
- **Ejecución frente a avance:**
  - Ejecutado 58.5% y 2 de 5 hitos cumplidos.
  - El avance declarado es 66%, pero el plan solo sustenta entre 40% y 60%.
  - Lo que no se sostiene es el 66%, no el dinero ejecutado.

### Alertas
- **Proyección:** excede el aprobado en 12.6%, sobre el umbral de 10%.
- **Tiempo:** la desviación es 13.3%, también sobre el umbral de 10%.
- **Línea base:** se movió 65 días sin autorización.
- **Estado declarado:** el informe dice "verde" sin dar cuenta de esas señales.
- **Ejecutado mayor que comprometido:** es lo contrario de lo normal y los documentos no lo explican. El "disponible real" depende de cuál sea la causa.
- **Compromiso sin fecha:** María Restrepo, "Entregar el punto 22".
- **Umbral de comprometido:** 41.0% está por debajo del umbral de 90%, así que no hay alerta por ahí.

### Sin dato
- Línea base de presupuesto separada del aprobado.
- Fecha del último movimiento de presupuesto. Por eso no puedo decir si la proyección es más vieja que ese movimiento.
- Documento de soporte, distinto del informe de avance, para comprometido, ejecutado y proyección.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/change-control`. CC-01 ya existe, pero solo cubre +130000000 COP, y la proyección excede el aprobado en 12.6%.

La salida está en `estado/corridas/salida-budget-tracking.md` y la corrida quedó registrada con el id `2026-10-15-budget-tracking-1`.

*Borrador de trabajo. Cada cifra viene de `compute` con la cita de su documento; la verificación es suya.*