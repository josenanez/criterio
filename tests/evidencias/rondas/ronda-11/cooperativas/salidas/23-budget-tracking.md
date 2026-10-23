# /criterio-portfolio:budget-tracking PRY-211

Terminé la corrida de presupuesto de PRY-211 Cobranza digital y quedó registrada como `2026-10-23-budget-tracking-1`. Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (v1.2, 2026-10-23), así que no hubo que registrarlos de nuevo. Las cifras derivadas salen de `compute` y de la ficha; las fuentes son el acta (2025-06-24) y el informe de avance (2026-10-19).

## Presupuesto — PRY-211 al 2026-10-23
**Moneda:** COP, única, sin conversiones.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 4.200.000.000 | 100 | acta de constitución | 2025-06-24 |
| Comprometido | 3.403.064.146 | 81.0 | informe de avance | 2026-10-19 |
| Ejecutado | 1.718.932.257 | 40.9 | informe de avance | 2026-10-19 |
| Proyección al cierre | 5.280.911.293 | 125.7 | informe de avance | 2026-10-19 |

**Disponible real** (aprobado menos comprometido): 796.935.854 COP.

La proyección es una declaración del informe, no un dato medido.

**Contra la línea base:** el aprobado original y el vigente son iguales (4.200.000.000), con 0 replanificaciones de presupuesto y 0 solicitudes de cambio. La proyección excede el aprobado en 25.7 %.

**Ejecución frente a avance:** ejecutado 40.9 %, hitos 3 de 3 y avance declarado 37 %. El gasto es coherente con el avance declarado, pero el plan sostiene 100 % (brecha de 63.0 puntos). El plan terminaba el 2026-03-07, hace 230 días, y los 3 hitos figuran como cumplidos sin evidencia. Los documentos no dicen si los hitos no se cumplieron o si el avance declarado está mal.

**Alertas**
- **Proyección:** está 25.7 % sobre el aprobado, con umbral de 10 %. El informe del 2026-10-19 declara estado verde sin explicar esa señal.
- **Comprometido:** 81.0 % está bajo el umbral de 90 %, así que no hay alerta. Aun así, la holgura real es 796.935.854 COP, mucho menos de lo que sugiere mirar solo el 40.9 % ejecutado, y la proyección dice que no alcanza.
- **Antigüedad:** el aprobado tiene 16 meses y nadie lo ha reconfirmado. El umbral es 12 meses.

**Sin dato**
- Ningún documento declara un presupuesto vigente distinto del original. Lo trato como igual solo porque no hay cambios registrados.
- La ficha no tiene proveedores para este proyecto, así que no hay detalle por proveedor.
- Faltan la autoridad que aprobó el presupuesto y la fase del proyecto.
- Comprometido, ejecutado y proyección salen del mismo informe, sin evidencia independiente que los respalde.

**Siguiente paso:** como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. No la preparé porque nadie la pidió.

El registro de la corrida (`estado/corridas/2026-10-23-budget-tracking.md`) cuenta 13 proyectos y 67 hallazgos, porque suma todo el portafolio y no solo PRY-211. El caso asociado es PRY-211. No pudo medir el número de documentos leídos.

El informe completo quedó guardado en `estado/corridas/salida-budget-tracking.md`.