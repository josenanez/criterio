# Corrida · 2026-10-01-portfolio-scan-1

**Agente:** Vera (portafolio) · **Comando:** `/criterio-portfolio:portfolio-scan`

**Inicio:** 2026-10-01T15:58:41 · **Fin:** 2026-10-01T16:04:14 · **Duración:** 333 s

**Subagentes:** ninguno · la configuración permite 1 a la vez

## Cifras medidas por la corrida

| Qué | Casos | Documentos | Segundos | Hallazgos | Nota |
|---|---:|---:|---:|---:|---|
| `portfolio-scan` | 6 | 45 | 306 | 37 | 3 proyectos leidos (PRY-208, PRY-221, PRY-229), 22 documentos de 45. Sin carpeta de entrada. Hallazgos criticos: PRY-221 y PRY-229 vencidos, PRY-208 con contradiccion cronograma/informe, factura CT-793 excede contractual, 4 entregables CT-915 vencidos sin recibo. |

Por señal (`portfolio-scan`): `milestone_met_without_evidence` 9, `vendor_deliverable_late` 4, `progress_vs_plan` 3, `variance_cost` 3, `variance_time` 3, `milestone_overdue` 2, `silent` 2, `declared_vs_evidence` 2, `commitment_undated` 1, `vendor_accepted_without_evidence` 1, `vendor_invoiced_over_accepted` 1, `vendor_invoiced_without_delivery` 1, `rebaseline_unauthorized` 1, `declaration_stale` 1, `change_without_baseline` 1, `budget_committed` 1, `commitment_overdue` 1

## Lo que el agente mostró

Corrida registrada. Resultados:

## Barrido — 2026-10-01

**Documentos:** 45 en la carpeta · 22 leidos · 23 sin cambio · 0 ilegibles
**Proyectos:** 6 con carpeta · 3 leidos (PRY-208, PRY-221, PRY-229) · 3 sin cambio (PRY-199, PRY-206, PRY-232)

### Hallazgos criticos

| Proyecto | Estado | Avance | Lo que hay que mirar |
|---|---|---|---|
| **PRY-208** Motor de decision | rojo | 60% | Cronograma dice todo cerrado pero informe dice 60% rojo. Factura CT-793 excede contractual en ~1.4B. 4 entregables CT-915 vencidos sin recibo. CC-01 pendiente de comite. |
| **PRY-221** Core de depositos | amarillo | 33% | **Vencido** (cierre era 2026-09-14). 39 dias en silencio. Proyeccion excede aprobado en 28.5%. Sin cronograma ni minutas. |
| **PRY-229** Nomina electronica | verde | 59% | **Vencido** (cierre era 2026-07-14). Declara verde al 59% pasado de fecha. Proyeccion excede aprobado en 25.2%. CC-01 aprobada, no reflejada en cronograma. |

**37 hallazgos** en total (6 proyectos), los mas frecuentes: 9 hitos cerrados sin evidencia, 4 entregables de proveedor vencidos, 3 desviaciones de costo, 3 desviaciones de tiempo.

**Compromisos que requieren accion inmediata:**
- Beatriz Cuellar (PRY-208): entregar el punto 27 — **vencido desde 2026-09-08**
- Liliana Torres (PRY-229): entregar el punto 40 — **vence el 2026-10-04** (en 3 dias)

---

Hay mas de un proyecto, asi que puedo producir el informe consolidado de portafolio si lo necesitas. Los 3 proyectos leidos tienen contradicciones entre lo declarado y la evidencia documental.
