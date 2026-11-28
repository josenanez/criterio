# /criterio-data-quality:rule-check 

Estas son las reglas de calidad del periodo contra su umbral. Hay dos reglas bajo su umbral, dos reglas de datos críticos sin corrida y dos datos críticos sin regla. La decisión sobre cada una es de quien firma el informe.

# Las reglas de calidad · Banco Austral Sintético · periodo 2026-11

**Entidad:** Banco Austral Sintético (97123456-k) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 1.0.0 · **Comando:** `rule-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Cliente.ingresos: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 6 |
| 2 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Crédito.calificación: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 7 |
| 3 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-02 sobre Movimiento.valor: dio 96.1 en el periodo y su umbral es 98 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 3 · `30-calidad/resultados_calidad.xlsx` fila 3 |
| 4 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-12 sobre Cliente.correo: dio 91 en el periodo y su umbral es 95 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 6 · `30-calidad/resultados_calidad.xlsx` fila 4 |
| 5 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-03 sobre Crédito.fecha_desembolso, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Crédito | — | `30-calidad/reglas_calidad.xlsx` fila 4 |
| 6 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-22 sobre Cuenta.saldo, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Finanzas | — | `30-calidad/reglas_calidad.xlsx` fila 7 |

## El resultado

| Regla | Dato | Crítico | Umbral | Resultado del periodo |
|---|---|---|---|---|
| RQ-01 | Cliente.documento | sí | 99 | 99.6 |
| RQ-02 | Movimiento.valor | sí | 98 | 96.1 |
| RQ-03 | Crédito.fecha_desembolso | sí | 97 | sin corrida |
| RQ-04 | Proveedor.correo | no | 90 | sin corrida |
| RQ-12 | Cliente.correo | no | 95 | 91 |
| RQ-22 | Cuenta.saldo | sí | 99 | sin corrida |

**Datos críticos sin regla:** Cliente.ingresos, Crédito.calificación.

Los umbrales los fija la política de datos de la organización.

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

- `30-calidad/datos_criticos.xlsx`
- `30-calidad/reglas_calidad.xlsx`
- `30-calidad/resultados_calidad.xlsx`
- Fuentes técnicas: F-01, F-03 (families/criterio-cdo/FUENTES.es.md)

La corrida quedó registrada como `2026-11-25-rule-check-1`. El reporte está en `estado-datos/97123456-k-banco-austral-sintetico/calidad/2026-11/reporte-rule-check.md`.