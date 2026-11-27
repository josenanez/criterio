# /criterio-campaigns:result-check 

Los términos están vigentes (versión 1.6, ya aceptados). Dos de los tres resultados del informe no coinciden con la plataforma. Usé el periodo 2026-10 porque es el que trae el informe de resultados.

# Cada resultado contra la plataforma · Consumo Maya Sintético · periodo 2026-10

**Entidad:** Consumo Maya Sintético (CMS210415XY3) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Próspero, versión 0.2.0 · **Comando:** `result-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-01 · Ventas atribuidas: el informe reporta 4,600 y la plataforma 4,100 al 2026-10-31; la política tolera un 2 % | 500.00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 2 |
| 2 | El resultado reportado no coincide con la exportación de la plataforma para el mismo corte, más allá de la tolerancia (`result_differs_from_platform`) | C-03 · Visitas a la tienda: el informe reporta 3,100 y la plataforma 2,850 al 2026-10-31; la política tolera un 2 % | 250.00 | — | — | `50-campanas/informe_de_resultados_2026-10.pdf` · `50-campanas/resultados_plataforma.xlsx` fila 3 |

## El resultado

**Tolerancia de la política entre el informe y la plataforma:** 2 %.

| Campaña | Indicador | Corte | Reportado | Plataforma | Estado |
|---|---|---|---|---|---|
| C-01 | Ventas atribuidas | 2026-10-31 | 4,600 | 4,100 | distinto |
| C-03 | Visitas a la tienda | 2026-10-31 | 3,100 | 2,850 | distinto |
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

La salida quedó en `corridas/salida-result-check.md` y la corrida quedó registrada como `2026-11-25-result-check-1`.