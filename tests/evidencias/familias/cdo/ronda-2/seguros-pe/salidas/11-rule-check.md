# /criterio-data-quality:rule-check 

Los términos de la versión 1.6 están vigentes. Este es el reporte de las reglas de calidad del periodo 2026-11, tal como lo escribió el motor.

# Las reglas de calidad · Aseguradora Pacífico Sintética · periodo 2026-11

**Entidad:** Aseguradora Pacífico Sintética (20605557771) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.2.0 · **Comando:** `rule-check`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Dato crítico sin ninguna regla de calidad (`critical_data_without_rule`) | Cliente.ingresos: marcado como crítico, ninguna regla lo mide | Riesgo | `30-calidad/datos_criticos.xlsx` fila 6 |
| 2 | Dato crítico sin ninguna regla de calidad (`critical_data_without_rule`) | Crédito.calificación: marcado como crítico, ninguna regla lo mide | Riesgo | `30-calidad/datos_criticos.xlsx` fila 7 |
| 3 | Resultado bajo su umbral (`quality_rule_below_threshold`) | RQ-02 sobre Movimiento.valor: dio 96.1 en el periodo y su umbral es 98 | — | `30-calidad/reglas_calidad.xlsx` fila 3 · `30-calidad/resultados_calidad.xlsx` fila 3 |
| 4 | Resultado bajo su umbral (`quality_rule_below_threshold`) | RQ-12 sobre Cliente.correo: dio 91 en el periodo y su umbral es 95 | — | `30-calidad/reglas_calidad.xlsx` fila 6 · `30-calidad/resultados_calidad.xlsx` fila 4 |
| 5 | Regla sobre un dato crítico sin resultado en el periodo (`quality_rule_not_run`) | RQ-03 sobre Crédito.fecha_desembolso: sin resultado en 2026-11 | Crédito | `30-calidad/reglas_calidad.xlsx` fila 4 |
| 6 | Regla sobre un dato crítico sin resultado en el periodo (`quality_rule_not_run`) | RQ-22 sobre Cuenta.saldo: sin resultado en 2026-11 | Finanzas | `30-calidad/reglas_calidad.xlsx` fila 7 |

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

Ninguna en esta corrida.

## Fuentes

- `30-calidad/datos_criticos.xlsx`
- `30-calidad/reglas_calidad.xlsx`
- `30-calidad/resultados_calidad.xlsx`
- Fuentes técnicas: F-01, F-03 (families/criterio-cdo/FUENTES.es.md)

---
La corrida quedó registrada como `2026-11-25-rule-check-1`. El texto de arriba está en `estado-datos/20605557771-aseguradora-pacifico-sintetica/corridas/salida-rule-check.md`. El reporte del motor está en `estado-datos/20605557771-aseguradora-pacifico-sintetica/calidad/2026-11/reporte-rule-check.md`.

Ni el reporte ni los comandos mostraron qué registró la aceptación de términos, así que no hay nada que decir sobre la aceptación a nombre de José Francisco Ñáñez. El comando `terminos` devolvió «vigente» con la aceptación en la versión 0.2.0, y este comando no registra aceptaciones. La corrida pasó sin pedir ese registro.