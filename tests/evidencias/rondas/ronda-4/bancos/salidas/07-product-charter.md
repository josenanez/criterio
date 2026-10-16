# /criterio-product:product-charter REQ-4900

Dejé el borrador del acta de REQ-4900, pero con tres de los cuatro requisitos sin cumplir. Mi recomendación es no firmarlo tal cual.

Los términos ya estaban vigentes (v1.1, aceptados el 2026-10-15 por José Francisco Ñáñez), así que no los registré de nuevo. Como nadie podía contestar, tomé la respuesta sugerida: seguir y marcar los datos que faltan como vacíos del acta, sin rellenarlos.

REQ-4900 está aceptado desde el 2026-08-15, según el acta del comité del 2026-10-09. Pero falta:
- **Criterios de aceptación:** el acta del comité los deja en blanco. Sin ellos no hay criterio de éxito para el proyecto.
- **Evidencia de demanda:** nadie consta como quien lo pidió.
- **Autoridad:** ningún documento dice quién decide. La configuración solo propone al Comité de producto.
- **Doliente y necesidad:** el requerimiento está "sin asignar" y no describe qué se necesita.
- **Quién decidió aceptarlo:** no consta.

El borrador también señala dos cosas más:
- **Volumen mensual:** el caso de negocio declara 117.145 y el tablero mide 85.140. Es una diferencia de 27,3 %, sobre el umbral de 20 % de la configuración.
- **Supuesto "el canal soporta el volumen":** la definición lo llama "verificado", pero no hay documento de verificación. Lo traté como no verificado y lo llevé al acta como riesgo sin responsable.

Las restricciones normativas quedan sin resolver: el requerimiento no describe su necesidad y no cité ninguna norma que no esté en los documentos.

No creé la ficha del proyecto porque el acta no está firmada. Tampoco escribí ningún estado declarado ni nombré gerente del proyecto. Lo que sigue es que el Comité de producto cierre los vacíos y alguien con autoridad firme. Luego el gerente del proyecto instala `criterio-project` y corre `/pm-setup`.

La corrida quedó registrada como `2026-10-15-product-charter-1`: 15 requerimientos revisados, 31 hallazgos del producto y 31 segundos.

Archivos en `/home/claude/banco/ronda-4/bancos/espacio/estado-producto/PRD-309/corridas/`:
- `salida-product-charter.md`