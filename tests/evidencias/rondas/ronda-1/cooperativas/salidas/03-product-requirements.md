# /criterio-product:product-requirements 

El registro de requerimientos de Crédito de libranza (PRD-300) está vacío, así que no hay vacíos que mostrar y no inventé ninguno.

- **Términos:** la configuración ya tenía registrada la aceptación de TERMS.md versión 1.0, por José Francisco Ñáñez el 2026-10-14. Coincide con la versión vigente, así que seguí.
- **Qué devolvió el cálculo:** `compute` dio 0 requerimientos. En `estado/PRD-300/producto.json` la identidad y la definición del producto están en `null`, y el código del producto sale como `?`. Nadie ha corrido el inventario sobre ese producto.
- **Qué hay en los documentos:** la carpeta `documentos/productos/PRD-300` tiene la definición, el caso de negocio, las entrevistas y el acta del comité del 2026-10-13. Nada de eso se ha convertido en requerimientos registrados.
- **Siguiente paso:** correr `/criterio-product:product-setup` para que lea esos documentos y levante el registro. Después se repite `/criterio-product:product-requirements`.
- **Corrida:** quedó registrada como `2026-10-14-product-requirements-1`, con 0 hallazgos. La salida mostrada está en `estado/PRD-300/corridas/salida-product-requirements.md`.