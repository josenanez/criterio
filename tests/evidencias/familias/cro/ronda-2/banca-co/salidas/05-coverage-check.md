# /criterio-risk-appetite:coverage-check 

Tres riesgos altos (R-04, R-12 y R-13) no tienen límite ni indicador clave. Si necesitan uno lo decide el comité de riesgos.

# Cada riesgo alto con su límite · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `coverage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |
| 2 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-12 · Riesgo de tasa de interés: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tesorería | — | `00-marco/matriz_de_riesgos.xlsx` fila 8 |
| 3 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-13 · Riesgo de modelo: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Gerencia de riesgos | — | `00-marco/matriz_de_riesgos.xlsx` fila 9 |

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Riesgo de crédito de consumo | Alto | sí | sí |
| R-02 · Riesgo de liquidez | Crítico | sí | sí |
| R-03 · Fraude externo en canales | Alto | sí | sí |
| R-04 · Continuidad del negocio | Alto | no | no |
| R-06 · Riesgo de contraparte | Alto | sí | no |
| R-12 · Riesgo de tasa de interés | Alto | no | no |
| R-13 · Riesgo de modelo | Alto | no | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

- `10-exposicion/exposicion_2026-10.xlsx`: L-01 · Cartera vencida de consumo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-02 · Indicador de cobertura de liquidez: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-03 · Concentración en el mayor deudor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-04 · Pérdidas por fraude externo sobre ingresos: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-05 · Exposición a contrapartes sin calificación: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-06 · Pérdidas operacionales sobre el patrimonio: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-07 · Exposición al mayor banco corresponsal: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-12 · Cartera vencida de vivienda: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-13 · Cartera vencida comercial: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-22 · Concentración sectorial de la cartera: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-23 · Descalce de plazos a 30 días: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-32 · Exposición en moneda extranjera: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-33 · Inversiones de baja liquidez: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-42 · Cupos de contraparte utilizados: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-43 · Pérdidas por errores operativos sobre ingresos: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-coverage-check-1`, con 16 hallazgos. La salida completa está en `estado-riesgos/901777333-banco-andino-sintetico/corridas/salida-coverage-check.md`.

Dos aclaraciones sobre cómo corrió:
- Los términos ya estaban vigentes (versión 1.6, aceptada con la versión 0.2.0 del plugin), así que no hizo falta registrar de nuevo la aceptación a nombre de José Francisco Ñáñez.
- No hubo preguntas que contestar.