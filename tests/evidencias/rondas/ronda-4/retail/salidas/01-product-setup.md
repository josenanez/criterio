# /criterio-product:product-setup documentos/productos/PRD-300

## Listo: Venta en línea (PRD-300)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

**Lo que leí:**
- Eran 4 documentos y todos se leyeron, incluidos los dos .docx.
- Solo 1 es de descubrimiento: una entrevista del 2025-11-24 con una sola frase de un cliente.
- La definición y el caso de negocio son del 2025-11-26.
- Lo más reciente es el acta del comité de producto del 2026-10-09.

**Términos:**
- José Francisco Ñáñez los aceptó el 2026-10-15 para la versión 0.3.10 (términos 1.1).
- El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.10-2026-10-15.md` y `.pdf`.
- Su SHA-256 empieza por fdf0177cc54e5055…

**Preguntas:**
- Eran 4 y nadie respondió, así que tomé lo sugerido.
- El gerente es María Restrepo, según la definición.
- Quien decide es el «Comité de producto», según el acta. El acta no dice quién decide dentro del comité, así que esto queda sin confirmar.
- El estado quedó en `estado-producto/PRD-300`, al lado de `documentos/` y no en `estado/`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Empresas no tiene venta en línea» | Solo la propia definición. La entrevista dice «Lo necesito y hoy no lo tengo», sin nombrar el segmento | 2025-11-26 / 2025-11-24 |
| Volumen mensual 228.369 | Solo el caso de negocio. No hay ninguna serie medida | 2025-11-26 |
| «Retorno esperado en 24 meses» | Nada: no hay cifra, cálculo ni fuente | 2025-11-26 |
| «Propuesta principal» | Es un marcador: la propuesta no está escrita | 2025-11-26 |
| El proveedor cumple el tiempo pactado | Un supuesto declarado, sin verificar desde hace 86 días | 2026-07-21 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** ningún documento lo dice.
- **De dónde sale 228.369 al mes:** nadie mide la cifra que el negocio afirmó.
- **Cuánto es el retorno:** no se dice contra qué inversión.
- **Qué se propone construir.**
- **Quién decide dentro del comité:** el acta tiene un solo asistente, María Restrepo, y no nombra a nadie que decida.
- **Qué proyecto lo construye:** la definición dice «Ninguno declarado» y ninguno de los 16 requerimientos tiene proyecto.
- **Qué proveedor** es el del supuesto, y qué tiempo se pactó.

### Requerimientos que levanté del acta (16)
Hay 13 aceptados y 3 propuestos. De los 16, 11 tienen evidencia (84,6 %) y 0 tiene proyecto (0,0 %).
- **Sin proyecto:** los 13 aceptados.
- **Sin criterio de aceptación:** REQ-2028, REQ-4001, REQ-4004 y REQ-4007.
- **Sin evidencia de quién los pidió:** REQ-4008 y REQ-4011.
- **Sin doliente («sin asignar»):** REQ-4004 y REQ-4009.
- **Propuestos sin decidir:** REQ-4003 (205 días), REQ-4005 (160) y REQ-4002 (96).
- **Evidencia repetida:** la evidencia de los 11 es la misma frase de la misma entrevista. El acta la atribuye a «Cliente entrevistado», pero la entrevista no nombra ningún requerimiento.
- **Sin texto de la necesidad:** los títulos son «Requerimiento REQ-xxxx», así que esa necesidad quedó en `not_found`.
- **Numeración rara:** REQ-2028 y REQ-2036 tienen otra numeración. REQ-2036 figura «desde» 2026-10-10, un día después del acta. No lo resolví; lo dejé anotado.
- **Decisión del comité:** el acta no dice quién aceptó ni cuándo (usé «Desde» como fecha). Su única decisión es «Se mantiene el plan», sin decir cuál.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- Las transcripciones completas de las entrevistas, porque hay una sola y de una frase.
- La serie medida del volumen mensual, con su fuente.
- El texto de cada requerimiento.
- Las decisiones del comité con quién decide, para distinguir un requerimiento descartado de uno que nadie miró.

### Dos cosas del proceso
- `sellar` exigió una corrida abierta y la ficha escrita después de abrirla. Por eso abrí con `corrida-inicio` y reescribí la ficha antes de sellar, aunque el comando decía que aquí no iba.
- La corrida quedó registrada como `2026-10-15-product-setup-1`, y la salida completa está en `estado-producto/PRD-300/corridas/salida-product-setup.md`.

Cuando tengas más entrevistas, `/product-discovery` las convierte en temas con la cita de quién los pidió.