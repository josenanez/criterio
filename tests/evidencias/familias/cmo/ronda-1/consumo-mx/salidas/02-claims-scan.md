# /criterio-claims:claims-scan 

Esta es la primera corrida contra el inventario, así que todos los documentos entraron como nuevos y se procesaron todos. La ficha de 2026-10 ya traía las seis afirmaciones y las dos promociones que muestran los documentos, y no cambió. El cálculo no devolvió ningún documento que faltara en la ficha.

# Qué cambió en las piezas · Consumo Maya Sintético · periodo 2026-10

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Lucía, versión 0.1.0 · **Comando:** `claims-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una pieza se publicó sin la aprobación que pide la política, o antes de ella (`piece_published_unapproved`) | P-05 · Hecho en casa: se publicó el 2026-10-12 y se aprobó el 2026-10-15, después | — | — | 3 | `10-piezas/registro_de_piezas.xlsx` fila 6 |
| 2 | Una base de contactos usada en una campaña no tiene autorización para mercadeo (`contact_base_without_consent`) | B-02: la usa la campaña C-02 y el registro de bases no le da autorización para mercadeo | — | — | — | `50-campanas/plan_de_mercadeo.xlsx` fila 3 · `40-bases/registro_de_bases_de_contactos.xlsx` fila 3 |
| 3 | Una afirmación comparativa no cita su fuente ni su fecha (`comparative_claim_without_source`) | P-02: «El precio más bajo del mercado en la canasta básica.» compara con la competencia y la pieza no dice su fuente ni su fecha | — | — | — | `10-piezas/pieza_P-02.pdf` |

## El resultado

**Piezas en el registro:** 6 · **Afirmaciones en la ficha:** 6 · **Promociones:** 2 · **Bases de contactos en uso:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-piezas/pieza_P-02.pdf`
- `10-piezas/registro_de_piezas.xlsx`
- `40-bases/registro_de_bases_de_contactos.xlsx`
- `50-campanas/plan_de_mercadeo.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cmo/FUENTES.es.md)