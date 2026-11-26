# /criterio-risk-appetite:framework-check 

Los términos estaban vigentes. La aceptación ya constaba para esta versión, así que no registré una nueva a nombre de José Francisco Ñáñez. El reporte está generado y la corrida quedó registrada. El motor cuenta 11 hallazgos; no averigüé de dónde sale esa cifra, y el reporte lista 4 señales y 11 avisos de «no se pudo procesar».

**Nota previa:** la declaración de apetito sale en blanco porque el periodo 2026-11 no tiene ficha. La declaración sí está en `00-marco/declaracao_de_apetite.pdf` y en la ficha de 2026-10. Corre `/criterio-risk-appetite:appetite-scan` para llevarla a este periodo. Hasta entonces el motor no evalúa si la junta la revisó a tiempo. La exposición del periodo tampoco está reportada, y eso lo cubre `limit-check`.

# El marco y la declaración · Cooperativa Vale Sintética · periodo 2026-11

**Entidad:** Cooperativa Vale Sintética (12345678000190) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Índice de liquidez de curto prazo: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |
| 2 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-22 · Concentração setorial da carteira: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 10 |
| 3 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-32 · Exposição em moeda estrangeira: su revisión tocaba el 2026-05-31 | — | Tesouraria | 178 | `00-marco/limites.xlsx` fila 11 |
| 4 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Índice de liquidez de curto prazo: su revisión tocaba el 2026-06-30 | — | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

| Límite | Métrica | Dueño | Próxima revisión |
|---|---|---|---|
| L-01 | Carteira vencida de crédito pessoal | Diretoria de crédito | 2027-03-31 |
| L-02 | Índice de liquidez de curto prazo | — | 2026-06-30 |
| L-03 | Concentração no maior devedor | Diretoria de crédito | 2027-03-31 |
| L-04 | Perdas por fraude externa sobre receitas | Operações | 2027-06-30 |
| L-05 | Exposição a contrapartes sem rating | Tesouraria | 2027-06-30 |
| L-06 | Perdas operacionais sobre o patrimônio | Operações | 2027-06-30 |
| L-07 | Exposição ao maior banco correspondente | Tesouraria | 2027-06-30 |
| L-12 | Carteira vencida imobiliária | Diretoria de crédito | 2027-03-31 |
| L-22 | Concentração setorial da carteira | — | 2027-03-31 |
| L-32 | Exposição em moeda estrangeira | Tesouraria | 2026-05-31 |
| L-42 | Limites de contraparte utilizados | Tesouraria | 2027-06-30 |

Quién es el dueño de un límite y cuándo se revisa lo fija el marco: aquí se dice cuál falta o se venció.

## Lo que no se pudo procesar

- `10-exposicion/exposicao_2026-10.xlsx`: ningún área reportó su exposición de 2026-11 para ninguno de los 11 límites (L-01, L-02, L-03, L-04, L-05, L-06, L-07, L-12, L-22, L-32, L-42).

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01, F-12 (families/criterio-cro/FUENTES.es.md)

La lista de «no se pudo procesar» la resumí aquí en una línea. El archivo del motor, `estado-riesgos/…/apetito/2026-11/reporte-framework-check.md`, la trae como 11 líneas separadas. Mi nota previa y el texto guardado en `corridas/salida-framework-check.md` siguen la versión larga, no esta.