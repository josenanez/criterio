# /criterio-claims:claims-scan 

Los términos están vigentes (los aceptó José Francisco Ñáñez el 2026-11-25). Es la primera vez que corre este comando, así que todos los documentos de la carpeta entraron como nuevos. La ficha del periodo que dejó la configuración inicial coincide con lo que dicen las piezas y las condiciones de las promociones, así que no la cambié. El motor no encontró documentos que faltaran en la ficha.

# Qué cambió en las piezas · Banco Altiplano Sintético · periodo 2026-10

**Entidad:** Banco Altiplano Sintético (20603335551) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claims-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una afirmación de una pieza aprobada no tiene un soporte en la carpeta de soportes (`claim_without_substantiation`) | P-03: «9 de cada 10 clientes nos recomiendan.» no tiene un soporte en la carpeta de soportes | — | — | — | `10-piezas/pieza_P-03.pdf` |
| 2 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Puntos dobles: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_puntos_dobles.pdf` |
| 3 | Una pieza pagada a un influenciador no se identifica como publicidad (`sponsored_content_unidentified`) | P-04 · Reseña de una creadora: es una pieza pagada a @creadora_sintetica y no se identifica como publicidad | — | — | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |

## El resultado

**Piezas en el registro:** 6 · **Afirmaciones en la ficha:** 6 · **Promociones:** 2 · **Bases de contactos en uso:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/pieza_P-03.pdf`
- `10-piezas/registro_de_piezas.xlsx`
- `30-promociones/bases_promocion_puntos_dobles.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

---

Lo que se mostró arriba quedó en `<espacio>/estado-mercadeo/20603335551-banco-altiplano-sintetico/corridas/salida-claims-scan.md`, y la corrida quedó registrada como `2026-11-25-claims-scan-1` con 3 hallazgos.