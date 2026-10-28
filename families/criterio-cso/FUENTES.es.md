# criterio-cso · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0019](../../docs/decisions/0019-scope-comercial-cso.md), regla 1).

## El rol

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | O*NET · 11-2022.00 Sales Managers | Datos de 2026 (O*NET OnLine) | [onetonline.org](https://www.onetonline.org/link/summary/11-2022.00) | 2026-10-28 | Verificada: Se consultaron las 19 tareas de la ocupación en O*NET OnLine, del Departamento de Trabajo de los Estados Unidos; la familia toma cinco: proyectar las ventas desde los registros, establecer y vigilar las metas, fijar precios y descuentos, revisar los registros de las ventas y preparar el presupuesto comercial. No se transcribe su contenido | El marco del rol de Augusto y de Valeria (ADR 0019) |

## Las exportaciones del CRM

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-02 | Salesforce · Field Reference · Opportunity | La referencia publicada al 28 de octubre de 2026 | [developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.sfFieldRef.meta/sfFieldRef/salesforce_field_reference_Opportunity.htm) | 2026-10-28 | Verificada: La referencia da el nombre de cada campo, su etiqueta, su tipo y su tamaño; las descripciones están en la Object Reference. El lector toma el nombre del campo (la exportación por API o Data Loader) o su etiqueta (la exportación de un informe) | El lector de la exportación de oportunidades de Salesforce |
| F-03 | Salesforce · Object Reference · OpportunityFieldHistory | La página de la versión 192.0 de la referencia | [developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.192.0.object_reference.meta/object_reference/sforce_api_objects_opportunityfieldhistory.htm) | 2026-10-28 | Verificada: El historial de campos de una oportunidad: el campo que cambió, el valor anterior y el nuevo. Se consultó la página de la versión 192.0, que avisa que hay una más nueva; se vuelve a consultar la vigente antes de liberar el lector | Las veces que se corrió la fecha de cierre, cuando el CRM exporta el historial |
| F-04 | HubSpot · HubSpot's default deal properties | Artículo actualizado el 29 de septiembre de 2026 | [knowledge.hubspot.com](https://knowledge.hubspot.com/properties/hubspots-default-deal-properties) | 2026-10-28 | Verificada: Las propiedades por omisión de un negocio con su etiqueta, que es la cabecera de la exportación. El artículo no da el nombre interno de cada una. La cuenta asociada sale en su propia columna (F-05), con un nombre que el artículo no fija: la configuración dice cuál es | El lector de la exportación de negocios de HubSpot |
| F-05 | HubSpot · Export records | Artículo actualizado el 2 de abril de 2026 | [knowledge.hubspot.com](https://knowledge.hubspot.com/import-and-export/export-records) | 2026-10-28 | Verificada: La exportación sale en CSV, XLSX o XLS; cada objeto asociado va en su propia columna, con el id y el nombre del registro asociado. El lector procesa CSV y XLSX | Los formatos de la exportación de HubSpot y la columna de la cuenta asociada |

## Los campos que procesa el motor

Cada campo de factura que lee `finanzas.py` está aquí con su identificador en la fuente. La
puerta falla si el motor usa uno que no está, o uno por verificar.

**F-02 · Salesforce · Field Reference · Opportunity**

| Id | Campo | Estado |
|---|---|---|
| Id | Opportunity ID · id | Verificado |
| Name | Name · string | Verificado |
| AccountId | Account ID · reference | Verificado |
| Amount | Amount · currency | Verificado |
| CloseDate | Close Date · date | Verificado |
| StageName | Stage · picklist | Verificado |
| Probability | Probability (%) · percent | Verificado |
| ForecastCategoryName | Forecast Category · picklist | Verificado |
| IsClosed | Closed · boolean | Verificado |
| IsWon | Won · boolean | Verificado |
| LastActivityDate | Last Activity · date | Verificado |
| OwnerId | Owner ID · reference | Verificado |
| CreatedDate | Created Date · datetime | Verificado |
| CurrencyIsoCode | Opportunity Currency · picklist | Verificado |

**F-03 · Salesforce · Object Reference · OpportunityFieldHistory**

| Id | Campo | Estado |
|---|---|---|
| OpportunityId | Opportunity ID · reference | Verificado |
| Field | el campo que cambió · picklist | Verificado |
| OldValue | el valor antes del cambio | Verificado |
| NewValue | el valor después del cambio | Verificado |

**F-04 · HubSpot · HubSpot's default deal properties**

| Id | Campo | Estado |
|---|---|---|
| Record ID | el identificador único del negocio | Verificado |
| Deal Name | el nombre del negocio | Verificado |
| Deal Stage | la etapa del negocio en su pipeline | Verificado |
| Pipeline | el pipeline del negocio | Verificado |
| Amount | el valor total del negocio en su moneda | Verificado |
| Close Date | el día en que se espera cerrar o se cerró | Verificado |
| Deal owner | el usuario a quien está asignado | Verificado |
| Create Date | la fecha en que se creó | Verificado |
| Last Activity Date | la última fecha pasada de una actividad registrada | Verificado |
| Deal probability | la probabilidad de cerrar | Verificado |
| Forecast category | Not forecasted, Pipeline, Best case, Commit o Closed won | Verificado |
| Currency | la moneda del valor del negocio | Verificado |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **4 de cada 5** líderes de ventas y de finanzas no acertaron al menos un pronóstico trimestral de ventas en el último año; el 52 % de los líderes de ventas dice que su pronóstico se desvía un 10 % o más | [Xactly con Regina Corso Consulting, 2024 Sales Forecasting Benchmark Report](https://www.xactlycorp.com/sites/default/files/file/2024-07/2024_sales_forecasting_benchmark_report.pdf) | 2024 | 405 profesionales de ventas, finanzas y operaciones de ingresos en Norteamérica, del 19 al 28 de marzo de 2024 | Verificada: Verificada contra el informe publicado por Xactly el 28 de octubre de 2026 |
| C-02 | **28 %** de su semana dedica un vendedor a vender; el 72 % se va en otras tareas, sobre todo gestionar los negocios y capturar datos | [Salesforce, State of Sales, quinta edición](https://www.salesforce.com/news/stories/sales-research-2023/) | 2022 | 7.775 profesionales de ventas en 38 países de Norteamérica, América Latina, Asia-Pacífico y Europa, del 24 de agosto al 30 de septiembre de 2022 | Verificada: Verificada contra la nota de Salesforce el 28 de octubre de 2026; la encuesta se hizo en 2022 y se publicó en 2023 |
| C-03 | **84 %** de los líderes de ventas dice que la analítica comercial influyó menos de lo esperado en el desempeño; el 44 % señala la mala calidad de los datos | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-02-06-gartner-survey-finds-sales-analytics-has-less-influence-on-sales-performance-than-what-leadership-expected) | 2023 | 303 líderes de ventas, julio de 2023 | Verificada: Verificada contra el comunicado de Gartner del 6 de febrero de 2024, el 28 de octubre de 2026 |

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
