# /criterio-data-quality:figure-check 

Seis de las nueve cifras del informe de junta 2026-10 requieren atención: dos no coinciden con su fuente al mismo corte, dos no tienen fuente y dos son las de otro corte. Cuál es la correcta lo decide quien firma el informe.

# Cada cifra contra su fuente · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | No coincide con su fuente al mismo corte, más allá de la tolerancia (`figure_differs_from_source`) | «Ventas netas»: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al 2026-10-31; diferencia de 120,000,000, más allá de la tolerancia del 0.5 % | 120,000,000.00 | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 6 |
| 2 | No coincide con su fuente al mismo corte (`figure_differs_from_source`) | «Depósitos»: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al 2026-10-31; diferencia de 100,000,000, más allá de la tolerancia del 0.5 % | 100,000,000.00 | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 10 |
| 3 | Sin fuente en el linaje ni en las cifras de la fuente (`figure_without_source`) | «Índice de satisfacción»: 8 | 8.10 | `20-informes/informe_junta_2026-10.pdf` |
| 4 | Sin fuente en el linaje ni en las cifras de la fuente (`figure_without_source`) | «Índice de rotación»: 4 | 4.20 | `20-informes/informe_junta_2026-10.pdf` |
| 5 | Es la cifra de la fuente en otro corte (`cutoff_mismatch`) | «Colocaciones»: el informe declara el corte 2026-10-31 y su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7,600,000,000.00 | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 13 |
| 6 | Es la cifra de la fuente en otro corte (`cutoff_mismatch`) | «Cartera vencida»: el informe declara el corte 2026-10-31 y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1,180,000,000.00 | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Indicador | Corte | En el informe | En la fuente | Estado |
|---|---|---|---|---|
| Cartera vencida | 2026-10-31 | 1,180,000,000 | 1,250,000,000 | otro corte |
| Clientes activos | 2026-10-31 | 84,200 | 84,200 | coincide |
| Ventas netas | 2026-10-31 | 9,520,000,000 | 9,400,000,000 | distinta |
| Margen operacional | 2026-10-31 | 3,400,000,000 | 3,400,000,000 | coincide |
| Depósitos | 2026-10-31 | 5,100,000,000 | 5,000,000,000 | distinta |
| Colocaciones | 2026-10-31 | 7,600,000,000 | 7,800,000,000 | otro corte |
| Costo de adquisición | 2026-10-31 | 185,000 | 185,000 | coincide |
| Índice de satisfacción | 2026-10-31 | 8 | — | sin fuente |
| Índice de rotación | 2026-10-31 | 4 | — | sin fuente |

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-informes/informe_junta_2026-10.pdf`
- `30-calidad/cifras_fuente.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cdo/FUENTES.es.md)

---
Corrida registrada como `2026-11-25-figure-check-1`. Lo mostrado quedó en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/salida-figure-check.md`.