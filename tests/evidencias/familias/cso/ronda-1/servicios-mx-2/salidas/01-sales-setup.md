# /criterio-sales:sales-setup comercial/SPM140708QJ2-servicios-profesionales-mexicanos

Augusto quedó instalado sobre Servicios Profesionales Mexicanos (SPM140708QJ2) y el primer reporte del embudo del periodo 2026-10 está escrito. Nadie respondió preguntas, así que tomé las respuestas de los documentos y las dejé registradas en la ficha.

**Lo que se instaló**
- **Carpeta:** 37 archivos, ninguno fuera de lugar ni ilegible. No moví ni marqué nada: nadie autorizó la marca `_CRITERIO_COMERCIAL.txt`, y no la dejé.
- **CRM:** las tres exportaciones de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03, con 22 filas cada una) no son de Salesforce ni de HubSpot. El motor las procesa con formato genérico, y registré en `crm.columns` qué columna trae cada dato. Las fechas van día/mes.
- **Umbrales:** 30 días sin actividad detienen una oportunidad y el cierre puede correrse 1 vez. Salen de `politica-comercial.md`.
- **Términos:** versión 1.3, aceptados a nombre de José Francisco Ñáñez el 2026-11-05. Los comprobantes quedaron en `.criterio/terminos/`.
- **Configuración y ficha:** la configuración está en `.criterio/comercial/SPM140708QJ2-servicios-profesionales-mexicanos/config.json`. La ficha del periodo 2026-10 lleva 14 propuestas, 7 órdenes de compra y el pronóstico comprometido en el acta del 2026-10-02. Los correos y teléfonos de contacto no entraron.

**Qué encontró el reporte de pipeline-check**
- **Sin orden de compra:** OPP-1520, OPP-1521 y OPP-1522 están en «Compromiso» y la ficha no tiene su orden de compra.
- **Cierre corrido 2 veces:** OPP-1504, OPP-1526, OPP-1527 y OPP-1528.
- **Detenidas 61 días:** OPP-1523, OPP-1524 y OPP-1525 siguen en «Calificación» sin actividad desde el 2026-09-05.
- **Pronóstico:** el motor marcó además una señal de pronóstico sin respaldo. Es de forecast-check y no sale en este reporte.

**Dónde quedó**
- Reporte: `estado-comercial/SPM140708QJ2-servicios-profesionales-mexicanos/comercial/2026-10/reporte-pipeline-check.md`
- Salida de la corrida: `estado-comercial/SPM140708QJ2-servicios-profesionales-mexicanos/corridas/salida-sales-setup.md`, registrada con el id 2026-11-05-sales-setup-1.

**Dos desvíos**
- Tuve que escribir la configuración antes de reconocer las exportaciones, porque el comando `exportacion` la necesita.
- `terminos` y `aceptar` no tienen una opción que fije la fecha de la prueba. Con `aceptar --today 2026-11-05` el comprobante salió con esa fecha. En `terminos` la corrí sin la opción y solo informó que faltaba la aceptación.