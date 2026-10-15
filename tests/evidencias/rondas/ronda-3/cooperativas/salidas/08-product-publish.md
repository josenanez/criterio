# /criterio-product:product-publish 

No publiqué la ficha de PRD-303 (Tarjeta débito). La configuración no define una carpeta de productos publicados. Sin un sitio común acordado, publicar no sirve, y ese acuerdo es una decisión de la organización. No inventé una ruta, no creé ninguna carpeta y no escribí ninguna ficha.

Los términos de la versión 0.3.9 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15. No hizo falta registrarlos otra vez.

Esto es lo que habría llevado la ficha, recalculado al 2026-10-15:
- **Requerimientos:** 16, de los cuales 11 están aceptados y 5 propuestos.
- **Proyectos:** ninguno, porque ningún requerimiento está vinculado a un proyecto.
- **Métricas afirmadas:** 1. Es `volumen_mensual`, con 250.670 declarado en `documentos/productos/PRD-303/00-definicion/2026-04-05-caso-de-negocio.md` (2026-04-05).
- **Segmento declarado:** Pensionados.

Para poder publicar hay que definir en la configuración la carpeta común (por ejemplo `productos/publicados/`) y volver a correr el comando.

La corrida quedó registrada como `2026-10-15-product-publish-1`, con la salida en `estado-producto/PRD-303/corridas/salida-product-publish.md`. Encontró 39 hallazgos en total. Los más frecuentes son evidencia vencida (12) y requerimientos sin trazar a un proyecto (11).