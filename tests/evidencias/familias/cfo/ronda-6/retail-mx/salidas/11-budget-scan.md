# /criterio-budget:budget-scan 

Inventario sin archivos nuevos, cambiados ni borrados (65 en total). Las tres actas de `40-actas/` ya estaban en la ficha y coinciden con los originales, así que no la modifiqué. Salieron tres señales.

# Qué cambió en el presupuesto · Tiendas del Bajío · presupuesto 2026, corte 2026-09

**Entidad:** Tiendas del Bajío (TBA180912Q37) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.11.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 10,500.00 en 2026-08 sin línea presupuestal | 10,500.00 | — | — | `2026-08/10-contabilidad/libro-mayor.xlsx` fila 18 |
| 2 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -14,250.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 4 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 4 |
| 3 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado/ (v2, 2026-06-30), que nace del traslado del acta 05; la v1 la aprueba el acta 01 del 20 de enero. No se fijó approved_version.
- ¿Fechas del comité de presupuesto? → Ninguna fecha en los documentos (el acta 06 dice «próximo comité» sin fecha); committee_dates queda vacío.
- ¿Dónde están las fichas de proyectos PMO? → estado-pmo/records (existe, trae PRY-310.json).
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `2026-08/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.xlsx`

La sección «El resultado» salió vacía del motor y la dejé así. La corrida quedó registrada como `2026-10-06-budget-scan-1` con 3 hallazgos. La salida completa está en `estado-finanzas/TBA180912Q37-tiendas-del-bajio/corridas/salida-budget-scan.md`.