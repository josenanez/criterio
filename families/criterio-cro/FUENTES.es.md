# criterio-cro · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0035](../../docs/decisions/0035-la-familia-cro.md), regla 1).

## Los marcos de la gestión de riesgos

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | ISO 31000:2018 · Gestión del riesgo — Directrices | Segunda edición, febrero de 2018; revisada y confirmada en 2023 | [iso.org](https://www.iso.org/standard/65694.html) | 2026-11-25 | Verificada: Verificada en iso.org: la segunda edición es de febrero de 2018, y la página dice que se revisó y confirmó en 2023. Norma de pago: se citan sus partes por su nombre —los principios, el marco y el proceso—, nunca su texto. Por verificar: el borrador de su revisión | El proceso de la gestión del riesgo en cualquier organización: el riesgo identificado en la matriz, su tratamiento y su seguimiento, que son las señales de Severo y de Casandra |
| F-02 | COSO · Enterprise Risk Management — Integrating with Strategy and Performance | 2017 | [coso.org](https://www.coso.org/) | 2026-11-25 | Por verificar: Sin verificar en su texto. Fuera de la 0.1.0 hasta verificarla | El apetito por riesgo atado a la estrategia y al desempeño, cuando entre |

## La regulación del apetito y la gestión integral de riesgos en el sector financiero

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-10 | Superintendencia Financiera de Colombia · Circular Externa 018 de 2021, el Sistema Integral de Administración de Riesgos (SIAR) | 22 de septiembre de 2021; rige desde el 1 de junio de 2023 | [el texto de la circular](https://www.ambitojuridico.com/sites/default/files/2021-09/circexterna-018-21%28superfinanciera%29.pdf) | 2026-11-25 | Verificada: Verificada en el texto de la circular: crea el Capítulo XXXI de la Circular Básica Contable y Financiera, el SIAR, y el XXXII para las entidades exceptuadas. Integra los riesgos de crédito, mercado, operacional, liquidez, contraparte, garantía, seguros y país; su Parte I trae el marco de apetito de riesgo y el gobierno de riesgos, y su Parte II la agregación de datos y los informes. Por verificar: el texto del Capítulo XXXI sobre el contenido del marco de apetito y el papel de la junta | El marco de apetito de riesgo de una entidad vigilada en Colombia |
| F-11 | Superintendencia de Banca, Seguros y AFP del Perú · Resolución SBS 272-2017, Reglamento de Gobierno Corporativo y de la Gestión Integral de Riesgos | 23 de enero de 2017; vigente desde el 1 de abril de 2018 | [el texto de la resolución](https://cmactacna.com.pe/wp-content/uploads/2021/08/Resolucion-SBS-N%C2%B0-272-2017.pdf) | 2026-11-25 | Verificada: Verificada en su texto: define el apetito, la capacidad y los límites de riesgo (art. 2); el directorio aprueba el sistema de apetito (art. 7) y firma una declaración anual de cumplimiento (art. 8); la unidad de riesgos es independiente de las de negocio (art. 25), su jefe reporta al directorio, a la gerencia o al comité de riesgos (art. 26), y la empresa envía a la SBS un informe anual de riesgos (art. 27) | El apetito y los límites que aprueba el directorio de una empresa supervisada en el Perú |
| F-12 | Banco Central do Brasil · Resolución CMN 4.557 de 2017, la estructura de gestión de riesgos y de capital | 23 de febrero de 2017 | [la versión en inglés del Banco Central](https://www.bcb.gov.br/ingles/norms/brprudential/Resolution4557.pdf) | 2026-11-25 | Verificada: Verificada en su versión en inglés del Banco Central: la declaración de apetito por riesgos, la RAS (art. 5), las pruebas de estrés (arts. 11 a 19) y los segmentos S1 a S4 (art. 2), con una estructura simplificada para el S5 (art. 3). Por verificar: los artículos del CRO y del comité de riesgos, y las reformas posteriores, en el texto vigente en portugués | La declaración de apetito por riesgos de una institución autorizada en Brasil |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **30 %** de las organizaciones describen sus procesos de supervisión de riesgos como maduros o robustos | [AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte, The State of Risk Oversight, 17.ª edición](https://www.aicpa-cima.com/news/article/rising-risk-complexity-outpaces-organizations-strategic-readiness-finds-new-aicpa-and-north-carolina-state-university-study) | 2026 | 331 altos ejecutivos y miembros de junta | Verificada: Verificada en el comunicado de AICPA y CIMA del 9 de septiembre de 2026: solo el 30 % describe los procesos de supervisión de riesgos de su organización como maduros o robustos. |
| C-02 | **29 %** de las organizaciones tienen un apetito por riesgo articulado formalmente en su planeación estratégica | [AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte, The State of Risk Oversight, 17.ª edición](https://www.aicpa-cima.com/news/article/rising-risk-complexity-outpaces-organizations-strategic-readiness-finds-new-aicpa-and-north-carolina-state-university-study) | 2026 | 331 altos ejecutivos y miembros de junta | Verificada: Verificada en el comunicado de AICPA y CIMA del 9 de septiembre de 2026: solo el 29 % ha articulado formalmente su apetito por riesgo en el contexto de la planeación estratégica. |
| C-03 | **11 %** de las organizaciones dicen que su gestión de riesgos les da una ventaja estratégica o competitiva | [AICPA y CIMA con la Iniciativa ERM de la Universidad Estatal de Carolina del Norte, The State of Risk Oversight, 17.ª edición](https://www.aicpa-cima.com/news/article/rising-risk-complexity-outpaces-organizations-strategic-readiness-finds-new-aicpa-and-north-carolina-state-university-study) | 2026 | 331 altos ejecutivos y miembros de junta | Verificada: Verificada en el comunicado de AICPA y CIMA del 9 de septiembre de 2026: solo el 11 % dice que el proceso de gestión de riesgos de su organización le da una ventaja estratégica o competitiva única. |

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
