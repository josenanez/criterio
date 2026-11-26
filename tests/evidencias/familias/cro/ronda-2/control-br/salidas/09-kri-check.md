# /criterio-risk-events:kri-check 

Los seis indicadores clave del marco llegaron sin valor en 2026-11, así que ninguno se pudo comparar con su umbral. Los términos estaban vigentes y no hubo preguntas.

# Cada indicador contra su umbral · Cooperativa Controle Sintética · periodo 2026-11

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-01 · Transações fraudulentas por milhão: no tiene valor en 2026-11 | — | Operações | — | `00-marco/indicadores_chave.xlsx` fila 2 |
| 2 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-02 · Disponibilidade dos canais digitais: no tiene valor en 2026-11 | — | Tecnologia | — | `00-marco/indicadores_chave.xlsx` fila 3 |
| 3 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-03 · Rotatividade da equipe de crédito: no tiene valor en 2026-11 | — | Diretoria de crédito | — | `00-marco/indicadores_chave.xlsx` fila 4 |
| 4 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-04 · Dias sem teste do plano de continuidade: no tiene valor en 2026-11 | — | Tecnologia | — | `00-marco/indicadores_chave.xlsx` fila 5 |
| 5 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-05 · Concentração dos depósitos nos 20 maiores: no tiene valor en 2026-11 | — | Tesouraria | — | `00-marco/indicadores_chave.xlsx` fila 6 |
| 6 | Un indicador clave no tiene valor en el periodo (`kri_not_reported`) | KRI-06 · Itens sem conciliar no fim do mês: no tiene valor en 2026-11 | — | Tesouraria | — | `00-marco/indicadores_chave.xlsx` fila 7 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 · Transações fraudulentas por milhão | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 · Disponibilidade dos canais digitais | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 · Rotatividade da equipe de crédito | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-04 · Dias sem teste do plano de continuidade | mayor es peor | 180 | 365 | — | sin valor | no |
| KRI-05 · Concentração dos depósitos nos 20 maiores | mayor es peor | 25 | 30 | — | sin valor | no |
| KRI-06 · Itens sem conciliar no fim do mês | mayor es peor | 5 | 10 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/indicadores_chave.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-kri-check-1`. Su salida está en `corridas/salida-kri-check.md`, dentro de la carpeta de estado de la entidad.

El comando de términos no pidió registrar ninguna aceptación, porque ya estaban vigentes. Por eso no registré a José Francisco Ñáñez.