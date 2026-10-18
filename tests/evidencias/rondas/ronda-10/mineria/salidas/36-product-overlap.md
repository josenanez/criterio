# /criterio-product:product-overlap PRD-301

No encontré la configuración de PRD-301, así que me detengo aquí.

Busqué en `.criterio/producto/PRD-301/config.json`, dentro de la carpeta donde corre la sesión. Esa carpeta no existe. En `.criterio/producto/` solo hay una: `PRD-308`.

No usé la de PRD-308 en lugar de la de PRD-301, y no inventé una configuración. Tampoco corrí `terminos`, `corrida-inicio` ni `overlap`, y no registré la aceptación de términos. Sin configuración no hay `--config` ni `--state` con los que correrlos.

Para seguir hay dos caminos:
- **Configurar PRD-301:** `/criterio-product:product-setup` crea esa configuración. Después se vuelve a correr `/product-overlap PRD-301`.
- **Si se quería PRD-308:** se corre `/product-overlap PRD-308`.