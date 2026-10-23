# criterio-cfo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 1).

## Formatos de factura y comprobantes electrónicos

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-01 | DIAN · Anexo técnico de la factura electrónica de venta | 1.9 | [dian.gov.co](https://www.dian.gov.co/impuestos/factura-electronica/Documents/Anexo-Tecnico-Factura-Electronica-de-Venta-vr-1-9.pdf) | 2026-10-20 | Verificada: La DIAN publica la versión 1.9 con la Resolución 000165 de 2023 (F-02); rige desde el 1 de mayo de 2024 (F-03), y la Resolución 227 de 2025 (F-07) mantiene vigentes los anexos de las resoluciones que compila. Se vuelve a consultar antes de cada versión del lector. Campos verificados en el texto del anexo, con su identificador: los que procesa el lector están en la lista de campos | Lector del XML de Colombia; material de prueba |
| F-02 | DIAN · Resolución 000165 de 2023 (sistema de facturación electrónica) | — | [normograma](https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0165_2023.htm) | 2026-10-20 | Verificada: Como norma que adopta los anexos | Contexto de F-01 |
| F-03 | DIAN · Resolución 000008 de 2024 (fija el 1 de mayo de 2024 para adoptar la versión 1.9) y Concepto 1531 de 2024 | — | [Resolución](https://normograma.icfes.gov.co/docs/pdf/resolucion_dian_0008_2024.pdf) · [Concepto](https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_1531_2024.htm) | 2026-10-20 | Verificada | Vigencia de F-01 |
| F-04 | SRI · Ficha técnica de comprobantes electrónicos, esquema offline | 2.34 (27 de julio de 2026) | [sri.gob.ec](https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/f8d9bb36-5632-4f96-b463-b9265b55338c/FICHA%20TE%CC%81CNICA%20COMPROBANTES%20ELECTRO%CC%81NICOS%20ESQUEMA%20OFFLINE%20Versio%CC%81n%202.34.pdf) | 2026-10-20 | Verificada: La portada dice «Actualizado julio 2026»; el control de cambios fecha la 2.33 el 13/07/2026 y la 2.34 el 27/07/2026 (anexo 26, información del proveedor del sistema, por F-10). Reemplaza a la 2.32 del 08/10/2025. Confirmados en el texto: la clave de acceso de 49 dígitos y su composición (tabla 1), el dígito verificador módulo 11 (factores 2 a 7; 11 da 0 y 10 da 1), los tipos 01, 03, 04, 05, 06 y 07 (tabla 3), el código 2 del IVA (tabla 16) y la respuesta de autorización con el comprobante en CDATA (7.2.3). Sus anexos de formato XML no se publican como texto: los nombres de los campos salen de F-09 | Lector del XML de Ecuador; material de prueba |
| F-07 | DIAN · Resolución 227 de 2025, Resolución Única en materia tributaria, aduanera y cambiaria (23 de septiembre de 2025, Diario Oficial 53.254) | — | [normograma](https://cancilleria.gov.co/normograma/compilacion/docs/resolucion_dian_0227_2025.htm) | 2026-10-20 | Verificada: Sus considerandos dicen que los anexos de las resoluciones compiladas siguen vigentes como parte del acto; el Título 5 compila el sistema de facturación | Vigencia de F-01 |
| F-09 | SRI · Ficha técnica de comprobantes electrónicos, esquema offline, con el formato XML de la factura | 2.09 (septiembre de 2017) | [sri.gob.ec](https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/fbb05cf5-32f2-4cc3-bc8a-b539c9e0ed74/FICHA+TECNICA+COMPROBANTES+ELECTRO%B4NICOS+offline.pdf) | 2026-10-20 | Verificada: Es la versión del SRI que publica como texto el formato XML de la factura. Confirmados en su ejemplo: infoTributaria (ruc, claveAcceso, codDoc, estab, ptoEmi, secuencial, razonSocial) e infoFactura (fechaEmision en dd/mm/aaaa, identificacionComprador, totalSinImpuestos, totalConImpuestos con totalImpuesto, codigo, codigoPorcentaje, baseImponible y valor). Los campos de valor de la nota de crédito y de los demás tipos no están en el texto: esos comprobantes se identifican por su clave de acceso y sus valores no se cruzan hasta verificarlos | Nombres de los campos del lector del XML de Ecuador |
| F-10 | SRI · Resolución NAC-DGERCGC26-00000027 (27 de julio de 2026): registro de proveedores de sistemas de facturación electrónica y el RUC del proveedor en la información adicional del comprobante | — | [Nota de LEXIS (secundaria)](https://www.lexis.com.ec/noticias/sri-crea-registro-obligatorio-de-proveedores-de-facturacion-electronica) | 2026-10-20 | Verificada: Se consultó el PDF firmado electrónicamente por la Directora General y certificado por la Secretaría General del SRI; el enlace es una nota secundaria, porque el texto oficial no tiene una dirección pública confirmada. El artículo 5 pide el RUC del proveedor en la información adicional, en 60 días desde su publicación en el Registro Oficial. No cambia los campos que procesa el lector | Contexto de F-04 |

## Marco contable

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-05 | Colombia · Ley 1314 de 2009 (13 de julio de 2009) y Decreto Único Reglamentario 2420 de 2015 (14 de diciembre de 2015), con los grupos 1, 2 y 3 de información financiera | Con sus modificaciones; el anexo 1 lo modificó el Decreto 1432 de 2020 | [Ley 1314](https://normograma.supersalud.gov.co/compilacion/docs/ley_1314_2009.htm) · [Decreto 2420](https://www.funcionpublica.gov.co/eva/gestornormativo/norma_pdf.php?i=76745) | 2026-10-20 | Verificada: El decreto define el grupo 1 (anexo 1), el grupo 2 (anexo 2, NIIF para las Pymes) y el grupo 3 (anexo 3, microempresas); el gestor normativo advierte que la vigencia se confirma en cada consulta | Pregunta de `finance-setup` sobre el grupo de la entidad; ninguna opinión de tratamiento en la primera versión |
| F-06 | Ecuador · Superintendencia de Compañías, Resolución 08.G.DSC.010 de 20 de noviembre de 2008 (Registro Oficial 498, 31 de diciembre de 2008): adopción obligatoria de las NIIF en tres grupos, 2010 a 2012 | — | [Superintendencia](https://www.supercias.gob.ec/bd_supercias/descargas/niif/Diferencias%20entre%20NIIF%20completas%20y%20NIIF%20para%20las%20PYMES%20y%20su%20aplicacion%20a%20las%20partidas%20contables.pdf) · [Texto en IAS Plus](https://iasplus.com/content/596f5d4d-01e2-4c37-9ee8-7a8b6524b02d) | 2026-10-20 | Verificada: El número, la fecha, el Registro Oficial y el cronograma los confirma un documento de la Superintendencia; el texto completo de la resolución se consultó en IAS Plus | Pregunta de `finance-setup` sobre el marco de la entidad |
| F-08 | Ecuador · Superintendencia de Compañías, Valores y Seguros, Resolución SCVS-INC-DNCDN-2019-0009 (Registro Oficial 39, 13 de septiembre de 2019): instructivo para aplicar las NIIF completas y la NIIF para las Pymes; su antecedente es la Resolución SC.INPA.UA.G-10.005 de 5 de noviembre de 2010 | — | [Cámara de Comercio de Quito, texto de la resolución](https://ccq.ec/wp-content/uploads/2019/10/consultatributariasept.2019.pdf) · [Ferrere](https://www.ferrere.com/en/news/ecuador-nuevos-montos-para-pymes/) · [Superintendencia, antecedente de 2010](https://www.supercias.gob.ec/bd_supercias/descargas/niif/Diferencias%20entre%20NIIF%20completas%20y%20NIIF%20para%20las%20PYMES%20y%20su%20aplicacion%20a%20las%20partidas%20contables.pdf) | 2026-10-23 | Verificada: Aplica la NIIF para las Pymes la compañía que cumple las tres condiciones: activos inferiores a 4 millones de dólares, ventas brutas anuales de hasta 5 millones y menos de 200 trabajadores en promedio anual ponderado. El texto de la resolución se consultó en el boletín de la Cámara de Comercio de Quito y lo confirma Ferrere; no se encontró una reforma posterior | Pregunta de `finance-setup` sobre si la entidad aplica la NIIF para las Pymes |

## Los campos que procesa el motor

Cada campo de factura que lee `finanzas.py` está aquí con su identificador en la fuente. La
puerta falla si el motor usa uno que no está, o uno por verificar.

**F-01 · DIAN · Anexo técnico de la factura electrónica de venta**

| Id | Campo | Estado |
|---|---|---|
| FAD05 | /Invoice/cbc:ID · prefijo más número | Verificado |
| FAD06 | /Invoice/cbc:UUID · CUFE, 96 caracteres | Verificado |
| FAD08 | /Invoice/cbc:UUID/@schemeName · CUFE-SHA384 (13.2.2) | Verificado |
| FAD09 | /Invoice/cbc:IssueDate · AAAA-MM-DD (5.4) | Verificado |
| FAJ21 | AccountingSupplierParty/Party/PartyTaxScheme/cbc:CompanyID · NIT del emisor; el DV en @schemeID (FAJ24) | Verificado |
| FAK21 | AccountingCustomerParty/Party/PartyTaxScheme/cbc:CompanyID · id del adquiriente, sin DV | Verificado |
| FAS02 | /Invoice/cac:TaxTotal/cbc:TaxAmount · valor del tributo | Verificado |
| FAS16 | TaxTotal/TaxSubtotal/TaxCategory/TaxScheme/cbc:ID · 01 es IVA en el ejemplo de 6.4 | Verificado |
| FAU04 | /Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount · base imponible | Verificado |
| FAU14 | /Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount · total a pagar | Verificado |
| CAD05 | /CreditNote/cbc:ID | Verificado |
| CAD06 | /CreditNote/cbc:UUID · CUDE | Verificado |
| CAD09 | /CreditNote/cbc:IssueDate | Verificado |
| CAJ21 | nota crédito: CompanyID del emisor | Verificado |
| CAK21 | nota crédito: CompanyID del adquiriente | Verificado |
| CAS02 | /CreditNote/cac:TaxTotal/cbc:TaxAmount | Verificado |
| CAU04 | /CreditNote/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount | Verificado |
| CAU14 | /CreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount | Verificado |
| CBG03 | /CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID · factura relacionada | Verificado |
| CBG04 | /CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:UUID · CUFE de la factura relacionada | Verificado |
| AD-6.4 | AttachedDocument/cac:Attachment/cac:ExternalReference/cbc:Description · el documento en CDATA (6.4) | Verificado |
| 5.2.1 | holgura de ±2,00 en valores monetarios y de ±5,00 en el IVA (5.2.1.1 y 5.2.1.2) | Verificado |

**F-04 · SRI · Ficha técnica de comprobantes electrónicos, esquema offline**

| Id | Campo | Estado |
|---|---|---|
| T1 | claveAcceso: fecha ddmmaaaa (8), tipo (2), RUC (13), ambiente (1), serie (6), secuencial (9), código numérico (8), tipo de emisión (1), verificador (1) | Verificado |
| MOD11 | dígito verificador módulo 11 sobre los 48 dígitos | Verificado |
| T3 | codDoc: 01 factura, 03 liquidación de compra, 04 nota de crédito, 05 nota de débito, 06 guía de remisión, 07 comprobante de retención | Verificado |
| T16 | codigo 2: IVA | Verificado |
| 7.2.3 | autorizacion: estado, numeroAutorizacion, fechaAutorizacion, comprobante en CDATA | Verificado |

**F-09 · SRI · Ficha técnica de comprobantes electrónicos, esquema offline, con el formato XML de la factura**

| Id | Campo | Estado |
|---|---|---|
| IT | infoTributaria: ruc, claveAcceso, codDoc, estab, ptoEmi, secuencial, razonSocial | Verificado |
| IF | infoFactura: fechaEmision (dd/mm/aaaa), identificacionComprador, totalSinImpuestos | Verificado |
| TI | totalConImpuestos/totalImpuesto: codigo, codigoPorcentaje, baseImponible, valor | Verificado |
| NC | notaCredito/infoNotaCredito: campos de valor | Por verificar |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **44 %** cerraba el trimestre en seis días hábiles en 2023, contra 49 % en 2019 | [Ventana Research / ISG, Smart Financial Close](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) | 2023 | No indicada en la nota | Verificada: Registro de cifras del proyecto |
| C-02 | **45 %** de los controles SOX son manuales en las organizaciones encuestadas; las horas del programa subieron 32 % en dos años, de 11.800 a 15.580 | [KPMG, SOX Survey](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) | 2025 | Cerca de 150 profesionales SOX | Verificada: La fuente dice «manuales», no «totalmente manuales» |
| C-03 | **18 días** es la mediana del cierre anual; los mejores lo hacen en 10 días o menos y los más lentos en 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) | 2026 | La nota no la indica; la medida de benchmarking reporta la mediana de 18,0 días con 2.214 organizaciones | Verificada: Los cuartiles de la medida de benchmarking son de acceso restringido; las cifras de 10 y 35 días salen de la nota |
| C-04 | **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad | [Gartner, comunicado del 21 de febrero de 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) | 2024 | 497 personas de la función de contraloría, encuesta de julio de 2023 | Verificada: La muestra es de la función de contraloría, no solo de contadores |

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
