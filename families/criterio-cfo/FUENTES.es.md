# criterio-cfo · las fuentes

<!-- generado por scripts/familias.py; no se edita a mano, desde fuentes.json -->

Toda fuente que la familia usa para procesar, documentar o probar, con su versión, su enlace, la
fecha en que se consultó y su estado. Es la única lista: el diseño, los skills, los lectores y el
material de prueba citan la fuente por su identificador, no copian su contenido. Se edita en
[`fuentes.json`](fuentes.json); este archivo lo escribe `scripts/familias.py`.

**Estados.** *Verificada*: se consultó el texto publicado por quien la emite. *Por verificar*: se
conoce por una fuente secundaria o falta confirmar la versión vigente; no se construye nada sobre
ella hasta verificarla ([ADR 0006](../../docs/decisions/0006-scope-cfo.md), regla 1).

## El rol

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-11 | O*NET · 11-3031.01 Treasurers and Controllers | — | [onetonline.org](https://www.onetonline.org/link/summary/11-3031.01) | 2026-10-23 | Verificada: La clasificación de ocupaciones del Departamento de Trabajo de los Estados Unidos: 23 tareas, entre ellas los estados financieros, el control interno, las auditorías de las cuentas y los impuestos. La misma ocupación reúne la tesorería | El marco del rol de Clara, la contralora, y de Áurea, la tesorería: O*NET reúne a tesoreros y contralores en la misma ocupación, y 7 de sus 23 tareas son de tesorería (ADR 0016) |
| F-12 | O*NET · 13-2031.00 Budget Analysts | — | [onetonline.org](https://www.onetonline.org/link/summary/13-2031.00) | 2026-10-23 | Verificada: Entre sus tareas: analizar los informes mensuales de presupuesto y contabilidad para mantener el control del gasto, revisar los presupuestos de operación y verificar que los ajustes sigan los cambios de los programas | El marco del rol de Tomás, FP&A |

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
| F-13 | SUNAT · Guía de elaboración de documentos electrónicos XML UBL 2.1, factura electrónica | 1.0 (mayo de 2017) | [cpe.sunat.gob.pe](https://cpe.sunat.gob.pe/sites/default/files/inline-files/guia%2Bxml%2Bfactura%2Bversion%202-1%2B1%2B0%20%282%29_0%20%282%29.pdf) | 2026-10-26 | Verificada: Confirmados en el texto: la raíz Invoice, UBLVersionID 2.1 y CustomizationID 2.0, la serie y el número en cbc:ID, la fecha en aaaa-mm-dd, el tipo 01, el RUC del emisor y el documento del adquirente en PartyTaxScheme/CompanyID, el tributo 1000 (IGV) con el 18.00 % en el ejemplo, y los totales en PEN. La guía no menciona PartyIdentification para el emisor: un XML que lo trae ahí se cruza por número, sin tercero. Se vuelve a consultar contra las reglas de validación vigentes antes del primer uso sobre documentación real | Lector del XML de Perú; material de prueba |
| F-14 | SUNAT · Cartilla 7, El IGV (portal de cultura tributaria) | 2025 | [cultura.sunat.gob.pe](https://cultura.sunat.gob.pe/sites/default/files/2026-01/2025_Cartilla7_IGV.pdf) | 2026-10-26 | Verificada: Dice: la tasa es del 18 %, 16 % de IGV y 2 % de Impuesto de Promoción Municipal. La guía F-13 trae el mismo 18.00 en su ejemplo | La tasa del IGV del material de prueba de Perú; el motor no la usa para calcular |
| F-16 | SII · Formato Documentos Tributarios Electrónicos | 2.5 (febrero de 2026) | [sii.cl](https://www.sii.cl/factura_electronica/factura_mercado/formato_dte_202602.pdf) | 2026-10-27 | Verificada: Confirmados en el texto: las áreas IdDoc, Emisor, Receptor y Totales del encabezado, el tipo 33 como factura electrónica, el folio, la fecha en aaaa-mm-dd, el RUT con guion y dígito verificador, y los montos neto, tasa, IVA y total. El formato no nombra el elemento raíz: el lector busca el Encabezado y no depende de él. Solo la factura (tipo 33) cruza valores en esta versión. Se vuelve a consultar contra el esquema vigente antes del primer uso sobre documentación real | Lector del DTE de Chile; material de prueba |
| F-17 | SII · Preguntas frecuentes: ¿Cuál es la tasa del Impuesto al Valor Agregado (IVA)? | revisada el 10 de junio de 2025 | [sii.cl](https://www.sii.cl/preguntas_frecuentes/impuestos_mensuales/001_130_0572.htm) | 2026-10-27 | Verificada: Dice: la tasa del IVA es de un 19 %, según el artículo 14 de la Ley sobre Impuesto a las Ventas y Servicios | La tasa del IVA del material de prueba de Chile; el motor no la usa para calcular |
| F-19 | SAT · Anexo 20, guía de llenado de los comprobantes fiscales digitales por Internet, CFDI versión 4.0; y el Anexo 20 de la Resolución Miscelánea Fiscal para 2022 en el Diario Oficial de la Federación | CFDI 4.0 (guía de 123 páginas; DOF del 13 de enero de 2022) | [sat.gob.mx](http://omawww.sat.gob.mx/tramitesyservicios/Paginas/documentos/Anexo_20_Guia_de_llenado_CFDI.pdf) · [dof.gob.mx](https://dof.gob.mx/2022/SHCP/SHCP_130122.pdf) | 2026-10-27 | Verificada: Confirmados en el texto: el nodo Comprobante con su espacio de nombres, la versión 4.0, la serie y el folio como control interno opcional, la fecha, el subtotal, el total, la moneda, el tipo de comprobante (I ingreso, E egreso), el RFC del emisor y del receptor, el traslado con el impuesto 002 (IVA) y la tasa 0.160000. El folio fiscal (UUID) del Timbre Fiscal Digital no se procesa en esta versión: su estándar no está en estos documentos y se verifica antes de leerlo. Se vuelve a consultar antes del primer uso sobre documentación real | Lector del CFDI de México; la tasa del IVA del material de prueba |

## Marco contable

| Id | Fuente | Versión | Enlace | Consultada | Estado | Uso |
|---|---|---|---|---|---|---|
| F-05 | Colombia · Ley 1314 de 2009 (13 de julio de 2009) y Decreto Único Reglamentario 2420 de 2015 (14 de diciembre de 2015), con los grupos 1, 2 y 3 de información financiera | Con sus modificaciones; el anexo 1 lo modificó el Decreto 1432 de 2020 | [Ley 1314](https://normograma.supersalud.gov.co/compilacion/docs/ley_1314_2009.htm) · [Decreto 2420](https://www.funcionpublica.gov.co/eva/gestornormativo/norma_pdf.php?i=76745) | 2026-10-20 | Verificada: El decreto define el grupo 1 (anexo 1), el grupo 2 (anexo 2, NIIF para las Pymes) y el grupo 3 (anexo 3, microempresas); el gestor normativo advierte que la vigencia se confirma en cada consulta | Pregunta de `finance-setup` sobre el grupo de la entidad; ninguna opinión de tratamiento en la primera versión |
| F-06 | Ecuador · Superintendencia de Compañías, Resolución 08.G.DSC.010 de 20 de noviembre de 2008 (Registro Oficial 498, 31 de diciembre de 2008): adopción obligatoria de las NIIF en tres grupos, 2010 a 2012 | — | [Superintendencia](https://www.supercias.gob.ec/bd_supercias/descargas/niif/Diferencias%20entre%20NIIF%20completas%20y%20NIIF%20para%20las%20PYMES%20y%20su%20aplicacion%20a%20las%20partidas%20contables.pdf) · [Texto en IAS Plus](https://iasplus.com/content/596f5d4d-01e2-4c37-9ee8-7a8b6524b02d) | 2026-10-20 | Verificada: El número, la fecha, el Registro Oficial y el cronograma los confirma un documento de la Superintendencia; el texto completo de la resolución se consultó en IAS Plus | Pregunta de `finance-setup` sobre el marco de la entidad |
| F-08 | Ecuador · Superintendencia de Compañías, Valores y Seguros, Resolución SCVS-INC-DNCDN-2019-0009 (Registro Oficial 39, 13 de septiembre de 2019): instructivo para aplicar las NIIF completas y la NIIF para las Pymes; su antecedente es la Resolución SC.INPA.UA.G-10.005 de 5 de noviembre de 2010 | — | [Cámara de Comercio de Quito, texto de la resolución](https://ccq.ec/wp-content/uploads/2019/10/consultatributariasept.2019.pdf) · [Ferrere](https://www.ferrere.com/en/news/ecuador-nuevos-montos-para-pymes/) · [Superintendencia, antecedente de 2010](https://www.supercias.gob.ec/bd_supercias/descargas/niif/Diferencias%20entre%20NIIF%20completas%20y%20NIIF%20para%20las%20PYMES%20y%20su%20aplicacion%20a%20las%20partidas%20contables.pdf) | 2026-10-23 | Verificada: Aplica la NIIF para las Pymes la compañía que cumple las tres condiciones: activos inferiores a 4 millones de dólares, ventas brutas anuales de hasta 5 millones y menos de 200 trabajadores en promedio anual ponderado. El texto de la resolución se consultó en el boletín de la Cámara de Comercio de Quito y lo confirma Ferrere; no se encontró una reforma posterior | Pregunta de `finance-setup` sobre si la entidad aplica la NIIF para las Pymes |
| F-15 | Perú · Consejo Normativo de Contabilidad (MEF), Resolución N° 002-2024-EF/30: la versión 2024 de las NIIF | 2024 | [mef.gob.pe](https://mef.gob.pe/es/consejo-normativo-de-contabilidad/normativa-internacional/niif) | 2026-10-26 | Verificada: La página del Consejo lista las NIC, NIIF, CINIIF y SIC de la versión 2024 bajo esa resolución. No dice qué entidades aplican las NIIF completas: eso se pregunta, no se supone | Pregunta de `finance-setup` sobre el marco de la entidad |
| F-18 | IFRS Foundation · perfil de jurisdicción de Chile | actualizado el 16 de junio de 2016 | [ifrs.org](https://www.ifrs.org/content/dam/ifrs/publications/jurisdictions/pdf-profiles/chile-ifrs-profile.pdf) | 2026-10-27 | Verificada: Dice: el Colegio de Contadores adoptó las NIIF como normas contables nacionales (Boletín Técnico 85, diciembre de 2013); las listadas usan NIIF completas; los bancos, las NIIF con dos cambios de su regulador; las demás, NIIF completas o NIIF para las PYMES desde 2013. El perfil es de 2016 y nombra a la SVS y la SBIF, hoy integradas en la CMF. Qué marco aplica la entidad se pregunta, no se supone | Pregunta de `finance-setup` sobre el marco de la entidad |
| F-20 | IFRS Foundation · perfil de jurisdicción de México | actualizado el 16 de junio de 2016 | [ifrs.org](https://www.ifrs.org/content/dam/ifrs/publications/jurisdictions/pdf-profiles/mexico-ifrs-profile.pdf) | 2026-10-27 | Verificada: Dice: las empresas listadas usan NIIF, salvo las instituciones financieras y las aseguradoras, que siguen las NIF mexicanas con los requisitos de la CNBV y la CNSF; las no listadas pueden usar NIIF, y la mayoría usa las NIF que emite el CINIF; México no adoptó la NIIF para las PYMES. Es el único de los países del registro donde una entidad no listada va, por lo común, por un marco distinto de las NIIF. Qué marco aplica la entidad se pregunta, no se supone | Pregunta de `finance-setup` sobre el marco de la entidad |

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

**F-13 · SUNAT · Guía de elaboración de documentos electrónicos XML UBL 2.1, factura electrónica**

| Id | Campo | Estado |
|---|---|---|
| p5-ID | /Invoice/cbc:ID · serie y número, F###-NNNNNNNN (p. 5 y 30) | Verificado |
| p5-UBL | /Invoice/cbc:UBLVersionID · 2.1 (p. 5) | Verificado |
| p5-FECHA | /Invoice/cbc:IssueDate · aaaa-mm-dd (p. 5 y 31) | Verificado |
| p5-TIPO | /Invoice/cbc:InvoiceTypeCode · 01, factura, catálogo 01 (p. 5) | Verificado |
| p7-EMISOR | AccountingSupplierParty/Party/PartyTaxScheme/cbc:CompanyID · RUC del emisor, el tipo de documento en @schemeID, catálogo 06 (p. 7) | Verificado |
| p8-ADQUIRENTE | AccountingCustomerParty/Party/PartyTaxScheme/cbc:CompanyID · documento del adquirente (p. 8) | Verificado |
| p12-IMPUESTO | TaxTotal/TaxSubtotal/cbc:TaxAmount · monto del tributo (p. 12) | Verificado |
| p21-IGV | TaxSubtotal/TaxCategory/TaxScheme/cbc:ID · código de tributo del catálogo 05; 1000 es IGV en el ejemplo (p. 13 y 21) | Verificado |
| p13-VALOR | LegalMonetaryTotal/cbc:LineExtensionAmount · total valor de venta (p. 13) | Verificado |
| p13-TOTAL | LegalMonetaryTotal/cbc:PayableAmount · importe total de la venta (p. 13) | Verificado |

**F-16 · SII · Formato Documentos Tributarios Electrónicos**

| Id | Campo | Estado |
|---|---|---|
| p12-TIPO | Encabezado/IdDoc/TipoDTE · 33, factura electrónica (p. 12) | Verificado |
| p12-FOLIO | Encabezado/IdDoc/Folio · folio autorizado por el SII, numérico de hasta 10 dígitos (p. 12) | Verificado |
| p12-FECHA | Encabezado/IdDoc/FchEmis · fecha de emisión en aaaa-mm-dd (p. 12) | Verificado |
| p17-EMISOR | Encabezado/Emisor/RUTEmisor · con guion y dígito verificador, 0 a 9 o K (p. 17) | Verificado |
| p19-RECEPTOR | Encabezado/Receptor/RUTRecep · el RUT del cliente, salvo en la factura de compra (p. 19) | Verificado |
| p29-NETO | Encabezado/Totales/MntNeto · suma de los ítems afectos, menos descuentos y más recargos globales; numérico de 18 (p. 29) | Verificado |
| p30-TASA | Encabezado/Totales/TasaIVA · en porcentaje (p. 30) | Verificado |
| p30-IVA | Encabezado/Totales/IVA · monto neto por la tasa (p. 30) | Verificado |
| p32-TOTAL | Encabezado/Totales/MntTotal · neto, exento, IVA e impuestos adicionales (p. 32) | Verificado |

**F-19 · SAT · Anexo 20, guía de llenado de los comprobantes fiscales digitales por Internet, CFDI versión 4.0; y el Anexo 20 de la Resolución Miscelánea Fiscal para 2022 en el Diario Oficial de la Federación**

| Id | Campo | Estado |
|---|---|---|
| p3-RAIZ | cfdi:Comprobante · espacio de nombres http://www.sat.gob.mx/cfd/4 (Anexo 20 publicado en el DOF del 13-01-2022, p. 3) | Verificado |
| p5-VERSION | Comprobante/@Version · «4.0» (p. 5) | Verificado |
| p5-SERIE | Comprobante/@Serie y @Folio · control interno del emisor, opcionales (p. 5) | Verificado |
| p5-FECHA | Comprobante/@Fecha · AAAA-MM-DDThh:mm:ss (p. 5) | Verificado |
| p8-SUBTOTAL | Comprobante/@SubTotal · suma de los conceptos antes de descuentos e impuestos (p. 8) | Verificado |
| p8-TIPO | Comprobante/@TipoDeComprobante · «I» (Ingreso) o «E» (Egreso), catálogo c_TipoDeComprobante (p. 8 y 11) | Verificado |
| p9-MONEDA | Comprobante/@Moneda · «MXN» en moneda nacional, ISO 4217 (p. 9) | Verificado |
| p10-TOTAL | Comprobante/@Total (p. 10) | Verificado |
| p15-EMISOR | Emisor/@Rfc · 12 posiciones en persona moral y 13 en persona física (p. 15) | Verificado |
| p17-RECEPTOR | Receptor/@Rfc (p. 17) | Verificado |
| p37-TRASLADADOS | Impuestos/@TotalImpuestosTrasladados (p. 37) | Verificado |
| p38-TRASLADO | Impuestos/Traslados/Traslado · @Impuesto e @Importe (p. 38) | Verificado |
| p26-IVA | c_Impuesto · 002 es IVA (p. 26) | Verificado |
| p27-TASA | c_TasaOCuota · 0.160000 es la tasa del IVA (p. 27) | Verificado |

## Cifras de terceros

| Id | Cifra | Fuente | Año | Muestra | Estado |
|---|---|---|---|---|---|
| C-01 | **44 %** cerraba el trimestre en seis días hábiles en 2023, contra 49 % en 2019 | [Ventana Research / ISG, Smart Financial Close](https://research.isg-one.com/analyst-perspectives/research-reveals-the-importance-of-technology-in-shortening-the-close) | 2023 | No indicada en la nota | Verificada: Registro de cifras del proyecto |
| C-02 | **45 %** de los controles SOX son manuales en las organizaciones encuestadas; las horas del programa subieron 32 % en dos años, de 11.800 a 15.580 | [KPMG, SOX Survey](https://kpmg.com/us/en/articles/2025/2025-kpmg-sox-survey.html) | 2025 | Cerca de 150 profesionales SOX | Verificada: La fuente dice «manuales», no «totalmente manuales» |
| C-03 | **18 días** es la mediana del cierre anual; los mejores lo hacen en 10 días o menos y los más lentos en 35 | [APQC, blog del 8 de abril de 2026, y su medida de Open Standards Benchmarking del cierre anual a nivel de sitio](https://www.apqc.org/resources/blog/how-streamline-annual-closing-process-and-speed-year-end-close) | 2026 | La nota no la indica; la medida de benchmarking reporta la mediana de 18,0 días con 2.214 organizaciones | Verificada: Los cuartiles de la medida de benchmarking son de acceso restringido; las cifras de 10 y 35 días salen de la nota |
| C-04 | **18 %** de las personas de la función de contraloría comete errores al menos a diario, y 59 % varios al mes, por restricciones de capacidad | [Gartner, comunicado del 21 de febrero de 2024](https://www.gartner.com/en/newsroom/press-releases/2024-02-21-gartner-survey-shows-that-a-third-of-accountants-make-several-error-per-weeo-due-to-capacity-constraints) | 2024 | 497 personas de la función de contraloría, encuesta de julio de 2023 | Verificada: La muestra es de la función de contraloría, no solo de contadores |
| C-05 | **79 %** de las organizaciones sufrió en 2024 un intento de fraude en pagos o un fraude consumado; el 63 % señala la suplantación por correo corporativo como la vía principal | [Association for Financial Professionals, 2025 Payments Fraud and Control Survey](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/survey-79-percent-of-organizations-were-victims-of-attempted-or-actual-payments-fraud-activity-in-2024) | 2025 | 521 profesionales de finanzas corporativas | Verificada: Lo dice la nota de prensa de la AFP del 15 de abril de 2025, verificada el 23 de octubre de 2026 (ADR 0016) |

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
