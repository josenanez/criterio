# /criterio-budget:forecast 

# Proyección al cierre del año · Cooperativa Sierra Alta · presupuesto 2026, corte 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Comité de presupuesto · **Comando:** `forecast`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv: Comercial · Eventos usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv` fila 3 |
| 2 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv: Comercial · Publicidad usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv` fila 2 |
| 3 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 24,000.00 | 23,520.00 (2026-09-30) | 23,280.00 | 23,460.00 |
| Administración | Servicios públicos | 36,000.00 | 35,280.00 (2026-09-30) | 34,920.00 | 35,190.00 |
| Comercial | Eventos | 21,000.00 | 20,580.00 (2026-09-30) | 19,400.00 | 20,550.00 |
| Comercial | Publicidad | 45,000.00 | 44,100.00 (2026-09-30) | 44,620.00 | 43,965.00 |
| Operaciones | Transporte | 42,000.00 | 41,160.00 (2026-07-15) | 40,740.00 | 41,055.00 |
| Personal | Nómina | 240,000.00 | 240,000.00 (2026-09-30) | 240,000.00 | 240,000.00 |
| Tecnología | Licencias | 60,000.00 | 58,800.00 (2026-09-30) | 58,200.00 | 58,650.00 |
| Tecnología | PRY-310 | 72,000.00 | 70,560.00 (2026-09-30) | 69,840.00 | 70,380.00 |

**Al ritmo:** el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan:** el ejecutado más lo que falta del aprobado según su distribución mensual.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Cooperativa Sierra Alta (RUC 1790012345001), presupuesto 2026; tomado del nombre de la carpeta y de presupuesto-2026/
- ¿Cuál es la versión aprobada y su acta? → El acta 01 (2026-01-20) aprueba la versión 1; el acta 05 (2026-06-28) aprueba un traslado de 3,000.00 que coincide con la versión 2 (2026-06-30), pero ningún acta nombra esa versión. Se registró lo que dicen las actas.
- ¿Áreas y responsables? → No encontrado: ningún documento nombra a los responsables de las áreas. Áreas tomadas del mapeo: Administración, Comercial, Tecnología, Operaciones, Personal.
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité? → No encontrado en los documentos; quedó vacío
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Dónde se guarda lo que se encuentra? → estado-finanzas/1790012345001-cooperativa-sierra-alta, fuera de la carpeta de documentos
- ¿Términos? → Aceptados por José Francisco Ñáñez, 2026-10-06, versión 1.2

## Fuentes

- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

---
La corrida quedó registrada como `2026-10-06-forecast-1`, con 4 hallazgos. Los términos ya estaban aceptados y vigentes (versión 1.2, José Francisco Ñáñez, 2026-10-06), así que no volví a registrarlos.