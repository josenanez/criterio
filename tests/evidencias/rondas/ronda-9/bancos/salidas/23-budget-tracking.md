# /criterio-portfolio:budget-tracking PRY-202

## Presupuesto de PRY-202 Migración a la nube, al 2026-10-17

El informe sale de la ficha `records/PRY-202.json`, del acta de constitución (2025-09-25) y del informe de avance (2026-10-13). Las cifras derivadas vienen de `compute`. Los términos están vigentes y quedaron registrados a nombre de José Francisco Ñáñez.

**Moneda:** COP. Es la única que aparece, así que no hubo conversiones.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 9.500.000.000 | — | Acta de constitución | 2025-09-25 |
| Comprometido | 6.552.528.459 | 69.0% | Informe de avance | 2026-10-13 |
| Ejecutado | 2.548.693.323 | 26.8% | Informe de avance | 2026-10-13 |
| Proyección al cierre | 12.125.785.918 | 27.6% por encima del aprobado | Informe de avance | 2026-10-13 |

El disponible real (aprobado menos comprometido) es 2.947.471.541 COP.

- **Línea base:** hay una sola versión (v1, 2025-09-25). El presupuesto original y el vigente son iguales, con desviación 0. No hay replanificaciones de presupuesto ni solicitudes de cambio.
- **Proyección:** es una declaración del gerente, no un dato duro. Es posterior al aprobado y ningún movimiento de presupuesto la contradice.
- **Ejecución frente a avance:** el avance declarado es 37.0%, con 2 de 3 hitos cumplidos. El plan sustenta entre 67% y 100%, así que el avance va 30.0 puntos por detrás. Los dos hitos "cumplidos" no tienen evidencia de recibo.

**Alertas**
- La proyección excede el aprobado en 27.6%, frente a un umbral de 10%.
- El informe del 2026-10-13 declara el proyecto en verde sin tener en cuenta el sobrecosto, la brecha de avance ni los hitos sin evidencia.
- Los hitos "Diseño funcional aprobado" (vencía 2026-02-27) y "Ambiente de pruebas certificado" (vencía 2026-07-22) figuran como cumplidos sin evidencia.
- El comprometido está en 69.0%, por debajo del umbral de 90%, así que no genera alerta.

**Sin dato**
- La ficha no registra proveedores ni contratos para PRY-202, así que no hay detalle por proveedor.
- El monto aprobado tiene 13 meses de antigüedad, por encima del umbral de 12.
- Faltan producto, autoridad y fase del proyecto.

**Siguiente paso:** como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto con `/criterio-portfolio:change-control`. No la preparé porque nadie puede responder en esta sesión.

Esto es un borrador de trabajo, no una decisión ni una asesoría. Lo que se haya hablado fuera de esos documentos no lo conozco. La verificación contra los documentos es de quien lo lea.

La corrida quedó registrada como `2026-10-17-budget-tracking-1`. El texto completo está en `estado/corridas/salida-budget-tracking.md`.