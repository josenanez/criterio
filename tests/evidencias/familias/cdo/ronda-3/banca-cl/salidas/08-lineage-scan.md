# /criterio-data-quality:lineage-scan 

No hay documentos nuevos, cambiados ni borrados desde la corrida anterior. Las nueve cifras del informe de junta ya estaban en la ficha con su fecha de corte, y el motor no encontró ningún documento que faltara en ella.

En las señales 3 y 4, la columna «Qué» muestra los índices de satisfacción y de rotación sin su decimal. El valor completo del informe está en la columna «Monto». Es un problema de formato del motor, no del informe.

# Qué cambió en la calidad · Banco Austral Sintético · periodo 2026-11

**Entidad:** Banco Austral Sintético (97123456-k) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 1.0.0 · **Comando:** `lineage-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Ventas netas» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 9,520,000,000 y la fuente 9,400,000,000 al mismo corte, 2026-10-31: una diferencia de 120,000,000, más allá de la tolerancia del 0.5 % | 120.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 6 |
| 2 | La cifra del informe no coincide con la de su fuente al mismo corte, más allá de la tolerancia que fija la organización (`figure_differs_from_source`) | «Depósitos» del informe 20-informes/informe_junta_2026-10.pdf: el informe trae 5,100,000,000 y la fuente 5,000,000,000 al mismo corte, 2026-10-31: una diferencia de 100,000,000, más allá de la tolerancia del 0.5 % | 100.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 10 |
| 3 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de satisfacción» del informe 20-informes/informe_junta_2026-10.pdf: 8 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 8,10 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 4 | Una cifra de un informe de dirección no tiene fuente en el linaje ni en las cifras de la fuente exportadas (`figure_without_source`) | «Índice de rotación» del informe 20-informes/informe_junta_2026-10.pdf: 4 no tiene fuente en el linaje ni en las cifras de la fuente exportadas | 4,20 | — | — | `20-informes/informe_junta_2026-10.pdf` |
| 5 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Colocaciones» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 7,600,000,000, es la de la fuente al 2026-09-30 | 7.600.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 13 |
| 6 | La cifra del informe es la de la fuente en un corte distinto al que el informe declara (`cutoff_mismatch`) | «Cartera vencida» del informe 20-informes/informe_junta_2026-10.pdf: el informe declara el corte 2026-10-31, y su cifra, 1,180,000,000, es la de la fuente al 2026-09-30 | 1.180.000.000,00 | — | — | `20-informes/informe_junta_2026-10.pdf` · `30-calidad/cifras_fuente.xlsx` fila 3 |
| 7 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Cliente.ingresos: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 6 |
| 8 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Crédito.calificación: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 7 |
| 9 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Clientes activos»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 5 |
| 10 | Un paso del linaje de una cifra no tiene su sistema de origen (`lineage_broken`) | «Ventas netas»: el paso 2 del linaje no tiene su sistema de origen | — | — | — | `30-calidad/linaje.xlsx` fila 8 |
| 11 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-02 sobre Movimiento.valor: dio 96.1 en el periodo y su umbral es 98 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 3 · `30-calidad/resultados_calidad.xlsx` fila 3 |
| 12 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-12 sobre Cliente.correo: dio 91 en el periodo y su umbral es 95 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 6 · `30-calidad/resultados_calidad.xlsx` fila 4 |
| 13 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-03 sobre Crédito.fecha_desembolso, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Crédito | — | `30-calidad/reglas_calidad.xlsx` fila 4 |
| 14 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-22 sobre Cuenta.saldo, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Finanzas | — | `30-calidad/reglas_calidad.xlsx` fila 7 |

## El resultado

**Cifras de los informes en la ficha:** 9 · **Indicadores con linaje:** 4 · **Reglas de calidad:** 6.

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

- `20-informes/informe_junta_2026-10.pdf`
- `30-calidad/cifras_fuente.xlsx`
- `30-calidad/datos_criticos.xlsx`
- `30-calidad/linaje.xlsx`
- `30-calidad/reglas_calidad.xlsx`
- `30-calidad/resultados_calidad.xlsx`
- Fuentes técnicas: F-01, F-02, F-03 (families/criterio-cdo/FUENTES.es.md)

---

Quedó guardado en `<espacio>/estado-datos/97123456-k-banco-austral-sintetico/corridas/salida-lineage-scan.md` y la corrida está registrada como `2026-11-25-lineage-scan-1`.