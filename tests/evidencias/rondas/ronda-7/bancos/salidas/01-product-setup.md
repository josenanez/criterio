# /criterio-product:product-setup documentos/productos/PRD-302

Alba quedó configurada para PRD-302 (Crédito hipotecario digital) y la corrida está registrada como `2026-10-17-product-setup-1`. La definición tiene tres afirmaciones sin sustento. En esta sesión sin interfaz no hice ninguna pregunta; tomé la respuesta sugerida en cada una.

**Qué hay escrito.** Leí 4 documentos; solo 1 es material de descubrimiento. Es una entrevista del 2025-09-12 con una sola cita, de un cliente sin nombre. Levanté la ficha del producto y los 14 requerimientos (REQ-4200 a REQ-4213) que nombra el acta del comité del 2026-10-11.

**Lo que tu definición no sostiene:**
- **Segmento:** no hay nada que diga que Personas tenga el problema.
- **Volumen:** los 130.646 mensuales salen solo del propio caso de negocio y no hay serie medida con la que contrastarlos.
- **Retorno:** el «retorno esperado en 24 meses» no trae cifra.
- **Sin escribir:** no hay criterio de éxito ni contenido bajo «Propuesta principal».

**Lo que muestra el registro:**
- Esa única entrevista, de hace 13 meses (pasó el umbral de 12), está detrás de 10 de los 14 requerimientos. Ninguna cita nombra un requerimiento.
- Los 9 aceptados no tienen proyecto que los ejecute.
- 3 aceptados no tienen quién los pidió.
- 3 propuestos no tienen doliente.
- 4 propuestos llevan más de 60 días sin decidirse.

**Dónde quedó todo:**
- **Configuración:** `.criterio/producto/PRD-302/config.json`; la verificación (`config`) dio ok.
- **Estado:** `estado-producto/PRD-302/`, no en `estado/`.
- **Términos:** versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17. El sí vino en el argumento del comando. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.3.13-2026-10-17.md` y `.pdf`; SHA-256 del Markdown: d85e8bd2335ac89a…
- **Salida completa:** `estado-producto/PRD-302/corridas/salida-product-setup.md`.

**Supuestos míos que conviene que revises:**
- **Quién decide:** puse «Comité de producto» como autoridad. Ningún documento lo declara; salió del acta.
- **Fecha del supuesto:** el supuesto de la definición lleva fecha 2026-06-26 dentro de un documento del 2025-11-22. Lo dejé tal cual y lo señalé como inconsistencia.
- **Marca de corrida:** `sellar` exige una corrida abierta y este comando dice que aquí no va `corrida-inicio`. Abrí la marca, reescribí la ficha con el mismo contenido y selló. También corregí una cita que traía texto además de la ruta.
- **Tiempo:** no medí los minutos hasta el primer resultado; la corrida registró 43 segundos.

Lo siguiente es `/product-discovery` sobre las entrevistas.