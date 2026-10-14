# /criterio-product:product-requirements 

No hay registro de requerimientos que revisar, así que este comando no produjo hallazgos. El registro de Gemelo digital (PRD-303) está vacío: `compute` devolvió 0 requerimientos y 0 señales. `estado/requirements/` no tiene archivos y `estado/producto.json` no tiene datos. La carpeta `estado/fichas` ni siquiera existe.

- **Términos:** `TERMS.md` está en versión 1.0 y la configuración ya trae la aceptación de José Francisco Ñáñez del 2026-10-14. No hizo falta pedirla.
- **Qué falta:** `documentos/productos/PRD-303` sí tiene documentos: la definición, el caso de negocio, las entrevistas, el tablero de métricas y el acta del comité del 2026-10-10. Nadie los ha convertido en requerimientos. Eso lo hace `/criterio-product:product-setup`, y no lo inventé aquí. Corre ese comando y luego este.
- **Qué no significa:** que no haya vacíos no quiere decir que el registro esté sano. Quiere decir que no hay nada registrado.
- **Corrida registrada:** el texto está en `estado/corridas/salida-product-requirements.md` y la corrida quedó como `2026-10-14-product-requirements-1`, con la nota del registro vacío. La salida del registro muestra el producto como `?`, porque `estado/producto.json` está vacío.