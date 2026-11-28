# /criterio-risk-appetite:limit-check 

Los términos (versión 1.6) ya estaban vigentes con una aceptación anterior, así que no hubo nada nuevo que registrar a nombre de José Francisco Ñáñez. El reporte lo escribió el motor y va tal cual.

# Cada exposición contra su límite · Banco Mesoamericano Sintético · periodo 2026-10

**Entidad:** Banco Mesoamericano Sintético (BMS0907153R2) · **Fecha de corte:** 2026-11-25 · **Agente:** Severo, versión 1.0.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Exposición sobre el límite, sin plan ni aprobación (`limit_breached_without_plan`) | L-12 · Cartera vencida de vivienda: la exposición de 2026-10 es 4.6 % y el límite máximo es 4 | 0.60 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 2 | Exposición sobre el límite, sin plan ni aprobación (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6 | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 3 | Reporte fuera de plazo (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó el 2026-11-18; el plazo del marco era hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 4 | Reporte fuera de plazo (`exposure_report_late`) | L-42 · Cupos de contraparte utilizados: Tesorería reportó el 2026-11-16; el plazo del marco era hasta el 2026-11-10 | — | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 12 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máx. 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Cobertura de liquidez | mín. 120 % | 131 | no | — | Tesorería | 2026-11-18 |
| L-03 | Concentración en el mayor deudor | máx. 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo / ingresos | máx. 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Contrapartes sin calificación | máx. 15 % | 12 | no | — | Tesorería | 2026-11-09 |
| L-06 | Pérdidas operacionales / patrimonio | máx. 1 % | 1.1 | sí | aprobado | Operaciones | 2026-11-08 |
| L-07 | Mayor banco corresponsal | máx. 20 % | 23 | sí | aprobado | Tesorería | 2026-11-09 |
| L-12 | Cartera vencida de vivienda | máx. 4 % | 4.6 | sí | — | Vicepresidencia de crédito | 2026-11-06 |
| L-22 | Concentración sectorial | máx. 25 % | 21 | no | — | Vicepresidencia de crédito | 2026-11-05 |
| L-32 | Moneda extranjera | máx. 20 % | 14 | no | — | Tesorería | 2026-11-04 |
| L-42 | Cupos de contraparte utilizados | máx. 80 % | 62 | no | — | Tesorería | 2026-11-16 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

**Lo que no se pudo procesar:** todo se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `00-marco/limites.xlsx`, `10-exposicion/exposicion_2026-10.xlsx`, F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-limit-check-1`, con 11 hallazgos. La salida está en `corridas/salida-limit-check.md`, dentro de la carpeta de estado.