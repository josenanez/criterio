# /criterio-risk-appetite:coverage-check 

Los términos ya estaban aceptados a nombre de José Francisco Ñáñez (2026-11-25), y el reporte salió para el periodo 2026-10 de la configuración.

# Cada riesgo alto con su límite · Seguros del Sur Sintética · periodo 2026-10

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `coverage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Riesgo de crédito de consumo | Alto | sí | sí |
| R-02 · Riesgo de liquidez | Crítico | sí | sí |
| R-03 · Fraude externo en canales | Alto | sí | sí |
| R-04 · Continuidad del negocio | Alto | no | no |
| R-06 · Riesgo de contraparte | Alto | sí | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---
La corrida quedó registrada como `2026-11-25-coverage-check-1`. El motor la registró con 3 hallazgos, aunque el reporte solo muestra 1 señal. No sé a qué se debe esa diferencia y no la investigué.