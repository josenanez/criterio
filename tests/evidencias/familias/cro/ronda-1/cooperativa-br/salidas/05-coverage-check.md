# /criterio-risk-appetite:coverage-check 

Nota: la tabla marca a R-04 sin límite y a R-06 sin indicador, aunque "Lo que hay que atender" sale vacío. Ese apartado solo cubre lo que procesa este comando. Si esos riesgos necesitan un límite o un indicador lo decide el comité de riesgos.

Los términos (versión 1.6) ya estaban vigentes. No tuve que registrar la aceptación de José Francisco Ñáñez, y este comando no la registra.

# Cada riesgo alto con su límite · Cooperativa Vale Sintética · periodo 2026-11

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `coverage-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Riesgo | Calificación | Con límite | Con indicador |
|---|---|---|---|
| R-01 · Risco de crédito pessoal | Alto | sí | sí |
| R-02 · Risco de liquidez | Crítico | sí | sí |
| R-03 · Fraude externa nos canais | Alto | sí | sí |
| R-04 · Continuidade de negócios | Alto | no | sí |
| R-06 · Risco de contraparte | Alto | sí | no |

Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos.

## Lo que no se pudo procesar

- `10-exposicion/exposicao_2026-10.xlsx`: L-01 · Carteira vencida de crédito pessoal: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-02 · Índice de liquidez de curto prazo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-03 · Concentração no maior devedor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-04 · Perdas por fraude externa sobre receitas: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-05 · Exposição a contrapartes sem rating: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-coverage-check-1`, con 3 hallazgos. Lo que te mostré está en `corridas/salida-coverage-check.md`, dentro de la carpeta de estado de la entidad.