# /criterio-claims:approval-check 

Un hallazgo para atender: la pieza P-04 se pagó a un influenciador y no se identifica como publicidad. La decisión es de legal y del área de mercadeo.

# La aprobación y la autorización · Banco Altiplano Sintético · periodo 2026-11

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `approval-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: es una pieza pagada a @creadora_sintetica y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |

## El resultado

| Pieza | Canal | Publicada | Aprobada | Aprobó | Pagada a un influenciador | Identificada |
|---|---|---|---|---|---|---|
| P-01 · Entrega en un día | Televisión | 2026-10-03 | 2026-09-28 | Legal | no | — |
| P-02 · Precio bajo | Prensa | 2026-10-06 | 2026-10-02 | Legal | no | — |
| P-03 · Recomendación | Redes sociales | 2026-10-08 | 2026-10-07 | Legal | no | — |
| P-04 · Reseña de una creadora | Instagram | 2026-10-10 | 2026-10-09 | Legal | sí | no |
| P-05 · Hecho en casa | Exteriores | 2026-10-12 | 2026-10-12 | Legal | no | — |
| P-06 · La nueva colección | TikTok | 2026-10-20 | 2026-10-18 | Legal | no | — |

| Base de contactos | Campaña | En el registro | Autorización para mercadeo |
|---|---|---|---|
| B-01 | C-01 | sí | sí |
| B-02 | C-02 | sí | sí |

Quién aprueba cada pieza lo fija la política de publicidad de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/registro_de_piezas.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---
Tres notas de la corrida:
- Los términos ya estaban vigentes (versión 1.6), así que no registré una aceptación nueva.
- El motor registró la corrida como `2026-11-25-approval-check-1` y contó 3 hallazgos. El reporte muestra una sola señal. No sé de dónde salen los otros dos, porque el motor no lo dice.
- La salida completa está en `estado-mercadeo/20603335551-banco-altiplano-sintetico/corridas/salida-approval-check.md`.