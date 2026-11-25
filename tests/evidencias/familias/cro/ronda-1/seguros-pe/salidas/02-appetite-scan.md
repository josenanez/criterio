# /criterio-risk-appetite:appetite-scan 

The terms are current (accepted by José Francisco Ñáñez). The period sheet already held what the documents say: the board's review of the appetite statement and the one breach the committee approved, L-04. The committee only "took note" of the L-03 action plan, so I did not record that as an approval. There were no questions to answer.

# Qué cambió en el apetito · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `appetite-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0.40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 2 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |
| 3 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | — | Tesorería | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Límites en el marco:** 5 · **Con exposición reportada:** 5 · **Excedidos:** 3 · **Riesgos altos o críticos en la matriz:** 5 · **Excesos aprobados en las actas:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- `00-marco/matriz_de_riesgos.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

This run is logged as `2026-11-25-appetite-scan-1`. What I showed you is saved in `<espacio>/estado-riesgos/20607773331-seguros-del-sur-sintetica/corridas/salida-appetite-scan.md`.