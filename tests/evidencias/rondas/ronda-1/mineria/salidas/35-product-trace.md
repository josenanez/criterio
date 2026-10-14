# /criterio-product:product-trace 

No hay nada que trazar para Gemelo digital (PRD-303). El registro de requerimientos está vacío, y la carpeta de fichas que indica la configuración (`estado/fichas`) no existe.

- **Registro vacío:** `estado/requirements` no tiene ningún requerimiento, y `estado/producto.json` no tiene cargadas la identidad ni la definición del producto. El cálculo dio 0 decididos, 0 con proyecto y 0 entregados. Por eso no armé ninguna cadena.
- **Sin fichas:** ninguna traza podría darse por confirmada aunque hubiera requerimientos. Existe una ficha, la de PRY-208, pero ningún requerimiento nombra ese proyecto, así que no hay nada que contrastar con ella.
- **Términos:** `terms_accepted` ya estaba en la configuración con versión 1.0, la misma de `TERMS.md`. No hizo falta pedir aceptación.
- **Siguiente paso:** registrar los requerimientos con `/criterio-product:product-requirements` y publicar las fichas de los proyectos en `estado/fichas`. Después se repite `/product-trace`.

La corrida quedó registrada como `2026-10-14-product-trace-1`, con la salida en `estado/corridas/salida-product-trace.md`. El campo del producto en el registro de la corrida salió como `?`, porque el estado no tiene el código cargado.