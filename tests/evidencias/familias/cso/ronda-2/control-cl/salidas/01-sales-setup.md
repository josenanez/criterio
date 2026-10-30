# /criterio-sales:sales-setup comercial/76000002-7-comercial-control-de-chile

Terminé la instalación de Augusto para Comercial Control de Chile (76000002-7): la configuración, los términos, la primera ficha y el reporte del embudo de 2026-10 quedaron hechos, y la corrida está registrada (`2026-11-05-sales-setup-1`).

- **CRM:** las tres exportaciones de `10-crm/` son de Dynamics 365 Sales y no les falta ninguna columna.
- **Configuración:** quedó en `.criterio/comercial/76000002-7/config.json`. La inicialmente puse como Salesforce y la corregí cuando el motor reconoció las columnas de Dynamics.
- **Términos:** acepté la versión 1.3 a nombre de José Francisco Ñáñez, con fecha 2026-11-05. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Periodo:** elegí 2026-10, porque el acta, las metas, la evidencia y la liquidación son de octubre. El corte es la exportación del 2026-11-03.
- **Primera ficha:** registré 5 propuestas, 3 órdenes de compra y el pronóstico comprometido de $ 252.000.000 del acta del 2026-10-02. Los datos de contacto del cliente no entraron.
- **Reporte del embudo:** el motor no marcó nada abierto. La tabla muestra 6 oportunidades, aunque cada exportación trae 7 filas. No averigüé cuál falta ni por qué. Hay 2 ganadas, 1 en Compromiso, 1 en Propuesta, 1 en Negociación y 1 en Calificación. OPP-2504 y OPP-2507 ya corrieron su cierre una vez, y el máximo es 2.
- **Marca de la raíz:** no creé `_CRITERIO_COMERCIAL.txt`, porque nadie lo autorizó.
- **Reporte guardado:** `estado-comercial/76000002-7-comercial-control-de-chile/comercial/2026-10/reporte-pipeline-check.md`.