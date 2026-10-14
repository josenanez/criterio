# /criterio-product:product-publish 

No publiqué la ficha de PRD-306 (Microseguros), con corte al 2026-10-14. Faltan dos cosas que este comando no puede inventar.

- **Estado vacío:** `estado/producto.json` no tiene código, nombre, gerente, problema, segmento ni métricas. `estado/requirements/` y `estado/metrics/` están sin archivos, y `compute` da 0 requerimientos y 0 métricas afirmadas. Una ficha así la leerían los demás productos como si fuera de hoy.
- **Sin carpeta de publicados:** la configuración solo define `documents`, `state` y `fichas`. Sin un sitio común acordado no hay dónde escribir `PRD-306.json`, y acordarlo es una conversación de la organización.

No escribí ninguna ficha ni creé carpetas de publicación.

Los términos ya estaban aceptados en la configuración (v1.0, 2026-10-14, José Francisco Ñáñez), así que no volví a pedirlos.

La corrida quedó registrada como `2026-10-14-product-publish-1`, con esta salida guardada en `estado/corridas/salida-product-publish.md`.

Para poder publicar, corre antes `/criterio-product:product-setup`, que lee `documentos/productos/PRD-306` y llena el estado. Después hay que acordar la carpeta de publicados.