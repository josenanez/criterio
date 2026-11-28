# /criterio-risk-appetite:appetite-scan 

Los once documentos de la carpeta entraron como nuevos en esta corrida. La ficha del periodo ya registraba la revisión de la declaración por la junta y los tres excesos que aprobó el comité. La mención del límite L-03 en el acta es una toma de nota de su plan, no una aprobación, así que no entra como tal.
La decisión sobre cada señal es de la junta, del comité de riesgos y de las áreas.

# Qué cambió en el apetito · Banco del Pichincha Sur Sintético · periodo 2026-10

**Entidad:** Banco del Pichincha Sur Sintético (1790123456001) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 1.1.0 · **Comando:** `appetite-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Cartera vencida de vivienda: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0.60 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicion_2026-10.xlsx` fila 9 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 3 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |
| 4 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-12 · Riesgo de tasa de interés: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tesorería | — | `00-marco/matriz_de_riesgos.xlsx` fila 8 |
| 5 | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco (`appetite_statement_outdated`) | Declaración de apetito por riesgo: la junta la revisó el 2025-08-28, y el marco pide revisarla cada 12 meses: tocaba el 2026-08-28 | — | — | 89 | `00-marco/declaracion_de_apetito.pdf` |
| 6 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 7 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Cupos de contraparte utilizados: Tesorería reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 6 | `10-exposicion/exposicion_2026-10.xlsx` fila 12 |
| 8 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Indicador de cobertura de liquidez: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |
| 9 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-22 · Concentración sectorial de la cartera: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 10 |
| 10 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-32 · Exposición en moneda extranjera: su revisión tocaba el 2026-05-31 | — | Tesorería | 178 | `00-marco/limites.xlsx` fila 11 |
| 11 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | — | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Límites en el marco:** 11 · **Con exposición reportada:** 11 · **Excedidos:** 6 · **Riesgos altos o críticos en la matriz:** 6 · **Excesos aprobados en las actas:** 3.

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