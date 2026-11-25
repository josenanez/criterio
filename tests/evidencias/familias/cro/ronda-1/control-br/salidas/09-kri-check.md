# /criterio-risk-events:kri-check 

Los términos están vigentes (versión 1.6, ya aceptados), así que no registré una aceptación nueva. Ninguno de los cinco indicadores trae valor en 2026-11, por lo que no hay nada que comparar con los umbrales.

# Cada indicador contra su umbral · Cooperativa Controle Sintética · periodo 2026-11

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `kri_not_reported` | KRI-01 · Transações fraudulentas por milhão: no tiene valor en 2026-11 | Operações | `00-marco/indicadores_chave.xlsx` fila 2 |
| 2 | `kri_not_reported` | KRI-02 · Disponibilidade dos canais digitais: no tiene valor en 2026-11 | Tecnologia | `00-marco/indicadores_chave.xlsx` fila 3 |
| 3 | `kri_not_reported` | KRI-03 · Rotatividade da equipe de crédito: no tiene valor en 2026-11 | Diretoria de crédito | `00-marco/indicadores_chave.xlsx` fila 4 |
| 4 | `kri_not_reported` | KRI-04 · Dias sem teste do plano de continuidade: no tiene valor en 2026-11 | Tecnologia | `00-marco/indicadores_chave.xlsx` fila 5 |
| 5 | `kri_not_reported` | KRI-05 · Concentração dos depósitos nos 20 maiores: no tiene valor en 2026-11 | Tesouraria | `00-marco/indicadores_chave.xlsx` fila 6 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor del periodo | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-04 | mayor es peor | 180 | 365 | — | sin valor | no |
| KRI-05 | mayor es peor | 25 | 30 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `00-marco/indicadores_chave.xlsx` · F-01 (families/criterio-cro/FUENTES.es.md)

La salida quedó en `estado-riesgos/98765432000110-cooperativa-controle-sintetica/corridas/salida-kri-check.md`. La corrida quedó registrada como `2026-11-25-kri-check-1`.