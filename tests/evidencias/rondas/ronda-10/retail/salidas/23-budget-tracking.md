# /criterio-portfolio:budget-tracking PRY-201

## Presupuesto — PRY-201 Programa de fidelización, al 2026-10-18

Hay un riesgo de costo real en PRY-201. La proyección al cierre pasa el presupuesto aprobado en 22.6 %, con un umbral de 10 %.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-18, así que no los registré de nuevo. El informe sale de la ficha `estado/records/PRY-201.json` y del cálculo de `portafolio.py compute`. Todo está en COP, sin conversiones.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 3.300.000.000 | 100 | Acta de constitución | 2026-03-12 |
| Comprometido | 2.647.230.813 | 80.2 | Informe de avance | 2026-10-17 |
| Ejecutado | 860.644.236 | 26.1 | Informe de avance | 2026-10-17 |
| Proyección al cierre | 4.046.399.504 | 22.6 por encima | Informe de avance | 2026-10-17 |

- **Disponible real:** 652.769.187 COP (aprobado menos comprometido).
- **Línea base:** el aprobado original y el vigente son ambos 3.300.000.000. Hay 0 replanificaciones de presupuesto y no hay solicitudes de cambio.
- **Proyección:** es una declaración del informe de avance, con un día de antigüedad. No hay movimientos de presupuesto posteriores que la dejen vencida.

**Ejecución frente a avance:** el informe declara 86 % de avance, pero el plan solo sustenta entre 60 y 80 %. Hay 3 de 5 hitos cumplidos y ninguno tiene evidencia. Con 80.2 % comprometido y 26.1 % ejecutado, el avance declarado no cuadra con el dinero causado.

**Alertas:**
- **Comprometido:** 80.2 %, por debajo del umbral de 90 %, pero con poca holgura frente a una proyección que excede el aprobado.
- **Facturación (CT-836, Tecnología para Tiendas Ltda.):** facturado 419.283.282, aceptado 311.826.194, diferencia de 107.457.088 COP.
- **Entregables vencidos:** "Bolsa de horas de desarrollo" está pendiente en dos contratos, con 53 días de atraso (CT-144) y 1 día (CT-836). "Licenciamiento de la plataforma" figura aceptado sin evidencia de recibo.
- **Estado declarado:** el informe dice verde, pero las señales abiertas de costo, proveedor y evidencia no lo sustentan.

**Sin dato:**
- No hay desglose del comprometido por proveedor.
- La autoridad y la fase del proyecto no están declaradas.
- No hay documento de cambio que distinga un presupuesto original de uno vigente.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. También puedo detallar el comprometido por proveedor, empezando por la diferencia facturada en CT-836.

**Registros:** el informe quedó en `estado/corridas/salida-budget-tracking.md`. La corrida quedó registrada con el id `2026-10-18-budget-tracking-1`. La corrida tardó 32 segundos y la medición de documentos leídos quedó en `null`. El conteo de señales de esa corrida (63 hallazgos) cubre los 13 proyectos del portafolio, no solo PRY-201.