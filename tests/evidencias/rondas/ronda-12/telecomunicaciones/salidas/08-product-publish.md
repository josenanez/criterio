# /criterio-product:product-publish 

No publiqué nada: la configuración de PRD-306 no define una carpeta de productos publicados.

- **Qué falta:** `.criterio/producto/PRD-306/config.json` solo trae `paths.documents` y `paths.state`. No hay carpeta para `publicados/`. La única carpeta `productos` que encontré es `documentos/productos`, que contiene los documentos del propio producto, no fichas de otros. No la usé como sitio común porque no está acordada.
- **Por qué paro:** el comando dice que sin un sitio común acordado esto no sirve, y que acordarlo es una conversación de la organización. Tampoco creé la carpeta, porque habría que preguntar antes y esta sesión no tiene a nadie que responda.
- **Qué hice:** los términos ya estaban vigentes (v1.3, aceptados por José Francisco Ñáñez el 2026-10-28), así que no los registré otra vez. Marqué el arranque de la corrida y recalculé las cifras. No registré la corrida con `corrida`, porque no se publicó nada.

La ficha ya está lista y no se escribió en ningún archivo. Cuando haya carpeta, tiene este contenido, con corte al 2026-10-28:
- **Producto:** PRD-306 Televisión IP, gerente Gustavo Neira.
- **Segmento declarado:** Grandes empresas.
- **Requerimientos:** 12 (11 aceptados y 1 propuesto, REQ-4605). Ninguno tiene proyecto asignado.
- **Proyectos:** 0.
- **Métricas afirmadas:** 1, `volumen_mensual` = 100016, según `documentos/productos/PRD-306/00-definicion/2026-03-07-caso-de-negocio.md` (2026-03-07).

La ficha saldría con cero proyectos, así que `/product-overlap` no podría detectar un proyecto compartido con otro producto.

Para seguir, la organización tiene que fijar la carpeta común y añadirla a la configuración. Después se vuelve a correr este comando.