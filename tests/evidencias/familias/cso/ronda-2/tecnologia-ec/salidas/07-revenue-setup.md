# /criterio-revenue:revenue-setup comercial/0990234566001-sistemas-integrados-del-guayas

Valeria quedó instalada sobre Sistemas Integrados del Guayas (0990234566001) y el primer cruce del periodo 2026-10 ya corrió. El reporte cuenta 5 señales para atender, más una comisión distinta del plan que el reporte no detalla.

**Instalación**
- La carpeta salió del argumento. Tiene 31 archivos, todos nuevos y ninguno fuera de lugar.
- Las 3 exportaciones del CRM (`Deals_2026_10_01.csv`, `Deals_2026_10_16.csv` y `Deals_2026_11_03.csv`) son de Zoho, tienen 19 filas cada una y no les falta ninguna columna.
- La configuración quedó en `.criterio/ingresos/0990234566001/config.json` y el motor la validó sin problemas.
- Las respuestas a las preguntas las tomé de los documentos, porque nadie podía contestar. Son una entidad en Ecuador con moneda USD, periodo 2026-10, facturación a 30 días y comisiones sin publicar en Rostrum. Los contratos los busco en `estado-legal/…/contratos` y las facturas en `estado-finanzas/…`.
- No creé `_CRITERIO_COMERCIAL.txt`, porque nadie autorizó marcar la carpeta.
- José Francisco Ñáñez aceptó los términos (versión 1.3) el 2026-11-05. El comprobante está en `.criterio/terminos/aceptacion-criterio-revenue-0.2.0-2026-11-05.md` y `.pdf`.

**Lo que muestra el cruce**
- **Ganado y firmado:** OPP-1801 y OPP-1802 tienen contrato firmado (CTR-1801 y CTR-1802) y factura (FE-1801 y FE-1802).
- **Firmados sin factura vencida:** CTR-1805 (96,000.00), CTR-1832 (60,000.00), CTR-1831 (48,000.00) y CTR-1830 (36,000.00). Todos pasaron del plazo de 30 días, con 26 a 28 días de vencimiento.
- **Ganada sin contrato:** OPP-1831 (36,000.00), cuyo cliente no tiene contrato firmado en las fichas de Fidel.
- **Comisión distinta del plan:** el motor la contó en el cruce, pero no está en el reporte de ganado a factura. Sale en el de comisiones.

Todo lo que llegó se procesó y el motor no hizo ninguna pregunta.

La salida completa quedó en `estado-comercial/0990234566001-sistemas-integrados-del-guayas/corridas/salida-revenue-setup.md` y la corrida está registrada con el id `2026-11-05-revenue-setup-1`. El reporte está en `estado-comercial/0990234566001-sistemas-integrados-del-guayas/ingresos/2026-10/reporte-won-to-invoice.md`.