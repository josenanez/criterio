# /criterio-sales:sales-setup comercial/901234567-almacenes-del-valle

Augusto quedó instalado para Almacenes del Valle (901234567), periodo 2026-10, y corrió el primer `pipeline-check`. El reporte salió con 12 puntos a atender, de las 21 oportunidades del embudo. La corrida quedó registrada con 13 hallazgos, uno más que el reporte.

- **Exportaciones:** las tres de oportunidades (cortes 2026-10-01, 10-16 y 11-03, 22 filas cada una) se reconocieron como Salesforce sin columnas faltantes. El historial del 2026-11-03 (13 filas) se reconoció como historial de fechas de cierre.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez el 2026-11-05. El comprobante en Markdown y PDF quedó en `.criterio/terminos/`.
- **Ficha:** cargué las 14 propuestas, las 5 órdenes de compra y el pronóstico comprometido del acta del 2 de octubre ($630.000.000). Dejé fuera los correos y teléfonos de contacto.
- **Marca de la carpeta:** no dejé `_CRITERIO_COMERCIAL.txt`; sin nadie que lo autorizara, no escribí nada en la carpeta de documentos.

**Lo que hay que atender, según el reporte:**
- **Compromiso sin orden de compra (5):** OPP-1103, 1120, 1121, 1122 y 1123.
- **Cierre corrido 3 veces (4):** OPP-1107, 1127, 1128 y 1129.
- **Detenidas 61 días (3):** OPP-1124, 1125 y 1126.

Corrí `compute` y el `pipeline-check` con `--today 2026-11-05` y la configuración quedó en la carpeta de la sesión. El comparativo del pronóstico y el de la meta no los generé; son otros comandos.

Archivos en `<espacio>/`:
- `.criterio/comercial/901234567-almacenes-del-valle/config.json`
- `estado-comercial/901234567-almacenes-del-valle/comercial/2026-10/ficha.json`
- `estado-comercial/901234567-almacenes-del-valle/comercial/2026-10/reporte-pipeline-check.md`
- `estado-comercial/901234567-almacenes-del-valle/corridas/salida-sales-setup.md`