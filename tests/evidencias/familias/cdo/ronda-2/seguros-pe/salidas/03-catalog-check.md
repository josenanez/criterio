# /criterio-data-governance:catalog-check 

Los términos (versión 1.6) ya estaban vigentes, así que no hizo falta registrar una aceptación nueva.

Los dos pasos que no encajan con el catálogo: el reporte avisa de 4 señales, pero la corrida quedó registrada con 13 hallazgos, y no sé a qué se debe la diferencia. Además, antes de leer la ruta del estado en la configuración, ejecuté el reporte una segunda vez. Es el mismo reporte, pero la corrida que se registró se hizo después de esa repetición.

Cuatro conjuntos del catálogo tienen un vacío:

- **Sin dueño de negocio:** DS-02 Movimientos y DS-12 Pagos a proveedores.
- **Sin clasificación de confidencialidad:** DS-03 Proveedores y DS-22 Contratos con proveedores, ambos a cargo de Compras.

Los otros cinco conjuntos tienen dueño y clasificación. Asignar el dueño y la clasificación corresponde al área de datos con el negocio.

El reporte completo está en `estado-datos/20605557771-aseguradora-pacifico-sintetica/corridas/salida-catalog-check.md`. La corrida quedó registrada como `2026-11-25-catalog-check-1`.