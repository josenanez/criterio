# /criterio-budget:budget-scan 

Inventario sin archivos nuevos, cambiados ni borrados (63 en total); las tres actas se leyeron y ya estaban en la ficha. Salieron cuatro señales. Ojo con las dos primeras: el motor toma como aprobada la versión 2 del presupuesto, pero la única acta de aprobación (la 01) aprueba la versión 1. La versión 2 no tiene acta propia, así que conviene que Sofía León confirme cuál rige.

# Qué cambió en el presupuesto · Minera Puna Alta · presupuesto 2026, corte 2026-09

**Entidad:** Minera Puna Alta (20730000015) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

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

- ¿Cuál es la versión aprobada? → La 1, acta 01 del 20 de enero de 2026. La v2 (2026-06-30) no tiene acta de aprobación propia; el acta 05 del 28 de junio aprueba un traslado de 18,000.00. Respuesta sugerida por los documentos, sin confirmar por una persona.
- ¿Fechas del comité de presupuesto? → No encontrado en los documentos; se deja vacío.
- ¿Áreas y responsables? → Áreas tomadas del mapeo: Administración, Comercial, Tecnología, Operaciones, Personal; responsables no encontrados.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 4 hallazgos. La salida completa está en `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-budget-scan.md`.

Dos aclaraciones sobre la sesión:
- **Términos:** ya estaban aceptados en la configuración a nombre de José Francisco Ñáñez (versión 1.2, 2026-10-06), así que no hizo falta registrarlos de nuevo.
- **Preguntas:** no hubo preguntas nuevas. Las de la sección «Las preguntas que hizo» son respuestas sugeridas de corridas anteriores, que siguen sin confirmar por una persona.