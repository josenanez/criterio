# /criterio-risk-appetite:appetite-scan 

La ficha de este periodo ya tenía la revisión de la declaración por la junta y los tres excesos que aprobó el comité (L-04, L-06 y L-07). El acta solo dice que el comité «toma conhecimento» del plan de L-03, así que eso no se contó como aprobación del exceso. Revisen las filas de L-02 y L-22 en la tabla de límites: les falta una celda, y por eso el motor no les encuentra dueño.

# Qué cambió en el apetito · Cooperativa Vale Sintética · periodo 2026-10

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `appetite-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-12 · Carteira vencida imobiliária: la exposición de 2026-10 es 4.6 % y el límite máximo es 4; no hay plan de acción ni aprobación del exceso | 0,60 | Diretoria de crédito | — | `00-marco/limites.xlsx` fila 9 · `10-exposicion/exposicao_2026-10.xlsx` fila 9 |
| 2 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Carteira vencida de crédito pessoal: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0,40 | Diretoria de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicao_2026-10.xlsx` fila 2 |
| 3 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidade de negócios: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnologia | — | `00-marco/matriz_de_riscos.xlsx` fila 5 |
| 4 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-12 · Risco de taxa de juros: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tesouraria | — | `00-marco/matriz_de_riscos.xlsx` fila 8 |
| 5 | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco (`appetite_statement_outdated`) | Declaração de apetite por riscos: la junta la revisó el 2025-08-28, y el marco pide revisarla cada 12 meses: tocaba el 2026-08-28 | — | — | 89 | `00-marco/declaracao_de_apetite.pdf` |
| 6 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Índice de liquidez de curto prazo: Tesouraria reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 8 | `10-exposicion/exposicao_2026-10.xlsx` fila 3 |
| 7 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-42 · Limites de contraparte utilizados: Tesouraria reportó su exposición de 2026-10 el 2026-11-16, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesouraria | 6 | `10-exposicion/exposicao_2026-10.xlsx` fila 12 |
| 8 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Índice de liquidez de curto prazo: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |
| 9 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-22 · Concentração setorial da carteira: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 10 |
| 10 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-32 · Exposição em moeda estrangeira: su revisión tocaba el 2026-05-31 | — | Tesouraria | 178 | `00-marco/limites.xlsx` fila 11 |
| 11 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Índice de liquidez de curto prazo: su revisión tocaba el 2026-06-30 | — | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Límites en el marco:** 11 · **Con exposición reportada:** 11 · **Excedidos:** 6 · **Riesgos altos o críticos en la matriz:** 6 · **Excesos aprobados en las actas:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/declaracao_de_apetite.pdf`
- `00-marco/limites.xlsx`
- `00-marco/matriz_de_riscos.xlsx`
- `10-exposicion/exposicao_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)