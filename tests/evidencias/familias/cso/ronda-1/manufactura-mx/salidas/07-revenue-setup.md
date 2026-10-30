# /criterio-revenue:revenue-setup comercial/MBA120315KT4-manufacturas-del-bajio

Instalé a Valeria sobre Manufacturas del Bajío (MBA120315KT4, México, MXN) y corrí el primer cruce del periodo 2026-10: salieron 6 señales, 2 de ganadas sin contrato y 4 de contratos sin factura. La configuración es válida y la corrida quedó registrada.

Nadie podía contestar, así que tomé las respuestas de los documentos; confírmalas:
- **Carpeta raíz:** la del argumento, `comercial/MBA120315KT4-manufacturas-del-bajio`.
- **Exportaciones del CRM:** las tres son Salesforce completas, con 19 filas y fechas mes/día.
- **Cuentas:** las 12 traen identificación.
- **Fichas:** los contratos de Fidel están en `estado-legal/…/contratos` y las facturas de Clara en `estado-finanzas/…`.
- **Plazo de facturación:** 30 días.
- **Comisiones:** no se publican en Rostrum.
- **Estado:** `estado-comercial/MBA120315KT4-manufacturas-del-bajio`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie la autorizó.

Mostré los términos tal cual y registré la aceptación de José Francisco Ñáñez con fecha 2026-11-05. El comprobante en Markdown y PDF quedó en `.criterio/terminos/`.

El reporte lo escribió el motor, con corte al 2026-10-31 y las 6 señales:

| Oportunidad o contrato | Señal | Monto (MXN) |
|---|---|---|
| OPP-1430, venta directa 30 | Ganada el 2026-10-06 sin contrato en las fichas de Fidel | 360,000.00 |
| OPP-1431, venta directa 31 | Ganada el 2026-10-07 sin contrato en las fichas de Fidel | 480,000.00 |
| CTR-1405 | Firmado el 2026-09-10, plazo vencido sin factura en las fichas de Clara | 960,000.00 |
| CTR-1432 | Firmado el 2026-09-10, plazo vencido sin factura | 600,000.00 |
| CTR-1431 | Firmado el 2026-09-09, plazo vencido sin factura | 480,000.00 |
| CTR-1430 | Firmado el 2026-09-08, plazo vencido sin factura | 360,000.00 |

Las otras dos ganadas, OPP-1401 y OPP-1402, tienen contrato y factura. CTR-1403 sigue dentro del plazo.

Archivos en `estado-comercial/MBA120315KT4-manufacturas-del-bajio/`:
- `ingresos/2026-10/reporte-won-to-invoice.md`
- `corridas/salida-revenue-setup.md`

La configuración está en `.criterio/ingresos/MBA120315KT4-manufacturas-del-bajio/config.json`.

Glob no estaba disponible en esta sesión, así que busqué las fichas con `find`.