# /criterio-risk-events:kri-check 

Los siete indicadores clave del marco no traen valor en 2026-11, así que ninguno se pudo comparar con su umbral.

# Cada indicador contra su umbral · Cooperativa Vale Sintética · periodo 2026-11

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Agente:** Casandra, versión 0.2.0 · **Comando:** `kri-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | `kri_not_reported` | KRI-01 · Transações fraudulentas por milhão | Operações | `00-marco/indicadores_chave.xlsx` fila 2 |
| 2 | `kri_not_reported` | KRI-02 · Disponibilidade dos canais digitais | Tecnologia | fila 3 |
| 3 | `kri_not_reported` | KRI-03 · Rotatividade da equipe de crédito | Diretoria de crédito | fila 4 |
| 4 | `kri_not_reported` | KRI-05 · Concentração dos depósitos nos 20 maiores | Tesouraria | fila 5 |
| 5 | `kri_not_reported` | KRI-06 · Itens sem conciliar no fim do mês | Tesouraria | fila 6 |
| 6 | `kri_not_reported` | KRI-12 · Reclamações por 10.000 clientes | Marketing | fila 7 |
| 7 | `kri_not_reported` | KRI-22 · Cancelamentos de produtos no primeiro mês | Marketing | fila 8 |

## El resultado

| Indicador | Sentido | Alerta | Límite | Valor | Zona | Acción |
|---|---|---|---|---|---|---|
| KRI-01 | mayor es peor | 40 | 60 | — | sin valor | no |
| KRI-02 | menor es peor | 99.5 | 99 | — | sin valor | no |
| KRI-03 | mayor es peor | 8 | 12 | — | sin valor | no |
| KRI-05 | mayor es peor | 25 | 30 | — | sin valor | no |
| KRI-06 | mayor es peor | 5 | 10 | — | sin valor | no |
| KRI-12 | mayor es peor | 15 | 25 | — | sin valor | no |
| KRI-22 | mayor es peor | 10 | 15 | — | sin valor | no |

Los umbrales los fija el marco de apetito de la organización.

Todo lo que llegó se procesó. El agente no hizo preguntas en esta corrida.

**Fuentes:** `00-marco/indicadores_chave.xlsx` · F-01 (families/criterio-cro/FUENTES.es.md)

---
Notas de la sesión:
- Los términos (v1.6) ya estaban vigentes y aceptados en la instalación 0.2.0. No hizo falta registrar una aceptación nueva, así que no registré la de José Francisco Ñáñez.
- El reporte completo está en `estado-riesgos/12345678000190-cooperativa-vale-sintetica/eventos/2026-11/reporte-kri-check.md`.
- La corrida quedó registrada como `2026-11-25-kri-check-1`.