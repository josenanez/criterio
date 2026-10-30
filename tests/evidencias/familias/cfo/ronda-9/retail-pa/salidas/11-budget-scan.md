# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (65 en el inventario). Las tres actas de `40-actas/` ya estaban en la ficha y coinciden con ella. Los términos (versión 1.3) ya estaban aceptados, así que no registré nada. La sección «El resultado» del reporte salió vacía, tal como la entrega el motor.

# Qué cambió en el presupuesto · Almacenes del Canal · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes del Canal (155791002-2-2017) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 1,050.00 en 2026-08 sin línea presupuestal | 1,050.00 | — | — | `2026-08/10-contabilidad/libro-mayor.xlsx` fila 18 |
| 2 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -1,425.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 4 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 4 |
| 3 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La versión 1, acta 01 del 2026-01-20; la vigente es la más reciente de 10-aprobado/ (v2, 2026-06-30), que nace del traslado del acta 05
- ¿Entidad y año presupuestal? → Almacenes del Canal (RUC 155791002-2-2017), presupuesto 2026, corte 2026-09 (tomado de la configuración de cierre y del inventario)
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días; son configuración, no norma
- ¿Fechas del comité de presupuesto? → No encontrado: ningún documento las trae; el acta 06 es del 2026-09-10 y no fija la siguiente
- ¿Fichas de proyectos PMO? → estado-pmo/records, con PRY-310.json

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `2026-08/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.xlsx`

La corrida quedó registrada como `2026-10-06-budget-scan-1` con 3 hallazgos. Lo que te mostré está guardado en `corridas/salida-budget-scan.md`.