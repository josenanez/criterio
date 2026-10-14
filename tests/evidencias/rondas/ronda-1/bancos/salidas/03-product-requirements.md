# /criterio-product:product-requirements 

El registro de Microseguros (PRD-306) está vacío: `estado/requirements/` no tiene ningún requerimiento y el cálculo da 0 en todo. No hay vacíos que mostrar porque no hay nada registrado, no porque esté todo en orden.

- **Términos:** la configuración ya tenía `terms_accepted` v1.0 (2026-10-14, José Francisco Ñáñez), igual a la versión de `TERMS.md`. No pedí nada más.
- **Definición:** no está cargada. Problema, quién, éxito y facultad de decisión salen como desconocidos.
- **Registro de la corrida:** guardé lo que te muestro en `estado/corridas/salida-product-requirements.md`. La corrida quedó como `2026-10-14-product-requirements-1`, con 0 hallazgos.
- **Código del producto:** `compute` devolvió `?` en vez de PRD-306. Esa corrida quedó registrada con `producto: "?"`, aunque `--caso PRD-306` sí quedó en el registro. Puede que `compute` no esté leyendo `estado/producto.json` ni el nombre del producto de la configuración. No lo inventé ni lo corregí.

Para avanzar, registra requerimientos desde `documentos/productos/PRD-306` o desde el descubrimiento que ya corrió (`/criterio-product:product-discovery`) y vuelve a correr este comando.