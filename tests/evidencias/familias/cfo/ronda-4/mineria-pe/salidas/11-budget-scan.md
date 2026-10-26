# /criterio-budget:budget-scan 

Cambió poco: las tres actas ya estaban en la ficha y no hubo archivos nuevos ni cambiados. Salen cuatro señales, dos de ellas por una proyección de Comercial que sigue en la versión 1.

# Qué cambió en el presupuesto · Minera Puna Alta · presupuesto 2026, corte 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv: Comercial · Eventos usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv` fila 3 |
| 2 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv: Comercial · Publicidad usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv` fila 2 |
| 3 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -5,700.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 4 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 4 |
| 4 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operaciones · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado/ (v2, 2026-06-30), nacida del traslado del acta 05; el acta 01 aprueba la v1 el 2026-01-20
- ¿Umbrales? → Los del ejemplo: desviación 10 %, comprometido 95 %, proyección vencida 45 días
- ¿Fechas del comité? → Ninguna registrada; ningún documento las trae
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

La sección «El resultado» salió vacía porque el motor no escribió nada en ella; no la rellené. La corrida quedó registrada como `2026-10-06-budget-scan-1` con 4 hallazgos.