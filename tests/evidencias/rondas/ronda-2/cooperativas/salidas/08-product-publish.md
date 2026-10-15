# /criterio-product:product-publish 

No publiqué la ficha de PRD-300 (Crédito de libranza) porque no hay carpeta de productos publicados configurada. En `.criterio/producto/PRD-300/config.json`, `paths.fichas` está vacío. No inventé una ruta, no creé ninguna carpeta y no escribí ninguna ficha.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no registré nada nuevo.

**Lo que habría publicado, con corte al 2026-10-15:**
- **Lleva:** 4 requerimientos, 0 proyectos y 1 métrica afirmada.
- **Segmento declarado:** Asociados rurales.
- **Métrica:** `volumen_mensual` = 156447, tomada de `documentos/productos/PRD-300/00-definicion/2026-04-09-caso-de-negocio.md` (2026-04-09).
- **Requerimientos:** REQ-1000, REQ-1001, REQ-1002 y REQ-1003, todos aceptados y ninguno con proyecto asignado.

**Conviene saber antes de publicar:**
- Como ningún requerimiento tiene proyecto, la ficha no permitiría cruzar por proyecto con otros productos.
- El cálculo da una brecha del 22.3 % entre la cifra declarada de `volumen_mensual` (156447) y la medida (121498, tablero del 2026-10-15). La ficha lleva la cifra declarada, no la medida.

**Para publicar:** define `paths.fichas` con la carpeta común acordada y vuelve a correr `/product-publish`.

La corrida quedó registrada como `2026-10-15-product-publish-1` (13 segundos, 9 hallazgos). El texto que te mostré está guardado en `estado-producto/PRD-300/corridas/salida-product-publish.md`.