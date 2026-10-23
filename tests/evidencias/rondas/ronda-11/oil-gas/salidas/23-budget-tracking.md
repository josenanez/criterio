# /criterio-portfolio:budget-tracking PRY-202

**Presupuesto de PRY-202 Gasoducto de interconexión, al 2026-10-23.** La proyección de cierre supera el presupuesto aprobado en 14.4%, por encima del umbral de 10%.

Los términos ya estaban vigentes (versión 0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23), así que no hubo que registrar nada nuevo. Todas las cifras vienen de `portafolio.py compute`, en COP, que es la única moneda del proyecto.

| | Monto (COP) | % del aprobado | Fuente (fecha) |
|---|---|---|---|
| Aprobado | 4.200.000.000 | 100 | Acta de constitución (2025-09-14) |
| Comprometido | 3.240.656534 | 77.2 | Informe de avance (2026-10-17) |
| Ejecutado | 1.691.183.267 | 40.3 | Informe de avance (2026-10-17) |
| Proyección al cierre | 4.804.009.661 | 14.4 por encima del aprobado | Informe de avance (2026-10-17) |

- **Disponible real:** COP 959.343.466 (aprobado menos comprometido).
- **Comprometido:** 77.2%, por debajo del umbral de 90%, así que no hay alerta por este concepto.
- **Línea base:** el presupuesto original y el vigente son iguales y no hay replanificaciones de presupuesto. No se registró ningún cambio.
- **Proyección:** es una declaración del gerente, no un dato duro. Tiene fuente y fecha, y no es más vieja que el último movimiento de presupuesto porque no hay ninguno.
- **Contra el avance:** el avance declarado es 75%, el plan sustenta 100% (4 de 4 hitos) y el gasto ejecutado es 40.3%. Esas tres lecturas no coinciden. Tres de los cuatro hitos figuran cumplidos sin acta de recibo: Licencia ambiental otorgada, Pozos perforados y Montaje de facilidades.
- **Compromiso vencido (fuera del presupuesto):** Rubén Cárdenas, "Entregar el punto 24", venció el 2026-10-05, hace 18 días.

Lo que no tengo:
- **Proveedores y desglose:** no hay proveedores ni contratos registrados, y ningún documento desglosa comprometido o ejecutado por rubro.
- **Respaldo de las cifras:** el comprometido, el ejecutado y la proyección salen de un informe de avance. Ningún documento contable las respalda.
- **Ficha desactualizada:** el aprobado y los campos de identidad tienen 13 meses, más que el umbral de 12. Faltan autoridad y fase.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. No ofrezco el detalle por proveedor porque el comprometido no está cerca del tope.

La corrida quedó registrada como `2026-10-23-budget-tracking-1` (38 segundos, caso PRY-202). Tardó 38 segundos y el número de documentos leídos no quedó medido.

El informe completo está en `estado/corridas/salida-budget-tracking.md`, dentro de la carpeta de trabajo.