# /criterio-product:product-setup documentos/productos/PRD-305

## Listo — Microcrédito (PRD-305)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

**Lo que miré:** 4 documentos, todos en Markdown y todos legibles. Solo 1 es de descubrimiento: una ronda de entrevistas del 2025-12-30. El caso de negocio y la definición son del 2025-12-01. Lo más reciente es el acta del comité del 2026-10-07. No hay transcripciones, tickets, encuestas ni ninguna serie medida.

**Las cuatro preguntas** (sesión sin interfaz, respuesta por defecto en cada una):
1. **Producto:** Microcrédito (PRD-305), gerente Ricardo Salas, tal como lo dice la definición.
2. **Quién decide qué se construye:** Comité de producto. Es una propuesta mía: el acta no dice quién decide dentro del comité.
3. **Dónde guardo lo que encuentro:** `estado-producto/PRD-305`, hermana de `documentos/`.
4. **Términos:** mostré el texto y tomé tu indicación como el sí de José Francisco Ñáñez.

**Términos:** aceptados para la versión 0.5.0 (texto 1.1) por José Francisco Ñáñez el 2026-10-18. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.5.0-2026-10-18.md` y `.pdf`. SHA-256 del `.md`: 05a6d511835489a1…

**Levantado desde lo escrito:** `producto.json` y 16 requerimientos (REQ-4500 a REQ-4515, del acta del 2026-10-07): 12 aceptados y 4 propuestos. Ninguno tiene proyecto que lo ejecute. La verificación de la configuración dio `ok`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Los Asociados urbanos no tienen microcrédito | Una sola entrevista: un «cliente entrevistado» dice «Lo necesito y hoy no lo tengo». No dice que sea Asociado urbano ni cuántos más lo viven | 2025-12-30 |
| El volumen mensual será de 166.254 | Solo el propio caso de negocio. No hay ninguna serie medida, así que nadie está midiendo lo que el negocio afirmó | 2025-12-01 |
| El proveedor cumple el tiempo pactado | Un supuesto declarado y sin verificar, desde hace 146 días | declarado 2026-05-25 |
| Propuesta principal | Nada: la definición escribe «Propuesta principal» y no dice cuál es | 2025-12-01 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Ni la definición ni el caso de negocio lo escriben.
- **El retorno.** Dice «Retorno esperado en 24 meses», sin cifra, sin cálculo y sin fuente.
- **La propuesta.** Qué se va a construir no está escrito.
- **El proyecto.** La definición dice «Ninguno declarado» y los 12 requerimientos aceptados tampoco tienen uno. El acta dice «Se mantiene el plan», pero ningún documento contiene ese plan.
- **Quién decide dentro del comité.** El acta registra un solo asistente, Ricardo Salas, que además es el gerente y el doliente de REQ-4509. Ninguna decisión del acta dice quién la tomó.
- **El problema de cada requerimiento.** Los 16 se llaman «Requerimiento REQ-45xx» y el acta no dice qué se necesita.

### Supuestos sobre los que está escrita
La definición declara un supuesto: «El proveedor cumple el tiempo pactado», sin verificar. Ningún documento dice quién es el proveedor ni cuál es el tiempo pactado.

La definición está fechada el 2025-12-01 y el supuesto, el 2026-05-25. El documento se tocó después de su fecha y nadie lo dice.

### Qué hay en el registro
- **Aceptados:** 12, de los cuales 9 tienen evidencia (75.0%) y 0 tienen proyecto (0.0%).
- **Aceptados sin evidencia:** REQ-4507, REQ-4511 y REQ-4514. El acta no dice quién los pidió.
- **Aceptados sin criterio de aceptación:** REQ-4500 y REQ-4511.
- **Sin doliente:** REQ-4502, REQ-4504, REQ-4505, REQ-4506 y REQ-4510. REQ-4505 y REQ-4506 ya están aceptados.
- **Propuestos sin decidir hace más de 60 días:** REQ-4502 (74 días), REQ-4503 (64), REQ-4504 (84) y REQ-4510 (104).
- **Evidencia de los demás:** 12 requerimientos se apoyan en la misma entrevista, la única, que no nombra ninguno. Sostiene que hay una necesidad, no que se pidiera cada uno. Todavía no pasa el umbral de 12 meses, así que no hay alerta de evidencia vieja.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- Las transcripciones de las entrevistas (hoy hay una página, de un solo cliente).
- La serie de `volumen_mensual` con su fuente.
- El criterio de éxito.
- Las decisiones del comité, con quién decide y por qué. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.

**Siguiente:** `/product-discovery` sobre el material de entrevistas, para que los temas se vuelvan requerimientos con la cita de quién lo pidió.

**Nota técnica:** `sellar` exigió abrir la corrida con `corrida-inicio`, que este comando dice que no lleva. La abrí por eso, así que el tiempo de la corrida cuenta desde ahí, no desde el inicio de la conversación.

La corrida quedó registrada como `2026-10-18-product-setup-1`, con 27 hallazgos. Esta salida está guardada entera en `estado-producto/PRD-305/corridas/salida-product-setup.md`.