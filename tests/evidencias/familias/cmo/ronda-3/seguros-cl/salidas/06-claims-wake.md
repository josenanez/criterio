# /criterio-claims:claims-wake 

Hoy solo tocaba `claims-scan`, por los documentos nuevos o la revisión semanal, y no había peticiones abiertas en Rostrum. El inventario no trae documentos nuevos, cambiados ni borrados desde la corrida anterior. La ficha del periodo ya estaba completa y el cálculo no dejó documentos fuera. Las dos corridas quedaron registradas (`2026-11-25-claims-scan-2` y `2026-11-25-claims-wake-1`).

# Qué cambió en las piezas · Seguros Cordillera Sintéticos · periodo 2026-10

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.0.0 · **Comando:** `claims-scan`

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

- ¿Cuál es la carpeta de la entidad? → mercadeo/96789012-3-seguros-cordillera-sinteticos, la única candidata
- ¿Entidad, identificación fiscal y país? → Seguros Cordillera Sintéticos, RUT 96789012-3, Chile (CLP)
- ¿Periodo? → 2026-10
- ¿Se publica en Rostrum? → Sí, por omisión; la política no dice otra cosa
- ¿Dónde se guarda el estado? → estado-mercadeo/96789012-3-seguros-cordillera-sinteticos
- ¿Acepta los términos 1.6? → Sí, José Francisco Ñáñez, 2026-11-25
- ¿Se marca la carpeta con _CRITERIO_MERCADEO.txt? → Sí

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