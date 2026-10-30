# /criterio-revenue:revenue-setup comercial/CCM101010AB3-comercial-control-de-mexico

Valeria quedó instalada sobre Comercial Control de México (CCM101010AB3), y el primer cruce de lo ganado contra lo firmado y lo facturado corrió sin hallazgos.

- **Carpeta raíz:** usé la del argumento. No la marqué con `_CRITERIO_COMERCIAL.txt` porque nadie lo autorizó.
- **Inventario:** hay 22 documentos y ninguno quedó fuera de lugar ni ilegible.
- **Exportaciones del CRM:** las tres (2026-10-01, 2026-10-16 y 2026-11-03) son HubSpot, con 7 filas cada una y ninguna columna faltante.
- **Términos:** mostré el texto corto y registré la aceptación de José Francisco Ñáñez con fecha 2026-11-05. Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-revenue-0.1.0-2026-11-05.md` y `.pdf`.
- **Configuración:** la escribí en `.criterio/ingresos/CCM101010AB3-comercial-control-de-mexico/config.json` y el motor la validó sin problemas. Tomé como respuestas sugeridas:
  - **Periodo y CRM:** periodo 2026-10, y la cuenta sale de "Associated Company" (igual que la configuración de Augusto).
  - **Fichas y plazo:** fichas de Fidel en `estado-legal/…/contratos` y de Clara en `estado-finanzas/…`, con 30 días para facturar.
  - **Comisiones:** no se publican en Rostrum.
- **Cruce de la venta a la factura:**
  - **OPP-1601:** tiene contrato CTR-1601 y factura FE-1601.
  - **OPP-1602:** tiene contrato CTR-1602 y factura FE-1602.
  - **CTR-1603:** firmado el 2026-10-20, sin factura todavía y en plazo hasta el 2026-11-19.
  - **Atención y no procesado:** el reporte no marca nada para atender y todo lo que llegó se procesó.

Lo que mostré quedó en `estado-comercial/CCM101010AB3-comercial-control-de-mexico/corridas/salida-revenue-setup.md`, y la corrida quedó registrada como `2026-11-05-revenue-setup-1`. El reporte del motor está en `estado-comercial/CCM101010AB3-comercial-control-de-mexico/ingresos/2026-10/reporte-won-to-invoice.md`.