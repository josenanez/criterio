# /criterio-sales:sales-setup comercial/77654321-7-soluciones-digitales-del-pacifico

Augusto quedó instalado sobre Soluciones Digitales del Pacífico (77654321-7, Chile, CLP). El reporte de `pipeline-check` del periodo 2026-10 salió con 11 señales, y la corrida quedó registrada.

- **Exportaciones:** las tres de `10-crm/` son HubSpot, con 20 filas cada una y sin columnas faltantes.
- **Preguntas:** no le hice ninguna a nadie. Solo hubo una propuesta mía, la columna de la empresa asociada, que registré como `Associated Company`.
- **Periodo:** elegí 2026-10, el del acta del comité del 2026-10-02 y de la liquidación. La carpeta también trae metas para 2026-09 y 2026-11.
- **Umbrales:** quedaron los de la política comercial. Treinta días sin actividad detienen una oportunidad y el cierre puede correrse una vez.
- **Términos:** la versión 1.3 quedó aceptada por José Francisco Ñáñez el 2026-11-05, con el comprobante en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt` porque nadie la autorizó.
- **Pronóstico:** el acta compromete 349.650.000 para octubre. El mejor escenario, 532.800.000, no se compromete y no entró a la ficha.

**Lo que muestra el reporte** (los montos y los días los calculó el motor):
- **Sin orden de compra:** OPP-2420, OPP-2421 y OPP-2422 están en «Compromiso» y la ficha no trae su orden de compra.
- **Cierre corrido dos veces:** OPP-2404, OPP-2426, OPP-2427 y OPP-2428.
- **Detenidas 61 días:** OPP-2423, OPP-2424 y OPP-2425, abiertas en «Calificación» sin actividad desde el 2026-09-05.
- **Meta:** hay una señal de meta contra lo cerrado (`target_vs_closed`), pero no aparece en la tabla de atención ni en el resultado del reporte. Queda para `target-check`.

El reporte está en `estado-comercial/77654321-7-soluciones-digitales-del-pacifico/comercial/2026-10/reporte-pipeline-check.md`. La configuración está en `.criterio/comercial/77654321-7/config.json` y la salida de la corrida en `corridas/salida-sales-setup.md`, dentro de la misma carpeta de estado.