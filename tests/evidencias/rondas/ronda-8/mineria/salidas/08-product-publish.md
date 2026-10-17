# /criterio-product:product-publish 

**No publiqué la ficha de PRD-304 (Trazabilidad).** La configuración no trae carpeta de productos publicados: `.criterio/producto/PRD-304/config.json` solo define `paths.documents` y `paths.state`. Sin un sitio común acordado, publicar no sirve, y acordarlo es una conversación de la organización. No inventé una ruta ni creé ninguna carpeta.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-17, así que no los registré otra vez.

**Lo que habría llevado (corte al 2026-10-17):** 16 requerimientos (11 aceptados, 5 propuestos), 0 proyectos y 2 métricas afirmadas.

**Segmento declarado:** Operadores.

**Métricas:**
- `volumen_mensual`: 240425, del caso de negocio `documentos/productos/PRD-304/00-definicion/2025-09-15-caso-de-negocio.md` (2025-09-15).
- `retorno_esperado`: sin cifra declarada, del mismo documento.

Ningún requerimiento tiene proyecto asignado (0 % trazados), así que otro producto no podría cruzar con esta ficha por proyecto compartido. Solo podría cruzar por la métrica `volumen_mensual` y por el segmento Operadores.

**Para publicar:** acordar la carpeta común de fichas publicadas, añadirla a la configuración y volver a correr `/product-publish`.

La corrida quedó registrada como `2026-10-17-product-publish-1`, con la salida guardada en `estado-producto/PRD-304/corridas/salida-product-publish.md`. Encontró 40 hallazgos en 16 requerimientos y tardó 12 segundos.