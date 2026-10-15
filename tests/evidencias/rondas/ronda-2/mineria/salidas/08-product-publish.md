# /criterio-product:product-publish 

No publiqué nada: la configuración de PRD-300 no tiene una carpeta de productos publicados, y no hay ninguna en el espacio.

En `.criterio/producto/PRD-300/config.json` solo están `paths.documents` y `paths.state`. Sin un sitio común acordado, la ficha no tiene dónde leerse. Acordar ese sitio es una conversación de la organización, no algo que este comando deba inventar. Tampoco creé la carpeta, porque el comando pide preguntar antes y esta sesión no tiene a quién preguntar. No registré la corrida de publicación, porque no quedó nada publicado.

- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.
- **Ficha lista:** `compute` y `publish` corrieron sin escribir nada, y la ficha quedó calculada con corte al 2026-10-15.
- **Qué llevaría:**
  - 4 requerimientos, todos aceptados: REQ-1000, REQ-1001, REQ-1002 y REQ-2017.
  - 0 proyectos. Ninguno de los 4 requerimientos tiene proyecto asignado.
  - 1 métrica afirmada: `volumen_mensual` = 164808, según `documentos/productos/PRD-300/00-definicion/2026-02-02-caso-de-negocio.md`.
  - Segmento declarado: Segmento Gerencia.
- **Para el otro lado:** el tablero del 2026-09-28 mide 102629 para esa métrica. Eso es un 37.7 % por debajo de lo declarado, pero esa medición no entra en la ficha.

Para publicar, hace falta que la organización acuerde la carpeta compartida (por ejemplo `productos/publicados/`) y que se registre en la configuración. Con eso corro de nuevo `/product-publish`.