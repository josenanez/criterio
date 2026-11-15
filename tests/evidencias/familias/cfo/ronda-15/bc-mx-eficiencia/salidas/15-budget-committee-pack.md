# /criterio-budget:budget-committee-pack 

Términos vigentes (aceptados por José Francisco Ñáñez, 2026-10-06). El compromiso del acta 06 sigue abierto: no hay evidencia en los documentos. El paquete no recomienda la decisión; la toma el comité.

# Paquete del comité de presupuesto · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `budget-committee-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

| Compromiso del comité anterior | Responsable | Estado | Evidencia |
|---|---|---|---|
| Revisar el contrato de vigilancia antes del próximo comité | Administración | abierto | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Distribuidora del Noroeste (DNO190402B43), 2026.
- ¿Cuál es la versión aprobada? → La versión 2 (2026-06-30), que nace del traslado del acta 05 sobre la versión 1 del acta 01.
- ¿Áreas y su responsable? → Responsables: no encontrados en los documentos.
- ¿Mapeo de cuentas a líneas? → `00-referencia/mapeo-presupuesto.csv`
- ¿Umbrales? → Desviación 10 %, comprometido 95 %, proyección vencida a los 45 días.
- ¿Fechas del comité? → No encontradas; el acta 06 menciona un próximo comité sin fecha.
- ¿Fichas PMO? → `estado-pmo/records` (PRY-310.json)
- ¿Dónde guardo el estado? → `estado-finanzas/DNO190402B43-distribuidora-del-noroeste`

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

La corrida quedó registrada como `2026-10-06-budget-committee-pack-1`, con 1 hallazgo. El reporte completo del motor está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/presupuesto/2026/reporte-budget-committee-pack.md`.

Dos aclaraciones sobre lo que escribí:
- Las preguntas de arriba son un resumen de las que trae el reporte del motor. En el archivo de la corrida guardé el reporte con el texto original del motor, no este resumen.
- El archivo de la corrida lleva además la línea inicial sobre los términos y el compromiso abierto, con la que empieza este mensaje.