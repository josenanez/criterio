# /criterio-sales:sales-setup comercial/1790123456001-comercial-andina-del-pacifico

Soy Augusto. Esta fue una instalación de prueba sin interfaz, así que tomé las respuestas sugeridas de los documentos.

- **CRM:** las tres exportaciones (2026-10-01, 2026-10-16 y 2026-11-03) son de Dynamics 365 Sales. Cada una tiene 19 filas y ninguna columna faltante. La configuración decía Salesforce al principio; la corregí a `dynamics`.
- **Entidad y periodo:** Comercial Andina del Pacífico, Ecuador, USD, periodo 2026-10 (el del acta del comité y la meta). Los umbrales son 30 días sin actividad y 2 cierres corridos, como dice la política comercial.
- **Términos:** versión 1.3 mostrada y aceptada por José Francisco Ñáñez el 2026-11-05. Los comprobantes quedaron en `.criterio/terminos/`.
- **Ficha:** 14 propuestas, 5 órdenes de compra y el pronóstico comprometido del acta del 2026-10-02 ($945,000). Los correos y teléfonos de contacto no entraron.
- **Carpeta sin marcar:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie lo autorizó.

## Lo que hay que atender

El reporte tiene 9 oportunidades con señal. El motor contó 10 señales en total: la décima es de pronóstico (`forecast_unsupported`) y no aparece en la tabla del `pipeline-check`. Probablemente la detalla `/forecast-check`.

- **Compromiso sin orden de compra:** OPP-1703 ($375,000), OPP-1723 ($165,000), OPP-1722 ($150,000), OPP-1721 ($135,000) y OPP-1720 ($120,000).
- **Detenidas, 35 días sin actividad (desde el 2026-10-01):** OPP-1705, OPP-1726, OPP-1725 y OPP-1724. Las cuatro están en «Calificación».

Las demás oportunidades no tienen señal. OPP-1704 y OPP-1707 tienen un cierre corrido, por debajo del máximo de 2.

El reporte completo está en `estado-comercial/1790123456001-comercial-andina-del-pacifico/comercial/2026-10/reporte-pipeline-check.md`. La salida que te mostré y la corrida registrada (`2026-11-05-sales-setup-1`) están en `corridas/salida-sales-setup.md`.