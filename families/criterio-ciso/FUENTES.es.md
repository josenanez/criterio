# criterio-ciso · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0023](../../docs/decisions/0023-la-familia-ciso.md), regla 1).

## El rol

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | O*NET · 15-1212.00 Information Security Analysts | Datos de 2026 (O*NET OnLine) | [onetonline.org](https://www.onetonline.org/link/summary/15-1212.00) | 2026-10-30 | Verificada: Se consultaron las 11 tareas de la ocupación, del Departamento de Trabajo de los Estados Unidos, que lista entre sus títulos el de Information Security Officer; la familia toma tres: documentar las políticas, los procedimientos y las pruebas de seguridad y de emergencia; vigilar el uso de los datos y regular el acceso; y planear el resguardo de la información. No se transcribe su contenido | El marco del rol de Alexis, Guillermo y Amparo (ADR 0023), con el NIST CSF 2.0 (F-02), que ordena la familia, y el NIST SP 800-61 Rev. 3 (F-04), que ordena la respuesta a incidentes |

## Los marcos

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-02 | NIST · The NIST Cybersecurity Framework (CSF) 2.0 · NIST CSWP 29 | Publicado el 26 de febrero de 2024 | [nist.gov](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) · [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) | 2026-10-30 | Verificada: Se consultó la publicación de NIST: las seis funciones —Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS) y Recover (RC)— y sus categorías. La familia se ordena por ellas; el motor no califica la madurez contra el marco | El orden de la familia: qué función cubre cada agente |
| F-03 | ISO/IEC 27001:2022 · Anexo A | La edición de 2022, con sus 93 controles en cuatro grupos (5 a 8) | [iso.org](https://www.iso.org/standard/27001) | 2026-10-30 | Por verificar: Norma de pago: el número y el nombre de cada control se cotejaron en una fuente secundaria. El motor no los trae: toma cada control de la declaración de aplicabilidad de la organización, con el número y el nombre que ella le da, y nunca cita el texto de la norma | El vocabulario de la declaración de aplicabilidad que procesa Alexis |
| F-04 | NIST · SP 800-61 Rev. 3 · Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile | Publicada el 3 de abril de 2025; reemplaza la Rev. 2 | [nist.gov](https://www.nist.gov/publications/incident-response-recommendations-and-considerations-cybersecurity-risk-management-csf) · [nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf) | 2026-10-30 | Verificada: La respuesta a incidentes como perfil comunitario del CSF 2.0: preparación, detección, respuesta y recuperación, con las lecciones aprendidas. Los plazos no salen de aquí: los fija la política de la organización | El orden de lo que procesa Amparo: la línea de tiempo del incidente, sus notificaciones y su revisión posterior |

## Las vulnerabilidades

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-05 | FIRST · Common Vulnerability Scoring System v4.0 · Specification Document | CVSS 4.0, publicado el 1 de noviembre de 2023; documento versión 1.2 | [first.org](https://www.first.org/cvss/specification-document) | 2026-10-30 | Verificada: La escala cualitativa de severidad (tabla 22): ninguna 0.0, baja 0.1–3.9, media 4.0–6.9, alta 7.0–8.9 y crítica 9.0–10.0. El documento dice que su uso es opcional. El motor la usa solo cuando la exportación del escáner trae el puntaje y no la severidad | La severidad de una vulnerabilidad desde su puntaje CVSS |
| F-06 | CISA · Known Exploited Vulnerabilities Catalog · el archivo CSV | El archivo publicado al 28 de octubre de 2026, con doce columnas | [github.com/cisagov/kev-data](https://github.com/cisagov/kev-data) | 2026-10-30 | Verificada: Se verificó la cabecera del archivo en el espejo oficial de CISA (cisagov/kev-data, actualización del 28 de octubre de 2026): la columna forensicTriage es nueva respecto de versiones anteriores. El motor procesa el archivo como lo descarga la organización; nunca se conecta a internet | El lector del catálogo KEV de Guillermo |
| F-07 | CISA · Binding Operational Directive 26-04 · Prioritizing Security Updates Based on Risk | Emitida el 10 de junio de 2026; revoca y reemplaza la BOD 22-01 | [fedramp.gov](https://www.fedramp.gov/notices/0014/) | 2026-10-30 | Por verificar: Se conoce por el aviso de FedRAMP y por fuentes secundarias; la página de CISA no se pudo consultar. Obliga a las agencias federales de los Estados Unidos, no a las organizaciones de la región. El motor no aplica sus plazos: toma la fecha de corrección que trae el catálogo (F-06) y los plazos de la política de la organización | El contexto de la fecha de corrección del catálogo KEV |

## Los campos que procesa el motor

Cada campo de factura que lee `finanzas.py` está aquí con su identificador en la fuente. La
puerta falla si el motor usa uno que no está, o uno por verificar.

**F-06 · CISA · Known Exploited Vulnerabilities Catalog · el archivo CSV**

| Id | Campo | Estado |
|---|---|---|
| cveID | El identificador CVE de la vulnerabilidad | Verificado |
| vendorProject | El fabricante o el proyecto | Verificado |
| product | El producto | Verificado |
| vulnerabilityName | El nombre de la vulnerabilidad | Verificado |
| dateAdded | La fecha en que entró al catálogo | Verificado |
| shortDescription | La descripción | Verificado |
| requiredAction | La acción requerida | Verificado |
| dueDate | La fecha de corrección | Verificado |
| knownRansomwareCampaignUse | Si se conoce su uso en campañas de ransomware: Known o Unknown | Verificado |
| forensicTriage | Si pide triaje forense: Yes o No | Verificado |
| notes | Las notas y sus enlaces | Verificado |
| cwes | Las debilidades CWE | Verificado |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **31 %** de las brechas empezaron por la explotación de una vulnerabilidad: es la primera vía de entrada, por delante del abuso de credenciales (13 %) | [Verizon, 2026 Data Breach Investigations Report, resumen ejecutivo](https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf) | 2026 | Más de 31.000 incidentes reales, de ellos más de 22.000 brechas confirmadas, de octubre de 2024 a noviembre de 2025 | Verificada: Verificada contra el resumen ejecutivo publicado por Verizon el 30 de octubre de 2026 |
| C-02 | **26 %** de las vulnerabilidades del catálogo KEV de CISA quedaron corregidas por completo en 2025, frente al 38 % del año anterior; la mediana para corregirlas subió a 43 días | [Verizon, 2026 Data Breach Investigations Report, resumen ejecutivo](https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf) | 2026 | Las organizaciones del conjunto de datos del informe, de octubre de 2024 a noviembre de 2025 | Verificada: Verificada contra el resumen ejecutivo publicado por Verizon el 30 de octubre de 2026 |
| C-03 | **48 %** de las brechas involucraron a un tercero, un 60 % más que en el informe anterior | [Verizon, 2026 Data Breach Investigations Report, resumen ejecutivo](https://www.verizon.com/business/resources/executivebriefs/2026-dbir-executive-summary.pdf) | 2026 | Más de 22.000 brechas confirmadas, de octubre de 2024 a noviembre de 2025 | Verificada: Verificada contra el resumen ejecutivo publicado por Verizon el 30 de octubre de 2026 |

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
