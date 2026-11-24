# 0033 · La familia CAE: la auditoría interna, con tres agentes sobre las Normas Globales de Auditoría Interna

**Fecha:** 2026-11-24 · **Estado:** propuesta: los nombres y la estructura, por aceptar por José. Las fuentes se verifican una a una (abajo, con la fecha de cada verificación) ·
**Modifica:** —

## Contexto

José Francisco Ñáñez fijó el orden de los nuevos diseños: primero la CAE, la auditoría interna;
después la CDO, los datos. Esta decisión propone la primera.

La auditoría interna es el área que más trabaja contra documentos, porque su producto es una
opinión sostenida en evidencia: cada hallazgo tiene que poder rastrearse hasta el papel de trabajo
que lo soporta, y cada plan de acción hasta la evidencia de que se implementó. Hoy esa trazabilidad
se revisa a mano, trabajo por trabajo, y lo que llega al comité de auditoría es un resumen.

Un punto manda sobre todo el diseño: **la opinión es del auditor.** La familia prepara el trabajo y
lo contrasta contra la evidencia y la metodología de la organización; no emite opiniones, no firma
informes y no cambia la calificación de un hallazgo. Como la CISO y la CHRO, el rol se define sobre
estándares internacionales, no sobre la ley de cada país:

| Marco | Qué aporta | Estado de la fuente |
|---|---|---|
| Normas Globales de Auditoría Interna (The IIA, 2024) | Cinco dominios y quince principios. Los que usa la familia: 9.4 Plan de Auditoría Interna, 9.5 Coordinación y confianza, 11.5 Comunicar la aceptación de los riesgos, 12.3 Supervisión y mejora del desempeño en los trabajos, 13.2 a 13.6 (riesgos, objetivos y alcance, criterios de evaluación, recursos y programa de trabajo), 14.1 a 14.6 (información, hallazgos, su evaluación, recomendaciones y planes de acción, conclusiones y documentación) y 15.1 y 15.2 (comunicación final y confirmación de la implementación de los planes de acción) | Verificado el 2026-11-24 en theiia.org: la versión en español, «Publicado el 9 de enero de 2024», con sus dominios, principios y normas tomados del índice; obligatorias desde el 9 de enero de 2025. **Uso restringido:** todos los derechos reservados; reproducir o traducir su texto pide permiso de The IIA (copyright@theiia.org). Se citan su número y su título, nunca su texto. **Por verificar:** el texto de cada norma que usa la familia (lo que exige 9.4 sobre la aprobación del plan, 14.3 sobre los elementos de un hallazgo, 15.2 sobre la confirmación), en la versión en español |
| Requisitos temáticos de The IIA | Lo que un trabajo de aseguramiento sobre un tema tiene que cubrir. Vigentes: Ciberseguridad, desde el 5 de febrero de 2026, y Terceros, desde el 15 de septiembre de 2026 | Verificado el 2026-11-24 en theiia.org/en/standards/2024-standards/topical-requirements. Cada uno rige doce meses después de su emisión; Comportamiento Organizacional (15 de diciembre de 2026), Resiliencia Organizacional (30 de abril de 2027) y Anticorrupción (23 de noviembre de 2027), emitidos y aún no vigentes |
| Modelo de las Tres Líneas (The IIA, 2020) | Dónde termina la gestión del riesgo de la primera y la segunda línea y empieza la auditoría interna: la familia procesa lo que la segunda línea entrega, no lo reemplaza | Por verificar en theiia.org |
| COSO, Control Interno — Marco Integrado (2013) | Cinco componentes y diecisiete principios: la referencia con la que se califica un control y se escribe el criterio de un hallazgo | Por verificar en coso.org. Publicación de pago: se citan sus componentes y sus principios, nunca su texto |
| ISO 19011:2018, directrices para la auditoría de sistemas de gestión | El programa de auditoría y la evidencia, para las auditorías de sistemas de gestión (ISO 27001, ISO 9001) | Norma de pago: se citan su número y sus capítulos. Por verificar en iso.org |

**La regulación de la auditoría interna en el sector financiero**, por país, identificada y por
verificar en su fuente primaria antes de construir:

| País | Norma | Qué exige a esta familia |
|---|---|---|
| Colombia | Superintendencia Financiera, Circular Básica Jurídica, parte I, título I, capítulo IV (el sistema de control interno), modificado por la Circular Externa 008 de 2023 | El plan de auditoría, el comité de auditoría y el seguimiento de las debilidades de control |
| Perú | SBS, Reglamento de Auditoría Interna, Resolución SBS 11699-2008, y sus modificaciones | El plan anual de trabajo, sus informes a la SBS y el seguimiento de las observaciones |
| Brasil | CMN, Resolución 4.879 de 2020, la auditoría interna de las instituciones autorizadas por el Banco Central | El plan, su aprobación por el consejo y el informe al comité de auditoría |
| México, Chile y Ecuador | La CNBV (Disposiciones de carácter general aplicables a las instituciones de crédito), la CMF (Recopilación Actualizada de Normas) y la Superintendencia de Bancos | Por identificar el capítulo exacto de cada una |

## Decisión

**Criterio CAE · La auditoría interna.** Tres agentes, uno por cada trabajo recurrente que hoy se
hace a mano contra documentos, y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Prudencia**, del latín *prudentia*, contracción de *providentia*, «ver antes»: el plan que mira el riesgo antes de que ocurra | `criterio-audit-plan` | Contrasta el plan de auditoría con el universo auditable y con la matriz de riesgos de la organización: qué riesgo alto no tiene un trabajo, qué unidad pasó su ciclo sin auditarse, qué trabajo va atrasado, qué cambio al plan no tiene aprobación y si las horas alcanzan |
| **Justo**, del latín *iustus*, «conforme a derecho»: cada hallazgo contra su criterio | `criterio-audit-work` | Contrasta cada trabajo con su programa y sus papeles: que cada hallazgo tenga su criterio, su condición, su causa y su efecto, con la referencia al papel que lo soporta; que cada paso del programa se haya ejecutado y revisado, y que el informe diga lo mismo que los papeles |
| **Remedios**, del latín *remedium*, «lo que vuelve a curar»: cada hallazgo hasta su remedio | `criterio-remediation` | Lleva cada hallazgo hasta su cierre: el plan de acción con responsable y fecha, la evidencia de que se implementó, las fechas que se corren una y otra vez, los hallazgos que vuelven a aparecer y los riesgos que la gerencia aceptó sin que lo supiera el comité |

### Las señales que calcula el código

| Agente | Señal | Cuándo |
|---|---|---|
| Prudencia | `high_risk_not_covered` | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo que fija la metodología |
| Prudencia | `auditable_unit_overdue` | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo |
| Prudencia | `engagement_behind_schedule` | Un trabajo del plan pasó su fecha de inicio o de cierre sin estar en curso o terminado |
| Prudencia | `plan_change_unapproved` | Un trabajo se agregó, se canceló o se aplazó sin el acta del comité o del consejo que lo apruebe |
| Prudencia | `plan_hours_exceed_capacity` | Las horas del plan superan las horas disponibles del equipo en el periodo |
| Prudencia | `topical_requirement_missing` | Un trabajo de aseguramiento sobre ciberseguridad o terceros no tiene en su programa el requisito temático vigente |
| Justo | `finding_element_missing` | Un hallazgo no tiene su criterio, su condición, su causa o su efecto |
| Justo | `finding_without_workpaper` | Un hallazgo no cita un papel de trabajo, o cita uno que no existe |
| Justo | `procedure_not_executed` | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica |
| Justo | `workpaper_not_reviewed` | Un papel de trabajo no tiene la revisión del supervisor antes de la fecha del informe |
| Justo | `report_differs_from_workpapers` | El informe trae un hallazgo, una calificación o una cifra distinta a la de sus papeles |
| Justo | `rating_inconsistent` | La calificación de un hallazgo no es la que da la metodología de la organización para su impacto y su probabilidad |
| Justo | `independence_statement_missing` | Un auditor asignado al trabajo no tiene su declaración de independencia del periodo |
| Remedios | `action_plan_missing` | Un hallazgo comunicado no tiene plan de acción, responsable o fecha |
| Remedios | `action_plan_overdue` | Un plan de acción pasó su fecha sin la evidencia de su implementación |
| Remedios | `due_date_extended_repeatedly` | La fecha de un plan se corrió más veces de las que permite la política |
| Remedios | `closure_without_evidence` | Un plan se dio por cerrado sin la evidencia de su implementación o sin la validación de auditoría |
| Remedios | `finding_repeated` | La misma condición, en el mismo proceso, vuelve a aparecer después de que su hallazgo se cerró |
| Remedios | `risk_accepted_not_reported` | La gerencia aceptó un riesgo por encima del apetito de la organización y no hay comunicación al comité o al consejo |
| Remedios | `external_finding_untracked` | Un hallazgo del revisor fiscal, del auditor externo o del supervisor no está en el registro con su plan |

**Los ciclos, los plazos, la escala de calificación y el apetito de riesgo los fija la
organización**, en su estatuto y su metodología de auditoría: el código calcula y el auditor decide.
Lo que viene de fuera es la estructura de las Normas Globales.

### Lo que nunca hace

- **Emitir una opinión.** No concluye sobre la eficacia del control interno, no firma ni aprueba
  informes y no comunica nada al comité: prepara y contrasta, y el auditor concluye.
- **Calificar por su cuenta.** La calificación de un hallazgo es del auditor; la familia señala
  cuando no corresponde a la metodología, y dice por qué.
- **Cambiar un papel de trabajo.** Procesa los papeles y los informes; nunca los edita.
- **Calificar a las personas.** Ni a los auditores ni a los auditados: el objeto es el trabajo y su
  evidencia.
- **Entrar a los sistemas auditados.** Procesa lo que la organización le entrega: las exportaciones
  de su herramienta de auditoría, los papeles y los documentos.

### Lo que cruza con las otras familias

| Lo que procesa Remedios | Con qué familia |
|---|---|
| Los riesgos aceptados de seguridad y los controles sin evidencia | CISO (Amparo, Guillermo) |
| Las obligaciones regulatorias y sus vencimientos | CLO (Constanza) |
| Los hallazgos sobre conciliaciones, pagos y presupuesto | CFO (Clara, Tomás) |
| La agenda y el material del comité de auditoría | EA (Ofelia) |

### Los documentos que procesan

| Documento | Formato esperado | Agente |
|---|---|---|
| El estatuto y la metodología de auditoría: ciclos, escala de calificación, plazos de seguimiento | Word o PDF | Los tres |
| El universo auditable y la matriz de riesgos de la segunda línea | Excel o CSV | Prudencia |
| El plan anual aprobado, sus cambios y las actas del comité de auditoría | Excel, Word o PDF | Prudencia |
| Los programas de trabajo y los papeles de trabajo de cada trabajo | Excel, Word o PDF, o la exportación de la herramienta de auditoría | Justo |
| Los informes de auditoría | Word o PDF | Justo |
| El registro de hallazgos y planes de acción | Excel o CSV, con el mapeo de columnas del setup | Remedios |
| Las evidencias de implementación | PDF, Excel o imagen con texto | Remedios |
| Los informes del revisor fiscal, del auditor externo y del supervisor | PDF | Remedios |

### Los comandos

Cada agente tiene su instalación (`*-setup`), su revisión completa (`*-scan`), un reporte por cada
grupo de señales y su despertador (`*-wake`):

- **Prudencia:** `plan-coverage` (el plan contra los riesgos y el universo), `plan-status` (el
  avance y los cambios), `plan-capacity` (las horas).
- **Justo:** `finding-check` (cada hallazgo y sus elementos), `workpaper-check` (el programa, los
  papeles y su revisión), `report-check` (el informe contra los papeles).
- **Remedios:** `action-status` (los planes contra su fecha), `closure-check` (cada cierre contra su
  evidencia), `committee-brief` (lo que el comité de auditoría tiene que saber: lo vencido, lo
  repetido y los riesgos aceptados).

### La prueba

- **Organizaciones sintéticas** de banca, cooperativas y seguros, más dos controles, con su universo
  auditable, su matriz de riesgos, el plan y sus actas, tres trabajos con sus programas, papeles e
  informes, y el registro de hallazgos con sus evidencias. Nombres, documentos y empresas
  inventados.
- **La clave** siembra las señales de los tres agentes; los controles no tienen ninguna.
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los tres
  agentes; estable con la regla de la decisión 0020.

## Lo que queda abierto

1. **Los nombres**: Prudencia, Justo y Remedios, por aceptar por José.
2. **La estructura**: tres agentes, sus señales y sus comandos, por aceptar por José.
3. **Las fuentes:** verificadas el 2026-11-24 las que dice la tabla; el motor no usa una fuente sin
   verificar. Antes de construir: el texto en español de las normas 9.4, 11.5, 14.3, 14.4 y 15.2, el
   Modelo de las Tres Líneas, COSO 2013 e ISO 19011.
4. **Los formatos de exportación:** las herramientas de auditoría que más se usan en la región
   —TeamMate+, AuditBoard, Ideagen (Pentana) y SAP Audit Management—, cada una con su fuente
   verificada o con los encabezados de una exportación real, como en la CFO.
5. **La regulación de cada país:** el capítulo exacto de México, Chile y Ecuador, y el texto vigente
   de Colombia, Perú y Brasil, para las señales que dependen de un plazo regulatorio.
6. **El sector público:** el control interno de las entidades públicas (en Colombia, la Ley 87 de
   1993 y el MIPG) queda fuera de la 0.1.0.
