[English](DISENO.md) · [← La familia](README.es.md)

# criterio-cae · el diseño de la familia

**Estado: estable, lanzada en su versión 1.0.0.** Los comandos, los skills y el motor de cálculo
se construyen sobre el núcleo común; el motor pasa su prueba determinista contra el material de
`tests/criterio-cae/`. En la 0.2.0, los tres agentes corrieron sobre todas las entidades del material, con una clave que no ven; en la 1.0.0, la ronda 2 en Colombia, Perú y Brasil: 76 señales y 352 datos, con un piso del 95,1 % en las señales y del 98,9 % en los datos, y ningún control con una señal: [las rondas](../../tests/evidencias/familias/cae/RONDAS.md). Alcance en [ADR 0033](../../docs/decisions/0033-la-familia-cae.md).

**Esta es la hoja de diseño de la familia**: las señales que calcula el código, cada comando con su
entrada, su proceso y su reporte, y las decisiones tomadas. Qué hace la familia, cómo se instala, la
estructura de carpetas y la hoja de ruta están en su [página](README.es.md).

El modelo de lenguaje (LLM) extrae; el código calcula; la opinión —qué se audita, qué prioridad tiene un
hallazgo, si un cierre se sostiene— es siempre del auditor. **El rol se define sobre las Normas Globales de
Auditoría Interna** (F-01) y sus requisitos temáticos (F-02), no sobre la ley de cada país; cada señal está
atada a su norma, citada por su número y su título.

**De dónde sale este documento.** Las tablas de agentes, señales, comandos y cifras no se escriben aquí:
salen de [`familia.json`](familia.json), [`carpetas.json`](carpetas.json) y [`fuentes.json`](fuentes.json).

## Un agente por rol

<!-- cae:agentes · generado por scripts/familias.py; no se edita a mano -->
| Rol | Agente | Plugin | Qué hace |
|---|---|---|---|
| El plan de auditoría | **Prudencia** — del latín *prudentia*, contracción de *providentia*, «ver antes»: el plan que mira el riesgo antes de que ocurra | `criterio-audit-plan` | El plan de auditoría contra el universo auditable y la matriz de riesgos: los riesgos altos sin un trabajo, las unidades que pasaron su ciclo, la evaluación de riesgos vencida, las áreas que el plan tiene que considerar, los cambios sin aprobación, los trabajos atrasados, las horas que no alcanzan, el requisito temático que falta y la evaluación externa de calidad |
| Los trabajos de auditoría | **Justo** — del latín *iustus*, «conforme a derecho»: cada hallazgo contra su criterio | `criterio-audit-work` | Cada trabajo contra su programa y sus papeles: el programa sin aprobar, el hallazgo sin su criterio, su condición, su causa, su efecto o su prioridad, el hallazgo sin papel, el paso sin ejecutar, el papel sin revisión, el informe que no dice lo que dicen los papeles, la prioridad que no da la metodología y el auditor que revisa lo que tuvo a su cargo |
| El seguimiento de los hallazgos | **Remedios** — del latín *remedium*, «lo que vuelve a curar»: cada hallazgo hasta su remedio | `criterio-remediation` | Cada hallazgo hasta su cierre: el plan de acción sin responsable o sin fecha, el vencido sin evidencia ni explicación, la fecha que se corre una y otra vez, el cierre sin evidencia o sin validación, el hallazgo que vuelve, el riesgo aceptado que no llegó a la alta dirección o al consejo y el hallazgo externo que no está en el registro |
<!-- /cae:agentes -->

## Las señales: lo que calcula el código

<!-- cae:senales · generado por scripts/familias.py; no se edita a mano -->
**Prudencia · El plan de auditoría**

| Señal | Se levanta cuando |
|---|---|
| `high_risk_not_covered` | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo de la metodología |
| `auditable_unit_overdue` | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo |
| `risk_assessment_outdated` | La evaluación de riesgos que sostiene el plan tiene más de un año (norma 9.4) |
| `plan_area_not_considered` | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué (norma 9.4) |
| `plan_change_unapproved` | Un trabajo se agregó, se canceló o se aplazó sin el acta del órgano que aprueba el plan |
| `engagement_behind_schedule` | Un trabajo del plan pasó su fecha de inicio o de cierre sin estar en curso o terminado |
| `plan_hours_exceed_capacity` | Las horas del plan superan las horas disponibles del equipo en el periodo |
| `topical_requirement_missing` | Un trabajo de aseguramiento sobre ciberseguridad o terceros no lleva en su programa el requisito temático vigente |
| `external_assessment_overdue` | La última evaluación externa de calidad tiene más de cinco años (norma 8.4) |

**Justo · Los trabajos de auditoría**

| Señal | Se levanta cuando |
|---|---|
| `work_program_not_approved` | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel (norma 13.6) |
| `finding_element_missing` | Un hallazgo no tiene su criterio, su condición, su efecto o su prioridad, o no tiene su causa raíz ni la razón por la que no se pudo identificar (normas 14.2 y 14.3) |
| `finding_without_workpaper` | Un hallazgo no cita un papel de trabajo, o cita uno que no existe (norma 14.6) |
| `procedure_not_executed` | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica (norma 12.3) |
| `workpaper_not_reviewed` | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe (normas 12.3 y 14.6) |
| `report_differs_from_workpapers` | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles |
| `rating_inconsistent` | La prioridad de un hallazgo no es la que da la metodología para su impacto y su probabilidad (norma 14.3) |
| `auditor_reviews_own_work` | Un auditor asignado a un trabajo de aseguramiento tuvo a su cargo la actividad auditada en los doce meses anteriores (norma 2.2) |

**Remedios · El seguimiento de los hallazgos**

| Señal | Se levanta cuando |
|---|---|
| `action_plan_missing` | Un hallazgo comunicado no tiene plan de acción, responsable o fecha (norma 15.1) |
| `action_plan_overdue` | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) |
| `due_date_extended_repeatedly` | La fecha de un plan se corrió más veces de las que permite la metodología |
| `closure_without_evidence` | Un plan se dio por cerrado sin la evidencia de su implementación o sin la validación de auditoría (norma 15.2) |
| `finding_repeated` | La misma condición, en el mismo proceso, vuelve a aparecer después de que su hallazgo se cerró |
| `risk_accepted_not_escalated` | La gerencia aceptó un riesgo por encima del apetito y no hay constancia de que se discutiera con la alta dirección o, sin resolverse, de que llegara al consejo (norma 11.5) |
| `external_finding_untracked` | Un hallazgo del revisor fiscal, del auditor externo o del supervisor no está en el registro con su plan |
<!-- /cae:senales -->

## Los comandos de Prudencia, en orden de importancia

<!-- cae:comandos-prudencia · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `plan-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, el ciclo de rotación de cada nivel de riesgo, desde qué calificación un riesgo es alto, quién aprueba el plan según el estatuto, la fecha de la última evaluación de riesgos y la de la última evaluación externa de calidad | Inventario de lo que hay; procesa el universo, la matriz de riesgos y el plan de `10-plan/` y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; las tablas reconocidas; la primera ficha del periodo |
| 1 | `plan-scan` | El universo, la matriz, el plan, las actas y la capacidad del equipo en `10-plan/`, y la ficha del periodo | Lleva a la ficha cada acta nueva —qué trabajo agrega, cancela o aplaza y quién lo aprobó—, con la cita; recalcula las señales | Lo que entró a la ficha; las actas que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `plan-coverage` | La matriz de riesgos, el universo auditable y el plan de `10-plan/`, con el ciclo de la configuración | Cruza cada riesgo alto con los trabajos del plan y cada unidad del universo con su último trabajo; comprueba que el plan considere el gobierno de TI, el fraude y el cumplimiento y ética, y que la evaluación de riesgos no tenga más de un año | Los riesgos altos sin trabajo, las unidades fuera de su ciclo, las áreas sin considerar y la edad de la evaluación de riesgos |
| 3 | `plan-status` | El plan de `10-plan/` y las actas de la ficha | Cada trabajo contra su fecha de inicio y de cierre, y cada cambio al plan contra el acta que lo aprueba | Los trabajos atrasados y los cambios sin aprobación, cada uno con su fecha y su cita |
| 4 | `plan-capacity` | El plan y la capacidad del equipo de `10-plan/` | Suma las horas del plan y las disponibles del equipo en el periodo; revisa que cada trabajo de aseguramiento sobre ciberseguridad o terceros lleve su requisito temático vigente | Horas del plan contra horas disponibles y los trabajos sin su requisito temático |
| 5 | `quality-status` | La fecha de la última evaluación externa de calidad, de la configuración o de `00-referencia/` | Cuenta los años desde la última evaluación externa contra los cinco que fija la norma 8.4 | La fecha de la última, la de la siguiente y cuánto falta o cuánto pasó |
| 6 | `plan-wake` | La configuración y el registro de corridas | Decide si toca procesar el plan —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 7 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cae:comandos-prudencia -->

## Los comandos de Justo, en orden de importancia

<!-- cae:comandos-justo · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `work-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo, la escala de prioridad de la metodología —cada nivel con su impacto y su probabilidad— y quién aprueba el programa y los papeles | Inventario de lo que hay; reconoce los trabajos de `20-trabajos/` y el equipo de `00-referencia/`; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; los trabajos reconocidos; la primera ficha del periodo |
| 1 | `work-scan` | Los programas, los papeles y los informes de `20-trabajos/`, y la ficha del periodo | Lleva a la ficha cada hallazgo nuevo o cambiado —su criterio, su condición, su causa, su efecto, su prioridad y los papeles que cita— y lo que dice el informe, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `finding-check` | Los hallazgos de la ficha y la escala de prioridad de la configuración | Revisa que cada hallazgo tenga su criterio, su condición, su efecto, su prioridad y su causa raíz —o la razón por la que no se pudo identificar—, y que su prioridad sea la que da la metodología para su impacto y su probabilidad | Cada hallazgo con lo que le falta y la prioridad que da la metodología |
| 3 | `workpaper-check` | El programa de trabajo y el índice de papeles de cada trabajo en `20-trabajos/` | Revisa que el programa se haya aprobado antes del primer papel, que cada paso tenga su papel o la razón por la que no aplica, que cada papel tenga su revisión y su aprobación antes del informe y que cada hallazgo cite un papel que existe | Cada trabajo con el programa, los pasos sin papel, los papeles sin revisión y los hallazgos sin papel |
| 4 | `report-check` | Lo que la ficha registra del informe y de los papeles de cada trabajo | Cruza cada hallazgo del informe con el de sus papeles: que esté, que tenga la misma prioridad y las mismas cifras | Las diferencias entre el informe y los papeles, cada una con las dos citas |
| 5 | `objectivity-check` | Las asignaciones de cada trabajo y la historia de cargos del equipo en `00-referencia/` | Cruza cada auditor asignado a un trabajo de aseguramiento con las actividades que tuvo a su cargo en los doce meses anteriores (norma 2.2) | Las asignaciones con un posible impedimento, con la fecha y la cita |
| 6 | `work-wake` | La configuración y el registro de corridas | Decide si toca procesar los trabajos —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 7 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cae:comandos-justo -->

## Los comandos de Remedios, en orden de importancia

<!-- cae:comandos-remedios · generado por scripts/familias.py; no se edita a mano -->
| # | Comando | Entrada | Proceso (lo calcula el código) | Reporte |
|---|---|---|---|---|
| 0 | `remediation-setup` | La carpeta raíz. Preguntas: entidad y su identificación fiscal, país, el periodo y cuántas veces permite la metodología correr la fecha de un plan | Inventario de lo que hay; procesa el registro de hallazgos y el de riesgos aceptados de `30-seguimiento/` y dice cuántas filas reconoce; compara la carpeta con la estructura recomendada; no crea, mueve ni renombra nada | Configuración guardada; inventario por carpeta; los registros reconocidos; la primera ficha del periodo |
| 1 | `remediation-scan` | El registro de hallazgos, las evidencias, los riesgos aceptados y los informes externos de `30-seguimiento/`, y la ficha del periodo | Lleva a la ficha cada evidencia y cada explicación de atraso nuevas y los hallazgos de cada informe externo, con la cita; recalcula las señales | Lo que entró a la ficha; los documentos que todavía no están en ella; las señales nuevas; lo que no se pudo procesar y por qué |
| 2 | `action-status` | El registro de hallazgos de `30-seguimiento/` y la ficha | Cada plan de acción contra su responsable, su fecha y sus reprogramaciones; los vencidos, con su evidencia o la explicación documentada del atraso | Los planes sin responsable o sin fecha, los vencidos y los que se corrieron más de lo que permite la metodología, con los días |
| 3 | `closure-check` | El registro de hallazgos, las evidencias de `30-seguimiento/` y los hallazgos anteriores | Revisa que cada cierre tenga su evidencia y su validación de auditoría, y busca la misma condición en el mismo proceso entre los hallazgos ya cerrados | Los cierres sin evidencia o sin validación y los hallazgos que vuelven, con las dos citas |
| 4 | `committee-brief` | El registro de hallazgos, el de riesgos aceptados y los informes externos de `30-seguimiento/` | Reúne lo vencido, lo repetido, los riesgos aceptados por encima del apetito que no llegaron a la alta dirección o al consejo (norma 11.5) y los hallazgos externos que no están en el registro | El resumen para el comité, cada punto con su cita; ninguna conclusión de auditoría |
| 5 | `remediation-wake` | La configuración y el registro de corridas | Decide si toca procesar el seguimiento —documentos nuevos o la revisión semanal— o un reporte con señales abiertas, y lo corre; si no toca nada, se calla | Lo que corrió y por qué, o nada |
| 6 | `share-findings` | El rastro de las corridas de este agente en esta carpeta | Arma un resumen sin datos —qué comandos corrieron, cuántas señales, qué no se pudo procesar— y pregunta si se comparte; nada se envía solo | El resumen y la pregunta |
<!-- /cae:comandos-remedios -->

## Cifras de terceros

<!-- cae:cifras · generado por scripts/familias.py; no se edita a mano -->
Solo entran las verificadas, con fuente, año y muestra, y están en [`FUENTES.es.md`](FUENTES.es.md). Verificadas: C-01 (ACFE), C-02 (ACFE), C-03 (ACFE).
<!-- /cae:cifras -->

## Decisiones cerradas

- Los nombres, Prudencia, Justo y Remedios, y la estructura: tres agentes, sus veinticuatro señales y sus comandos (decisión 0033).
- Las Normas Globales de Auditoría Interna se citan por su número y su título: su texto tiene todos los derechos reservados.
- La regulación de cada país no sostiene ninguna señal hasta verificarse en su texto oficial: Colombia (F-10) y Brasil (F-12) están verificados; el Perú (F-11), todavía no. ISO 19011 queda fuera de la 0.1.0 hasta verificar su edición vigente.
- El sector público queda fuera de la 0.1.0.
