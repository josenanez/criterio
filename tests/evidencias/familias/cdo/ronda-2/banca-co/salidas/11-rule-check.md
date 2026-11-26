# /criterio-data-quality:rule-check 

Términos vigentes, registrados a nombre de José Francisco Ñáñez. Estas son las reglas de calidad del periodo 2026-11 contra su umbral; lo que sigue lo calculó el motor.

# Las reglas de calidad · Banco Cordillera Sintético · periodo 2026-11

**Entidad:** Banco Cordillera Sintético (901555777) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `rule-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Cliente.ingresos: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 7 |
| 2 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Crédito.calificación: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 9 |
| 3 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Garantía.valor: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 8 |
| 4 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-02 sobre Movimiento.valor: dio 96.1 en el periodo y su umbral es 98 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 3 · `30-calidad/resultados_calidad.xlsx` fila 3 |
| 5 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-12 sobre Cliente.correo: dio 91 en el periodo y su umbral es 95 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 6 · `30-calidad/resultados_calidad.xlsx` fila 4 |
| 6 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-13 sobre Movimiento.fecha: dio 97.5 en el periodo y su umbral es 99 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 7 · `30-calidad/resultados_calidad.xlsx` fila 5 |
| 7 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-03 sobre Crédito.fecha_desembolso, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Crédito | — | `30-calidad/reglas_calidad.xlsx` fila 4 |
| 8 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-22 sobre Cuenta.saldo, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Finanzas | — | `30-calidad/reglas_calidad.xlsx` fila 8 |
| 9 | Una regla de calidad sobre un dato crítico no tiene resultado en el periodo (`quality_rule_not_run`) | RQ-23 sobre Crédito.tasa, un dato crítico: no tiene resultado en el periodo 2026-11 | — | Finanzas | — | `30-calidad/reglas_calidad.xlsx` fila 9 |

## El resultado

| Regla | Dato | Crítico | Umbral | Resultado del periodo |
|---|---|---|---|---|
| RQ-01 | Cliente.documento | sí | 99 | 99.6 |
| RQ-02 | Movimiento.valor | sí | 98 | 96.1 |
| RQ-03 | Crédito.fecha_desembolso | sí | 97 | sin corrida |
| RQ-04 | Proveedor.correo | no | 90 | sin corrida |
| RQ-12 | Cliente.correo | no | 95 | 91 |
| RQ-13 | Movimiento.fecha | no | 99 | 97.5 |
| RQ-22 | Cuenta.saldo | sí | 99 | sin corrida |
| RQ-23 | Crédito.tasa | sí | 98 | sin corrida |

**Datos críticos sin regla:** Cliente.ingresos, Garantía.valor, Crédito.calificación.

Los umbrales los fija la política de datos de la organización.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-calidad/datos_criticos.xlsx`
- `30-calidad/reglas_calidad.xlsx`
- `30-calidad/resultados_calidad.xlsx`
- Fuentes técnicas: F-01, F-03 (families/criterio-cdo/FUENTES.es.md)

---
El reporte quedó en `calidad/2026-11/reporte-rule-check.md`. La corrida quedó registrada como `2026-11-25-rule-check-1`, con la salida en `corridas/salida-rule-check.md`.