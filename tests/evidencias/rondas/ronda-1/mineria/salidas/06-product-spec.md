# /criterio-product:product-spec 

No hay especificación que redactar para Gemelo digital (PRD-303), porque el registro de requerimientos está vacío. `/product-spec` solo toma los requerimientos en `aceptado` o `en_construccion`, y hay 0. Los criterios de aceptación habría que inventarlos desde los documentos, así que no los escribí.

- **Documentos sin inventariar:** en `documentos/productos/PRD-303` están la definición y el caso de negocio (2025-12-09), las entrevistas (2026-08-31), el tablero de métricas (2026-10-12) y el acta del comité (2026-10-10). Nadie los ha inventariado como requerimientos.
- **Términos:** la configuración ya tiene la aceptación de José Francisco Ñáñez (versión 1.0, 2026-10-14), igual a la versión de `TERMS.md`, así que no volví a pedirla.
- **Qué sigue:** inventariar los requerimientos con `/criterio-product:product-requirements` o `/criterio-product:product-setup`. Cuando el comité acepte alguno, se vuelve a correr `/product-spec`.
- **Corrida:** quedó registrada como `2026-10-14-product-spec-1` (12 s, 0 requerimientos). Lo que te mostré está en `estado/corridas/salida-product-spec.md`.

El registro dice `producto: "?"` en su campo de producto, aunque sí guardó el caso PRD-303. Eso coincide con que `estado/producto.json` no tiene la identidad cargada, algo que `product-setup` debería llenar.