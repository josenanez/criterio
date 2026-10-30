# /criterio-revenue:revenue-setup comercial/901234567-almacenes-del-valle

Valeria quedó instalada sobre Almacenes del Valle (901234567), y el cruce del periodo 2026-10 encontró 5 señales. La configuración, la aceptación de términos y el primer cruce corrieron sin errores, y la corrida quedó registrada.

**Lo que se instaló**
- **Carpeta:** `comercial/901234567-almacenes-del-valle`, tomada del argumento. Tiene 35 archivos nuevos, ninguno fuera de lugar ni ilegible.
- **Exportaciones del CRM:** las tres de oportunidades (2026-10-01, 2026-10-16 y 2026-11-03) y el historial de 2026-11-03 son de Salesforce. No les faltan columnas.
- **Configuración:** `.criterio/ingresos/901234567-almacenes-del-valle/config.json`, y el motor la validó.
- **Fichas de Fidel y de Clara:** `estado-legal/901234567-almacenes-del-valle/contratos` y `estado-finanzas/901234567-almacenes-del-valle`. Comprobé que existen y que traen contratos y facturas.
- **Valores que tomé por omisión, sin preguntar:** factura a 30 días, comisiones sin publicar en Rostrum y estado en `estado-comercial/901234567-almacenes-del-valle`.
- **Términos:** versión 1.3, aceptados a nombre de José Francisco Ñáñez el 2026-11-05. Los comprobantes quedaron en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt` en la carpeta, porque nadie podía autorizarlo en esta prueba.

**Lo ganado contra lo firmado y lo facturado, 2026-10**
- **Ganadas sin contrato en las fichas de Fidel (3):**
  - OPP-1108, 50.000.000 (cliente 830011002).
  - OPP-1133, 40.000.000 (cliente 830011008).
  - OPP-1132, 30.000.000 (cliente 830011007).
- **Contratos firmados sin factura en las fichas de Clara, con el plazo vencido (2):**
  - CTR-1131, 40.000.000 (cliente 830011010).
  - CTR-1130, 30.000.000 (cliente 830011009).
- **Lo que sí cruzó completo:** OPP-1101 y OPP-1102 tienen contrato (CTR-1101 y CTR-1102) y factura (FE-1101 y FE-1102). CTR-1103 todavía está en plazo.

El reporte completo está en `estado-comercial/901234567-almacenes-del-valle/ingresos/2026-10/reporte-won-to-invoice.md`. La salida íntegra de esta sesión está en `corridas/salida-revenue-setup.md`.