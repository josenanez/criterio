# /criterio-data-quality:lineage-check 

Los términos están vigentes (versión 1.6, aceptados por José Francisco Ñáñez el 2026-11-25). Tres indicadores tienen un hilo cortado en su linaje. No corrijo ni decido nada: eso le toca a quien firma el informe.

# El linaje de cada cifra · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `lineage-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Clientes activos»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 5 |
| 2 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Margen operacional»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 9 |
| 3 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Ventas netas»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 8 |

## El resultado

| Indicador | Pasos | Pasos sin sistema de origen |
|---|---|---|
| Cartera vencida | 2 | — |
| Clientes activos | 2 | 2 |
| Margen operacional | 2 | 2 |
| Ventas netas | 2 | 2 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-calidad/linaje.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-lineage-check-1`. La salida completa está en `estado-datos/901555777-banco-cordillera-sintetico/corridas/salida-lineage-check.md`.