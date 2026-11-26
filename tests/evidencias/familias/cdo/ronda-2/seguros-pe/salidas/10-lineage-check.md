# /criterio-data-quality:lineage-check 

Los términos de la versión 1.6 ya estaban vigentes, con la aceptación de José Francisco Ñáñez registrada el 2026-11-25. Corrí el linaje del periodo 2026-11 y dos indicadores tienen el linaje cortado.

# El linaje de cada cifra · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `lineage-check`

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

La corrida quedó registrada como `2026-11-25-lineage-check-1`. La salida está en `corridas/salida-lineage-check.md`, dentro de la carpeta de estado. No hizo falta preguntar nada.

La tabla de resultado muestra «2» pasos sin sistema de origen en «Clientes activos» y en «Ventas netas», aunque la señal habla solo del paso 2 de cada uno. Esa tabla sale del motor y no la corregí.