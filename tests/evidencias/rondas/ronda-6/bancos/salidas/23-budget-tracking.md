# /criterio-portfolio:budget-tracking PRY-203

## Presupuesto — PRY-203 Open Banking al 2026-10-16

**Moneda:** COP. Todos los montos del proyecto están en COP y no hubo conversiones.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré otra vez. Las cifras salen de la ficha PRY-203 y de `compute` del 2026-10-16.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 18.000.000.000 | 100 % | Acta de constitución | 2026-01-22 |
| Comprometido | 9.797.767.251 | 54,4 % | Informe de avance | 2026-09-25 |
| Ejecutado | 7.810.329.197 | 43,4 % | Informe de avance | 2026-09-25 |
| Proyección al cierre | 22.250.676.721 | 123,6 % | Informe de avance | 2026-09-25 |

**Disponible real** (aprobado menos comprometido): 8.202.232.749 COP.

**Contra la línea base**
- El aprobado original y el vigente son iguales: 18.000.000.000 COP, sin replanificaciones de presupuesto.
- La proyección excede el aprobado en 23,6 %, con un umbral de 10 %.
- La solicitud de cambio CC-01 pide +66.000.000 COP y +33 días. Está pendiente y sin decisor, así que no cambia el aprobado.

**Ejecución frente a avance**
- Ejecutado 43,4 %, hitos cumplidos 2 de 4, avance declarado 46 %. El plan sustenta entre 50 y 75 %.
- El gasto va alineado con el avance declarado. El problema está en la proyección, no en la ejecución.

**Alertas**
- El informe del 2026-09-25 declara estado **verde**, pero su propia proyección supera el aprobado en 23,6 %. La proyección es una declaración, no una medición, y tiene 21 días.
- Ninguna solicitud de cambio cubre la brecha de 4.250.676.721 COP entre proyección y aprobado. CC-01 solo pide 66.000.000 COP.
- El comprometido (54,4 %) está lejos del umbral de 90 %, así que hoy no es la señal.
- El cronograma se movió 33 días (de 2027-03-21 a 2027-04-23) sin un cambio autorizado.
- El hito "Ambiente de pruebas certificado" figura cumplido sin evidencia de recibo.

**Sin dato**
- El desglose del comprometido por proveedor, porque la ficha no tiene proveedores registrados.
- La fecha del último movimiento de presupuesto. Por eso no puedo decir si la proyección es más vieja que ese movimiento.
- La autoridad y la fase del proyecto.

**Siguiente paso posible:** como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto con `/change-control`. Tendría que sustentar la brecha de 4.250.676.721 COP.

Este es un borrador de trabajo, no una decisión. La verificación de las cifras es suya.

La salida quedó guardada en `estado/corridas/salida-budget-tracking.md`. La corrida quedó registrada como `2026-10-16-budget-tracking-1` y tardó 26 segundos. El registro cuenta los hallazgos de los 13 proyectos del portafolio, no solo los de PRY-203.