# /criterio-budget:forecast 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Una sola señal: Tecnología · PRY-310 proyecta por encima de lo aprobado. Ninguna de las tres proyecciones es la correcta por definición: la decisión de cuál usar es de una persona.

# Proyección al cierre del año · Almacenes Caribe · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `forecast`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La proyección al cierre del año supera lo aprobado (`forecast_over_approved`) | Tecnología · PRY-310: la proyección al cierre, la del área, es 63.360.000,00 y lo aprobado 57.600.000,00 | 5.760.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 7 · `2026-01/10-contabilidad/libro-mayor.csv` fila 12 · `2026-02/10-contabilidad/libro-mayor.csv` fila 12 |

## El resultado

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 19.200.000,00 | 18.816.000,00 (2026-09-30) | 20.693.333,33 | 20.320.000,00 |
| Administración | Servicios públicos | 28.800.000,00 | 28.224.000,00 (2026-09-30) | 27.936.000,00 | 28.152.000,00 |
| Comercial | Eventos | 16.800.000,00 | 16.464.000,00 (2026-09-30) | 15.520.000,00 | 16.440.000,00 |
| Comercial | Publicidad | 36.000.000,00 | 35.280.000,00 (2026-09-30) | 35.856.000,00 | 35.292.000,00 |
| Operaciones | Transporte | 33.600.000,00 | 32.928.000,00 (2026-09-30) | 32.592.000,00 | 32.844.000,00 |
| Personal | Nómina | 192.000.000,00 | 192.000.000,00 (2026-09-30) | 192.000.000,00 | 192.000.000,00 |
| Tecnología | Licencias | 48.000.000,00 | 47.040.000,00 (2026-09-30) | 46.560.000,00 | 46.920.000,00 |
| Tecnología | PRY-310 | 57.600.000,00 | 63.360.000,00 (2026-09-30) | 55.872.000,00 | 56.304.000,00 |

**Al ritmo:** el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan:** el ejecutado más lo que falta del aprobado según su distribución mensual.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Sin nadie que conteste, se propone la 2 (presupuesto-2026-v2-2026-06-30.csv), cuyo cambio coincide con el traslado del acta 05 del 2026-06-28; el acta 01 del 2026-01-20 aprueba solo la versión 1 y ningún acta dice 'versión 2'.
- ¿Qué cuentas entran como gasto? → Prefijo 51, el de las cuentas del mapeo-presupuesto (5105, 5135, 5145, 5195).
- ¿Fechas del comité de presupuesto? → No encontrado: el acta 06 no fija fecha del próximo comité.
- ¿Dónde están las fichas PMO? → estado-pmo/records (contiene PRY-310.json).
- ¿Se deja la marca _CRITERIO_FINANZAS.txt en la carpeta de documentos? → No: nadie autorizó escribir en los documentos.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

---
Corrida registrada como `2026-10-06-forecast-1`. El motor la registró con 2 hallazgos, aunque el reporte solo muestra una señal y no sé cuál es la segunda. La nota que pasé al registro («áreas sobre lo aprobado, proyecciones vencidas») es la del comando y no la verifiqué contra este resultado: aquí solo una línea supera lo aprobado.