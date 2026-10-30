# /criterio-revenue:revenue-setup comercial/900876543-soluciones-digitales-andinas

Valeria quedó instalada sobre Soluciones Digitales Andinas (900876543), periodo 2026-10. El primer cruce, de lo ganado a lo firmado y a lo facturado, ya corrió, y la corrida quedó registrada.

- **Configuración:** está en `.criterio/ingresos/900876543/config.json` y el motor la validó sin problemas. Las rutas de las fichas de Fidel (`estado-legal/…/contratos`) y de Clara (`estado-finanzas/…`) las comprobé antes de usarlas.
- **Exportaciones del CRM:** las tres de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) se reconocieron como HubSpot, con 19 filas cada una y sin columnas faltantes.
- **Términos:** versión 1.3, registrados a nombre de José Francisco Ñáñez con fecha 2026-11-05. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie lo autorizó en esta prueba.
- **Plazo y comisiones:** tomé 30 días para facturar un contrato firmado, que es el valor por omisión. Las comisiones no se publican en Rostrum.

**Qué mostró el cruce (cortado al 2026-10-31):**

| Señal | Casos |
|---|---|
| Contratos firmados sin factura dentro del plazo | CTR-1205, CTR-1232, CTR-1231 y CTR-1230 |
| Oportunidad ganada sin contrato firmado | OPP-1231, por 24.000.000 |
| Facturado correctamente | OPP-1201 y OPP-1202 |

CTR-1203 sigue en plazo para facturar. El motor marcó además una diferencia de comisión contra el plan; no entra en este reporte y se revisa con `/criterio-revenue:commission-check`.

El reporte completo, tal como lo escribió el motor, está en `estado-comercial/900876543-soluciones-digitales-andinas/ingresos/2026-10/reporte-won-to-invoice.md`. Lo que te mostré quedó en `estado-comercial/…/corridas/salida-revenue-setup.md`.