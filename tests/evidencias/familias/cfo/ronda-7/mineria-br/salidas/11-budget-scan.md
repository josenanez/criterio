# /criterio-budget:budget-scan 

Inventario sin archivos nuevos ni cambiados; las tres actas de `40-actas/` ya estaban en la ficha y coinciden con su texto. El cálculo dejó cinco señales: dos traslados sin acta, dos filas del informe de Comercial con la versión 1 y una proyección vencida.

# Qué cambió en el presupuesto · Mineração Serra Azul · presupuesto 2026, corte 2026-09

**Entidad:** Mineração Serra Azul (28903114000160) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.12.1 · **Aprueba:** Sofia Leão · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operações · Transporte: cambió 48.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 48.000,00 | — | — | `presupuesto-2026/10-aprobado/orcamento-2026-v2-2026-06-30.xlsx` · `presupuesto-2026/10-aprobado/orcamento-2026-v1-2026-01-15.xlsx` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnologia · Licenças: cambió -48.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -48.000,00 | — | — | `presupuesto-2026/10-aprobado/orcamento-2026-v2-2026-06-30.xlsx` · `presupuesto-2026/10-aprobado/orcamento-2026-v1-2026-01-15.xlsx` |
| 3 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/projecao-comercial-2026-09-30.xlsx: Comercial · Eventos usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/projecao-comercial-2026-09-30.xlsx` fila 3 |
| 4 | El informe usa una versión del presupuesto distinta de la aprobada (`budget_version_mismatch`) | presupuesto-2026/30-proyecciones/projecao-comercial-2026-09-30.xlsx: Comercial · Publicidade usa la versión 1 y la aprobada es la 2 | — | — | — | `presupuesto-2026/30-proyecciones/projecao-comercial-2026-09-30.xlsx` fila 2 |
| 5 | La proyección del área no se actualizó en los días configurados (`forecast_stale`) | Operações · Transporte: la proyección del área es del 2026-07-15, hace 83 días | — | — | 83 | `presupuesto-2026/30-proyecciones/projecao-operacoes-2026-07-15.csv` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Mineração Serra Azul (28903114000160), 2026, corte 2026-09 (sugerido por los documentos)
- ¿Cuál es la versión aprobada? → La más reciente de 10-aprobado/ (v2, 2026-06-30); la v1 la aprueba el acta del 2026-01-20
- ¿Dónde están las fichas de proyectos PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Fechas del comité de presupuesto? → No encontradas en los documentos; quedan vacías

## Fuentes

- `presupuesto-2026/10-aprobado/orcamento-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/orcamento-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/projecao-comercial-2026-09-30.xlsx`
- `presupuesto-2026/30-proyecciones/projecao-operacoes-2026-07-15.csv`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con cinco hallazgos.

Dos notas sobre cómo corrió:
- **Términos:** ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez (fecha 2026-10-06, versión 1.3). No hubo nada que registrar.
- **El resultado:** la sección «El resultado» salió vacía en el reporte. Es lo que entregó el motor y no la llené.