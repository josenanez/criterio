# /criterio-budget:budget-scan 

Inventario sin archivos nuevos, cambiados ni borrados; las tres actas ya estaban en la ficha. Tres señales, abajo.

# Qué cambió en el presupuesto · Almacenes de la Meseta · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes de la Meseta (3101612904) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.0.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Días | Cita |
|---|---|---|---|---|---|
| 1 | Gasto sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 525.000,00 en 2026-08 sin línea presupuestal | 525.000,00 | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |
| 2 | Ejecutado más comprometido cerca de lo aprobado (`committed_near_approved`) | Administración · Mantenimiento: 96,0 % de lo aprobado en el año | -712.500,00 | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · libro mayor 2026-01 fila 4 · libro mayor 2026-02 fila 4 |
| 3 | Proyección del área vencida (`forecast_stale`) | Operaciones · Transporte: proyección del 2026-07-15, hace 83 días | — | 83 | `presupuesto-2026/30-proyecciones/proyeccion-operaciones-2026-07-15.xlsx` fila 2 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La vigente es la más reciente de 10-aprobado (v2, 2026-06-30); el acta 01 aprueba la v1 y el acta 05 el traslado de 2,250,000.00 de Publicidad a Eventos.
- ¿Fechas del comité de presupuesto? → No encontrado: el acta 06 dice «próximo comité» sin fecha.
- ¿Dejo la marca `_CRITERIO_FINANZAS.txt` en la raíz? → No.

## Fuentes

Libros mayores 2026-01, 2026-02 y 2026-08; presupuesto v2 (2026-06-30); proyección de Operaciones (2026-07-15).

---
Dos notas de la corrida:
- Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez (2026-10-06), así que no hubo nada que registrar.
- La sección «El resultado» del reporte salió vacía; el motor no la llenó y no la completé.

La salida quedó en `estado-finanzas/3101612904-almacenes-de-la-meseta/corridas/salida-budget-scan.md`. La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 3 hallazgos.