# /criterio-product:product-publish 

No publiqué la ficha de PRD-303 (Pago con QR). La configuración no define una carpeta de productos publicados: `paths` solo trae `documents` y `state`. Sin un sitio común acordado no se puede publicar, y acordarlo es una conversación de la organización, no un comando. No creé ni busqué ninguna carpeta, y no escribí ningún `PRD-303.json`.

Los términos ya estaban vigentes con el nombre de José Francisco Ñáñez (2026-10-15), así que no hubo que registrarlos de nuevo.

Esto habría llevado la ficha, con corte al 2026-10-15:
- **Requerimientos:** 5, todos aceptados y ninguno ligado a un proyecto.
- **Proyectos:** 0.
- **Segmento declarado:** Clientes frecuentes.
- **Métrica afirmada:** `volumen_mensual` = 243100.0, del caso de negocio `documentos/productos/PRD-303/00-definicion/2025-10-19-caso-de-negocio.md` (2025-10-19).

Las alertas que salieron al recalcular:
- **Requerimientos sin trazar:** los 5 no están ligados a ningún proyecto.
- **Sin criterio de aceptación:** REQ-2017 y REQ-2025, aunque están aceptados.
- **Supuesto sin verificar:** "La demanda se sostiene sin descuento", hace 212 días.
- **Datos que la definición no trae:** el criterio de éxito y la autoridad.

Dejé la corrida registrada como `2026-10-15-product-publish-1` (8 hallazgos, 12 segundos), con la salida guardada en `estado-producto/PRD-303/corridas/salida-product-publish.md`. La nota de la corrida dice que no se publicó. Para publicar hay que acordar y configurar la carpeta de publicados, y después volver a correr el comando.