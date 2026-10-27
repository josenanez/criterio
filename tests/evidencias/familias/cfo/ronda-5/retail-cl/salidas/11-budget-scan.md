# /criterio-budget:budget-scan 

Sin archivos nuevos, cambiados ni borrados desde la corrida anterior. Las tres actas de `40-actas` ya estaban en la ficha, así que no cambió nada. El motor reporta 4 señales.

# Qué cambió en el presupuesto · Tiendas Pacífico · presupuesto 2026, corte 2026-09

**Entidad:** Tiendas Pacífico (76083001-1) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La proyección al cierre del año supera lo aprobado (`forecast_over_approved`) | Tecnología · PRY-310: la proyección al cierre, la del área, es 19.800.000,00 y lo aprobado 18.000.000,00 | 1.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 7 · `2026-01/10-contabilidad/libro-mayor.csv` fila 12 · `2026-02/10-contabilidad/libro-mayor.csv` fila 12 |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 1.200.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 1.200.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -1.200.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -1.200.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 175.000,00 en 2026-08 sin línea presupuestal | 175.000,00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La vigente es la más reciente de 10-aprobado (v2, 2026-06-30); la v1 la aprueba el acta 01 del 2026-01-20 y la v2 nace del traslado del acta 05 del 2026-06-28
- ¿Áreas y responsables? → Las áreas salen del presupuesto; no hay documento que nombre responsables, quedan sin registrar
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida a 45 días
- ¿Fechas del comité? → No hay en los documentos; queda vacío
- ¿Fichas del PMO? → estado-pmo/records, donde existe PRY-310.json

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `2026-08/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`. El texto mostrado está en `estado-finanzas/76083001-1-tiendas-pacifico/corridas/salida-budget-scan.md`.