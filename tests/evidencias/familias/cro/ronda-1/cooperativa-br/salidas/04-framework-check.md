# /criterio-risk-appetite:framework-check 

Términos vigentes (versión 1.6). La declaración de apetito no aparece en la ficha del periodo: no tiene fecha de revisión ni próxima revisión. Por eso no puedo decir si está vencida. Hay un límite sin dueño.

# El marco y la declaración · Cooperativa Vale Sintética · periodo 2026-11

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Índice de liquidez de curto prazo: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

| Límite | Métrica | Dueño | Próxima revisión |
|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | Diretoria de crédito | 2027-03-31 |
| L-02 | Índice de liquidez de curto prazo | — | 2026-12-15 |
| L-03 | Concentração no maior devedor | Diretoria de crédito | 2027-03-31 |
| L-04 | Perdas por fraude externa sobre receitas | Operações | 2027-06-30 |
| L-05 | Exposição a contrapartes sem rating | Tesouraria | 2027-06-30 |

Quién es el dueño de un límite y cuándo se revisa lo fija el marco: aquí se dice cuál falta o se venció.

## Lo que no se pudo procesar

- `10-exposicion/exposicao_2026-10.xlsx`: L-01 · Carteira vencida de crédito pessoal: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-02 · Índice de liquidez de curto prazo: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-03 · Concentração no maior devedor: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-04 · Perdas por fraude externa sobre receitas: ningún área reportó su exposición de 2026-11
- `10-exposicion/exposicao_2026-10.xlsx`: L-05 · Exposição a contrapartes sem rating: ningún área reportó su exposición de 2026-11

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-framework-check-1`. Lo mostrado está guardado en `estado-riesgos/12345678000190-cooperativa-vale-sintetica/corridas/salida-framework-check.md`.

Dos aclaraciones sobre cómo se hizo la corrida:
- **Aceptación de términos:** el comando `terminos` dijo que ya estaban vigentes (aceptada en la 0.1.0), así que no registré una aceptación nueva a nombre de José Francisco Ñáñez. Ese registro lo hace `/criterio-risk-appetite:appetite-setup` y no hacía falta.
- **Declaración de apetito:** el motor no encontró ninguna declaración en la ficha, y no la inventé.