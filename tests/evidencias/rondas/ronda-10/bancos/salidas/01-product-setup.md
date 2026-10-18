# /criterio-product:product-setup documentos/productos/PRD-304

## Listo — Tarjeta de crédito digital (PRD-304)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

**Lo que miré:** 6 documentos. Solo 1 es de descubrimiento: una ronda de entrevistas del 2025-10-03 con una sola cita de un solo cliente. Están la definición y el caso de negocio del 2026-01-21. Lo más reciente es el acta del comité de producto del 2026-10-18. Pude leer los 6 (md y docx).

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-18 para la versión 1.1 (familia 0.5.0). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.5.0-2026-10-18.md` y `.pdf`. SHA-256 05a6d511835489a1…

**Sin interfaz, tomé la respuesta por defecto en las 4 preguntas:**
- **Quién eres y qué producto es:** Liliana Torres, gerente de Tarjeta de crédito digital (PRD-304), segmento Personas, como dice la definición.
- **Quién decide qué se construye:** el «Comité de producto». Es lo único que los documentos permiten proponer, porque ninguno nombra a una persona que decida.
- **Dónde guardo el estado:** `estado-producto/PRD-304`, separada de `estado/`, que es la del portafolio.
- **Términos:** quedaron registrados arriba.

**Lo que levanté:** la ficha del producto y 18 requerimientos del acta del comité (17 aceptados y 1 propuesto), solo con lo que está escrito. Lo que ningún documento dice queda como `not_found`. La lectura de los 6 documentos quedó sellada.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| El segmento Personas no tiene tarjeta de crédito digital | Una cita: «Lo necesito y hoy no lo tengo». Sostiene que una persona la necesita, no mide el segmento | 2025-10-03 |
| Volumen mensual de 263.889 | El tablero mide 272.644: diferencia de 3,3 %, bajo el umbral de 20 %. Coincide | Declarado 2026-01-21 · medido 2026-10-15 |
| La demanda declarada se sostiene sin campaña | Un supuesto. El anexo dice «se confirmó» y cita un documento técnico del proveedor | Supuesto 2026-08-02 · verificado 2026-09-11 |
| Retorno esperado en 24 meses | Nada: sin cifra, sin cálculo, sin fuente | — |
| Los 17 requerimientos aceptados responden a demanda | 12 citan «cliente entrevistado», que es la misma entrevista de 2025-10-03 y no nombra ninguno de ellos. 5 no citan a nadie | 2025-10-03 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** No está en la definición ni en el caso de negocio, y sin él nada se puede cerrar después.
- **Quién decide, como persona.** El acta registra un solo asistente, Liliana Torres. La decisión «Se mantiene el plan» no dice qué plan ni quién lo mantiene. Tampoco consta quién aceptó cada requerimiento.
- **Qué es la «propuesta».** La definición solo dice «Propuesta principal».
- **De dónde sale el retorno a 24 meses.**
- **Qué sostiene que la demanda se sostiene sin campaña.** El documento del proveedor del 2026-09-11 no está en la carpeta, y un documento técnico de proveedor no prueba que alguien pidió algo. Registré la verificación como el anexo la declara, pero no pude comprobarla.
- **Un proyecto que construya algo.** La definición dice «Ninguno declarado» y 0 de los 17 requerimientos aceptados tienen proyecto (0,0 %).
- **Qué cuenta el volumen mensual.** El tablero mide 272.644 de un producto sin proyecto declarado y no dice qué se está contando.

### Lo que el registro ya muestra (calculado)
- **Aceptados sin proyecto:** 17 de 17.
- **Evidencia vencida (más de 12 meses):** 13 requerimientos. Toda la evidencia es la entrevista del 2025-10-03.
- **Aceptados sin evidencia:** 5 (REQ-2038, REQ-4402, REQ-4409, REQ-4410, REQ-4413). Con evidencia: 12 de 17 (70,6 %).
- **Aceptados sin criterio de aceptación:** 3 (REQ-4400, REQ-4412, REQ-4414).
- **Sin doliente:** 2 (REQ-4407 y REQ-4408, «sin asignar»).
- **Propuesto sin decidir:** REQ-4401, 65 días.
- **Numeración distinta:** REQ-2030 y REQ-2038 llevan otra numeración y fecha de octubre. Los registré como están y conviene confirmar que son de este producto.

### Supuestos sobre los que está escrita
Declara uno: «La demanda declarada se sostiene sin campaña» (declarado 2026-08-02, verificado 2026-09-11 según el anexo). La definición lleva fecha 2026-01-21 pero contiene texto de agosto y septiembre, y no dice cuándo se revisó.

### Qué le falta a tu carpeta
- Las transcripciones completas de las entrevistas. Hay una cita y no se sabe cuántos clientes hablaron, así que la demanda de 17 requerimientos descansa en una frase.
- Una entrevista o serie de demanda más reciente que octubre de 2025.
- El documento técnico del proveedor del 2026-09-11.
- La serie histórica de `volumen_mensual` (hay un solo punto, 2026-10-15) y qué cuenta.
- El criterio de éxito y las decisiones del comité por requerimiento. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.

### Después
`/product-discovery` sobre el material de entrevistas: ahí los temas se vuelven requerimientos con la cita de quién lo pidió.

*Nota técnica: `sellar` exigió abrir una corrida (`corrida-inicio`) y reescribir la ficha después. Por eso el tiempo hasta el primer resultado (32 s) es aproximado.*

La corrida quedó registrada como `2026-10-18-product-setup-1`. El texto completo está en `estado-producto/PRD-304/corridas/salida-product-setup.md`.