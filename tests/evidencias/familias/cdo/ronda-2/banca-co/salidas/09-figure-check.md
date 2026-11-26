# /criterio-data-quality:figure-check 

Términos vigentes. De las 13 cifras del informe de junta de octubre hay 9 señales abiertas: 3 distintas de su fuente, 3 sin fuente y 3 que son las de otro corte. Cuál es la correcta lo decide quien firma el informe.

# Cada cifra contra su fuente · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Agente:** Ariadna 0.2.0 · **Comando:** `figure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Cita |
|---|---|---|---|---|
| 1 | No coincide con su fuente al mismo corte, más allá de la tolerancia (`figure_differs_from_source`) | «Ventas netas»: informe 9,520,000,000, fuente 9,400,000,000 al 2026-10-31. Diferencia de 120,000,000, tolerancia 0.5 % | 120.000.000,00 | `informe_junta_2026-10.pdf` · `cifras_fuente.xlsx` fila 6 |
| 2 | Ídem | «Depósitos»: informe 5,100,000,000, fuente 5,000,000,000. Diferencia de 100,000,000 | 100.000.000,00 | … fila 10 |
| 3 | Ídem | «Gastos operacionales»: informe 2,060,000,000, fuente 2,000,000,000. Diferencia de 60,000,000 | 60.000.000,00 | … fila 12 |
| 4 | Sin fuente en el linaje ni en las cifras exportadas (`figure_without_source`) | «Participación de mercado»: 12 | 12,50 | `informe_junta_2026-10.pdf` |
| 5 | Ídem | «Índice de satisfacción»: 8 | 8,10 | ídem |
| 6 | Ídem | «Índice de rotación»: 4 | 4,20 | ídem |
| 7 | Es la cifra de otro corte (`cutoff_mismatch`) | «Colocaciones»: el informe declara 2026-10-31, pero su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7.600.000.000,00 | … fila 15 |
| 8 | Ídem | «Cartera vencida»: 1,180,000,000 es la cifra del 2026-09-30 | 1.180.000.000,00 | … fila 3 |
| 9 | Ídem | «Provisiones»: 610,000,000 es la cifra del 2026-09-30 | 610.000.000,00 | … fila 17 |

## El resultado

**Tolerancia de la política de datos:** 0.5 %.

| Indicador | En el informe | En la fuente | Estado |
|---|---|---|---|
| Cartera vencida | 1,180,000,000 | 1,250,000,000 | otro corte |
| Clientes activos | 84,200 | 84,200 | coincide |
| Ventas netas | 9,520,000,000 | 9,400,000,000 | distinta |
| Margen operacional | 3,400,000,000 | 3,400,000,000 | coincide |
| Depósitos | 5,100,000,000 | 5,000,000,000 | distinta |
| Gastos operacionales | 2,060,000,000 | 2,000,000,000 | distinta |
| Colocaciones | 7,600,000,000 | 7,800,000,000 | otro corte |
| Provisiones | 610,000,000 | 640,000,000 | otro corte |
| Costo de adquisición | 185,000 | 185,000 | coincide |
| Tasa de retención | 88 | 88 | coincide |
| Índice de satisfacción | 8 | — | sin fuente |
| Participación de mercado | 12 | — | sin fuente |
| Índice de rotación | 4 | — | sin fuente |

Todas las filas son del informe `informe_junta_2026-10.pdf`, con corte 2026-10-31.

Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide con su fuente.

**Lo que no se pudo procesar:** todo lo que llegó se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `20-informes/informe_junta_2026-10.pdf`, `30-calidad/cifras_fuente.xlsx`, F-01 y F-02 (families/criterio-cdo/FUENTES.es.md).

Dejé la corrida registrada como `2026-11-25-figure-check-1`. La salida completa está en `estado-datos/901555777-banco-cordillera-sintetico/corridas/salida-figure-check.md`.