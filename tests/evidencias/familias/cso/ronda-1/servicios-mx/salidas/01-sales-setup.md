# /criterio-sales:sales-setup comercial/SPM140708QJ2-servicios-profesionales-mexicanos

Augusto quedó instalado para Servicios Profesionales Mexicanos (SPM140708QJ2). El reporte del embudo de octubre marcó seis oportunidades que atender, y la corrida quedó registrada con 7 hallazgos. La séptima señal es de pronóstico sin respaldo, y la revisa `/forecast-check`.

- **Carpeta:** el inventario encontró 36 archivos, ninguno fuera de lugar ni ilegible.
- **Exportaciones del CRM:** las tres (1 de octubre, 16 de octubre y 3 de noviembre) las reconoció como formato genérico, con 22 filas cada una y sin columnas faltantes. Tuve que declarar en la configuración qué columna trae cada dato. Las fechas van día/mes/año.
- **Configuración:** quedó en `.criterio/comercial/SPM140708QJ2/config.json`, con periodo 2026-10, México y MXN. Los umbrales son los de ejemplo: 30 días sin actividad y 2 cierres corridos. Nadie los confirmó, así que conviene revisarlos.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez el 2026-11-05. Los comprobantes están en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie la autorizó.
- **Ficha de 2026-10:** lleva 21 documentos de evidencia y el pronóstico que el comité comprometió el 2 de octubre, de 6,345,000. Los correos y teléfonos de los clientes no entraron.

## Qué hay que atender en el embudo
- **Sin orden de compra:** OPP-1520, OPP-1521 y OPP-1522 están en «Compromiso» y la ficha no tiene la orden de compra que esa etapa exige.
- **Sin actividad hace 61 días:** OPP-1523, OPP-1524 y OPP-1525, abiertas en «Calificación», sin actividad desde el 2026-09-05.

Los demás puntos del reporte, incluida la tabla de las 21 oportunidades, están en `estado-comercial/SPM140708QJ2-servicios-profesionales-mexicanos/comercial/2026-10/reporte-pipeline-check.md`. La salida completa de esta sesión quedó en `.../corridas/salida-sales-setup.md`.

Nadie respondió preguntas en esta sesión. Cuando una respuesta no venía en los documentos usé la sugerida, y registré la corrida con 0 preguntas a la persona.