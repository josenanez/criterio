# /criterio-risk-appetite:appetite-scan 

Los términos están vigentes. La ficha del periodo ya tenía la declaración de apetito con su última revisión por la junta y los tres excesos que aprobó el comité en el acta. Sobre L-03 el acta solo dice que el comité "toma nota" del plan, así que no lo registré como aprobación.
No quedaron documentos fuera de la ficha ni preguntas pendientes. Este es el reporte del motor:

# Qué cambió en el apetito · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `appetite-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-13 · Cartera vencida comercial: la exposición de 2026-10 es 5.9 % y el límite máximo es 5; no hay plan de acción ni aprobación del exceso | 0,90 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 10 · `10-exposicion/exposicion_2026-10.xlsx` fila 10 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Cartera vencida de vivienda: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0,60 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 3 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0,40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 4 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |
| 5 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-12 · Riesgo de tasa de interés: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tesorería | — | `00-marco/matriz_de_riesgos.xlsx` fila 8 |
| 6 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-13 · Riesgo de modelo: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Gerencia de riesgos | — | `00-marco/matriz_de_riesgos.xlsx` fila 9 |
| 7 | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco (`appetite_statement_outdated`) | Declaración de apetito por riesgo: la junta la revisó el 2025-08-28, y el marco pide revisarla cada 12 meses: tocaba el 2026-08-28 | — | — | 89 | `00-marco/declaracion_de_apetito.pdf` |
| 8 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-43 · Pérdidas por errores operativos sobre ingresos: Operaciones reportó su exposición de 2026-10 el 2026-11-21, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Operaciones | 11 | `10-exposicion/exposicion_2026-10.xlsx` fila 16 |
| 9 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 10 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Cupos de contraparte utilizados: Tesorería reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 15 |
| 11 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Indicador de cobertura de liquidez: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |
| 12 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-22 · Concentración sectorial de la cartera: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 11 |
| 13 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-23 · Descalce de plazos a 30 días: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 12 |
| 14 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-33 · Inversiones de baja liquidez: su revisión tocaba el 2026-04-30 | — | Tesorería | 209 | `00-marco/limites.xlsx` fila 14 |
| 15 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-32 · Exposición en moneda extranjera: su revisión tocaba el 2026-05-31 | — | Tesorería | 178 | `00-marco/limites.xlsx` fila 13 |
| 16 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | — | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Límites en el marco:** 15 · **Con exposición reportada:** 15 · **Excedidos:** 7 · **Riesgos altos o críticos en la matriz:** 7 · **Excesos aprobados en las actas:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/declaracion_de_apetito.pdf`
- `00-marco/limites.xlsx`
- `00-marco/matriz_de_riesgos.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)