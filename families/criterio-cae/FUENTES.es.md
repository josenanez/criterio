# criterio-cae · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0033](../../docs/decisions/0033-la-familia-cae.md), regla 1).

## Las normas de la auditoría interna

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | The IIA · Normas Globales de Auditoría Interna (Global Internal Audit Standards) | 2024; publicadas el 9 de enero de 2024, obligatorias desde el 9 de enero de 2025; versión en español de The IIA | [theiia.org/standards](https://www.theiia.org/en/standards/) · [versión en español](https://www.theiia.org/globalassets/site/standards/editable-versions/global-internal-audit-standards-spanish.pdf) | 2026-11-24 | Verificada: Cinco dominios y quince principios. Verificados: los títulos de la versión en español y el texto de 2.2 y 2.3 en ella; el de 8.4, 9.4, 9.5, 11.5, 12.1, 12.3, 13.6, 14.3, 14.4, 14.6 y 15.2 en la versión condensada en inglés del mismo sitio. Todos los derechos reservados: reproducir o traducir su texto pide permiso de The IIA (copyright@theiia.org). Se citan su número y su título, nunca su texto | La estructura de los tres agentes: el plan (9.4), la coordinación (9.5), la escalada de un riesgo aceptado (11.5), la supervisión (12.3), el programa (13.6), el hallazgo y su prioridad (14.2 y 14.3), los planes de acción (14.4, 15.1), la documentación (14.6), la confirmación (15.2), la objetividad (2.2) y la evaluación externa (8.4) |
| F-02 | The IIA · Requisitos temáticos (Topical Requirements) | Ciberseguridad, vigente desde el 5 de febrero de 2026; Terceros, desde el 15 de septiembre de 2026 | [theiia.org/topical-requirements](https://www.theiia.org/en/standards/2024-standards/topical-requirements/) | 2026-11-24 | Verificada: Obligatorios para los trabajos de aseguramiento sobre su tema; cada uno rige doce meses después de su emisión. Emitidos y aún no vigentes: Comportamiento Organizacional (15 de diciembre de 2026), Resiliencia Organizacional (30 de abril de 2027) y Anticorrupción (23 de noviembre de 2027) | La señal topical_requirement_missing de Prudencia, con las fechas de vigencia |
| F-03 | The IIA · Assurance and Advice in Support of Effective Governance: Three Lines Model, declaración de posición | Publicada el 8 de julio de 2026; reemplaza el documento de 2020 | [theiia.org/statements-of-position](https://www.theiia.org/en/resources/statements-of-position/) | 2026-11-24 | Verificada: El consejo, la primera línea que gestiona el riesgo, la segunda que apoya y desafía, y la auditoría interna como tercera línea independiente. Acceso libre, todos los derechos reservados; en inglés y portugués | Dónde termina lo que entrega la segunda línea —la matriz de riesgos— y empieza lo que procesa la familia |
| F-04 | COSO · Control Interno — Marco Integrado | 1992, actualizado en 2013 | [coso.org/guidance-on-ic](https://www.coso.org/guidance-on-ic) | 2026-11-24 | Verificada: Cinco componentes —entorno de control, evaluación de riesgos, actividades de control, información y comunicación, y supervisión— y diecisiete principios, según el póster de COSO de descarga libre. El marco es de pago: se citan sus componentes y sus principios, nunca su texto | La referencia con la que se escribe el criterio de un hallazgo de control |
| F-05 | ISO 19011 · Directrices para la auditoría de sistemas de gestión | La edición de 2018 aparece retirada en iso.org; la de 2026 figura en los catálogos de ANSI, AFNOR y BSI | [iso.org/standard/70017](https://www.iso.org/standard/70017.html) | 2026-11-24 | Por verificar: La página de la edición de 2026 en iso.org no respondió. Norma de pago. Fuera de la 0.1.0 hasta verificar su edición vigente | El programa de auditoría de un sistema de gestión, cuando entre |

## La regulación de la auditoría interna en el sector financiero

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-10 | Superintendencia Financiera de Colombia · Circular Externa 008 de 2023, que reemplaza el capítulo IV del título I de la parte I de la Circular Básica Jurídica | 16 de mayo de 2023 | [superfinanciera.gov.co, Circulares Externas 2023](https://www.superfinanciera.gov.co/publicaciones/10113115/normativanormativa-generalcirculares-externas-cartas-circulares-y-resoluciones-desde-el-ano-circulares-externascirculares-externas-10113115/) | 2026-11-24 | Verificada: Verificada en el anexo oficial de la circular (ance008_23.docx, descargado de la página de circulares externas 2023 de la SFC): el comité de auditoría aprueba el plan anual de auditoría interna (4.2.1.1), sus modificaciones se sustentan y aprueban por el mismo proceso que la aprobación inicial (3.1.13), el comité monitorea su cumplimiento (4.2.5.3), verifica que se implementen las recomendaciones de la auditoría interna, la revisoría fiscal y los auditores externos (4.2.3.7) e informa a la junta directiva al menos cada 6 meses (4.2.2.1) | Quién aprueba el plan y sus cambios en Colombia: el comité de auditoría |
| F-11 | SBS del Perú · Reglamento de Auditoría Interna, Resolución SBS 11699-2008, con sus modificaciones | 28 de noviembre de 2008; modificada por las resoluciones SBS 1325-2018 y 1132-2025, entre otras | [compilación de terceros](https://regalert.today/document/sbs-resolution-no-11699-2008-internal-audit-regulation-798e2930-665d-4b71-9bff-c4d0c2152508) | 2026-11-24 | Por verificar: Según la compilación: el directorio aprueba el plan anual y una copia llega a la SBS a más tardar el 31 de diciembre (art. 16); el comité aprueba sus cambios significativos (art. 17); cada informe de avance trae el estado de las observaciones de la SBS (art. 18). Falta el texto oficial: el sitio de la SBS no lo trae en su sección de regulación y El Peruano no tiene en línea la edición de 2008 | Los plazos del plan en el Perú, cuando se verifique |
| F-12 | Conselho Monetário Nacional · Resolución 4.879 del 23 de diciembre de 2020, la auditoría interna | Vigente desde el 1 de enero de 2021; modificada por las resoluciones 5.117 y 5.177 de 2024 | [bcb.gov.br, exibenormativo](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20CMN&numero=4879) | 2026-11-24 | Verificada: Verificada en el texto del Banco Central do Brasil: el plan anual de auditoría interna, basado en la evaluación de riesgos, con los procesos por nivel de riesgo, el cronograma y los recursos (art. 19, I), y los papeles de trabajo de cada trabajo (art. 19, II, b); el plan y el informe anual los aprueban el consejo de administración y el comité de auditoría, cuando está constituido (art. 19, parágrafo único); los documentos, cinco años a disposición del Banco Central (art. 25). Modificada por las resoluciones CMN 5.117/2024 (art. 1) y 5.177/2024 (art. 16, IV; revoca el art. 10), que no tocan esos artículos | Quién aprueba el plan en Brasil: el consejo de administración y el comité de auditoría |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **5 %** de sus ingresos pierden las organizaciones por fraude cada año, según la estimación de los examinadores de fraude | [ACFE, Occupational Fraud 2026: A Report to the Nations](https://acfe.com/RTTN) | 2026 | 2.402 casos de 143 países y territorios, investigados entre enero de 2024 y septiembre de 2025 | Verificada: Verificada contra el informe de la ACFE el 24 de noviembre de 2026 (pp. 4 y 9). Uso con atribución: Copyright 2026 by the Association of Certified Fraud Examiners, Inc. |
| C-02 | **43 %** de los fraudes se detectan por una denuncia, casi tres veces más que por el método que le sigue | [ACFE, Occupational Fraud 2026: A Report to the Nations](https://acfe.com/RTTN) | 2026 | 2.402 casos de 143 países y territorios, investigados entre enero de 2024 y septiembre de 2025 | Verificada: Verificada contra el informe de la ACFE el 24 de noviembre de 2026 (pp. 4 y 23). Uso con atribución: Copyright 2026 by the Association of Certified Fraud Examiners, Inc. |
| C-03 | **12 meses** dura, en la mediana, un fraude antes de que se detecte | [ACFE, Occupational Fraud 2026: A Report to the Nations](https://acfe.com/RTTN) | 2026 | 2.402 casos de 143 países y territorios, investigados entre enero de 2024 y septiembre de 2025 | Verificada: Verificada contra el informe de la ACFE el 24 de noviembre de 2026 (pp. 4 y 18). Uso con atribución: Copyright 2026 by the Association of Certified Fraud Examiners, Inc. |

## Cómo se agrega una fuente

1. Se agrega en `fuentes.json` con el siguiente identificador libre —F-NN para fuentes técnicas
   y normativas, C-NN para cifras de terceros— y la fila entera: versión, enlace al emisor, fecha
   de consulta, estado y uso. Después se corre `python3 scripts/familias.py`.
2. Un campo de factura que procese el motor va en la lista de campos de su fuente, con su
   identificador en el anexo; la puerta falla si el motor usa uno que no está verificado.
3. Mientras diga «por verificar», nada se construye sobre ella: la puerta falla si un comando
   la cita.
4. Cuando una fuente cambia de versión, se agrega la nueva fila y la anterior se marca como
   reemplazada, sin borrarla: el material de prueba generado con ella sigue citándola.
