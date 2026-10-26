# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (59 en el inventario). Las tres actas ya estaban en la ficha y coinciden con su texto. Los términos 1.2 estaban vigentes, con la aceptación de José Francisco Ñáñez del 2026-10-06. Salen cuatro señales.

# Qué cambió en el presupuesto · Cooperativa Sierra Alta · presupuesto 2026, corte 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx: Comercial · Eventos usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx` fila 3 |
| 2 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx: Comercial · Publicidad usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx` fila 2 |
| 3 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Tecnología · Licencias: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -2,390.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 6 · `2026-01/10-contabilidad/libro-mayor.csv` fila 10 · `2026-02/10-contabilidad/libro-mayor.csv` fila 10 |
| 4 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Sugerida: la más reciente de 10-aprobado/ (v2, 2026-06-30), nacida del traslado del acta 05; la v1 la aprueba el acta 01 del 2026-01-20
- ¿Áreas y responsables? → Sugerida: Administración, Comercial, Tecnología, Operaciones y Personal, tal como las trae el mapeo; responsable por área no consta en los documentos

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 4 hallazgos.