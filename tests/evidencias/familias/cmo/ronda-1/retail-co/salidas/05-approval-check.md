# /criterio-claims:approval-check 

Los términos (v1.6) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva. El reporte marca tres señales abiertas: una pieza publicada antes de su aprobación, una base de contactos sin autorización para mercadeo y una pieza pagada a un influenciador sin identificarse como publicidad.

# La aprobación y la autorización · Almacenes del Valle Sintéticos · periodo 2026-11

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `approval-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | — | — | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-02: la usa la campaña C-02 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 3 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: es una pieza pagada a @creadora_sintetica y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |

## El resultado

| Pieza | Canal | Publicada | Aprobada | Aprobó | Pagada a un influenciador | Identificada |
|---|---|---|---|---|---|---|
| P-01 · Entrega en un día | Televisión | 2026-10-03 | 2026-09-28 | Legal | no | — |
| P-02 · Precio bajo | Prensa | 2026-10-06 | 2026-10-02 | Legal | no | — |
| P-03 · Recomendación | Redes sociales | 2026-10-08 | 2026-10-07 | Legal | no | — |
| P-04 · Reseña de una creadora | Instagram | 2026-10-10 | 2026-10-09 | Legal | sí | no |
| P-05 · Hecho en casa | Exteriores | 2026-10-12 | 2026-10-15 | Legal | no | — |
| P-06 · La nueva colección | TikTok | 2026-10-20 | 2026-10-18 | Legal | no | — |

| Base de contactos | Campaña | En el registro | Autorización para mercadeo |
|---|---|---|---|
| B-01 | C-01 | sí | sí |
| B-02 | C-02 | sí | no |

Quién aprueba cada pieza lo fija la política de publicidad de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/registro_de_piezas.xlsx`
- `40-bases/registro_de_bases_de_contactos.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-01, F-10 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-approval-check-1`, con 6 hallazgos. La salida completa está en `estado-mercadeo/901333555-almacenes-del-valle-sinteticos/corridas/salida-approval-check.md`.