# /criterio-claims:promo-check 

Corrí el periodo 2026-10, que es el de la ficha con las promociones registradas. El periodo 2026-11 no tiene ficha, y su reporte salió vacío. Dos promociones, Cumpleaños y Puntos dobles, no publican el fin de su vigencia en sus bases.

# Cada promoción con sus condiciones · Almacenes del Canal Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Canal Sintéticos (155634567-2-2020) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 1.1.0 · **Comando:** `promo-check`

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

- ¿Carpeta de la entidad? → mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos (única candidata)
- ¿Entidad, identificación fiscal y país? → Almacenes del Canal Sintéticos, 155634567-2-2020, PA, USD
- ¿Periodo? → 2026-10
- ¿Publicar en Rostrum? → Sí; la política no dice otra cosa
- ¿Dónde guardar el estado? → estado-mercadeo/155634567-2-2020-almacenes-del-canal-sinteticos
- ¿Términos 1.6? → Aceptados por José Francisco Ñáñez, 2026-11-25
- ¿Marcar la carpeta? → Sí

## Fuentes

- `30-promociones/bases_promocion_cumpleanos.pdf`
- `30-promociones/bases_promocion_puntos_dobles.pdf`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-promo-check-1`, con la salida en `corridas/salida-promo-check.md`.

Al comprobar los términos (vigentes, versión 1.6), vi que ya estaban aceptados desde `claims-setup`. No hizo falta registrar la aceptación otra vez.

También dejé un `reporte-promo-check.md` vacío en `piezas/2026-11`, de mi primera corrida, antes de ver que ese periodo no tiene ficha.