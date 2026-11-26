# /criterio-data-quality:lineage-scan 

Desde la corrida anterior no llegó, cambió ni se borró ningún documento. Las cifras del informe a la junta ya estaban en la ficha del periodo y coinciden con el texto del informe, así que no hubo que agregar ninguna.
La decisión sobre cada diferencia es de quien firma el informe.

# Qué cambió en la calidad · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `lineage-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Ventas netas» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al mismo corte, 2026-10-31: una diferencia de 120,000,000, más allá de la tolerancia del 0.5 % | 120.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 6 |
| 2 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Depósitos» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al mismo corte, 2026-10-31: una diferencia de 100,000,000, más allá de la tolerancia del 0.5 % | 100.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 10 |
| 3 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Gastos operacionales» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 2,060,000,000 y la fuente 2,000,000,000 al mismo corte, 2026-10-31: una diferencia de 60,000,000, más allá de la tolerancia del 0.5 % | 60.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 12 |
| 4 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Participación de mercado» del informe 20-informes/informe_junta_2026-10.pdf: 12 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 12,50 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de satisfacción» del informe 20-informes/informe_junta_2026-10.pdf: 8 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 8,10 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 6 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de rotación» del informe 20-informes/informe_junta_2026-10.pdf: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4,20 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 7 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Colocaciones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7.600.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 15 |
| 8 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Cartera vencida» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1.180.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |
| 9 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Provisiones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 610,000,000, es la de la fuente al 2026-09-30 | 610.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 17 |
| 10 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Cliente.ingresos: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 7 |
| 11 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Crédito.calificación: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 9 |
| 12 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Garantía.valor: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 8 |
| 13 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Clientes activos»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 5 |
| 14 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Margen operacional»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 9 |
| 15 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Ventas netas»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 8 |
| 16 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-02 sobre Movimiento.valor: dio 96.1 en el periodo y su umbral es 98 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 3 · `30-calidad/resultados_calidad.xlsx` fila 3 |
| 17 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-12 sobre Cliente.correo: dio 91 en el periodo y su umbral es 95 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 6 · `30-calidad/resultados_calidad.xlsx` fila 4 |
| 18 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-13 sobre Movimiento.fecha: dio 97.5 en el periodo y su umbral es 99 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 7 · `30-calidad/resultados_calidad.xlsx` fila 5 |
| 19 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-03 sobre Crédito.fecha_desembolso, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Crédito | — | `30-calidad/reglas_calidad.xlsx` fila 4 |
| 20 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-22 sobre Cuenta.saldo, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Finanzas | — | `30-calidad/reglas_calidad.xlsx` fila 8 |
| 21 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-23 sobre Crédito.tasa, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Finanzas | — | `30-calidad/reglas_calidad.xlsx` fila 9 |

## El resultado

**Cifras de los informes en la ficha:** 13 · **Indicadores con linaje:** 4 · **Reglas de calidad:** 8.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `20-informes/informe_junta_2026-10.pdf`
- `30-calidad/cifras_fuente.xlsx`
- `30-calidad/datos_criticos.xlsx`
- `30-calidad/linaje.xlsx`
- `30-calidad/reglas_calidad.xlsx`
- `30-calidad/resultados_calidad.xlsx`
- Fuentes técnicas: F-01, F-02, F-03 (families/criterio-cdo/FUENTES.es.md)