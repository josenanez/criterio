# /criterio-audit-plan:plan-scan 

Las dos actas de `10-plan/actas/` ya estaban en la ficha con su cita: la cancelación de TR-05 y la adición de TR-06, aprobadas por el comité de auditoría. No hubo nada nuevo que llevar.
El inventario dice que `30-seguimiento/informe_revisor_fiscal_2026.pdf` y `30-seguimiento/riesgos_aceptados.xlsx` están fuera de lugar. Esto contradice la estructura recomendada, que pone ambos en `30-seguimiento/`, así que no los moví. Es un aviso para el motor, no para la carpeta.

# Qué cambió en el plan · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 2 | La última evaluación externa de calidad tiene más de cinco años (norma 8.4) (`external_assessment_overdue`) | la última evaluación externa de calidad fue el 2021-03-31; la siguiente tocaba a más tardar el 2026-03-28 (norma 8.4) | — | — | 241 | `00-referencia/metodologia-de-auditoria.pdf` |
| 3 | La evaluación de riesgos que sostiene el plan tiene más de un año (norma 9.4) (`risk_assessment_outdated`) | la evaluación de riesgos que sostiene el plan es del 2025-09-15: tiene 435 días, y la norma 9.4 la pide al menos una vez al año | — | — | 70 | `00-referencia/metodologia-de-auditoria.pdf` |
| 4 | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) (`plan_area_not_considered`) | el plan no considera los programas de cumplimiento y ética ni dice por qué (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` |
| 5 | Las horas del plan superan las horas disponibles del equipo en el periodo (`plan_hours_exceed_capacity`) | el plan suma 2200 horas y el equipo tiene 2000 disponibles en el periodo: faltan 200 | — | — | — | `10-plan/plan_anual_2026.xlsx` · `00-referencia/equipo.xlsx` |

## El resultado

**Trabajos activos en el plan:** 6 · **Riesgos en la matriz:** 5 · **Unidades del universo:** 7 · **Aprobaciones en la ficha:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/equipo.xlsx`
- `00-referencia/metodologia-de-auditoria.pdf`
- `10-plan/plan_anual_2026.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)