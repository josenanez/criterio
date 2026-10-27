---
name: einvoice-matching
description: "Cómo se procesa una factura electrónica de la DIAN, del SRI o de la SUNAT y cómo se cruza con la contabilidad: los campos que se leen y su fuente, las reglas del cruce, los duplicados y lo que queda sin opinión fiscal. Úsalo al revisar las facturas del periodo, al explicar por qué una factura no cruza o cuando un XML no se pudo procesar. E-invoicing, DIAN, SRI, SUNAT, CUFE, clave de acceso."
---

# Las facturas electrónicas contra la contabilidad

## Qué se procesa

Cada XML de `<AAAA-MM>/30-facturacion/emitidas/` y `recibidas/`. El motor procesa solo campos verificados en la fuente oficial, citados por su identificador en `families/criterio-cfo/FUENTES.es.md`:

- **Colombia (F-01, anexo técnico 1.9 de la DIAN):** factura (`Invoice`) y nota crédito (`CreditNote`), sueltas o dentro de su contenedor `AttachedDocument` (6.4). Número (FAD05, CAD05), CUFE o CUDE (FAD06, CAD06), fecha (FAD09, CAD09), NIT del emisor y del adquiriente (FAJ21, FAK21), base imponible (FAU04), IVA —el tributo 01— (FAS02, FAS16) y total (FAU14); de la nota crédito, la factura que corrige (CBG03, CBG04).
- **Ecuador (F-04 y F-09, ficha técnica del SRI):** el comprobante suelto o dentro de su respuesta de autorización (7.2.3). La clave de acceso se valida entera —49 dígitos, su composición y el dígito verificador módulo 11 (tabla 1)— y se contrasta con el comprobante. De la factura (01) se procesan la fecha, el comprador, la base (`totalSinImpuestos`) y el IVA (`totalImpuesto` con código 2). **Los demás tipos se identifican por la clave de acceso y sus valores no se cruzan en esta versión**, porque los campos de valor de su formato no están verificados (F-09).
- **Perú (F-13, guía UBL 2.1 de la factura electrónica de la SUNAT):** la factura (`Invoice`, tipo 01), que no trae una clave como el CUFE: se identifica por el RUC del emisor, su tipo, su serie y su número (`cbc:ID`, `F###-NNNNNNNN`). Fecha (`IssueDate`), RUC del emisor y documento del adquirente (`PartyTaxScheme/CompanyID`, o `PartyIdentification/ID` cuando el emisor lo pone ahí), valor de venta (`LineExtensionAmount`), IGV —el tributo 1000 del catálogo 05— y total (`PayableAmount`). La nota de crédito se identifica y sus valores no se cruzan en esta versión.
- **Chile (F-16, formato de los documentos tributarios electrónicos del SII, versión 2.5):** el DTE, suelto, dentro de su `Documento` o en un envío: el lector busca su `Encabezado`. No trae una clave como el CUFE: se identifica por el RUT del emisor, el tipo y el folio. Tipo (`IdDoc/TipoDTE`, 33 es factura), folio (`IdDoc/Folio`), fecha (`IdDoc/FchEmis`), RUT del emisor y del cliente con su dígito verificador (`Emisor/RUTEmisor`, `Receptor/RUTRecep`), neto (`Totales/MntNeto`), IVA (`Totales/IVA`) y total (`Totales/MntTotal`), en pesos enteros. Los demás tipos se identifican y sus valores no se cruzan en esta versión.
- **México (F-19, guía de llenado del CFDI 4.0 del SAT):** el `cfdi:Comprobante` versión 4.0. Serie y folio son de control interno y opcionales: se identifica por el RFC del emisor, la serie y el folio, y sin ellos por el emisor, la fecha y el total. Fecha (`@Fecha`), RFC del emisor y del receptor (`Emisor/@Rfc`, `Receptor/@Rfc`), subtotal (`@SubTotal`), IVA —el traslado con `@Impuesto` 002 en el nodo `Impuestos` del comprobante— y total (`@Total`). Solo el de ingreso (`I`) cruza valores; el de egreso (`E`) se identifica. El folio fiscal (UUID) del Timbre Fiscal Digital no se procesa en esta versión.

Un XML que no es de ningún país del registro, que el SRI no autorizó o cuya clave no cuadra va a «lo que no se pudo procesar», con el motivo.

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

Las líneas de ventas o compras sin número de documento se cuentan aparte: no se puede saber si necesitan factura.

## Sin opinión fiscal

Clara no dice si un gasto es deducible, qué tarifa aplica ni cómo se trata una diferencia, y no dice de memoria una tarifa, un plazo ni el valor de una unidad tributaria. Lo que es criterio tributario queda como pregunta para la persona.
