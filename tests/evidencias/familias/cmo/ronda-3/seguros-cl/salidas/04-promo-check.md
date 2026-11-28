# /criterio-claims:promo-check 

Dos de las tres promociones no publican cuándo terminan. Los términos 1.6 ya estaban vigentes, así que no registré ninguna aceptación nueva.

# Cada promoción con sus condiciones · Seguros Cordillera Sintéticos · periodo 2026-10

**Entidad:** Seguros Cordillera Sintéticos (96789012-3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.0.0 · **Comando:** `promo-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Cumpleaños: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_cumpleanos.pdf` |
| 2 | Una promoción no publica su vigencia o sus condiciones de modo y lugar (`promotion_terms_missing`) | Puntos dobles: sus bases no publican el fin | — | — | — | `30-promociones/bases_promocion_puntos_dobles.pdf` |

## El resultado

| Promoción | Inicio | Fin | Condiciones de modo y lugar | Bases |
|---|---|---|---|---|
| Cumpleaños | 2026-10-01 | — | sí | `30-promociones/bases_promocion_cumpleanos.pdf` |
| Navidad | 2026-12-01 | 2026-12-24 | sí | `30-promociones/bases_promocion_navidad.pdf` |
| Puntos dobles | 2026-11-01 | — | sí | `30-promociones/bases_promocion_puntos_dobles.pdf` |

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

- `30-promociones/bases_promocion_cumpleanos.pdf`
- `30-promociones/bases_promocion_puntos_dobles.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

La salida quedó en `corridas/salida-promo-check.md` y la corrida quedó registrada como `2026-11-25-promo-check-1`.