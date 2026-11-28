# /criterio-risk-appetite:coverage-check 

Los términos están vigentes (versión 1.6, aceptación registrada). Dos riesgos altos de la matriz no tienen límite ni indicador que los mida.

# Cada riesgo alto con su límite · Banco Mesoamericano Sintético · periodo 2026-11

**Entidad:** Banco Mesoamericano Sintético (BMS0907153R2) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 1.0.0 · **Comando:** `coverage-check`

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

- `10-exposicion/exposicion_2026-10.xlsx`: L-01, L-02, L-03, L-04, L-05, L-06, L-07, L-12, L-22, L-32 y L-42: ningún área reportó su exposición de 2026-11 (11 límites en total; el motor da el detalle de cada nombre en el reporte).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/matriz_de_riesgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

La corrida quedó registrada como `2026-11-25-coverage-check-1`. El reporte completo está en `apetito/2026-11/reporte-coverage-check.md`, dentro de la carpeta de estado.

Dos precisiones sobre lo que muestro arriba:
- En "Lo que no se pudo procesar" resumí los 11 límites en una sola línea. El reporte del motor los lista uno por uno con su nombre, y el archivo de salida guardado tiene esa versión completa.
- No fijo ni cambio ningún límite. Si R-04 y R-12 necesitan límite o indicador lo decide el comité de riesgos.