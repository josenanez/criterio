# /criterio-claims:approval-check 

Este reporte dice qué salió sin aprobación, sin identificarse como publicidad o con una base sin autorización. La decisión es de legal y del área de mercadeo.

# La aprobación y la autorización · Consumo Maya Sintético · periodo 2026-11

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.2.0 · **Comando:** `approval-check`

## Lo que hay que atender

| # | Señal | Qué | Días | Cita |
|---|---|---|---|---|
| 1 | Pieza publicada sin la aprobación que pide la política, o antes de ella | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Pieza publicada sin la aprobación que pide la política, o antes de ella | P-42 · Devoluciones: se publicó el 2026-10-14 y se aprobó el 2026-10-16, después | 2 | `10-piezas/registro_de_piezas.xlsx` fila 11 |
| 3 | Base de contactos usada en una campaña sin autorización para mercadeo | B-02: la usa la campaña C-02 y el registro de bases no le da autorización para mercadeo | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 4 | Base de contactos usada en una campaña sin autorización para mercadeo | B-12: la usa la campaña C-12 y el registro de bases no le da autorización para mercadeo | — | `50-campanas/plan_de_mercadeo.xlsx` fila 6 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 5 |
| 5 | Pieza pagada a un influenciador que no se identifica como publicidad | P-04 · Reseña de una creadora: pagada a @creadora_sintetica, sin identificar como publicidad | — | `10-piezas/registro_de_piezas.xlsx` fila 5 |
| 6 | Pieza pagada a un influenciador que no se identifica como publicidad | P-32 · Visita de un creador: pagada a @creador_invitado_sintetico, sin identificar como publicidad | — | `10-piezas/registro_de_piezas.xlsx` fila 10 |

## El resultado

| Pieza | Canal | Publicada | Aprobada | Aprobó | Pagada a un influenciador | Identificada |
|---|---|---|---|---|---|---|
| P-01 · Entrega en un día | Televisión | 2026-10-03 | 2026-09-28 | Legal | no | — |
| P-02 · Precio bajo | Prensa | 2026-10-06 | 2026-10-02 | Legal | no | — |
| P-03 · Recomendación | Redes sociales | 2026-10-08 | 2026-10-07 | Legal | no | — |
| P-04 · Reseña de una creadora | Instagram | 2026-10-10 | 2026-10-09 | Legal | sí | no |
| P-05 · Hecho en casa | Exteriores | 2026-10-12 | 2026-10-15 | Legal | no | — |
| P-06 · La nueva colección | TikTok | 2026-10-20 | 2026-10-18 | Legal | no | — |
| P-12 · Atención rápida | Radio | 2026-10-05 | 2026-10-01 | Legal | no | — |
| P-22 · Útiles escolares | Prensa | 2026-10-07 | 2026-10-03 | Legal | no | — |
| P-32 · Visita de un creador | Instagram | 2026-10-14 | 2026-10-13 | Legal | sí | no |
| P-42 · Devoluciones | Redes sociales | 2026-10-14 | 2026-10-16 | Legal | no | — |

| Base de contactos | Campaña | En el registro | Autorización para mercadeo |
|---|---|---|---|
| B-01 | C-01 | sí | sí |
| B-02 | C-02 | sí | no |
| B-12 | C-12 | sí | no |

Quién aprueba cada pieza lo fija la política de publicidad de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/registro_de_piezas.xlsx`
- `40-bases/registro_de_bases_de_contactos.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)

Los términos ya estaban vigentes, así que no hizo falta registrar una aceptación nueva. Dejé el reporte en `estado-mercadeo/…/piezas/2026-11/reporte-approval-check.md` y la corrida registrada como `2026-11-25-approval-check-1`.

Dos precisiones sobre lo que mostré:
- **Tabla de señales:** quité las columnas Monto y Responsable, que venían vacías (—).
- **Salida guardada:** el archivo `corridas/salida-approval-check.md` lleva el reporte completo del motor, con esas dos columnas.