# /criterio-data-quality:lineage-check 

Revisé el linaje de cada indicador contra su sistema de origen. Abajo está el reporte tal cual lo escribió el motor.

# El linaje de cada cifra · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `lineage-check`

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

**Registro de la corrida:** `2026-11-25-lineage-check-1`. La salida quedó en `corridas/salida-lineage-check.md`.

**Nota:** la tabla de resultados muestra 2 pasos sin sistema de origen en «Clientes activos», pero la señal cita una sola fila (la 5). Ese desajuste es del motor y no lo corregí. Quien firma el informe debe revisar `30-calidad/linaje.xlsx` para ver qué pasos quedan sin origen.