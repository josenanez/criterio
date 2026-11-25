# /criterio-campaigns:result-check 

Se contrastó cada resultado del informe de 2026-10 con la exportación de la plataforma: uno no coincide.

# Cada resultado contra la plataforma · Almacenes del Valle Sintéticos · periodo 2026-10

**Entidad:** Almacenes del Valle Sintéticos (901333555) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.1.0 · **Comando:** `result-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-01 · Ventas atribuidas: el informe reporta 4,600 y la plataforma 4,100 al 2026-10-31; la política tolera un 2 % | 500,00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 2 |

## El resultado

**Tolerancia de la política entre el informe y la plataforma:** 2 %.

| Campaña | Indicador | Corte | Reportado | Plataforma | Estado |
|---|---|---|---|---|---|
| C-01 | Ventas atribuidas | 2026-10-31 | 4,600 | 4,100 | distinto |
| C-03 | Visitas a la tienda | 2026-10-31 | 2,850 | 2,850 | coincide |
| C-04 | Impresiones | 2026-10-31 | 1,840,000 | 1,840,000 | coincide |

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con la plataforma.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `50-campanas/informe_de_resultados_2026-10.pdf`
- `50-campanas/resultados_plataforma.xlsx`
- Fuentes técnicas: F-02 (families/criterio-cmo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-result-check-1`.