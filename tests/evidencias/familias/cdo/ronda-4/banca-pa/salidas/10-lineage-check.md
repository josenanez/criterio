# /criterio-data-quality:lineage-check 

Dos pasos de linaje no tienen sistema de origen: «Clientes activos» y «Ventas netas».

# El linaje de cada cifra · Banco Canal Sintético · periodo 2026-11

**Entidad:** Banco Canal Sintético (155698765-2-2018) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 1.1.0 · **Comando:** `lineage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Clientes activos»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 5 |
| 2 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Ventas netas»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 8 |

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

Los términos ya estaban vigentes (aceptados en la versión 1.1.0), así que no registré ninguna aceptación nueva. La corrida quedó registrada como `2026-11-25-lineage-check-1`.