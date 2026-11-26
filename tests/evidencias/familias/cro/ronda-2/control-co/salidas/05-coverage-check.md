# /criterio-risk-appetite:coverage-check 

Dos huecos de cobertura en la matriz: R-04 no tiene límite y R-06 no tiene indicador; decide el comité de riesgos si los necesitan.

Los términos (versión 1.6) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva.

# Cada riesgo alto con su límite · Banco Control de Riesgos Sintético · periodo 2026-11

**Entidad:** Banco Control de Riesgos Sintético (901888444) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `coverage-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Riesgo de crédito de consumo | Alto | sí | sí |
| R-02 · Riesgo de liquidez | Crítico | sí | sí |
| R-03 · Fraude externo en canales | Alto | sí | sí |
| R-04 · Continuidad del negocio | Alto | no | sí |
| R-06 · Riesgo de contraparte | Alto | sí | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

- `10-exposicion/exposicion_2026-10.xlsx`: L-01 · Cartera vencida de consumo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-02 · Indicador de cobertura de liquidez: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-03 · Concentración en el mayor deudor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-04 · Pérdidas por fraude externo sobre ingresos: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-05 · Exposición a contrapartes sin calificación: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-06 · Pérdidas operacionales sobre el patrimonio: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicion_2026-10.xlsx`: L-07 · Exposición al mayor banco corresponsal: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-coverage-check-1`. La salida completa está en `corridas/salida-coverage-check.md`.