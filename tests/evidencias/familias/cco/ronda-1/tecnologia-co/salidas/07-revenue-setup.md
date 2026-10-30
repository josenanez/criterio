# /criterio-revenue:revenue-setup comercial/900876543-soluciones-digitales-andinas

Terminé la instalación de Valeria para Soluciones Digitales Andinas (periodo 2026-10, fecha de prueba 2026-11-05). El primer cruce dejó 5 señales para atender, más una comisión que difiere del plan. Esa comisión no está en el reporte de ingresos: la revisa `/commission-check`.

- **Configuración:** `.criterio/ingresos/900876543-soluciones-digitales-andinas/config.json`. Usa HubSpot con la cuenta en `Associated Company`, las fichas de Fidel en `estado-legal/…/contratos` y las de Clara en `estado-finanzas/…`. El plazo para facturar es de 30 días y las comisiones no se publican en Rostrum. `init` y `config` pasaron sin problemas.
- **Exportaciones del CRM:** las tres de `10-crm/` se reconocen como HubSpot, con 19 filas cada una y sin columnas faltantes (fechas 10-01, 10-16 y 11-03).
- **Términos:** quedaron aceptados por José Francisco Ñáñez el 2026-11-05, con comprobantes en Markdown y PDF en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie la autorizó.

Las 5 señales son:
- **Sin factura (4):** cuatro contratos firmados en septiembre tienen la factura vencida: CTR-1205 (64.000.000), CTR-1232 (40.000.000), CTR-1231 (32.000.000) y CTR-1230 (24.000.000).
- **Sin contrato (1):** OPP-1231, ganada el 2026-10-06 por 24.000.000, no tiene contrato firmado en las fichas de Fidel.
- **Cruzadas sin problema:** OPP-1201 y OPP-1202 tienen contrato y factura.

El reporte completo quedó en `estado-comercial/900876543-soluciones-digitales-andinas/ingresos/2026-10/reporte-won-to-invoice.md`. Lo mostrado a la persona quedó en `corridas/salida-revenue-setup.md` y la corrida está registrada como `2026-11-05-revenue-setup-1`.