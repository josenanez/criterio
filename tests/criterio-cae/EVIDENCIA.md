# criterio-cae · qué prueba el material

Escrito a mano. El material lo genera `generar.py`, que es determinista: el mismo material cada vez,
byte a byte. La clave de cada entidad, `material/<entidad>/clave.json`, la escribe el generador al
sembrar cada defecto; el motor no la ve. Los nombres, las empresas, las personas y los documentos son
inventados.

## Las entidades

| Carpeta del material | País | Industria | Señales esperadas |
|---|---|---|---:|
| `banca-co` | Colombia | banca | 25 |
| `cooperativa-pe` | Perú | cooperativas | 14 |
| `seguros-br` | Brasil | seguros | 12 |
| `control-co` | Colombia | banca | 0 |
| `control-pe` | Perú | cooperativas | 0 |

Cada una trae su carpeta de auditoría interna al 24 de noviembre de 2026, con el periodo de noviembre:
el estatuto y la metodología en PDF, el equipo con sus horas y los cargos anteriores; el universo
auditable, la matriz de riesgos, el plan anual en Excel y las actas del comité en PDF; dos trabajos con
su programa y su índice de papeles en Excel, sus papeles, la aprobación del programa y el informe en PDF,
y las asignaciones; y el registro de hallazgos, el de riesgos aceptados, las evidencias, la explicación
de un atraso y el informe del revisor fiscal.

## Lo que se siembra, y la señal que tiene que levantar

La lista exacta está en la clave de cada entidad, en `esperado`. Las veinticuatro señales se siembran al
menos una vez.

| Agente | Lo que se siembra | Señal |
|---|---|---|
| Prudencia | Un riesgo crítico de una unidad que ningún trabajo cubre | `high_risk_not_covered` |
| Prudencia | Una unidad media auditada en 2023 y una baja sin trabajo registrado, ninguna en el plan | `auditable_unit_overdue` |
| Prudencia | La evaluación de riesgos de hace 435 días | `risk_assessment_outdated` |
| Prudencia | Un plan sin el tema de fraude o sin el de cumplimiento | `plan_area_not_considered` |
| Prudencia | Un trabajo agregado sin el acta que lo apruebe | `plan_change_unapproved` |
| Prudencia | Un trabajo planeado que tenía que empezar el 2 de noviembre | `engagement_behind_schedule` |
| Prudencia | Un plan de 2.200 horas para un equipo de 2.000 | `plan_hours_exceed_capacity` |
| Prudencia | Un trabajo de ciberseguridad que empezó después del 5 de febrero de 2026 sin su requisito temático | `topical_requirement_missing` |
| Prudencia | La última evaluación externa de calidad, de marzo de 2021 | `external_assessment_overdue` |
| Justo | Un programa aprobado una semana después del primer papel | `work_program_not_approved` |
| Justo | Un hallazgo sin causa ni la razón por la que no se identificó | `finding_element_missing` |
| Justo | Un hallazgo que cita un papel que no está en el índice | `finding_without_workpaper` |
| Justo | Un paso del programa sin papel ni razón | `procedure_not_executed` |
| Justo | Un papel sin la revisión del supervisor | `workpaper_not_reviewed` |
| Justo | Un informe con otra cifra para un hallazgo | `report_differs_from_workpapers` |
| Justo | Un hallazgo con impacto 4 y probabilidad 4 calificado de prioridad media | `rating_inconsistent` |
| Justo | Un auditor asignado a Tecnología, que tuvo a su cargo hasta después de empezar el trabajo | `auditor_reviews_own_work` |
| Remedios | Un hallazgo sin responsable | `action_plan_missing` |
| Remedios | Un plan vencido sin evidencia ni explicación | `action_plan_overdue` |
| Remedios | Un plan con tres reprogramaciones cuando se permiten dos | `due_date_extended_repeatedly` |
| Remedios | Un cierre validado sin evidencia | `closure_without_evidence` |
| Remedios | La misma condición en Crédito, después de que su hallazgo se cerró en 2025 | `finding_repeated` |
| Remedios | Un riesgo aceptado por encima del apetito sin discusión con la alta dirección | `risk_accepted_not_escalated` |
| Remedios | Un hallazgo del revisor fiscal que no está en el registro | `external_finding_untracked` |

## Lo que se parece a un defecto y no lo es

En las entidades de control: un riesgo alto cubierto por la unidad y no por su código, un ciclo que vence
el mes que viene, una evaluación de riesgos de hace 358 días, una evaluación externa que vence en
diciembre, un trabajo de ciberseguridad que empezó antes de que rigiera su requisito temático, horas del
plan iguales a la capacidad, una causa que no se pudo identificar con su razón, un paso que no aplica con
su razón, un papel revisado el mismo día del informe, un auditor que dejó la unidad catorce meses antes,
un plan vencido con su explicación, dos reprogramaciones cuando se permiten dos, la misma condición en
otro proceso, un riesgo aceptado que se discutió y se resolvió y un hallazgo externo que está en el
registro por su referencia. Ninguno puede levantar una señal.

## Lo que el material no prueba

- **La extracción.** El evaluador escribe la ficha con la extracción correcta, de la clave. Que el agente
  procese las actas, los papeles, los informes y las evidencias y los registre bien lo prueba la ronda con
  los agentes, desde la 0.2.0: [las rondas](../evidencias/familias/cae/RONDAS.md).
- **Las exportaciones reales** de TeamMate+, AuditBoard, Ideagen o SAP Audit Management: el material usa
  tablas con columnas en español; el setup mapea las de cualquier exportación.
- **La regulación de cada país**: la de Colombia (F-10) y Brasil (F-12), verificada, no entra a ninguna señal todavía; la del Perú (F-11), por verificar.
- **El juicio del auditor**: si una evidencia sostiene un cierre, si una causa es la raíz o si una
  prioridad es la correcta más allá de la escala.
