# /criterio-risk-appetite:limit-check 

Un límite excedido no tiene plan de acción ni aprobación. El reporte completo sigue abajo.

# Cada exposición contra su límite · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `limit-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-11-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Cartera vencida de consumo | máximo 6 % | 6.4 | sí | — | Crédito | 2026-11-06 |
| L-02 | Indicador de cobertura de liquidez | mínimo 120 % | 131 | no | — | Tesorería | 2026-11-10 |
| L-03 | Concentración en el mayor deudor | máximo 10 % | 11.2 | sí | plan | Crédito | 2026-11-05 |
| L-04 | Pérdidas por fraude externo sobre ingresos | máximo 0.5 % | 0.62 | sí | aprobado | Operaciones | 2026-11-07 |
| L-05 | Exposición a contrapartes sin calificación | máximo 15 % | 12 | no | — | Tesorería | 2026-11-09 |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01, F-11 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-limit-check-1`.