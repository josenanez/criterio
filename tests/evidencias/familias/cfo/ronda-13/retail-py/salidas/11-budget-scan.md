# /criterio-budget:budget-scan 

Los términos vigentes (v1.3) ya estaban aceptados por José Francisco Ñáñez, así que no hizo falta registrarlos otra vez. El inventario no trae archivos nuevos ni cambiados. Las tres actas de `40-actas/` ya estaban en la ficha, sin cambios. El motor levantó tres señales.

# Qué cambió en el presupuesto · Distribuidora del Ybytyruzú (sintética) · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Ybytyruzú (sintética) (88612904-4) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.2.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 7.000.000,00 en 2026-08 sin línea presupuestal | 7.000.000,00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |
| 2 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96,0 % de lo aprobado en el año | -9.500.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.csv` fila 4 · `2026-02/10-contabilidad/libro-mayor.csv` fila 4 |
| 3 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

(El motor dejó esta sección vacía; no hay cifras que copiar.)

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado/ (v2, 2026-06-30); acta 01 aprueba la v1 y acta 05 el traslado que origina la v2
- ¿Fechas del comité de presupuesto? → No hay fecha futura en los documentos; queda vacío
- ¿Dónde están las fichas PMO? → estado-pmo/records (PRY-310)

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `2026-08/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 3 hallazgos. Dos cosas que no coinciden con lo que pide el comando:

- **Línea "El resultado":** en el archivo `salida-budget-scan.md` la sección está vacía, igual que en el reporte del motor. La nota entre paréntesis solo está aquí.
- **Reporte del motor:** el comando dice que queda en `presupuesto/2026/reporte-budget-scan.md`. No comprobé que ese archivo exista. En esa carpeta solo vi `reporte-variance-report.md`, `resultados.json` y `ficha.json`.