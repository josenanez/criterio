# /criterio-product:product-publish 

**No publiqué la ficha de PRD-304 (Tarjeta de crédito digital).** La configuración no define ninguna carpeta de productos publicados. `config.json` solo trae `paths.documents`, `paths.state` y `paths.fichas`, y en el espacio no existe una carpeta `productos/publicados`. Sin un sitio común acordado, publicar no sirve, y acordarlo es una conversación de la organización. No creé ninguna carpeta ni escribí `PRD-304.json`.

**Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-18). No hizo falta registrarlos otra vez.

**Lo que habría llevado la ficha** (corte al 2026-10-18, según `compute` y `publish`):
- **Requerimientos:** 18, de los cuales 17 están aceptados y 1 propuesto (REQ-4401).
- **Proyectos:** 0. Ningún requerimiento tiene proyecto asignado, así que `/product-overlap` no encontraría proyectos compartidos con otros productos.
- **Métricas afirmadas:** 1. `volumen_mensual` declara 263889, según `documentos/productos/PRD-304/00-definicion/2026-01-21-caso-de-negocio.md` (2026-01-21).
- **Segmento declarado:** Personas.

**La corrida quedó registrada** como `2026-10-18-product-publish-1`, con la nota de que no se publicó. Lo que le mostré a usted está en `/home/claude/banco/ronda-10/bancos/espacio/estado-producto/PRD-304/corridas/salida-product-publish.md`.

**Para publicar:** acordar y configurar la carpeta común de productos publicados, y volver a correr `/product-publish`.