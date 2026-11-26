# /criterio-risk-appetite:limit-check 

Corrí el periodo 2026-11 con corte al 2026-11-25. Ninguna área ha reportado exposición de ese periodo, así que no hay nada que contrastar contra los límites. El archivo de exposición que hay en la carpeta es `exposicao_2026-10.xlsx`, de 2026-10. No corrí 2026-10 por mi cuenta.

Los términos (versión 1.6) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva.

# Cada exposición contra su límite · Cooperativa Controle Sintética · periodo 2026-11

**Entidad:** Cooperativa Controle Sintética (98765432000110) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `limit-check`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

**Plazo del marco para reportar:** 10 días después del cierre, hasta el 2026-12-10.

| Límite | Métrica | Límite | Exposición | Excedido | Plan o aprobación | Área | Reportó |
|---|---|---|---|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | máximo 6 % | — | no | — | — | — |
| L-02 | Índice de liquidez de curto prazo | mínimo 120 % | — | no | — | — | — |
| L-03 | Concentração no maior devedor | máximo 10 % | — | no | plan | — | — |
| L-04 | Perdas por fraude externa sobre receitas | máximo 0.5 % | — | no | — | — | — |
| L-05 | Exposição a contrapartes sem rating | máximo 15 % | — | no | — | — | — |
| L-06 | Perdas operacionais sobre o patrimônio | máximo 1 % | — | no | — | — | — |
| L-07 | Exposição ao maior banco correspondente | máximo 20 % | — | no | — | — | — |

Qué se hace con un exceso lo deciden el comité y la junta: aquí se dice cuál no tiene plan ni aprobación.

## Lo que no se pudo procesar

- `10-exposicion/exposicao_2026-10.xlsx`: L-01 a L-07: ningún área reportó su exposición de 2026-11 (los siete límites, uno por uno en el reporte).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- Sin documentos citados.
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-limit-check-1`, con 0 hallazgos. La salida está en `corridas/salida-limit-check.md`.