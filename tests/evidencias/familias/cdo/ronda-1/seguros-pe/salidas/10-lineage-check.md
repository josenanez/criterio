# /criterio-data-quality:lineage-check 

Los términos están vigentes (versión 1.6). La aceptación de José Francisco Ñáñez ya figuraba registrada, así que no hizo falta volver a pedirla.

# El linaje de cada cifra · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `lineage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Clientes activos»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 5 |

## El resultado

| Indicador | Pasos | Pasos sin sistema de origen |
|---|---|---|
| Cartera vencida | 2 | — |
| Clientes activos | 2 | 2 |
| Margen operacional | 1 | — |
| Ventas netas | 1 | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-calidad/linaje.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

---

- **Reporte:** `estado-datos/20605557771-aseguradora-pacifico-sintetica/calidad/2026-11/reporte-lineage-check.md`.
- **Corrida:** quedó registrada como `2026-11-25-lineage-check-1`.
- **Salida guardada:** `estado-datos/20605557771-aseguradora-pacifico-sintetica/corridas/salida-lineage-check.md`.

El motor no devolvió un conteo de pasos sin sistema para «Clientes activos» que coincida con la señal. La tabla marca 2 de 2 pasos sin sistema, y la señal solo cita el paso 2. Qué hacer con esa diferencia lo decide quien firma el informe.