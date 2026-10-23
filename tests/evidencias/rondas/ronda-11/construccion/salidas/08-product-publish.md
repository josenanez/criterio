# /criterio-product:product-publish 

No publiqué la ficha de PRD-305 (Locales comerciales). La configuración no tiene una carpeta común de productos publicados, y sin un sitio acordado la publicación no sirve. Acordarlo es una conversación de la organización, no un comando, así que no inventé una ruta ni creé carpetas. No escribí ningún archivo de ficha.

Los términos v1.2 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-22, así que no los registré de nuevo.

La ficha quedó calculada con corte al 2026-10-22 y habría llevado:

- **Requerimientos, proyectos y métricas:** 15 requerimientos (13 aceptados, 2 propuestos), 0 proyectos y 1 métrica afirmada.
- **Segmento declarado:** Entidades públicas.
- **Métrica:** `volumen_mensual` = 214841, tomada de `documentos/productos/PRD-305/00-definicion/2025-09-25-caso-de-negocio.md` (2025-09-25). No hay serie medida que la contraste.
- **Cruces posibles:** ningún requerimiento tiene proyecto asignado (0 trazados). Con esta ficha no saldría ningún cruce por proyecto, solo por métrica y por segmento.

Para publicar, la organización tiene que acordar la carpeta común (por ejemplo `productos/publicados/`) y dejarla en la configuración. Después se vuelve a correr `/product-publish`.

La corrida quedó registrada como `2026-10-22-product-publish-1`, con 26 hallazgos y 15 segundos medidos. Lo que te mostré está en `estado-producto/PRD-305/corridas/salida-product-publish.md`.