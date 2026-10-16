# /criterio-product:product-setup documentos/productos/PRD-306

Dejé a Alba lista sobre PRD-306 (App de clientes). Tomé la respuesta sugerida en cada pregunta, porque nadie iba a responder.

**Dónde quedó**
- **Configuración:** `.criterio/producto/PRD-306/config.json`. La verificación con `config` dio ok.
- **Estado:** `estado-producto/PRD-306/`, con la ficha del producto y 16 requerimientos, uno por cada fila del acta del comité del 2026-10-16.
- **Términos:** aceptados por José Francisco Ñáñez para la versión 0.3.11 (términos 1.1). El comprobante en Markdown y PDF está en `.criterio/terminos/`, con SHA-256 `f969d4f658630df3…`.
- **Corrida registrada:** `2026-10-16-product-setup-1`.

**Lo que miré:** 4 documentos, de los cuales 1 es de descubrimiento: una entrevista del 2025-09-29, de un cliente sin nombre. No hay transcripciones, tickets, encuestas ni serie medida de ninguna métrica.

**Lo que no está dicho en ninguna parte**
- El criterio de éxito del producto.
- De dónde sale el volumen mensual de 67.794, y que alguien lo mida.
- La cifra del retorno esperado en 24 meses.
- La propuesta: la definición solo dice «Propuesta principal».
- Quién decide qué se construye. Puse Comité de producto porque el acta es suya, pero ningún documento lo dice.
- Un proyecto que construya el producto: «Ninguno declarado».
- Qué pidió cada requerimiento. Los 16 citan «Cliente entrevistado», pero la única entrevista no nombra ninguno.

**Señales sobre los requerimientos (39 en total)**
- 15 no tienen proyecto que los ejecute.
- 14 tienen su evidencia vieja: la entrevista tiene 12 meses.
- 5 aceptados no tienen criterio de aceptación (REQ-4603, 4604, 4608, 4609, 4613).
- 2 aceptados no tienen evidencia de demanda (REQ-4608 y REQ-2028).
- REQ-4607 no tiene doliente.
- REQ-4600 lleva 120 días propuesto sin decidirse.
- El único supuesto declarado, «La demanda se sostiene sin descuento», lleva 196 días sin verificar.

**Dos defectos**
- `sellar` exigió abrir la corrida con `corrida-inicio` y que la ficha se escribiera después, aunque el comando dice que aquí no va. Lo hice así y reescribí la ficha para que contara como de esta corrida.
- La nota de la corrida dice «38 señales» y «unos 10 minutos». Lo que cuenta el script es 39 hallazgos y 31 segundos. Esa nota ya quedó registrada y no la corregí.

El siguiente paso es `/product-discovery` sobre las entrevistas. El resultado completo está en `estado-producto/PRD-306/corridas/salida-product-setup.md`.