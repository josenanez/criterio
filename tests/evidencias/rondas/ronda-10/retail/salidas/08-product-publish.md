# /criterio-product:product-publish 

**No publiqué la ficha de PRD-300 (Venta en línea).** La configuración no define una carpeta de productos publicados: `config.json` solo trae `paths.documents` y `paths.state`.

Sin un sitio común acordado, publicar no sirve, y acordarlo es una conversación de la organización, no un comando. No creé ninguna carpeta ni escribí ninguna ficha.

Los términos ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-18), así que no hizo falta registrarlos otra vez.

**La ficha que se publicaría, con corte al 2026-10-18:**
- **Lleva:** 15 requerimientos · 0 proyectos · 1 métrica afirmada.
- **Segmento declarado:** Pequeños negocios.
- **Métrica:** `volumen_mensual` = 162820, del documento `00-definicion/2026-05-30-caso-de-negocio.md` (2026-05-30).

Los 15 requerimientos (REQ-2028 y REQ-4000 a REQ-4013) están en estado «aceptado». Ninguno tiene un proyecto que lo ejecute. Cuando se publique, `/product-overlap` solo podrá cruzar la métrica y el segmento, no proyectos compartidos.

**Para desbloquearlo:** acordar la carpeta común (por ejemplo `productos/publicados/`), configurarla y volver a correr el comando. Entonces escribiría `PRD-300.json` ahí.

La corrida quedó registrada como `2026-10-18-product-publish-1`. Contó 34 hallazgos: 15 sin trazar, 9 con evidencia vieja, 6 aceptados sin evidencia y 4 sin criterio de aceptación. La salida que guardé está en `estado-producto/PRD-300/corridas/salida-product-publish.md`.