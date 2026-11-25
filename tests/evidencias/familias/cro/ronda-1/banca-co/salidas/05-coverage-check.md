# /criterio-risk-appetite:coverage-check 

Un riesgo alto sin límite ni indicador clave y un riesgo alto sin indicador; los demás están cubiertos. Si cada riesgo necesita un límite o un indicador lo decide el comité de riesgos.

# Cada riesgo alto con su límite · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `coverage-check`

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

- `10-exposicion/exposicion_2026-10.xlsx`: L-01 · Cartera vencida de consumo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-02 · Indicador de cobertura de liquidez: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-03 · Concentración en el mayor deudor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-04 · Pérdidas por fraude externo sobre ingresos: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-05 · Exposición a contrapartes sin calificación: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---
La corrida quedó registrada como `2026-11-25-coverage-check-1`. La salida completa está en `estado-riesgos/901777333-banco-andino-sintetico/corridas/salida-coverage-check.md`.

Dos cosas que no coinciden con lo que pedía el encargo:

- **Términos:** ya estaban vigentes y aceptados (versión 1.6, aceptación del 2026-11-25). No hizo falta registrar la aceptación de José Francisco Ñáñez, así que no la repetí.
- **`--today`:** `reporte` y `corrida` aceptaron `--today 2026-11-25`, pero el comando `terminos` no lo acepta y lo corrí sin él.