# 0033 · La familia CAE: la auditoría interna, con tres agentes sobre las Normas Globales de Auditoría Interna

**Fecha:** 2026-11-24 · **Estado:** aceptada: los nombres y la estructura, por José el 2026-11-24. Las fuentes se verifican una a una (abajo, con la fecha de cada verificación) ·
**Modifica:** —

## Contexto

José Francisco Ñáñez fijó el orden de los nuevos diseños: primero la CAE, la auditoría interna;
después la CDO, los datos. Esta decisión es la primera.

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
| Normas Globales de Auditoría Interna (The IIA, 2024) | Cinco dominios y quince principios. Lo que usa la familia: el plan basado en una evaluación de riesgos documentada, hecha al menos una vez al año, que considera el gobierno de TI, el riesgo de fraude y los programas de cumplimiento y ética, y que el consejo aprueba con sus cambios significativos (9.4); la coordinación con otros proveedores de aseguramiento (9.5); la escalada de un riesgo aceptado por encima del apetito, primero a la alta dirección y después al consejo (11.5); la supervisión de cada trabajo y su evidencia (12.3); el programa de trabajo, aprobado antes de ejecutarse (13.6); cada hallazgo como la diferencia entre el criterio y la condición, con su causa raíz cuando se pueda identificar, su efecto y su prioridad según la metodología (14.2 y 14.3); las recomendaciones y los planes de acción (14.4); la documentación revisada y aprobada (14.6); la comunicación final con el responsable y la fecha de cada plan (15.1); la confirmación de su implementación, con la explicación documentada de cada atraso (15.2); la objetividad del auditor, que no da aseguramiento sobre lo que tuvo a su cargo en los doce meses anteriores (2.2 y 2.3), y la evaluación externa de calidad, al menos una vez cada cinco años (8.4) | Verificado el 2026-11-24 en theiia.org: la versión en español, «Publicado el 9 de enero de 2024», con sus dominios, principios y títulos, y el texto de 2.2 y 2.3; el de las demás normas, en la versión condensada en inglés del mismo día. Obligatorias desde el 9 de enero de 2025. **Uso restringido:** todos los derechos reservados; reproducir o traducir su texto pide permiso de The IIA (copyright@theiia.org). Se citan su número y su título, nunca su texto |
| Requisitos temáticos de The IIA | Lo que un trabajo de aseguramiento sobre un tema tiene que cubrir. Vigentes: Ciberseguridad, desde el 5 de febrero de 2026, y Terceros, desde el 15 de septiembre de 2026 | Verificado el 2026-11-24 en theiia.org/en/standards/2024-standards/topical-requirements. Cada uno rige doce meses después de su emisión; Comportamiento Organizacional (15 de diciembre de 2026), Resiliencia Organizacional (30 de abril de 2027) y Anticorrupción (23 de noviembre de 2027), emitidos y aún no vigentes |
| Modelo de las Tres Líneas (The IIA, declaración de posición de julio de 2026) | El consejo, la gestión del riesgo de la primera línea, el apoyo y el desafío de la segunda y el aseguramiento independiente de la auditoría interna: la familia procesa lo que la segunda línea entrega, no lo reemplaza | Verificado el 2026-11-24 en theiia.org/en/resources/statements-of-position: «Assurance and Advice in Support of Effective Governance: Three Lines Model», publicada el 8 de julio de 2026, reemplaza el documento de 2020. Acceso libre, todos los derechos reservados; sin versión en español |
| COSO, Control Interno — Marco Integrado (2013) | Cinco componentes —entorno de control, evaluación de riesgos, actividades de control, información y comunicación, y supervisión— y diecisiete principios: la referencia con la que se escribe el criterio de un hallazgo de control | Verificado el 2026-11-24 en coso.org/guidance-on-ic: emitido en 1992 y actualizado en 2013; el marco es de pago y el póster de los principios, de descarga libre. Se citan sus componentes y sus principios, nunca su texto |
| ISO 19011, directrices para la auditoría de sistemas de gestión | El programa de auditoría y la evidencia, para las auditorías de sistemas de gestión (ISO 27001, ISO 9001) | La edición de 2018 aparece retirada en iso.org/standard/70017 (verificado el 2026-11-24). La de 2026 figura en los catálogos de ANSI, AFNOR y BSI; su página de iso.org no respondió. Norma de pago. **Fuera de la 0.1.0** hasta verificar su edición vigente |

**La regulación de la auditoría interna en el sector financiero**, por país:

| País | Norma | Qué exige a esta familia | Estado de la fuente |
|---|---|---|---|
| Colombia | Superintendencia Financiera, Circular Externa 008 del 16 de mayo de 2023, que reemplaza el capítulo IV del título I de la parte I de la Circular Básica Jurídica (el sistema de control interno) | El comité de auditoría aprueba el plan anual de auditoría interna y sus cambios, y vigila que se implementen las recomendaciones de la auditoría interna, la externa y el revisor fiscal; informa a la junta al menos cada seis meses | Verificado en parte el 2026-11-24: la fecha y el reemplazo del capítulo, en la carta de la circular; el numeral de la auditoría interna, en la compilación de Colpensiones, que se cortó. **Por verificar** en el texto oficial de la SFC |
| Perú | SBS, Reglamento de Auditoría Interna, Resolución SBS 11699-2008, del 28 de noviembre de 2008, modificada por las resoluciones SBS 1325-2018 y 1132-2025, entre otras | El directorio aprueba el plan anual de trabajo y una copia llega a la SBS a más tardar el 31 de diciembre del año anterior (art. 16); el comité de auditoría aprueba sus cambios significativos (art. 17); cada informe de avance trae el estado de las observaciones de la SBS (art. 18) | Verificado el 2026-11-24 en una compilación de terceros (regalert.today), hasta el art. 18. **Por verificar** en el texto oficial de la SBS, con sus modificaciones |
| Brasil | CMN, Resolución 4.879 del 23 de diciembre de 2020, vigente desde el 1 de enero de 2021, modificada por las resoluciones CMN 5.117 y 5.177 de 2024 | Un plan anual basado en la evaluación de riesgos, con los procesos por nivel de riesgo, el cronograma y los recursos, aprobado por el consejo de administración y el comité de auditoría (art. 19), y un informe de seguimiento de las recomendaciones; los documentos, cinco años a disposición del Banco Central (art. 25) | Verificado el 2026-11-24 en legisweb.com.br, con las modificaciones. **Por verificar** en normativos.bcb.gov.br |
| México, Chile y Ecuador | La CNBV, la CMF y la Superintendencia de Bancos | Por identificar el capítulo exacto de cada una | — |

## Decisión

**Criterio CAE · La auditoría interna.** Tres agentes, uno por cada trabajo recurrente que hoy se
hace a mano contra documentos, y Rostrum, como en las demás familias:

| Agente | Plugin | Lo que hace |
|---|---|---|
| **Prudencia**, del latín *prudentia*, contracción de *providentia*, «ver antes»: el plan que mira el riesgo antes de que ocurra | `criterio-audit-plan` | Contrasta el plan de auditoría con el universo auditable y con la matriz de riesgos de la organización: qué riesgo alto no tiene un trabajo, qué unidad pasó su ciclo sin auditarse, qué trabajo va atrasado, qué cambio al plan no tiene aprobación y si las horas alcanzan |
| **Justo**, del latín *iustus*, «conforme a derecho»: cada hallazgo contra su criterio | `criterio-audit-work` | Contrasta cada trabajo con su programa y sus papeles: que cada hallazgo tenga su criterio, su condición, su causa y su efecto, con la referencia al papel que lo soporta; que cada paso del programa se haya ejecutado y revisado, y que el informe diga lo mismo que los papeles |
| **Remedios**, del latín *remedium*, «lo que vuelve a curar»: cada hallazgo hasta su remedio | `criterio-remediation` | Lleva cada hallazgo hasta su cierre: el plan de acción con responsable y fecha, la evidencia de que se implementó, las fechas que se corren una y otra vez, los hallazgos que vuelven a aparecer y los riesgos aceptados que no llegaron a quien debían llegar |

### Las señales que calcula el código

| Agente | Señal | Cuándo | Norma |
|---|---|---|---|
| Prudencia | `high_risk_not_covered` | Un riesgo calificado alto o crítico en la matriz no tiene un trabajo en el plan dentro del ciclo que fija la metodología | 9.4 |
| Prudencia | `auditable_unit_overdue` | Una unidad del universo auditable pasó su ciclo de rotación sin un trabajo | 9.4 |
| Prudencia | `risk_assessment_outdated` | La evaluación de riesgos que sostiene el plan tiene más de un año | 9.4 |
| Prudencia | `plan_area_not_considered` | El plan no considera el gobierno de TI, el riesgo de fraude o los programas de cumplimiento y ética, ni dice por qué | 9.4 |
| Prudencia | `plan_change_unapproved` | Un trabajo se agregó, se canceló o se aplazó sin el acta del órgano que aprueba el plan según el estatuto | 9.4 |
| Prudencia | `engagement_behind_schedule` | Un trabajo del plan pasó su fecha de inicio o de cierre sin estar en curso o terminado | 9.4 |
| Prudencia | `plan_hours_exceed_capacity` | Las horas del plan superan las horas disponibles del equipo en el periodo | 9.4 |
| Prudencia | `topical_requirement_missing` | Un trabajo de aseguramiento sobre ciberseguridad o terceros no tiene en su programa el requisito temático vigente | Requisitos temáticos |
| Prudencia | `external_assessment_overdue` | La última evaluación externa de calidad tiene más de cinco años | 8.4 |
| Justo | `work_program_not_approved` | El programa de trabajo no tiene la aprobación del responsable de auditoría antes de su primer papel | 13.6 |
| Justo | `finding_element_missing` | Un hallazgo no tiene su criterio, su condición, su efecto o su prioridad, o no tiene su causa raíz ni la razón por la que no se pudo identificar | 14.2 y 14.3 |
| Justo | `finding_without_workpaper` | Un hallazgo no cita un papel de trabajo, o cita uno que no existe | 14.6 |
| Justo | `procedure_not_executed` | Un paso del programa de trabajo no tiene un papel de trabajo ni la razón por la que no aplica | 12.3 |
| Justo | `workpaper_not_reviewed` | Un papel de trabajo no tiene la revisión del supervisor y la aprobación del responsable de auditoría antes de la fecha del informe | 12.3 y 14.6 |
| Justo | `report_differs_from_workpapers` | El informe trae un hallazgo, una prioridad o una cifra distinta a la de sus papeles | 14.6 |
| Justo | `rating_inconsistent` | La prioridad de un hallazgo no es la que da la metodología para su impacto y su probabilidad | 14.3 |
| Justo | `auditor_reviews_own_work` | Un auditor asignado a un trabajo de aseguramiento tuvo a su cargo la actividad auditada en los doce meses anteriores | 2.2 |
| Remedios | `action_plan_missing` | Un hallazgo comunicado no tiene plan de acción, responsable o fecha | 15.1 |
| Remedios | `action_plan_overdue` | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso | 15.2 |
| Remedios | `due_date_extended_repeatedly` | La fecha de un plan se corrió más veces de las que permite la metodología | 15.2 |
| Remedios | `closure_without_evidence` | Un plan se dio por cerrado sin la evidencia de su implementación o sin la validación de auditoría | 15.2 |
| Remedios | `finding_repeated` | La misma condición, en el mismo proceso, vuelve a aparecer después de que su hallazgo se cerró | 15.2 |
| Remedios | `risk_accepted_not_escalated` | La gerencia aceptó un riesgo por encima del apetito y no hay constancia de que se discutiera con la alta dirección o, si no se resolvió, de que llegara al consejo | 11.5 |
| Remedios | `external_finding_untracked` | Un hallazgo del revisor fiscal, del auditor externo o del supervisor no está en el registro con su plan | 9.5 |

**Los ciclos, los plazos, la escala de prioridad y el apetito de riesgo los fija la organización**,
en su estatuto y su metodología de auditoría: el código calcula y el auditor decide. Lo que viene
de fuera es la estructura de las Normas Globales y los plazos de la regulación de cada país.

### Lo que nunca hace

- **Emitir una opinión.** No concluye sobre la eficacia del control interno, no firma ni aprueba
  informes y no comunica nada al comité: prepara y contrasta, y el auditor concluye.
- **Calificar por su cuenta.** La prioridad de un hallazgo es del auditor; la familia señala cuando
  no corresponde a la metodología, y dice por qué.
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
| El estatuto y la metodología de auditoría: ciclos, escala de prioridad, plazos de seguimiento | Word o PDF | Los tres |
| El universo auditable, la matriz de riesgos de la segunda línea y la evaluación de riesgos de auditoría | Excel o CSV | Prudencia |
| El plan anual aprobado, sus cambios, las actas del comité y la última evaluación externa de calidad | Excel, Word o PDF | Prudencia |
| Los programas de trabajo y los papeles de trabajo de cada trabajo, con su revisión | Excel, Word o PDF, o la exportación de la herramienta de auditoría | Justo |
| Las asignaciones del equipo y la historia de cargos de cada auditor | Excel o CSV | Justo |
| Los informes de auditoría | Word o PDF | Justo |
| El registro de hallazgos y planes de acción | Excel o CSV, con el mapeo de columnas del setup | Remedios |
| Las evidencias de implementación y las explicaciones de los atrasos | PDF, Excel o imagen con texto | Remedios |
| Los informes del revisor fiscal, del auditor externo y del supervisor | PDF | Remedios |

### Los comandos

Cada agente tiene su instalación (`*-setup`), su revisión completa (`*-scan`), un reporte por cada
grupo de señales y su despertador (`*-wake`):

- **Prudencia:** `plan-coverage` (el plan contra los riesgos y el universo), `plan-status` (el
  avance y los cambios), `plan-capacity` (las horas), `quality-status` (la evaluación externa).
- **Justo:** `finding-check` (cada hallazgo y sus elementos), `workpaper-check` (el programa, los
  papeles y su revisión), `report-check` (el informe contra los papeles), `objectivity-check` (las
  asignaciones contra la historia de cada auditor).
- **Remedios:** `action-status` (los planes contra su fecha), `closure-check` (cada cierre contra su
  evidencia), `committee-brief` (lo que el comité de auditoría tiene que saber: lo vencido, lo
  repetido y los riesgos aceptados).

### La prueba

- **Organizaciones sintéticas** de banca, cooperativas y seguros, más dos controles, en Colombia,
  Perú y Brasil, con su universo auditable, su matriz de riesgos, el plan y sus actas, tres trabajos
  con sus programas, papeles e informes, y el registro de hallazgos con sus evidencias. Nombres,
  documentos y empresas inventados.
- **La clave** siembra las señales de los tres agentes; los controles no tienen ninguna.
- **Versiones:** la 0.1.0, construida con su motor probado; la 0.2.0, con la ronda de los tres
  agentes; estable con la regla de la decisión 0020.

## Lo que queda abierto

1. **Los nombres y la estructura**: aceptados por José el 2026-11-24. Queda cerrado.
2. **Las fuentes:** verificadas el 2026-11-24 las que dicen las tablas; el motor no usa una fuente
   sin verificar. Antes de construir los plazos de cada país: los textos oficiales de la SFC, la SBS
   y el Banco Central de Brasil.
3. **Los formatos de exportación:** las herramientas de auditoría que más se usan en la región
   —TeamMate+, AuditBoard, Ideagen (Pentana) y SAP Audit Management—, cada una con su fuente
   verificada o con los encabezados de una exportación real, como en la CFO. Mientras tanto, el
   setup mapea las columnas de cualquier Excel o CSV.
4. **La regulación de México, Chile y Ecuador:** el capítulo exacto de cada una.
5. **ISO 19011:** su edición vigente, para las auditorías de sistemas de gestión.
6. **El sector público:** el control interno de las entidades públicas (en Colombia, la Ley 87 de
   1993 y el MIPG) queda fuera de la 0.1.0.
