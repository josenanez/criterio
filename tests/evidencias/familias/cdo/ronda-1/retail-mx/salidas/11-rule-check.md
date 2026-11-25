# /criterio-data-quality:rule-check 

Términos vigentes (versión 1.6, aceptada por José Francisco Ñáñez el 2026-11-25). Periodo tomado de la configuración: 2026-11.

# Las reglas de calidad · Retail Central Sintético · periodo 2026-11

**Entidad:** Retail Central Sintético (RCM190305AB1) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Ariadna, versión 0.1.0 · **Comando:** `rule-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un dato marcado como crítico no tiene ninguna regla de calidad (`critical_data_without_rule`) | Crédito.calificación: está marcado como dato crítico y ninguna regla de calidad lo mide | — | Riesgo | — | `30-calidad/datos_criticos.xlsx` fila 5 |
| 2 | El resultado de una regla de calidad en el periodo está bajo su umbral (`quality_rule_below_threshold`) | RQ-02 sobre Movimiento.valor: dio 96.1 en el periodo y su umbral es 98 | — | — | — | `30-calidad/reglas_calidad.xlsx` fila 3 · `30-calidad/resultados_calidad.xlsx` fila 3 |

## El resultado

| Regla | Dato | Crítico | Umbral | Resultado del periodo |
|---|---|---|---|---|
| RQ-01 | Cliente.documento | sí | 99 | 99.6 |
| RQ-02 | Movimiento.valor | sí | 98 | 96.1 |
| RQ-03 | Crédito.fecha_desembolso | sí | 97 | 97.4 |
| RQ-04 | Proveedor.correo | no | 90 | sin corrida |

**Datos críticos sin regla:** Crédito.calificación.

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

La corrida quedó registrada como `2026-11-25-rule-check-1`. El texto completo está en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/salida-rule-check.md`.