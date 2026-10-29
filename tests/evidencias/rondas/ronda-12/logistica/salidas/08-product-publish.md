# /criterio-product:product-publish 

No publiqué la ficha de PRD-303 (Logística de frío), porque no hay una carpeta de productos publicados. La configuración no tiene esa ruta y en el espacio no existe ninguna carpeta `publicados`. No creé una ni inventé la ruta. Acordar el sitio común es una conversación de la organización, no algo que este comando pueda resolver.

Los términos ya estaban vigentes (versión 0.12.1, aceptados por José Francisco Ñáñez el 2026-10-28). No hizo falta registrarlos de nuevo.

**Lo que la ficha llevaría, con corte al 2026-10-28** (calculado, no escrito en ningún sitio):
- **Requerimientos:** 15 (13 aceptados, 2 propuestos).
- **Proyectos:** 0. Ningún requerimiento tiene proyecto asignado, así que otro producto no podría cruzar con este por proyecto compartido.
- **Métricas afirmadas:** 1.
- **Segmento declarado:** Farmacéuticas.
- **Métrica:** `volumen_mensual` = 70118. Sale de `documentos/productos/PRD-303/00-definicion/2026-05-27-caso-de-negocio.md` (2026-05-27). No hay serie medida con la que contrastarla.

La corrida quedó registrada como `2026-10-28-product-publish-1`, con la salida guardada en `estado-producto/PRD-303/corridas/salida-product-publish.md`. Registra 35 hallazgos sobre los requerimientos (13 sin trazar a un proyecto, 11 con evidencia de hace 12 meses o más, 6 aceptados sin criterio de aceptación, 3 aceptados sin evidencia, 2 sin decidir).

Para publicar, hay que indicar la carpeta común de fichas de producto (por ejemplo `productos/publicados/`) y volver a correr `/product-publish`.