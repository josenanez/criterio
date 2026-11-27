# /criterio-audit-plan:plan-scan 

I found the 27 documents for the entity. `10-plan/` has only one meeting record, the cancellation of TR-05, and it was already on the period's sheet, so nothing needed to be added to it. Here is the engine's report as it came out:

# Qué cambió en el plan · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.2.2 · **Comando:** `plan-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo de la metodología (`high_risk_not_covered`) | R-06 · Pérdida de información de clientes: calificado Crítico en la matriz y ningún trabajo del plan lo cubre (norma 9.4) | — | — | — | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Un trabajo se agregó, se canceló o se aplazó sin el acta del órgano que aprueba el plan (`plan_change_unapproved`) | TR-06 · Nómina: el plan lo agrega y no hay un acta del órgano que aprueba el plan que lo apruebe (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` fila 7 |
| 4 | Un trabajo de aseguramiento sobre ciberseguridad o terceros no lleva en su programa el requisito temático vigente (`topical_requirement_missing`) | TR-02 · Ciberseguridad de canales: trabajo de aseguramiento sobre ciberseguridad que empieza el 2026-03-02, y el requisito temático de Ciberseguridad rige desde el 2026-02-05; su programa no lo lleva | — | — | — | `10-plan/plan_anual_2026.xlsx` fila 3 |
| 5 | La última evaluación externa de calidad tiene más de cinco años (norma 8.4) (`external_assessment_overdue`) | la última evaluación externa de calidad fue el 2021-03-31; la siguiente tocaba a más tardar el 2026-03-28 (norma 8.4) | — | — | 241 | `00-referencia/metodologia-de-auditoria.pdf` |
| 6 | La evaluación de riesgos que sostiene el plan tiene más de un año (norma 9.4) (`risk_assessment_outdated`) | la evaluación de riesgos que sostiene el plan es del 2025-09-15: tiene 435 días, y la norma 9.4 la pide al menos una vez al año | — | — | 70 | `00-referencia/metodologia-de-auditoria.pdf` |
| 7 | Un trabajo del plan pasó su fecha de inicio o de cierre sin estar en curso o terminado (`engagement_behind_schedule`) | TR-06 · Nómina: tenía que empezar el 2026-11-02 y sigue Planeado | — | — | 22 | `10-plan/plan_anual_2026.xlsx` fila 7 |
| 8 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera los programas de cumplimiento y ética ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |
| 9 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera el riesgo de fraude ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |
| 10 | Las horas del plan superan las horas disponibles del equipo en el periodo (`plan_hours_exceed_capacity`) | el plan suma 2200 horas y el equipo tiene 2000 disponibles en el periodo: faltan 200 | — | — | — | `10-plan/plan_anual_2026.xlsx` · `00-referencia/equipo.xlsx` |

## El resultado

**Trabajos activos en el plan:** 6 · **Riesgos en la matriz:** 6 · **Unidades del universo:** 7 · **Aprobaciones en la ficha:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/equipo.xlsx`
- `00-referencia/metodologia-de-auditoria.pdf`
- `10-plan/matriz_de_riesgos.xlsx`
- `10-plan/plan_anual_2026.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cae/FUENTES.es.md)

---

The terms were already accepted for version 0.2.2, so I didn't record a new acceptance. The run is logged as `2026-11-24-plan-scan-1`, and the output shown here is saved in `estado-auditoria/31452078000190-seguradora-atlantica-sintetica/corridas/salida-plan-scan.md`.