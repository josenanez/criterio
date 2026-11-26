# /criterio-risk-appetite:framework-check 

Los términos de esta versión ya estaban vigentes, así que no hizo falta registrar la aceptación. Hay dos límites sin dueño (L-02 y L-22), dos con la revisión vencida (L-32 y L-02), y la declaración de apetito no aparece en la ficha, así que no se pudo medir su revisión por la junta.

# El marco y la declaración · Seguros del Sur Sintética · periodo 2026-11

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Indicador de cobertura de liquidez: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |
| 2 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-22 · Concentración sectorial de la cartera: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 10 |
| 3 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-32 · Exposición en moneda extranjera: su revisión tocaba el 2026-05-31 | — | Tesorería | 178 | `00-marco/limites.xlsx` fila 11 |
| 4 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | — | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

| Límite | Métrica | Dueño | Próxima revisión |
|---|---|---|---|
| L-01 | Cartera vencida de consumo | Vicepresidencia de crédito | 2027-03-31 |
| L-02 | Indicador de cobertura de liquidez | — | 2026-06-30 |
| L-03 | Concentración en el mayor deudor | Vicepresidencia de crédito | 2027-03-31 |
| L-04 | Pérdidas por fraude externo sobre ingresos | Operaciones | 2027-06-30 |
| L-05 | Exposición a contrapartes sin calificación | Tesorería | 2027-06-30 |
| L-06 | Pérdidas operacionales sobre el patrimonio | Operaciones | 2027-06-30 |
| L-07 | Exposición al mayor banco corresponsal | Tesorería | 2027-06-30 |
| L-12 | Cartera vencida de vivienda | Vicepresidencia de crédito | 2027-03-31 |
| L-22 | Concentración sectorial de la cartera | — | 2027-03-31 |
| L-32 | Exposición en moneda extranjera | Tesorería | 2026-05-31 |
| L-42 | Cupos de contraparte utilizados | Tesorería | 2027-06-30 |

Quién es el dueño de un límite y cuándo se revisa lo fija el marco: aquí se dice cuál falta o se venció.

## Lo que no se pudo procesar

- `10-exposicion/exposicion_2026-10.xlsx`: ningún área reportó su exposición de 2026-11 para ninguno de los 11 límites (L-01, L-02, L-03, L-04, L-05, L-06, L-07, L-12, L-22, L-32 y L-42).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01, F-11 (families/criterio-cro/FUENTES.es.md)

Resumí la sección "Lo que no se pudo procesar", que el motor trae como 11 líneas iguales. El archivo guardado en `corridas/salida-framework-check.md` tiene el texto completo del motor.

La corrida quedó registrada como `2026-11-25-framework-check-1`, con 11 hallazgos. El reporte completo está en `apetito/2026-11/reporte-framework-check.md`.