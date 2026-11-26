# /criterio-risk-appetite:limit-check 

Corrí el periodo 2026-10, el último con exposición reportada. El de 2026-11 sigue abierto hasta el 2026-12-10 y no tiene reportes todavía.

# Cada exposición contra su límite · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Agente:** Severo, versión 0.2.0

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Exceso sin plan ni aprobación | L-12 · Cartera vencida de vivienda: 4.6 % contra un máximo de 4 % | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 2 | Exceso sin plan ni aprobación | L-01 · Cartera vencida de consumo: 6.4 % contra un máximo de 6 % | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 3 | Reporte fuera de plazo | L-02 · Cobertura de liquidez: Tesorería reportó el 2026-11-18 y el plazo vencía el 2026-11-10 | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 4 | Reporte fuera de plazo | L-42 · Cupos de contraparte: Tesorería reportó el 2026-11-16 y el plazo vencía el 2026-11-10 | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 12 |

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

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `00-marco/limites.xlsx`, `10-exposicion/exposicion_2026-10.xlsx`; fuentes técnicas F-01 y F-11.

La corrida quedó registrada como `2026-11-25-limit-check-1` y la salida está en `corridas/salida-limit-check.md`.

Pasé a este reporte un resumen de las tablas del motor. La versión entera está en `apetito/2026-10/reporte-limit-check.md`.

Antes de este reporte generé también uno de 2026-11. No tiene exposición reportada y su archivo quedó en `apetito/2026-11/`.