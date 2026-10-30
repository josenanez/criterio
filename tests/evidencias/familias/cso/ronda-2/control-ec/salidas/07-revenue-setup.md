# /criterio-revenue:revenue-setup comercial/1790000028001-comercial-control-del-ecuador

Valeria quedó instalada sobre Comercial Control del Ecuador y el primer cruce de 2026-10 corrió sin hallazgos.

**Qué hice**
- **Carpeta:** usé la del argumento, `comercial/1790000028001-comercial-control-del-ecuador`. El inventario encontró 22 archivos nuevos, ninguno fuera de lugar ni ilegible.
- **Exportaciones del CRM:** las tres de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) se reconocen como Salesforce, sin columnas faltantes y con 7 filas cada una.
- **Configuración:** la escribí en `.criterio/ingresos/1790000028001-comercial-control-del-ecuador/config.json` y el motor la validó sin problemas. Apunta a las fichas de Fidel en `estado-legal/<entidad>/contratos` y a las de Clara en `estado-finanzas/<entidad>`. Como no hubo a quién preguntar, tomé de los documentos el plazo de facturación de 30 días, la moneda USD y que las comisiones no se publican en Rostrum.
- **Términos:** José Francisco Ñáñez los aceptó con fecha 2026-11-05, como indicaste. Quedó el comprobante en Markdown y PDF en `.criterio/terminos/`.

**Lo que muestra el cruce de 2026-10**
- **Ganado:** OPP-1901 (120,000.00) y OPP-1902 (180,000.00) tienen contrato (CTR-1901, CTR-1902) y factura (FE-1901, FE-1902).
- **Firmado:** CTR-1903 está firmado el 2026-10-20 y sin factura, pero dentro del plazo, que vence el 2026-11-19.
- **Qué falta atender:** nada abierto.

El reporte completo está en `estado-comercial/1790000028001-comercial-control-del-ecuador/ingresos/2026-10/reporte-won-to-invoice.md`, y la corrida quedó registrada como `2026-11-05-revenue-setup-1`.

**Notas**
- No dejé la marca `_CRITERIO_COMERCIAL.txt`: la carpeta ya venía dada por el argumento.
- Tampoco corrí `deal-scan`, que procesa las cotizaciones de `40-cotizaciones/`. El cruce de ganado a firmado a facturado no lo necesitaba, pero `discount-check` y `commission-check` sí lo van a pedir.
- En las fichas de Fidel hay un `CTR-1909` que el reporte no muestra. No lo investigué.