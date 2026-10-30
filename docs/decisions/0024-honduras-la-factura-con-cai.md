# 0024 · Honduras: la factura con su CAI, no un XML

**Fecha:** 2026-10-30 · **Estado:** aceptada el 2026-10-30 · **Modifica:** el lector de factura de la familia CFO

## Contexto

Cada país del registro entra a la CFO con el lector de su factura electrónica, que procesa el XML
desde su esquema verificado: la DIAN, el SRI, la SUNAT, el SII, el SAT de México, la NF-e, ARCA, la
DGI de Panamá, la FEL de Guatemala y el comprobante 4.4 de Costa Rica.

**Honduras no publica un esquema.** El SAR no tiene un XSD ni una especificación técnica en su
sección de facturación ni entre sus leyes de facturación, revisadas el 30 de octubre de 2026. Su
régimen es el del Acuerdo 481-2017, reformado por los Acuerdos 609-2017, 725-2018 y 817-2018, con
un texto consolidado actualizado el 1 de abril de 2025. El texto verificado es el original, que
trajo José Francisco Ñáñez: La Gaceta n.º 34,413 del 10 de agosto de 2017. Ese régimen autoriza cada documento fiscal
con una **Clave de Autorización de Impresión (CAI)**, un **rango autorizado** y una **fecha límite
de emisión** (artículo 10), y un número correlativo de dieciséis dígitos, `NNN-NNN-NN-NNNNNNNN`:
el establecimiento, el punto de emisión, el tipo de documento (01 es factura) y el correlativo.
Define también los documentos fiscales electrónicos con su código de autorización de emisión
electrónica (CAEE, artículo 4), pero no publica su formato. Las guías comerciales describen la
factura electrónica como voluntaria, con software homologado.

La tasa general del Impuesto Sobre Ventas es del 15 % (Ley del ISV, texto consolidado de 2016,
artículo 6).

## Propuesta

Honduras entra a la CFO con la factura como documento, no como XML:

- **El agente extrae** de cada factura recibida, en PDF o imagen con texto, su CAI, el rango
  autorizado, la fecha límite de emisión, el número correlativo, la fecha de emisión, el RTN del
  emisor y del cliente, el subtotal, el ISV y el total, cada dato con su cita.
- **El motor calcula**:
  - que el número correlativo tenga la forma del artículo 10 y su tipo sea 01;
  - que caiga dentro del rango autorizado;
  - que la fecha de emisión no pase la fecha límite;
  - que el ISV sea el 15 % del subtotal gravado, con la tolerancia del país.
- **Una señal nueva**, `invoice_outside_authorization`: una factura recibida fuera de su rango
  autorizado o emitida después de su fecha límite no sustenta el crédito fiscal del ISV, y el
  agente la pone al lado del registro contable que la usa. Las demás señales de la factura son las
  de siempre.
- **El validador del SAR** —el de documentos fiscales de la oficina virtual— lo usa la persona;
  el agente no se conecta a él.
- **Fuentes verificadas el 30 de octubre de 2026**, en los textos que trajo José Francisco Ñáñez:
  - el Acuerdo 481-2017 en La Gaceta n.º 34,413: artículo 3, definiciones 7 (CAI), 9 (CAEE) y
    36 (rango autorizado); artículo 10, requisitos de la factura, con el correlativo
    `NNN-NNN-NN-NNNNNNNN` (01 = factura, la casa matriz es el establecimiento 000, el correlativo
    empieza en 00000001); artículo 11, los datos que se completan al emitirla (RTN del cliente,
    fecha, subtotales por tarifa, impuestos por tarifa, total);
  - la Ley del ISV, texto consolidado al 10 de junio de 2016, artículo 6: «La tasa general del
    impuesto es del quince por ciento (15%)».
- **Por verificar:** si las reformas de 2017 y 2018 tocaron los artículos 10 y 11. Se cierra con el
  texto consolidado de 2025; mientras tanto el material cita el texto original.

## La CLO en Honduras

La Ley de Contratación del Estado (Decreto 74-2001), en el texto que trajo José Francisco Ñáñez,
fija la garantía de cumplimiento en un porcentaje único, no en una banda: «equivalente al quince
por ciento (15%) de su valor» (artículo 100), y la de mantenimiento de oferta en al menos el 2 %
(artículo 99). La regla de la CLO entra como en los demás países, con mínimo y tope iguales al
15 %. El sistema de publicación no está en ese texto; queda por verificar.

## Lo que se decidió

1. José Francisco Ñáñez aprobó el 30 de octubre de 2026 la señal nueva y que Honduras entre sin
   lector XML.
2. Si el SAR publica el formato de la factura electrónica con su CAEE, entra como un lector más,
   desde su fuente verificada, y esta decisión se modifica.
3. Los textos son los que hay: el Acuerdo 481-2017 original. Si llega el consolidado de 2025, se
   revisan los artículos 10 y 11 contra él.
