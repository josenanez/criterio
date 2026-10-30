# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (64 en total). Las tres actas de `40-actas/` ya estaban en la ficha con su cita, así que no cambié nada. Los términos estaban vigentes, por lo que no hubo que registrar aceptación. Salieron tres señales.

# Qué cambió en el presupuesto · Almacenes del Valle de Sula · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes del Valle de Sula (08010006129040) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.1.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 28,000.00 en 2026-08 sin línea presupuestal | 28,000.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |
| 2 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -38,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.csv` fila 4 · `2026-02/10-contabilidad/libro-mayor.csv` fila 4 |
| 3 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado (v2, 2026-06-30), nacida del traslado del acta 05; el acta 01 aprueba la v1
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días
- ¿Prefijos de gasto? → 51, según las cuentas del mapeo-presupuesto
- ¿Fichas PMO? → estado-pmo/records (existe y trae PRY-310)
- ¿Fechas del comité? → No encontrado en los documentos; queda vacío

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `2026-08/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 3 hallazgos. El reporte está en `presupuesto/2026/reporte-budget-scan.md`.