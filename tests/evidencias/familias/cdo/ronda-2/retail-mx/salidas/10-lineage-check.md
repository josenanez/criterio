# /criterio-data-quality:lineage-check 

Los términos vigentes ya estaban aceptados, así que no hizo falta registrar la aceptación. Dos indicadores tienen pasos de linaje sin sistema de origen.

# El linaje de cada cifra · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `lineage-check`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Clientes activos»: el paso 2 del linaje no tiene su sistema de origen | `30-calidad/linaje.xlsx` fila 5 |
| 2 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Ventas netas»: el paso 2 del linaje no tiene su sistema de origen | `30-calidad/linaje.xlsx` fila 8 |

## El resultado

| Indicador | Pasos | Pasos sin sistema de origen |
|---|---|---|
| Cartera vencida | 2 | — |
| Clientes activos | 2 | 2 |
| Margen operacional | 1 | — |
| Ventas netas | 2 | 2 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-calidad/linaje.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-lineage-check-1`. El reporte está en `calidad/2026-11/reporte-lineage-check.md`, y lo que ve aquí está en `corridas/salida-lineage-check.md`.