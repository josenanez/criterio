# criterio-clo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0009](../../docs/decisions/0009-scope-clo.md), regla 1).

## El rol

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-02 | NCMA y World Commerce & Contracting · Contract Management Standard | Cuarta edición, 19 de junio de 2025 | [worldcc.com](https://news.worldcc.com/ccmi/contract-management-standard-fourth-edition-launch) | 2026-10-23 | Verificada: Se consultó el anuncio de su publicación por el Commerce & Contract Management Institute: cuarta edición, con un marco armonizado para todos los mercados, industrias y funciones. No se transcribe su contenido | El marco del rol de Fidel, quien responde por lo que la empresa firmó. El de Constanza es la ISO 37301 (F-01) |

## Marcos de referencia

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | ISO 37301:2021 · Sistemas de gestión del cumplimiento — Requisitos con orientación para su uso | Edición 1, abril de 2021; confirmada en su revisión sistemática de 2026 | [iso.org](https://www.iso.org/standard/75080.html) | 2026-10-20 | Verificada: Se consultó la ficha de la norma en ISO: título, edición, estado y alcance —establecer, desarrollar, implementar, evaluar, mantener y mejorar un sistema de gestión del cumplimiento—. Se usa como modelo de la matriz de obligaciones: cada obligación con su fuente, su responsable y su evidencia. No se transcribe su contenido | El modelo de la matriz de obligaciones que procesa Constanza; ninguna obligación sale de aquí: las define la organización |

## La contratación pública

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-03 | Colombia · Decreto 1082 de 2015, artículo 2.2.1.1.1.7.1 · Publicidad en el SECOP | La compilación del decreto publicada por la CRA, consultada el 30 de octubre de 2026 | [normas.cra.gov.co](https://normas.cra.gov.co/gestor/docs/decreto_1082_2015.htm) | 2026-10-30 | Verificada: La Entidad Estatal publica en el SECOP los documentos y los actos del Proceso de Contratación dentro de los tres días siguientes a su expedición. El decreto dice «días»: el motor los cuenta hábiles, sin festivos, la lectura que menos señales levanta | El plazo para publicar un contrato público de Colombia |
| F-04 | Colombia Compra Eficiente · ¿Cuál debe ser el valor de las garantías? · y concepto C-1270 de 2025 | La página del 7 de febrero de 2017 y el concepto del 9 de octubre de 2025 | [operaciones.colombiacompra.gov.co](https://operaciones.colombiacompra.gov.co/node/20711) · [relatoria.colombiacompra.gov.co](https://relatoria.colombiacompra.gov.co/conceptos/c-1270-de-2025/) | 2026-10-30 | Verificada: La garantía de cumplimiento vale por lo menos el 10 % del valor del contrato, salvo que el contrato supere 1.000.000 de SMMLV (Decreto 1082 de 2015, artículos 2.2.1.2.3.1.11 a 2.2.1.2.3.1.16), y está vigente hasta la liquidación | El mínimo de la garantía de cumplimiento de un contrato público de Colombia |
| F-05 | Ecuador · Procuraduría General del Estado · Boletín «Reflexiones sobre contratación pública» | El boletín publicado en agosto de 2022 | [biblioteca.pge.gob.ec](https://biblioteca.pge.gob.ec/images/2022/INFOGRAFIAS/AGOSTO/boletin_reflexiones_contratacion.pdf) | 2026-10-30 | Verificada: La garantía de fiel cumplimiento es el 5 % del valor del contrato (LOSNCP, artículos 74 a 76); no se exige en los contratos cuya cuantía es menor que el coeficiente 0,000002 por el Presupuesto Inicial del Estado (RGLOSNCP, artículo 261). Ese umbral cambia con cada presupuesto: lo dice la configuración | El mínimo de la garantía de fiel cumplimiento de un contrato público de Ecuador y su umbral |
| F-06 | Perú · OECE · Opinión sobre la garantía de fiel cumplimiento, Reglamento de la Ley 32069 (DS 009-2025-EF) | La opinión del 14 de septiembre de 2026 (expediente 112712) | [lpderecho.pe](https://img.lpderecho.pe/wp-content/uploads/2026/10/opinion-d099-2026-oece-dtn_lp_derecho.pdf) | 2026-10-30 | Verificada: El artículo 113.1 del Reglamento fija la garantía de fiel cumplimiento en una suma equivalente al 10 % del monto del contrato original | El mínimo de la garantía de fiel cumplimiento de un contrato público de Perú |
| F-07 | Chile · Decreto 661 de 2024, Hacienda · Reglamento de la Ley 19.886, artículos 39 y 77 | El texto publicado el 12 de diciembre de 2024, el que trajo José Francisco Ñáñez desde la BCN y una copia de la Asociación Chilena de Municipalidades | [bcn.cl](https://bcn.cl/hEf6Ya) · [achm.cl](https://achm.cl/wp-content/uploads/2025/03/Decreto-661-Hacienda.pdf) | 2026-10-30 | Verificada: El contrato está siempre disponible en el Sistema de Información (artículo 39), sin un plazo en días. En el trato directo, la resolución, el texto del contrato y la orden de compra se publican dentro de veinticuatro horas (artículo 77) | El plazo para publicar un contrato de trato directo en Chile |
| F-08 | ChileCompra · Garantías | La página actualizada el 25 de marzo de 2026 | [chilecompra.cl](https://www.chilecompra.cl/garantias) | 2026-10-30 | Verificada: En las contrataciones superiores a 1.000 UTM se exige, como regla general, una garantía de fiel y oportuno cumplimiento del 5 % del precio adjudicado (Ley 19.886, artículo 11; Reglamento, artículos 121 a 125). El umbral en pesos cambia con la UTM: lo dice la configuración | El mínimo de la garantía de fiel cumplimiento de un contrato público de Chile y su umbral |
| F-09 | México · Ley de Adquisiciones, Arrendamientos y Servicios del Sector Público, artículo 69 | La ley nueva publicada en el DOF el 16 de abril de 2025, el texto vigente de la Cámara de Diputados que trajo José Francisco Ñáñez | [diputados.gob.mx](https://www.diputados.gob.mx/LeyesBiblio/index.htm) | 2026-10-30 | Verificada: El proveedor garantiza el cumplimiento del contrato; las bases, la forma y el porcentaje los fija cada dependencia o entidad, no la ley. La garantía se presenta en el plazo de la convocatoria o, en su defecto, a más tardar dentro de los diez días naturales siguientes a la firma del contrato | El plazo de entrega de la garantía de cumplimiento de un contrato público de México |
| F-10 | TCU · Licitações e Contratos: Orientações e Jurisprudência · Lei 14.133/2021, artigos 94 e 98 | El manual actualizado el 29 de agosto de 2025 | [licitacoesecontratos.tcu.gov.br](https://licitacoesecontratos.tcu.gov.br/5-11-7-divulgacao) · [licitacoesecontratos.tcu.gov.br](https://licitacoesecontratos.tcu.gov.br/5-4-4-garantia-adicional-2/) | 2026-10-30 | Verificada: La divulgación del contrato en el PNCP es condición indispensable de su eficacia: dentro de 20 días hábiles desde la firma si hubo licitación, y de 10 días hábiles si fue contratación directa (artículo 94). La garantía de ejecución es de hasta el 5 % del valor inicial del contrato, y puede subir hasta el 10 % si se justifica por la complejidad técnica y los riesgos (artículo 98) | El plazo de divulgación y el tope de la garantía de un contrato público de Brasil |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **8,6 %** del valor de los contratos se erosiona en promedio por una gestión contractual deficiente; los mejores, poco más de 3 %, los peores, más de 20 % | [World Commerce & Contracting con Deloitte](https://www.deloitte.com/us/en/services/tax/articles/contract-management-lifecycle-insights.html) | 2022 | Más de 1.200 organizaciones | Verificada: Actualización de 2022 de la investigación de 2014, que daba 9,2 %; la nota de Deloitte dice «más de 1.200 organizaciones», no un número exacto |
| C-02 | **90 %** de las organizaciones tiene dificultad para encontrar sus propios contratos | [EY Law y Harvard Law School Center on the Legal Profession](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) | 2021 | 1.000 líderes de contratación, dentro de una investigación de más de 2.000 personas en 22 países, enero de 2021 | Verificada: Página 7 del informe |
| C-03 | **19.000** contratos al año gestiona en promedio el equipo de contratación de una organización grande | [EY Law y Harvard Law School Center on the Legal Profession](https://clp.law.harvard.edu/wp-content/uploads/2022/10/ey-contracting-report-june-2021.pdf) | 2021 | 1.000 líderes de contratación, enero de 2021 | Verificada: Página 14 del informe |
| C-04 | **46 %** de las denuncias que llegan al canal ético se comprueban: la tasa mediana más alta que se ha registrado | [NAVEX, Whistleblowing & Incident Management Benchmark Report](https://www.navex.com/en-us/resources/reports/whistleblowing-incident-management-report/) | 2025 | 2,15 millones de reportes de más de 4.000 organizaciones | Verificada: Lo dice la página del informe de 2025 en NAVEX: «2,15 millones de reportes de más de 4.000 organizaciones» y una tasa mediana de comprobación del 46 %, la más alta registrada |

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
