# /criterio-risk-appetite:appetite-wake 

Hoy tocaba solo la revisión semanal (`appetite-scan`) y no había peticiones abiertas. No llegaron documentos nuevos ni cambiados, y la ficha del periodo no tenía documentos pendientes. Abajo va el reporte tal como lo escribió el motor.

# Qué cambió en el apetito · Banco Andino Sintético · periodo 2026-10

**Entidad:** Banco Andino Sintético (901777333) · **Fecha de corte:** 2026-11-25 · **Procesado:** 2026-11-25 · **Agente:** Severo, versión 0.1.0 · **Comando:** `appetite-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una exposición supera su límite y no tiene plan de acción ni aprobación del exceso (`limit_breached_without_plan`) | L-01 · Cartera vencida de consumo: la exposición de 2026-10 es 6.4 % y el límite máximo es 6; no hay plan de acción ni aprobación del exceso | 0,40 | Vicepresidencia de crédito | — | `00-marco/limites.xlsx` fila 2 · `10-exposicion/exposicion_2026-10.xlsx` fila 2 |
| 2 | Un riesgo calificado alto o crítico en la matriz no tiene límite ni indicador clave (`risk_without_limit`) | R-04 · Continuidad del negocio: calificado Alto en la matriz, sin límite en el marco ni indicador clave que lo mida | — | Tecnología | — | `00-marco/matriz_de_riesgos.xlsx` fila 5 |
| 3 | La declaración de apetito no tiene la revisión de la junta en el plazo que fija el marco (`appetite_statement_outdated`) | Declaración de apetito por riesgo: la junta la revisó el 2025-08-28, y el marco pide revisarla cada 12 meses: tocaba el 2026-08-28 | — | — | 89 | `00-marco/declaracion_de_apetito.pdf` |
| 4 | Un área reportó su exposición después del plazo que fija el marco (`exposure_report_late`) | L-02 · Indicador de cobertura de liquidez: Tesorería reportó su exposición de 2026-10 el 2026-11-18, y el marco da 10 días después del cierre: hasta el 2026-11-10 | — | Tesorería | 8 | `10-exposicion/exposicion_2026-10.xlsx` fila 3 |
| 5 | Un límite del marco no tiene dueño (`limit_without_owner`) | L-02 · Indicador de cobertura de liquidez: el límite no tiene un dueño que responda por él | — | — | — | `00-marco/limites.xlsx` fila 3 |
| 6 | Un límite pasó su fecha de revisión (`limit_review_overdue`) | L-02 · Indicador de cobertura de liquidez: su revisión tocaba el 2026-06-30 | — | — | 148 | `00-marco/limites.xlsx` fila 3 |

## El resultado

**Límites en el marco:** 5 · **Con exposición reportada:** 5 · **Excedidos:** 3 · **Riesgos altos o críticos en la matriz:** 5 · **Excesos aprobados en las actas:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-marco/declaracion_de_apetito.pdf`
- `00-marco/limites.xlsx`
- `00-marco/matriz_de_riesgos.xlsx`
- `10-exposicion/exposicion_2026-10.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cro/FUENTES.es.md)

---

Quedaron registradas las dos corridas con el caso 2026-10: `2026-11-25-appetite-scan-2` y `2026-11-25-appetite-wake-1`. Lo que se mostró quedó guardado en `estado-riesgos/901777333-banco-andino-sintetico/corridas/`.