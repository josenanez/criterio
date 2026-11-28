# /criterio-data-quality:lineage-check 

Los términos v1.6 estaban vigentes, y quedaron aceptados por José Francisco Ñáñez el 2026-11-25. Dos indicadores tienen un paso del linaje sin sistema de origen.

# El linaje de cada cifra · Banco Austral Sintético · periodo 2026-11

**Entidad:** Banco Austral Sintético (97123456-k) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 1.0.0 · **Comando:** `lineage-check`

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

- Entidad, RUT y país → Banco Austral Sintético, 97123456-K, CL (de la configuración de Custodia)
- Periodo → 2026-11 (el mismo de Custodia)
- Diferencia tolerada entre una cifra y su fuente → 0.5 % (00-referencia/politica_de_datos.pdf)
- ¿Se publica en Rostrum? → Sí; la política de datos no dice otra cosa
- Dónde se guarda el estado → estado-datos/97123456-k-banco-austral-sintetico
- Términos v1.6 → Aceptados por José Francisco Ñáñez el 2026-11-25

## Fuentes

- `30-calidad/linaje.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-lineage-check-1`, con la salida guardada en `corridas/salida-lineage-check.md`.