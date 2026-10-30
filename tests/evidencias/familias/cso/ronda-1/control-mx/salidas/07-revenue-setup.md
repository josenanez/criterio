# /criterio-revenue:revenue-setup comercial/CCM101010AB3-comercial-control-de-mexico

Dejé a Valeria instalada para Comercial Control de México (CCM101010AB3), periodo 2026-10. El primer cruce corrió, pero las dos oportunidades ganadas no se pudieron cruzar con nada, porque no traen cuenta.

Nadie contestó preguntas en esta sesión, así que tomé las respuestas sugeridas de los documentos.

- **Exportaciones del CRM:** las tres de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) son de HubSpot, con 7 filas cada una y sin columnas faltantes.
- **Contratos y facturas:** las fichas de Fidel están en `estado-legal/.../contratos` y las de Clara en `estado-finanzas/...`. El plazo de facturación es de 30 días y las comisiones no se publican en Rostrum.
- **Términos (versión 1.3):** quedaron aceptados por José Francisco Ñáñez, con fecha 2026-11-05. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-revenue-0.1.0-2026-11-05.md` y `.pdf`.
- **Marca de la carpeta:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie la autorizó.
- **Oportunidades ganadas:** OPP-1601 (840,000.00) y OPP-1602 (1,260,000.00) aparecen como «(sin cuenta)». Sin la identificación del cliente no se cruzan con los contratos de Fidel ni con las facturas de Clara. El reporte lo marca en «Lo que no se pudo procesar», aunque en «Lo que hay que atender» dice «Nada abierto».
- **Contratos firmados:** CTR-1601 y CTR-1602 están facturados (FE-1601 y FE-1602). CTR-1603 sigue en plazo para facturar, hasta el 2026-11-19.
- **Comisiones:** el cálculo encontró 2 señales de comisión distinta del plan. El detalle sale con `/commission-check`, que no corrí aquí.

El reporte quedó en `estado-comercial/CCM101010AB3-comercial-control-de-mexico/ingresos/2026-10/reporte-won-to-invoice.md`. La configuración quedó en `.criterio/ingresos/CCM101010AB3/config.json`. Lo que te mostré quedó en `corridas/salida-revenue-setup.md`, y la corrida está registrada como `2026-11-05-revenue-setup-1`.