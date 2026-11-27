# /criterio-claims:claims-scan 

Revisé la ficha de 2026-10 contra las piezas, los soportes y las bases de las promociones. Coincide con los documentos, así que no la cambié. El motor no encontró documentos fuera de la ficha.
Esto es lo que se detectó. La decisión sobre cada punto es de legal y del área de mercadeo.

# Qué cambió en las piezas · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `claims-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | — | — | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-43 · Garantía: se publicó el 2026-10-22 y se aprobó el 2026-10-25, después | — | — | 3 | `10-piezas/registro_de_piezas.xlsx` fila 15 |
| 3 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-42 · Devoluciones: se publicó el 2026-10-14 y se aprobó el 2026-10-16, después | — | — | 2 | `10-piezas/registro_de_piezas.xlsx` fila 14 |
| 4 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 5 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-12: «Atención en menos de 5 minutos en todas las sucursales.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-12.pdf` |
| 6 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-13: «Más de 500 puntos de atención en el país.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-13.pdf` |
| 7 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-02: la usa la campaña C-02 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 8 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-12: la usa la campaña C-12 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 6 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 5 |
| 9 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-13: la usa la campaña C-13 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 7 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 6 |
| 10 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |
| 11 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-22: «Más barato que cualquier otra cadena en útiles escolares.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-22.pdf` |
| 12 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-23: «El envío más rápido del mercado.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-23.pdf` |
| 13 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Cumpleaños: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_cumpleanos.pdf` |
| 14 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Puntos dobles: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_puntos_dobles.pdf` |
| 15 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Regreso a clases: sus bases no publican las condiciones de modo y lugar | — | — | — | `30-promociones/bases_promocion_regreso_a_clases.pdf` |
| 16 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: es una pieza pagada a @creadora_sintetica y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |
| 17 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-32 · Visita de un creador: es una pieza pagada a @creador_invitado_sintetico y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 12 |
| 18 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-33 · Reseña de cafés: es una pieza pagada a @creador_invitado_sintetico y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 13 |

## El resultado

**Piezas en el registro:** 14 · **Afirmaciones en la ficha:** 14 · **Promociones:** 4 · **Bases de contactos en uso:** 4.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-13.pdf`
- `10-piezas/pieza_P-22.pdf`
- `10-piezas/pieza_P-23.pdf`
- `10-piezas/registro_de_piezas.xlsx`
- `30-promociones/bases_promocion_cumpleanos.pdf`
- `30-promociones/bases_promocion_puntos_dobles.pdf`
- `30-promociones/bases_promocion_regreso_a_clases.pdf`
- `40-bases/registro_de_bases_de_contactos.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-01, F-10 (families/criterio-cmo/FUENTES.es.md)