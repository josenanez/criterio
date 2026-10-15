# /criterio-product:product-setup documentos/productos/PRD-308

**Listo — Marketplace (PRD-308).** La configuración está escrita y verificada, y los términos quedaron aceptados.

**Lo que miré:** 5 documentos, todos legibles (4 en Markdown y 1 .docx). Solo uno es de descubrimiento: una ronda de entrevistas del 2026-02-08 con una sola cita de un cliente sin nombre. La definición y el caso de negocio son del 2025-10-14, y lo más reciente es el acta del comité del 2026-10-12.

**Preguntas:** no hice ninguna porque la sesión no tiene interfaz; tomé la respuesta sugerida en cada una. Ningún documento dice quién decide qué se construye. En la configuración quedó «Comité de producto» como propuesta sin confirmar, y en la ficha ese campo queda como no encontrado.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.3.9 (textos 1.1), el 2026-10-15. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.3.9-2026-10-15.md` y `.pdf`. SHA-256 del Markdown: `eff52306622e7cd2…`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Empresas no tiene marketplace | Solo en parte: una cita de un cliente sin nombre y sin segmento («Lo necesito y hoy no lo tengo») que no menciona marketplace | 2026-02-08 |
| volumen_mensual de 209.097 | El caso de negocio. La serie medida da 131.628 al 2026-10-01, **37.0 % por debajo de lo declarado** | 2025-10-14 / 2026-10-01 |
| La regulación de datos lo permite | Un supuesto marcado «verificado», sin decir quién ni con qué | 2026-07-22 |
| Retorno esperado en 24 meses | Nada: no hay cifra ni cálculo | — |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Sin él no hay contra qué cerrar el producto.
- **Quién decide qué se construye.**
- **La propuesta de valor.** La definición dice solo «Propuesta principal».
- **El retorno esperado.** No hay monto, método ni supuestos.
- **Qué proyecto construye el producto.** Ninguno de los 13 requerimientos aceptados tiene proyecto (0.0 %).
- **Evidencia de demanda en 5 de los 13 aceptados:** REQ-4800, 4801, 4806, 4813 y 4815. Los otros 8 (61.5 %) se apoyan en esa única cita, que no nombra ningún requerimiento.
- **Criterio de aceptación en 4 aceptados:** REQ-4806, 4807, 4813 y 4814. En los demás es «se verifica en producción», que no es medible.
- **Doliente en REQ-4808 y REQ-4815:** ambos dicen «sin asignar».

### Supuestos sobre los que está escrita
Hay uno declarado, y está dado por verificado sin fuente. Su fecha de declaración (2026-07-22) es posterior a la del documento que lo contiene (2025-10-14). Como toca datos personales, vale un barrido normativo.

### Qué le falta a tu carpeta
- **Transcripciones de las entrevistas:** hoy hay una cita para 17 requerimientos.
- **Serie de la métrica principal:** hay una sola medición, así que no se ve la tendencia.
- **Decisiones del comité:** el acta solo dice «Se mantiene el plan». Tres requerimientos propuestos llevan más de 60 días sin decisión: REQ-4803 (103 días), REQ-4804 (101) y REQ-4808 (144).
- **REQ-2030:** su numeración difiere de la del resto (REQ-48xx). No sé si es un error o viene de otro producto.

**Dos cosas que conviene saber:**
- `sellar` exigió una corrida abierta, así que corrí `corrida-inicio` antes. El comando decía que aquí no iba.
- El registro de la corrida quedó como `2026-10-15-product-setup-1`. Tiene todo lo mostrado, tal cual, en `estado-producto/PRD-308/corridas/salida-product-setup.md`.

**Siguiente paso que te ofrezco:** `/product-discovery` sobre las entrevistas, para que los temas queden con la cita de quién los pidió.