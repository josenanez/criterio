# /criterio-risk-appetite:coverage-check 

Dos riesgos calificados Alto en la matriz, R-04 y R-12, no tienen límite ni indicador clave. Si les corresponde uno lo decide el comité de riesgos.

# Cada riesgo alto con su límite · Cooperativa Vale Sintética · periodo 2026-11

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `coverage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidade de negócios: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnologia | — | `00-marco/matriz_de_riscos.xlsx` fila 5 |
| 2 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-12 · Risco de taxa de juros: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tesouraria | — | `00-marco/matriz_de_riscos.xlsx` fila 8 |

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Risco de crédito pessoal | Alto | sí | sí |
| R-02 · Risco de liquidez | Crítico | sí | sí |
| R-03 · Fraude externa nos canais | Alto | sí | sí |
| R-04 · Continuidade de negócios | Alto | no | no |
| R-06 · Risco de contraparte | Alto | sí | no |
| R-12 · Risco de taxa de juros | Alto | no | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

- `10-exposicion/exposicao_2026-10.xlsx`: L-01 · Carteira vencida de crédito pessoal: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-02 · Índice de liquidez de curto prazo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-03 · Concentração no maior devedor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-04 · Perdas por fraude externa sobre receitas: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-05 · Exposição a contrapartes sem rating: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-06 · Perdas operacionais sobre o patrimônio: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-07 · Exposição ao maior banco correspondente: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-12 · Carteira vencida imobiliária: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-22 · Concentração setorial da carteira: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-32 · Exposição em moeda estrangeira: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-42 · Limites de contraparte utilizados: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riscos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-coverage-check-1`.