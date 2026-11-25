# /criterio-audit-plan:plan-wake 

Hoy tocaba la revisión semanal (`plan-scan`). No llegó ningún documento nuevo ni cambiado y no había peticiones abiertas. Los términos están vigentes, así que no hubo que registrar la aceptación. El inventario marca dos archivos fuera de lugar: `30-seguimiento/informe_revisor_fiscal_2026.pdf` iría en `20-trabajos/` y `30-seguimiento/riesgos_aceptados.xlsx` en `10-plan/`.

# Qué cambió en el plan · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Prudencia, versión 0.1.0 · **Comando:** `plan-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo de la metodología (`high_risk_not_covered`) | R-06 · Pérdida de información de clientes: calificado Crítico en la matriz y ningún trabajo del plan lo cubre (norma 9.4) | — | — | — | `10-plan/matriz_de_riesgos.xlsx` fila 7 |
| 2 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-03 · Tesorería: el último trabajo fue el 2023-03-10, su ciclo de 24 meses venció el 2025-03-10 y no está en el plan | — | — | 624 | `10-plan/universo_auditable.xlsx` fila 4 |
| 3 | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo (`auditable_unit_overdue`) | U-10 · Canales físicos: no tiene un trabajo registrado y no está en el plan; su ciclo es de 36 meses | — | — | — | `10-plan/universo_auditable.xlsx` fila 8 |
| 4 | Un trabajo se agregó, se canceló o se aplazó sin el acta del órgano que aprueba el plan (`plan_change_unapproved`) | TR-06 · Nómina: el plan lo agrega y no hay un acta del órgano que aprueba el plan que lo apruebe (norma 9.4) | — | — | — | `10-plan/plan_anual_2026.xlsx` fila 7 |
| 5 | Un trabajo de aseguramiento sobre ciberseguridad o terceros no lleva en su programa el requisito temático vigente (`topical_requirement_missing`) | TR-02 · Ciberseguridad de canales: trabajo de aseguramiento sobre ciberseguridad que empieza el 2026-03-02, y el requisito temático de Ciberseguridad rige desde el 2026-02-05; su programa no lo lleva | — | — | — | `10-plan/plan_anual_2026.xlsx` fila 3 |
| 6 | Un trabajo del plan pasó su fecha de inicio o de cierre sin estar en curso o terminado (`engagement_behind_schedule`) | TR-06 · Nómina: tenía que empezar el 2026-11-02 y sigue Planeado | — | — | 22 | `10-plan/plan_anual_2026.xlsx` fila 7 |

## El resultado

**Trabajos activos en el plan:** 6 · **Riesgos en la matriz:** 6 · **Unidades del universo:** 7 · **Aprobaciones en la ficha:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `10-plan/matriz_de_riesgos.xlsx`
- `10-plan/plan_anual_2026.xlsx`
- `10-plan/universo_auditable.xlsx`
- Fuentes técnicas: F-01, F-02 (families/criterio-cae/FUENTES.es.md)

---

Ambas corridas quedaron registradas: `2026-11-24-plan-scan-2` y `2026-11-24-plan-wake-1`. Sus salidas están en `estado-auditoria/20601777321-cooperativa-de-ahorro-altiplano-sintetica/corridas/`. Qué hacer con cada señal lo deciden el responsable de auditoría y el consejo.