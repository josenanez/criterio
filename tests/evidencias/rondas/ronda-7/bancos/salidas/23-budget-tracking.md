# /criterio-portfolio:budget-tracking PRY-201

Fuentes: la ficha de PRY-201, el acta de constitución (2026-01-22), el informe de avance (corte 2026-10-10), la solicitud de cambio CC-01 (2026-10-05) y los cronogramas v1 y v2. Las cifras derivadas salen de `portafolio.py compute`, al 2026-10-17. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-17), así que no los registré de nuevo.

## Presupuesto — PRY-201 Core de depósitos al 2026-10-17
**Moneda:** COP. Es la única moneda, sin conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 800.000.000 | 100 | Acta | 2026-01-22 |
| Comprometido | 341.241.342 | 42,7 | Informe de avance (declaración) | 2026-10-10 |
| Ejecutado | 281.689.586 | 35,2 | Informe de avance (declaración) | 2026-10-10 |
| Proyección al cierre | 993.865.329 | 24,2 por encima del aprobado | Informe de avance (declaración) | 2026-10-10 |

**Disponible real** (aprobado menos comprometido): 458.758.658 COP.

La proyección es una declaración con 7 días de antigüedad. Comprometido, ejecutado y proyección salen del mismo informe, sin respaldo contable.

**Contra la línea base**
- El presupuesto aprobado no cambió: 800.000.000 original y vigente.
- Replanificaciones de presupuesto: 0.
- La CC-01 pide 214.000.000 COP adicionales y está pendiente de presentación al comité. No hay aprobación.

**Ejecución frente a avance**
- Ejecutado 35,2 %, hitos cumplidos 3 de 4, avance declarado 66 %.
- La ejecución está muy por debajo del avance declarado. Puede ser trabajo hecho y no causado, o un avance inflado.
- Los tres hitos cumplidos no traen evidencia. Con los documentos no se puede decidir cuál de las dos lecturas es la correcta.

**Alertas**
- **Proyección sobre el aprobado:** supera el umbral del 10 %, sin cambio de presupuesto autorizado.
- **Línea base de tiempo:** la v2 mueve el cierre 107 días, de 2026-10-15 a 2027-01-30, sin autorización ni motivo.
- **Estado «verde»:** el informe no da cuenta de la desviación de costo, la de tiempo, el movimiento de línea base ni los hitos sin evidencia.
- **Comprometido:** 42,7 %, por debajo del umbral de 90 %. No hay alerta de tope.

**Sin dato**
- Si la proyección incluye los 214.000.000 de la CC-01.
- Respaldo contable de comprometido y ejecutado.
- Desglose por proveedor: la ficha no tiene proveedores.
- Motivo de la línea base v2.
- Autoridad y fase del proyecto.

**Siguiente paso:** como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto con `/criterio-portfolio:change-control`. No lo hago sin que lo pidas.

La salida quedó guardada en `estado/corridas/salida-budget-tracking.md` y la corrida registrada como `2026-10-17-budget-tracking-1`. La corrida midió el tiempo (30 s) pero no el número de documentos.

*Borrador de trabajo basado solo en los documentos citados. Verifica cada cifra contra su fuente antes de usarla.*