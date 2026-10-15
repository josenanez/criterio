# /criterio-product:product-publish 

**No publiqué la ficha de PRD-301.** La configuración no tiene una carpeta de productos publicados: `paths` solo trae `documents` y `state`. Tampoco existe una carpeta `publicados` en el espacio. Sin un sitio común acordado esto no sirve, y acordarlo es una conversación de la organización, no un comando. No la creé ni la inventé.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no hubo que registrarlos de nuevo.

Con corte al 2026-10-15, esto es lo que habría llevado la ficha:

- **Lleva:** 18 requerimientos, 0 proyectos y 1 métrica afirmada.
- **Segmento declarado:** Base de la pirámide.
- **Métrica:** `volumen_mensual`, 267895, del caso de negocio `documentos/productos/PRD-301/00-definicion/2025-09-03-caso-de-negocio.md` (2025-09-03).

Dos cosas conviene saber antes de publicar:

- **Sin proyectos:** ningún requerimiento tiene proyecto asociado, y los 17 aceptados salen sin trazar.
- **Cifra declarada por encima de la medida:** el tablero del 2026-09-29 mide 201716 de `volumen_mensual`, y la definición declara 267895, un 24.7 % más. La ficha publicaría la cifra declarada, no la medida.

**Para publicar:** indica la carpeta común de productos publicados, agrégala a la configuración y vuelve a correr el comando.

La corrida quedó registrada como `2026-10-15-product-publish-1` en `estado-producto/PRD-301/corridas/`, con la nota de que no se publicó. Tardó 15 segundos y registró 44 hallazgos, que son las señales que ya traía el registro.