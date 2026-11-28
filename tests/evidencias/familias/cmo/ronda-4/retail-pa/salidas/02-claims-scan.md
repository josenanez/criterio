# /criterio-claims:claims-scan 

Esta es la primera vez que se corre claims-scan sobre esta carpeta, así que los 27 documentos entraron como nuevos. La ficha que dejó el setup ya tenía cada afirmación de las piezas y cada promoción tal como las dicen los documentos, y no la cambié. La corrida quedó registrada como `2026-11-25-claims-scan-1`.

# Qué cambió en las piezas · Almacenes del Canal Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Canal Sintéticos (155634567-2-2020) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.1.0 · **Comando:** `claims-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | — | — | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-42 · Devoluciones: se publicó el 2026-10-14 y se aprobó el 2026-10-16, después | — | — | 2 | `10-piezas/registro_de_piezas.xlsx` fila 11 |
| 3 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 4 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-12: «Atención en menos de 5 minutos en todas las sucursales.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-12.pdf` |
| 5 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-02: la usa la campaña C-02 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 6 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-12: la usa la campaña C-12 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 6 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 5 |
| 7 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |
| 8 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-22: «Más barato que cualquier otra cadena en útiles escolares.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-22.pdf` |
| 9 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Cumpleaños: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_cumpleanos.pdf` |
| 10 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Puntos dobles: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_puntos_dobles.pdf` |
| 11 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: es una pieza pagada a @creadora_sintetica y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |
| 12 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-32 · Visita de un creador: es una pieza pagada a @creador_invitado_sintetico y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 10 |

## El resultado

**Piezas en el registro:** 10 · **Afirmaciones en la ficha:** 10 · **Promociones:** 3 · **Bases de contactos en uso:** 3.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Carpeta de la entidad? → mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos (única candidata)
- ¿Entidad, identificación fiscal y país? → Almacenes del Canal Sintéticos, 155634567-2-2020, PA, USD
- ¿Periodo? → 2026-10
- ¿Publicar en Rostrum? → Sí; la política no dice otra cosa
- ¿Dónde guardar el estado? → estado-mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos
- ¿Términos 1.6? → Aceptados por José Francisco Ñáñez, 2026-11-25
- ¿Marcar la carpeta? → Sí

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/pieza_P-03.pdf`
- `10-piezas/pieza_P-12.pdf`
- `10-piezas/pieza_P-22.pdf`
- `10-piezas/registro_de_piezas.xlsx`
- `30-promociones/bases_promocion_cumpleanos.pdf`
- `30-promociones/bases_promocion_puntos_dobles.pdf`
- `40-bases/registro_de_bases_de_contactos.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)