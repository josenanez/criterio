# /criterio-claims:claims-scan 

Términos vigentes (aceptados por José Francisco Ñáñez el 2026-11-25). El inventario ve los 19 documentos de la carpeta como nuevos frente a la corrida anterior, y no hay ninguno cambiado, borrado, fuera de lugar ni ilegible. Revisé la ficha de 2026-10 contra las piezas y las bases de las promociones, y coincide, así que no tuve que agregar nada ni hacer ninguna pregunta.

# Qué cambió en las piezas · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claims-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | — | — | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 3 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-02: la usa la campaña C-02 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 4 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |
| 5 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Puntos dobles: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_puntos_dobles.pdf` |
| 6 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: es una pieza pagada a @creadora_sintetica y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |

## El resultado

**Piezas en el registro:** 6 · **Afirmaciones en la ficha:** 6 · **Promociones:** 2 · **Bases de contactos en uso:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/registro_de_piezas.xlsx`
- `30-promociones/bases_promocion_puntos_dobles.pdf`
- `40-bases/registro_de_bases_de_contactos.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-01, F-10 (families/criterio-cmo/FUENTES.es.md)