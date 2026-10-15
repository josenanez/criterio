# /criterio-product:product-publish 

No publiqué la ficha de PRD-308 (Marketplace), porque no hay una carpeta de productos publicados configurada. La configuración no define esa ruta y no existe `productos/publicados` en el espacio. No la inventé ni la creé. Acordar ese sitio común es una decisión de la organización, no de este comando.

Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-15, así que no hubo que registrarlos de nuevo.

**La ficha habría llevado, con corte al 2026-10-15:**
- **Requerimientos:** 17 (13 aceptados y 4 propuestos). Ninguno está ligado a un proyecto.
- **Proyectos:** 0.
- **Métrica afirmada:** `volumen_mensual` = 209097, del caso de negocio del 2025-10-14 (`documentos/productos/PRD-308/00-definicion/2025-10-14-caso-de-negocio.md`).
- **Segmento declarado:** Empresas.

La medición del 2026-10-01 en la bodega de datos da 131628, un 37.0 % por debajo de lo declarado. Esa medición no se publica.

Para publicar, indica la ruta de la carpeta común y vuelvo a correr el comando. La ficha quedaría en `<ruta>/PRD-308.json`.

Dejé la corrida registrada como `2026-10-15-product-publish-1`, con la nota de que no se publicó nada. La salida quedó en `estado-producto/PRD-308/corridas/salida-product-publish.md`.