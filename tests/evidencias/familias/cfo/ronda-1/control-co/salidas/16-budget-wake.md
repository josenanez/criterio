# /criterio-budget:budget-wake 

Hoy tocaban `budget-scan`, `variance-report` y `forecast`, porque había contabilidad nueva de 2026-01 a 2026-08. El inventario encontró 58 documentos, sin nuevos, cambiados, borrados ni fuera de lugar. El corte procesado es 2026-09.

No había peticiones abiertas. Los términos (versión 1.2) ya estaban registrados a nombre de José Francisco Ñáñez, con fecha 2026-10-06.

**Ejecución contra aprobado** (versión vigente 2, `presupuesto-2026-v2-2026-06-30.csv`):

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 12.000.000,00 | 9.000.000,00 | 8.730.000,00 | 300.000,00 | 2.970.000,00 | -270.000,00 | -3,00 |
| Administración | Servicios públicos | 18.000.000,00 | 13.500.000,00 | 13.095.000,00 | 450.000,00 | 4.455.000,00 | -405.000,00 | -3,00 |
| Comercial | Eventos | 10.500.000,00 | 7.500.000,00 | 7.275.000,00 | 300.000,00 | 2.925.000,00 | -225.000,00 | -3,00 |
| Comercial | Publicidad | 22.500.000,00 | 17.250.000,00 | 16.732.500,00 | 525.000,00 | 5.242.500,00 | -517.500,00 | -3,00 |
| Operaciones | Transporte | 21.000.000,00 | 15.750.000,00 | 15.277.500,00 | 525.000,00 | 5.197.500,00 | -472.500,00 | -3,00 |
| Tecnología | Licencias | 30.000.000,00 | 22.500.000,00 | 21.825.000,00 | 750.000,00 | 7.425.000,00 | -675.000,00 | -3,00 |
| Tecnología | PRY-310 | 36.000.000,00 | 27.000.000,00 | 26.190.000,00 | 900.000,00 | 8.910.000,00 | -810.000,00 | -3,00 |
| Personal | Nómina | 120.000.000,00 | 90.000.000,00 | 90.000.000,00 | 3.000.000,00 | 27.000.000,00 | 0,00 | 0,00 |

Nada queda abierto y todo lo que llegó se procesó. El reporte no cita documentos.

**Proyección al cierre del año:**

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 12.000.000,00 | 11.760.000,00 (2026-09-30) | 11.640.000,00 | 11.730.000,00 |
| Administración | Servicios públicos | 18.000.000,00 | 17.640.000,00 (2026-09-30) | 17.460.000,00 | 17.595.000,00 |
| Comercial | Eventos | 10.500.000,00 | 10.290.000,00 (2026-09-30) | 9.700.000,00 | 10.275.000,00 |
| Comercial | Publicidad | 22.500.000,00 | 22.050.000,00 (2026-09-30) | 22.310.000,00 | 21.982.500,00 |
| Operaciones | Transporte | 21.000.000,00 | 20.580.000,00 (2026-09-30) | 20.370.000,00 | 20.527.500,00 |
| Personal | Nómina | 120.000.000,00 | 120.000.000,00 (2026-09-30) | 120.000.000,00 | 120.000.000,00 |
| Tecnología | Licencias | 30.000.000,00 | 29.400.000,00 (2026-09-30) | 29.100.000,00 | 29.325.000,00 |
| Tecnología | PRY-310 | 36.000.000,00 | 35.280.000,00 (2026-09-30) | 34.920.000,00 | 35.190.000,00 |

**Al ritmo** es el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan** es el ejecutado más lo que falta del aprobado según su distribución mensual. Tampoco aquí queda nada abierto ni sin procesar.

La salida completa está en `estado-finanzas/900000001-distribuidora-control/corridas/salida-budget-wake.md`. Registré la corrida y los tres comandos (`budget-scan`, `variance-report`, `forecast`) con el caso 2026-09, sin hallazgos. No corrí `budget-committee-pack`, porque `committee_dates` está vacío y el motor no lo marcó como pendiente.