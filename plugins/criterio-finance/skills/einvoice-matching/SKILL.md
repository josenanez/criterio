---
name: einvoice-matching
description: "Cómo se procesa la factura electrónica de cada país del registro —la DIAN, el SRI, la SUNAT, el SII, el SAT, la NF-e, ARCA, la DGI de Panamá, la FEL, el comprobante de Hacienda y la factura de Honduras con su CAI— y cómo se cruza con la contabilidad: los campos que se leen y su fuente, las reglas del cruce, los duplicados y lo que queda sin opinión fiscal. Úsalo al revisar las facturas del periodo, al explicar por qué una factura no cruza o cuando un documento no se pudo procesar. E-invoicing, DIAN, SRI, SUNAT, CUFE, clave de acceso, CAI."
---

# Las facturas electrónicas contra la contabilidad

## Qué se procesa

Cada XML de `<AAAA-MM>/30-facturacion/emitidas/` y `recibidas/`. El motor procesa solo campos verificados en la fuente oficial, citados por su identificador en `families/criterio-cfo/FUENTES.es.md`:

- **Colombia (F-01, anexo técnico 1.9 de la DIAN):** factura (`Invoice`) y nota crédito (`CreditNote`), sueltas o dentro de su contenedor `AttachedDocument` (6.4). Número (FAD05, CAD05), CUFE o CUDE (FAD06, CAD06), fecha (FAD09, CAD09), NIT del emisor y del adquiriente (FAJ21, FAK21), base imponible (FAU04), IVA —el tributo 01— (FAS02, FAS16) y total (FAU14); de la nota crédito, la factura que corrige (CBG03, CBG04).
- **Ecuador (F-04 y F-09, ficha técnica del SRI):** el comprobante suelto o dentro de su respuesta de autorización (7.2.3). La clave de acceso se valida entera —49 dígitos, su composición y el dígito verificador módulo 11 (tabla 1)— y se contrasta con el comprobante. De la factura (01) se procesan la fecha, el comprador, la base (`totalSinImpuestos`) y el IVA (`totalImpuesto` con código 2). **Los demás tipos se identifican por la clave de acceso y sus valores no se cruzan en esta versión**, porque los campos de valor de su formato no están verificados (F-09).
- **Perú (F-13, guía UBL 2.1 de la factura electrónica de la SUNAT):** la factura (`Invoice`, tipo 01), que no trae una clave como el CUFE: se identifica por el RUC del emisor, su tipo, su serie y su número (`cbc:ID`, `F###-NNNNNNNN`). Fecha (`IssueDate`), RUC del emisor y documento del adquirente (`PartyTaxScheme/CompanyID`, o `PartyIdentification/ID` cuando el emisor lo pone ahí), valor de venta (`LineExtensionAmount`), IGV —el tributo 1000 del catálogo 05— y total (`PayableAmount`). La nota de crédito se identifica y sus valores no se cruzan en esta versión.
- **Chile (F-16, formato de los documentos tributarios electrónicos del SII, versión 2.5):** el DTE, suelto, dentro de su `Documento` o en un envío: el lector busca su `Encabezado`. No trae una clave como el CUFE: se identifica por el RUT del emisor, el tipo y el folio. Tipo (`IdDoc/TipoDTE`, 33 es factura), folio (`IdDoc/Folio`), fecha (`IdDoc/FchEmis`), RUT del emisor y del cliente con su dígito verificador (`Emisor/RUTEmisor`, `Receptor/RUTRecep`), neto (`Totales/MntNeto`), IVA (`Totales/IVA`) y total (`Totales/MntTotal`), en pesos enteros. Los demás tipos se identifican y sus valores no se cruzan en esta versión.
- **México (F-19, guía de llenado del CFDI 4.0 del SAT):** el `cfdi:Comprobante` versión 4.0. Serie y folio son de control interno y opcionales: se identifica por el RFC del emisor, la serie y el folio, y sin ellos por el emisor, la fecha y el total. Fecha (`@Fecha`), RFC del emisor y del receptor (`Emisor/@Rfc`, `Receptor/@Rfc`), subtotal (`@SubTotal`), IVA —el traslado con `@Impuesto` 002 en el nodo `Impuestos` del comprobante— y total (`@Total`). Solo el de ingreso (`I`) cruza valores; el de egreso (`E`) se identifica. El folio fiscal (UUID) del Timbre Fiscal Digital no se procesa en esta versión.
- **Brasil (F-21, MOC 7.0, Anexo I de la NF-e):** `infNFe` con la chave de acesso en su `Id`, suelta o dentro de `nfeProc`. Modelo, serie, número, fecha y tipo de operación en `ide`; el CNPJ del emitente y del destinatario; y los totales de `ICMSTot`. El ICMS va dentro del valor de la nota: la base es `vNF` sin el ICMS. Solo el modelo 55 de salida cruza valores; el protocolo de la SEFAZ no se procesa en esta versión.
- **Argentina (F-24, manual WSFEv1 de ARCA):** la solicitud `FECAESolicitar` con su respuesta, como la archiva el ERP. Punto de venta y tipo (`FeCabReq`), documento del comprador, número, fecha e importes (`FECAEDetRequest`), y el CAE. La base es el neto gravado, el no gravado y el exento; `ImpIVA` es el IVA. Se identifica por su CAE. Solo una factura aprobada (`Resultado` A) cruza valores.
- **Panamá (F-27, ficha técnica de la DGI, versión 1.00):** `rFE` con el CUFE en `dId`; tipo, número, punto de facturación y fecha en `gDGen`; el RUC del emisor y del receptor; y los totales de `gTot` —el neto, el ITBMS y el total—. Solo la factura de operación interna (`iDoc` 01) cruza valores.
- **Guatemala (F-30 y F-31, la FEL de la SAT, GT_Documento 0.2.1):** `GTDocumento/SAT/DTE`, con el tipo, la fecha, el NIT del emisor, el documento del receptor, cada impuesto por su nombre corto y el gran total, y el número de autorización con su serie y su número. Se identifica por el UUID de la autorización. Solo la factura (`FACT`) cruza valores.
- **Costa Rica (F-34, Anexos y Estructuras 4.4 de Hacienda):** `FacturaElectronica` o `NotaCreditoElectronica` en su espacio de nombres; la clave de cincuenta posiciones, el consecutivo, la fecha, la cédula del emisor y la del receptor, y en el resumen la venta neta, el total de impuesto y el total. Se identifica por su clave. Solo la factura cruza valores.
- **Honduras (F-37, Acuerdo 481-2017, y F-38, Ley del ISV):** el SAR no publica un esquema, así que **la factura es un documento —PDF o imagen con texto— y no un XML** (decisión 0024). La extraes a `invoices` de la ficha del cierre aplicando **close-record**, con su cita: la CAI, el rango autorizado, la fecha límite de emisión, el número correlativo, la fecha de emisión, el RTN del emisor y del cliente, el subtotal gravado, el ISV y el total. El motor comprueba que el número tenga la forma `NNN-NNN-NN-NNNNNNNN` del artículo 10 —el tipo 01 es factura; los demás se identifican y no cruzan—, que el ISV sea el 15 % de lo gravado y que la factura esté dentro de su autorización. Un documento de `30-facturacion/` que no está en la ficha queda en «lo que no se pudo procesar».

Un XML que no es de ningún país del registro, que el SRI no autorizó o cuya clave no cuadra va a «lo que no se pudo procesar», con el motivo; igual una factura de Honduras sin la forma del artículo 10 o con un ISV que no cuadra con su subtotal, que vuelve a la extracción.

## El cruce

Con los registros del libro mayor en las cuentas que la configuración asocia a cada lado:

| | Base | IVA o IGV |
|---|---|---|
| Emitidas | `accounts.sales` | `accounts.vat_generated` |
| Recibidas | `accounts.purchases` | `accounts.vat_deductible` |

Se cruza por **número de documento**; el tercero se contrasta y, si no es el del XML, queda para revisar. Las señales:

- `einvoice_not_recorded`: la factura no tiene registro.
- `recorded_without_einvoice`: un documento en las cuentas de ventas o compras sin factura en su lado.
- `einvoice_amount_mismatch`: la base o el IVA no son los del registro, más allá de la tolerancia (la de cada país en su registro; en Colombia, ±2,00 y ±5,00 del IVA, F-01 5.2.1).
- `einvoice_duplicate`: el mismo CUFE, clave de acceso o serie y número del mismo emisor en dos archivos, o la misma factura registrada en dos asientos.
- `invoice_outside_authorization`: una factura recibida de Honduras cae fuera de su rango autorizado o se emitió después de su fecha límite de emisión (Acuerdo 481-2017, art. 10). No sustenta el crédito fiscal del ISV; el motor la pone al lado del registro que la usa, y lo que se hace con ese crédito es criterio tributario de la persona.

Las líneas de ventas o compras sin número de documento se cuentan aparte: no se puede saber si necesitan factura.

## Sin opinión fiscal

Clara no dice si un gasto es deducible, qué tarifa aplica ni cómo se trata una diferencia, y no dice de memoria una tarifa, un plazo ni el valor de una unidad tributaria. Lo que es criterio tributario queda como pregunta para la persona.
