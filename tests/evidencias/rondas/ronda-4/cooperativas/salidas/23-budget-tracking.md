# /criterio-portfolio:budget-tracking PRY-211

## Presupuesto — PRY-211 Cobranza digital, al 2026-10-15

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo. Todas las cifras salen de la ficha del proyecto (actualizada el 2026-10-15) y del cálculo del script. La moneda es COP, sin otras monedas ni conversiones.

| | Monto (COP) | % del aprobado |
|---|---|---|
| Aprobado | 9.500.000.000 | — |
| Comprometido | 4.607.236.341 | 48.5 |
| Ejecutado | 3.697.963.264 | 38.9 |
| Proyección al cierre | 11.146.984.265 | 17.3 por encima del aprobado |

- **Fuente de las cuatro cifras:** el informe de avance del 2026-10-15, que es una declaración del gerente.
- **Disponible real:** 4.892.763.659 COP (aprobado menos comprometido).
- **Replanificaciones de presupuesto:** 0, y no hay solicitudes de cambio registradas.

### Ejecución frente a avance
- **Avance declarado:** 44 %. El plan sustenta entre 60 y 80 %, así que el proyecto va 16.0 puntos por detrás.
- **Hitos:** 3 de 5 figuran como cumplidos, pero solo uno tiene acta de recibo (ambiente de pruebas certificado, 2026-10-13). «Diseño funcional aprobado» e «Integración con el core cooperativo» están dados por cumplidos sin evidencia. Con evidencia, el cumplimiento es 1 de 5.

### Alertas
- **Proyección sobre el aprobado:** supera en 17.3 % el aprobado, con un umbral de 10 %.
- **Facturado sin entrega:** Red Rural de Pagos S.A.S. (contrato CT-884) facturó 513.489.020 COP el 2026-09-26 y no tiene ningún entregable aceptado (0 de 4). Tres están vencidos y pendientes, con 247, 128 y 8 días de atraso.
- **Comprometido:** 48.5 %, por debajo del umbral de 90 %, así que no hay alerta de tope.

### Sin dato
- **Línea base de costo original:** no aparece en ningún documento, así que no puedo medir la desviación contra el original.
- **Desglose del comprometido y del ejecutado:** por proveedor o rubro, no está declarado.
- **Fecha de aprobación del presupuesto vigente:** no está declarada, así que no puedo decir si la proyección es más vieja que el último movimiento de presupuesto.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. También puedo detallar el contrato CT-884 con `/criterio-portfolio:vendor-tracking`.

La corrida quedó registrada como `2026-10-15-budget-tracking-1`. El informe completo está en `estado/corridas/salida-budget-tracking.md`.