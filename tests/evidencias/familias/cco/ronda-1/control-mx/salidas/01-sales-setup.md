# /criterio-sales:sales-setup comercial/CCM101010AB3-comercial-control-de-mexico

La instalación quedó lista y el primer reporte no encontró nada abierto en las 6 oportunidades que lista.

Una cosa queda sin explicar: las tres exportaciones traen 7 filas, pero el reporte muestra 6 y OPP-1606 no aparece. El motor no dice por qué; no lo he inventado.

- **Carpeta raíz:** `comercial/CCM101010AB3-comercial-control-de-mexico`, tal como venía en el argumento. No la marqué con `_CRITERIO_COMERCIAL.txt`, porque nadie podía autorizarlo en esta prueba.
- **CRM:** las tres exportaciones de `10-crm/` (2026-10-01, 2026-10-16 y 2026-11-03) son HubSpot, con 7 filas cada una y sin columnas faltantes. La configuración decía Salesforce y la cambié a HubSpot.
- **Preguntas:** hice 2, sobre el CRM y el periodo, y las contesté yo desde los documentos. El periodo es 2026-10, por el acta del 2 de octubre, la liquidación y la meta de octubre.
- **Umbrales:** quedaron los del ejemplo de configuración (30 días sin actividad, máximo 2 cierres corridos, tolerancias de 10 % y 15 %). No los confirmó nadie, así que conviene revisarlos con quien responde por el pronóstico.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez el 2026-11-05. Los comprobantes están en `.criterio/terminos/`.
- **Ficha 2026-10:** registré 8 documentos de evidencia (5 propuestas y 3 órdenes de compra) y el pronóstico comprometido por el comité el 2 de octubre, de $2,205,000. No incluí los correos ni teléfonos de contacto que traen las propuestas.
- **Corrida:** quedó registrada como `2026-11-05-sales-setup-1`, con 0 hallazgos.

Archivos en `<espacio>`:
- `.criterio/comercial/CCM101010AB3/config.json`
- `estado-comercial/CCM101010AB3-comercial-control-de-mexico/comercial/2026-10/reporte-pipeline-check.md`
- `estado-comercial/CCM101010AB3-comercial-control-de-mexico/corridas/salida-sales-setup.md`