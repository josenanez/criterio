# /criterio-data-quality:figure-check 

Cada cifra del informe de junta se comparó contra su fuente. De las nueve cifras, tres coinciden, dos difieren más allá de la tolerancia, dos son de otro corte y dos no tienen fuente. Los términos estaban vigentes y ya aceptados por José Francisco Ñáñez el 2026-11-25, así que no hubo que registrar nada.

# Cada cifra contra su fuente · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Agente:** Ariadna 0.2.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto |
|---|---|---|---|
| 1 | No coincide con la fuente al mismo corte (`figure_differs_from_source`) | «Ventas netas»: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al 2026-10-31. Diferencia de 120,000,000, más allá de la tolerancia del 0.5 %. Cita: `30-calidad/cifras_fuente.xlsx` fila 6 | 120,000,000.00 |
| 2 | No coincide con la fuente al mismo corte (`figure_differs_from_source`) | «Depósitos»: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al 2026-10-31. Diferencia de 100,000,000, más allá de la tolerancia del 0.5 %. Cita: fila 10 | 100,000,000.00 |
| 3 | Sin fuente (`figure_without_source`) | «Índice de satisfacción»: 8 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 8.10 |
| 4 | Sin fuente (`figure_without_source`) | «Índice de rotación»: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4.20 |
| 5 | Corte distinto (`cutoff_mismatch`) | «Colocaciones»: el informe declara el corte 2026-10-31, pero su cifra, 7,600,000,000, es la de la fuente al 2026-09-30. Cita: fila 13 | 7,600,000,000.00 |
| 6 | Corte distinto (`cutoff_mismatch`) | «Cartera vencida»: el informe declara el corte 2026-10-31, pero su cifra, 1,180,000,000, es la de la fuente al 2026-09-30. Cita: fila 3 | 1,180,000,000.00 |

Todas las señales citan `20-informes/informe_junta_2026-10.pdf`. Ninguna trae responsable ni días.

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Indicador | En el informe | En la fuente | Estado |
|---|---|---|---|
| Cartera vencida | 1,180,000,000 | 1,250,000,000 | otro corte |
| Clientes activos | 84,200 | 84,200 | coincide |
| Ventas netas | 9,520,000,000 | 9,400,000,000 | distinta |
| Margen operacional | 3,400,000,000 | 3,400,000,000 | coincide |
| Depósitos | 5,100,000,000 | 5,000,000,000 | distinta |
| Colocaciones | 7,600,000,000 | 7,800,000,000 | otro corte |
| Costo de adquisición | 185,000 | 185,000 | coincide |
| Índice de satisfacción | 8 | — | sin fuente |
| Índice de rotación | 4 | — | sin fuente |

Cuál cifra es la correcta lo decide quien firma el informe: aquí solo se dice cuál no coincide con su fuente.

**Lo que no se pudo procesar:** nada, todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `20-informes/informe_junta_2026-10.pdf`, `30-calidad/cifras_fuente.xlsx`, y las fuentes técnicas F-01 y F-02.

La corrida quedó registrada como `2026-11-25-figure-check-1`, con 14 hallazgos. Lo mostrado se guardó en `estado-datos/20605557771-aseguradora-pacifico-sintetica/corridas/salida-figure-check.md`, y el reporte del motor está en `calidad/2026-11/reporte-figure-check.md`.