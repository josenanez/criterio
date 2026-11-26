# /criterio-risk-appetite:coverage-check 

De los seis riesgos altos o críticos de la matriz, dos no tienen límite ni indicador clave. Lo que sigue es el reporte del motor, tal cual.

Los términos (versión 1.6) ya estaban vigentes y aceptados desde el setup, así que no registré una aceptación nueva.

# Cada riesgo alto con su límite · Seguros del Sur Sintética · periodo 2026-11

**Entidad:** Seguros del Sur Sintética (20607773331) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `coverage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |
| 2 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-12 · Riesgo de tasa de interés: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tesorería | — | `00-marco/matriz_de_riesgos.xlsx` fila 8 |

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Riesgo de crédito de consumo | Alto | sí | sí |
| R-02 · Riesgo de liquidez | Crítico | sí | sí |
| R-03 · Fraude externo en canales | Alto | sí | sí |
| R-04 · Continuidad del negocio | Alto | no | no |
| R-06 · Riesgo de contraparte | Alto | sí | no |
| R-12 · Riesgo de tasa de interés | Alto | no | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

- `10-exposicion/exposicion_2026-10.xlsx`: ningún área reportó su exposición de 2026-11 para L-01, L-02, L-03, L-04, L-05, L-06, L-07, L-12, L-22, L-32 y L-42 (11 límites).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La salida quedó en `corridas/salida-coverage-check.md` y la corrida se registró como `2026-11-25-coverage-check-1`.

Nota: en "Lo que no se pudo procesar" agrupé en una línea los 11 límites que el reporte del motor lista por separado. Cada uno trae el mismo motivo. El archivo del reporte y el de la corrida conservan el detalle completo.