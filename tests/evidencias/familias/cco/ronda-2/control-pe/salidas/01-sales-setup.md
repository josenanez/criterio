# /criterio-sales:sales-setup comercial/20210047035-comercial-control-del-peru

La instalación quedó lista y el primer reporte tiene una señal: OPP-2205 está detenida.

**Qué hice**
- **Exportaciones del CRM:** las tres de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) se reconocieron como Zoho CRM. Cada una trae 6 oportunidades y ninguna columna faltante. Las fechas van día/mes.
- **Preguntas:** hice 2 (el CRM y el orden de las fechas) y las respondí con lo que traen los documentos.
- **Configuración:** quedó en `.criterio/comercial/20210047035/config.json`, con periodo 2026-10, umbral de 30 días sin actividad y máximo de 2 cierres corridos. La validación salió sin problemas.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez, con fecha 2026-11-05. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Ficha del periodo:** registré 8 documentos de evidencia (5 propuestas y 3 órdenes de compra). El pronóstico comprometido del acta del 2026-10-02 es de S/ 787,500.

**Qué encontró el reporte**
- **OPP-2205 · Ampliación de contrato:** está en «Calificación» y no tiene actividad desde el 2026-10-01 (35 días). Pasa el umbral de 30 días de la política comercial.
- **Evidencia:** el reporte no marca documentos faltantes.
- **Lo demás:** todo lo que llegó se procesó. OPP-2201 y OPP-2202 figuran como ganadas, y OPP-2204 y OPP-2207 llevan un cierre corrido, dentro del máximo de 2.

**Lo que no hice**
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt` en la carpeta, porque en esta sesión nadie podía autorizarlo.
- **Búsqueda de la raíz:** no corrí `buscar-raiz`, porque el argumento ya traía la ruta.

El reporte completo está en `estado-comercial/20210047035-comercial-control-del-peru/comercial/2026-10/reporte-pipeline-check.md`. La salida de esta sesión está en `corridas/salida-sales-setup.md` y la corrida quedó registrada como `2026-11-05-sales-setup-1`.