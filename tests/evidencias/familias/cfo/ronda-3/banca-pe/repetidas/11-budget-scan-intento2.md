# /criterio-budget:budget-scan 

Se leyeron las tres actas de `40-actas` (aprobación, traslado y comité) y la ficha ya las recogía, sin cambios. El motor levantó 14 señales; van abajo tal cual. Cambiaron dos extractos bancarios de 2026-09, que no son del presupuesto.

# Qué cambió en el presupuesto · Banco Ribera · presupuesto 2026, corte 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 16,200.00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 19,200.00 entre la versión 1 y la 2 sin acta que lo apruebe | 19,200.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -19,200.00 entre la versión 1 y la 2 sin acta que lo apruebe | -19,200.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 124,200.00 contra 108,000.00 aprobado al corte (+15.0 %) | 16,200.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` fila 2 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 2 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 2 |
| 5 | La proyección al cierre del año supera lo aprobado (`forecast_over_approved`) | Operaciones · Transporte: la proyección al cierre, la del área, es 183,456.00 y lo aprobado 168,000.00 | 15,456.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` fila 8 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 14 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 14 |
| 6 | La proyección al cierre del año supera lo aprobado (`forecast_over_approved`) | Comercial · Eventos: la proyección al cierre, la del área, es 82,320.00 y lo aprobado 72,000.00 | 10,320.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` fila 5 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 8 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 8 |
| 7 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-administracion-2026-09-30.xlsx: Administración · Mantenimiento usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-administracion-2026-09-30.xlsx` fila 3 |
| 8 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-administracion-2026-09-30.xlsx: Administración · Servicios públicos usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-administracion-2026-09-30.xlsx` fila 2 |
| 9 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-comercial-2026-09-30.xlsx: Comercial · Eventos usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx` fila 3 |
| 10 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-comercial-2026-09-30.xlsx: Comercial · Publicidad usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx` fila 2 |
| 11 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-operaciones-2026-09-30.csv: Operaciones · Transporte usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-09-30.csv` fila 2 |
| 12 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-personal-2026-09-30.csv: Personal · Nómina usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-personal-2026-09-30.csv` fila 2 |
| 13 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-tecnologia-2026-09-30.xlsx: Tecnología · Licencias usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-tecnologia-2026-09-30.xlsx` fila 2 |
| 14 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | proyeccion-tecnologia-2026-09-30.xlsx: Tecnología · PRY-310 usa la versión 2 y la aprobada es la 1 | — | — | — | `presupuesto-2026/30-proyecciones/proyeccion-tecnologia-2026-09-30.xlsx` fila 3 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La 1: el acta 01 del 2026-01-20 la aprueba. El acta 05 solo aprueba un traslado; ningún acta aprueba la 2 (sugerida por los documentos, sin respuesta de la persona)

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`
- `presupuesto-2026/30-proyecciones/proyeccion-administracion-2026-09-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-comercial-2026-09-30.xlsx`
- `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-09-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-personal-2026-09-30.csv`
- `presupuesto-2026/30-proyecciones/proyeccion-tecnologia-2026-09-30.xlsx`

Dos precisiones sobre lo anterior:

- En las filas 7 a 14 del reporte original, la columna "Qué" empezaba con la ruta completa (`presupuesto-2026/30-proyecciones/…`). Aquí la acorté al nombre del archivo. La ruta completa sigue en la columna "Cita". El reporte guardado en `estado-finanzas/20710000019-banco-ribera/presupuesto/2026/reporte-budget-scan.md` tiene el texto original.
- Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez (versión 1.2, 2026-10-06), así que no hizo falta registrar nada nuevo. La corrida quedó registrada con el motor como `2026-10-06-budget-scan-2`, con las 14 señales.