# /criterio-product:product-overlap PRD-302

No encontré la configuración de PRD-302, así que paro aquí.

Esperaba `.criterio/producto/PRD-302/config.json` en `/home/claude/banco/ronda-2/bancos/espacio`. Esa carpeta no existe. En `.criterio/producto/` solo hay un producto configurado, PRD-303.

No usé la configuración de PRD-303 en su lugar, porque el argumento pedía PRD-302 y no quiero cruzar otro producto. Tampoco inventé una configuración.

No corrí `terminos`, `corrida-inicio` ni `overlap`, y no registré la aceptación de términos de José Francisco Ñáñez. Sin configuración no hay un producto al que atar el comprobante.

Dos formas de seguir:
- Si PRD-302 debía existir, corre `/criterio-product:product-setup` para crearlo y luego repite `/product-overlap PRD-302`.
- Si en realidad querías PRD-303, repite el comando con ese código.