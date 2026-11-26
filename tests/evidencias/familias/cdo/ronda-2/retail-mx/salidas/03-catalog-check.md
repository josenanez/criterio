# /criterio-data-governance:catalog-check 

El catálogo tiene cuatro conjuntos con un dato faltante: dos sin dueño y dos sin clasificación. Los términos 1.6 estaban vigentes, aceptados por José Francisco Ñáñez el 2026-11-25. Todo lo que llegó se procesó.

- **Sin dueño de negocio:** DS-02 Movimientos (fila 3 del catálogo) y DS-12 Pagos a proveedores (fila 7).
- **Sin clasificación de confidencialidad:** DS-03 Proveedores (fila 4) y DS-22 Contratos con proveedores (fila 8). En ambos el área responsable es Compras.

Los otros cinco conjuntos tienen dueño y clasificación. Asignar el dueño y la clasificación le toca al área de datos con el negocio.

El reporte quedó en `<estado>/gobierno/2026-11/reporte-catalog-check.md`. Lo que te mostré está en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/salida-catalog-check.md`, y la corrida quedó registrada como `2026-11-25-catalog-check-1`. El registro de la corrida dice 13 hallazgos, y no sé a qué corresponde esa cifra, porque el reporte lista 4.