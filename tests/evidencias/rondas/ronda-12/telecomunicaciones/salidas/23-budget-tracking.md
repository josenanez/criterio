# /criterio-portfolio:budget-tracking PRY-210

## Presupuesto: PRY-210, Conectividad para colegios públicos, al 2026-10-28

Los términos ya estaban vigentes (v0.12.1, aceptados por José Francisco Ñáñez el 2026-10-28), así que no los volví a registrar. Las cifras salen de la ficha PRY-210 y de `compute`. Todo está en COP, sin conversión de moneda.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 3.300.000.000 | 100% | Acta de constitución | 2026-05-14 |
| Comprometido | 1.565.215.894 | 47.4% | Informe de avance (declaración) | 2026-10-28 |
| Ejecutado | 1.847.276.551 | 56.0% | Informe de avance (declaración) | 2026-10-28 |
| Proyección al cierre | 3.951.444.314 | 19.7% por encima del aprobado | Informe de avance (declaración) | 2026-10-28 |

**Disponible real** (aprobado menos comprometido): 1.734.784.106 COP.

- **Contra la línea base:** el presupuesto vigente sigue siendo el del acta (3.300.000.000 COP) y no hay replanificaciones de presupuesto aprobadas. La solicitud de cambio CC-01 (2026-10-27) pide 220.000.000 COP más y +110 días. Está pendiente, sin decisión ni decisor.
- **Ejecución frente a avance:** el 56.0% ejecutado va por delante del avance. El avance declarado es 50%, el plan solo sostiene entre 20% y 40%, y hay 1 hito de 5 cumplido, sin evidencia.

**Alertas**
- La proyección supera el aprobado en 19.7%, sobre el umbral de 10%.
- Lo ejecutado va por encima de lo que respalda el plan.
- El hito "Diseño de red aprobado" figura como cumplido sin evidencia desde hace 71 días.
- La línea base de tiempo se movió 110 días sin autorización.
- El comprometido (47.4%) no llega al umbral de 90%, así que no hay alerta por ese concepto.
- El ejecutado es mayor que el comprometido, lo que normalmente no ocurre. No lo interpreté. Hay que pedirle la explicación a quien firma el informe de avance.

**Sin dato**
- Ninguna cifra salvo el aprobado tiene evidencia: las otras tres son declaraciones del mismo informe de avance.
- La ficha no registra proveedores, así que no hay detalle por proveedor.
- No sé si los 220.000.000 de CC-01 cubren la diferencia entre proyección y aprobado, porque `compute` no la da.

Como la proyección excede el aprobado y CC-01 está pendiente, puedo evaluarla con `/criterio-portfolio:change-control` si quieres.

La corrida quedó registrada como `2026-10-28-budget-tracking-1` (35 segundos). Lo que te mostré está guardado en `estado/corridas/salida-budget-tracking.md`.