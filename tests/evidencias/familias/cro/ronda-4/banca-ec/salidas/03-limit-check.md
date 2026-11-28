# /criterio-risk-appetite:limit-check 

# Cada exposición contra su límite · Banco del Pichincha Sur Sintético · periodo 2026-10

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 1.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Cartera vencida de vivienda: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0.60 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 3 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 4 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Cupos de contraparte utilizados: Tesorería reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 12 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-18 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |
| L-06 | Pérdidas operacionales sobre el patrimonio | máximo 1 % | 1.1 | sí | aprobado | Operaciones | 2026-11-08 |
| L-07 | Exposición al mayor banco corresponsal | máximo 20 % | 23 | sí | aprobado | Tesorería | 2026-11-09 |
| L-12 | Cartera vencida de vivienda | máximo 4 % | 4.6 | sí | — | Vicepresidencia de crédito | 2026-11-06 |
| L-22 | Concentración sectorial de la cartera | máximo 25 % | 21 | no | — | Vicepresidencia de crédito | 2026-11-05 |
| L-32 | Exposición en moneda extranjera | máximo 20 % | 14 | no | — | Tesorería | 2026-11-04 |
| L-42 | Cupos de contraparte utilizados | máximo 80 % | 62 | no | — | Tesorería | 2026-11-16 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)