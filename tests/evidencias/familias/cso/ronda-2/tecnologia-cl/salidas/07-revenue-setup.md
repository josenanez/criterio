# /criterio-revenue:revenue-setup comercial/77654321-7-soluciones-digitales-del-pacifico

Valeria quedó instalada sobre Soluciones Digitales del Pacífico (77654321-7) y el primer cruce del periodo 2026-10 dio 6 señales.

Como la sesión no tenía interfaz, no hice preguntas: tomé las respuestas de los documentos. Dejé el reporte completo en `estado-comercial/77654321-7-soluciones-digitales-del-pacifico/ingresos/2026-10/reporte-won-to-invoice.md`.

- **Carpeta e inventario:** usé la carpeta del argumento. Hay 33 archivos, todos en su sitio y legibles. No dejé la marca `_CRITERIO_COMERCIAL.txt`, porque nadie la autorizó.
- **Exportaciones del CRM:** las tres son HubSpot, con 20 filas cada una y sin columnas faltantes (2026-10-01, 2026-10-16 y 2026-11-03).
- **Fichas:** las de Fidel están en `estado-legal/…/contratos` y las de Clara en `estado-finanzas/…`. El plazo de facturación es de 30 días y las comisiones no se publican en Rostrum.
- **Términos:** la aceptación anterior era de `criterio-sales`, así que no valía para este agente. Mostré los términos (versión 1.3) y los registré a nombre de José Francisco Ñáñez, fecha 2026-11-05.
- **Configuración:** quedó en `.criterio/ingresos/77654321-7/config.json`. Es distinta de la de ventas, que ya existía en `.criterio/comercial/`.

**Lo que muestra el cruce**
- **Ganado sin contrato en las fichas de Fidel (2):**
  - OPP-2432, por 36.000.000, ganada el 2026-10-07.
  - OPP-2431, por 27.000.000, ganada el 2026-10-06.
- **Firmado sin factura en las fichas de Clara, con el plazo vencido (3):**
  - CTR-2405, por 72.000.000, firmado el 2026-09-10.
  - CTR-2431, por 36.000.000, firmado el 2026-09-09.
  - CTR-2430, por 27.000.000, firmado el 2026-09-08.
- **Comisión distinta de la que da el plan (1):** el motor la cuenta en el resumen, pero el reporte no la desarrolla. Eso se ve con `/commission-check`.
- **Sin problema:** OPP-2401 y OPP-2402 tienen contrato y factura. CTR-2403 sigue dentro del plazo.

Dejé la salida en `estado-comercial/77654321-7-soluciones-digitales-del-pacifico/corridas/salida-revenue-setup.md` y la corrida quedó registrada como `2026-11-05-revenue-setup-1`.