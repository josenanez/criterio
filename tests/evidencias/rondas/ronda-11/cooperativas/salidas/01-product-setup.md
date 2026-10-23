# /criterio-product:product-setup documentos/productos/PRD-306

## Listo — Recaudos (PRD-306)

La definición de Recaudos casi no tiene nada que la sostenga. La configuración y los términos quedaron registrados y la corrida está guardada. Dos pasos no se completaron: no pude sellar la lectura de los documentos y no dejé la marca en tu carpeta.

**Lo que miré:** 5 documentos, todos legibles. Solo 1 es de descubrimiento: una ronda de entrevistas del 2025-09-23 con una sola cita. La definición y el caso de negocio son del 2026-05-20, y lo más reciente es el acta del comité del 2026-10-23. No hay serie de métricas.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.8.0 (términos 1.2), con fecha 2026-10-23. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.8.0-2026-10-23.md` y `.pdf`. Las huellas SHA-256 empiezan por d1497e5f9c284733 (md) y 1972f5ac032ba1ef (pdf).

**Respuestas por defecto**, porque nadie iba a contestar:
- **Gerente de producto:** Camilo Beltrán.
- **Quién decide:** el «Comité de producto». Es el nombre del acta, y en ella el único asistente es Camilo Beltrán.
- **Dónde queda el estado:** `estado-producto/PRD-306`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «Microempresarios no tiene recaudos» | Una cita anónima: «Lo necesito y hoy no lo tengo.» No dice de qué segmento es ni qué es «lo» | 2025-09-23 (13 meses) |
| «El proveedor cumple el tiempo pactado» | Un supuesto verificado en el anexo del 2026-10-01 | 2026-10-01 |
| Volumen de 214.523 al mes | Solo el propio caso de negocio. No hay serie medida con qué contrastarlo | 2026-05-20 |
| Retorno esperado en 24 meses | Nada. No trae monto ni cálculo | — |
| 14 requerimientos aceptados | 10 citan «cliente entrevistado» (71,4 %) y 4 no citan a nadie | acta 2026-10-23 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** ningún documento lo dice, así que el cierre no tendrá contra qué juzgarse.
- **Origen de 214.523:** nadie lo está midiendo.
- **Propuesta principal:** la definición solo trae ese título, sin contenido.
- **Qué pidió cada requerimiento:** el acta los llama «Requerimiento REQ-46xx» y no dice la necesidad.
- **Proyecto que los construya:** ninguno de los 14 aceptados tiene uno (0,0 %).
- **Cuál es «el plan»:** el comité decidió mantenerlo y no hay plan en la carpeta.
- **Criterio de aceptación:** faltan en 5 aceptados (REQ-4601, 4603, 4610, 4611, 4613).
- **Evidencia de demanda:** faltan en 4 aceptados (REQ-4604, 4606, 4608, 4614).
- **Decisión sobre los propuestos:** REQ-4602 lleva 208 días sin decisión y REQ-4607 lleva 142.

### Supuestos sobre los que está escrita
Declara uno solo, y tiene dos reparos:
- La definición está fechada 2026-05-20, pero recoge un supuesto de septiembre. Se editó después de su fecha.
- El anexo dice que se verificó con un documento técnico del proveedor que no está en la carpeta, y no dice qué tiempo se pactó. La evidencia es una línea.

Ningún supuesto cubre la demanda: que los microempresarios usarían el producto no está escrito como supuesto, y por eso nadie lo ha verificado.

### Qué le falta a tu carpeta
- **Descubrimiento:** una cita de hace 13 meses sostiene 12 requerimientos, y esa cita no nombra ninguno.
- **Serie del volumen mensual**, con su fuente.
- **Criterios de aceptación que digan qué mirar:** «se verifica en producción» aparece en 11 requerimientos y no dice qué se verifica.
- **Acta de constitución de algún proyecto**, para que las decisiones del comité se estén construyendo.
- **Decisiones del comité con quién decidió y cuándo:** el acta solo dice «Se mantiene el plan».

**Señales del cálculo:** sin proyecto 14 · evidencia vieja 12 · sin criterio de aceptación 5 · aceptado sin evidencia 4 · sin decidir 2.

**Lo que no pude hacer:**
- **Sellar la lectura:** `sellar` pide una corrida abierta con `corrida-inicio`, y este comando dice que aquí no va. La lectura queda sin sellar.
- **Marca `_CRITERIO_PRODUCTO.txt`:** no la dejé en tu carpeta. Es la única escritura dentro de los documentos y nadie respondió que sí.

**Qué quedó escrito:**
- **Configuración:** `.criterio/producto/PRD-306/config.json`.
- **Ficha del producto y 16 requerimientos:** en `estado-producto/PRD-306/`.
- **Corrida:** `2026-10-23-product-setup-1`, con el resultado en `estado-producto/PRD-306/corridas/salida-product-setup.md`. No abrí el HTML de la corrida.

**Siguiente paso:** `/product-discovery` sobre las entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.