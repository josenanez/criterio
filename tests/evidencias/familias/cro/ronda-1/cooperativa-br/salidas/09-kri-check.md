# /criterio-risk-events:kri-check 

Los términos (v1.6) ya estaban vigentes, así que no hizo falta registrar una aceptación nueva. Corrí el reporte de 2026-11 con corte al 2026-11-25.

# Cada indicador contra su umbral · Cooperativa Vale Sintética · periodo 2026-11

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra, versión 0.1.0 · **Comando:** `kri-check`

## Lo que hay que atender

Ninguno de los cinco indicadores tiene valor en 2026-11 (`kri_not_reported`).

| # | Indicador | Responsable | Cita |
|---|---|---|---|
| 1 | KRI-01 · Transações fraudulentas por milhão | Operações | `00-marco/indicadores_chave.xlsx` fila 2 |
| 2 | KRI-02 · Disponibilidade dos canais digitais | Tecnologia | fila 3 |
| 3 | KRI-03 · Rotatividade da equipe de crédito | Diretoria de crédito | fila 4 |
| 4 | KRI-04 · Dias sem teste do plano de continuidad | Tecnologia | fila 5 |
| 5 | KRI-05 · Concentração dos depósitos nos 20 maiores | Tesouraria | fila 6 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-04 | mayor es peor | 180 | 365 | — | sin valor | no |
| KRI-05 | mayor es peor | 25 | 30 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

Todo lo que llegó se procesó. No hubo preguntas en esta corrida.

**Fuentes:** `00-marco/indicadores_chave.xlsx`; F-01 (families/criterio-cro/FUENTES.es.md).

La corrida quedó registrada como `2026-11-25-kri-check-1`, con 3 hallazgos según el motor. La salida está en `estado-riesgos/12345678000190-cooperativa-vale-sintetica/corridas/salida-kri-check.md`.