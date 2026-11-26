# /criterio-risk-appetite:framework-check 

Los términos están vigentes (versión 1.6, aceptación registrada en 0.2.0). La declaración de apetito no está registrada en la ficha del periodo (aparece en «—»), así que no hay revisión de la junta que contrastar. El resto del marco sí se revisó.

# El marco y la declaración · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.2.0 · **Comando:** `framework-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Días | Cita |
|---|---|---|---|---|---|
| 1 | Límite sin dueño (`limit_without_owner`) | L-02 · Indicador de cobertura de liquidez | — | — | `00-marco/limites.xlsx` fila 3 |
| 2 | Límite sin dueño (`limit_without_owner`) | L-22 · Concentración sectorial de la cartera | — | — | `00-marco/limites.xlsx` fila 11 |
| 3 | Límite sin dueño (`limit_without_owner`) | L-23 · Descalce de plazos a 30 días | — | — | `00-marco/limites.xlsx` fila 12 |
| 4 | Revisión vencida (`limit_review_overdue`) | L-33 · Inversiones de baja liquidez: tocaba el 2026-04-30 | Tesorería | 209 | `00-marco/limites.xlsx` fila 14 |
| 5 | Revisión vencida (`limit_review_overdue`) | L-32 · Exposición en moneda extranjera: tocaba el 2026-05-31 | Tesorería | 178 | `00-marco/limites.xlsx` fila 13 |
| 6 | Revisión vencida (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: tocaba el 2026-06-30 | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Declaración de apetito:** — · revisada por la junta el — · próxima revisión —.

Los 15 límites del marco están en el reporte completo, con dueño y próxima revisión. Los tres sin dueño son L-02, L-22 y L-23. Tienen la revisión vencida L-33, L-32 y L-02.

## Lo que no se pudo procesar

Para los 15 límites, ningún área reportó su exposición de 2026-11. El archivo disponible es `10-exposicion/exposicion_2026-10.xlsx`.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/limites.xlsx`
- Fuentes técnicas: F-01, F-10

El reporte completo está en `estado-riesgos/901777333-banco-andino-sintetico/apetito/2026-11/reporte-framework-check.md`. Lo que le mostré a la persona quedó en `corridas/salida-framework-check.md`. La corrida quedó registrada como `2026-11-25-framework-check-1`, con 16 hallazgos.