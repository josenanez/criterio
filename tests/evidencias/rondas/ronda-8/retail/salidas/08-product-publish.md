# /criterio-product:product-publish 

**No publiqué la ficha de PRD-309.** La configuración no define ninguna carpeta de productos publicados, y en el espacio tampoco existe `productos/publicados/`. Sin ese sitio común no hay dónde escribir `PRD-309.json`. No lo inventé ni creé ninguna carpeta, porque nadie podía responder en esta sesión. Acordar la carpeta es una conversación de la organización, no un comando.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no los registré de nuevo.

Esto es lo que publicaría, con corte al 2026-10-17:
- **Producto:** PRD-309 · Tarjeta de la tienda · gerente Elena Duarte.
- **Requerimientos:** 15 (11 aceptados y 4 propuestos), cada uno con id, título y estado.
- **Proyectos:** 0. Ningún requerimiento tiene un proyecto que lo ejecute.
- **Métricas afirmadas:** 1, `volumen_mensual` = 106991.0, según `documentos/productos/PRD-309/00-definicion/2025-11-12-caso-de-negocio.md` (fuente del 2025-11-12). No hay serie medida con la que contrastarla.
- **Segmento declarado:** Clientes frecuentes.

Con 0 proyectos, `/product-overlap` no podría detectar el caso de un mismo proyecto construyendo para dos dueños. Sí podría detectar una métrica o un segmento compartidos.

La corrida quedó registrada como `2026-10-17-product-publish-1` (20 segundos, 34 hallazgos), con lo anterior guardado en `estado-producto/PRD-309/corridas/salida-product-publish.md`.

Para publicar, hay que acordar la carpeta común de fichas, ponerla en la configuración y volver a correr este comando.