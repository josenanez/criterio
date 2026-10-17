# /criterio-product:product-definition 

## Definición de Tarjeta de la tienda (PRD-309), contrastada al 2026-10-17

**Documentos:** `00-definicion/2026-07-12-definicion-producto.docx` y `00-definicion/2026-07-12-caso-de-negocio.md`, ambos del 2026-07-12. Tienen 5 afirmaciones.

**Términos:** ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-17 (v1.1). No los registré de nuevo.

**Lo que la evidencia contradice:** ningún documento contradice a otro. Lo único que no coincide es una cifra, en la sección siguiente.

**El negocio y los datos**

| Métrica | Declarado | Medido | Diferencia | Fuentes |
|---|---|---|---|---|
| volumen_mensual | 272.424 | 208.658 | 23,4 %, declarado por encima | Caso de negocio, 2026-07-12 · tablero de producto de la bodega de datos, corte 2026-10-10 |

- La serie tiene un solo punto, así que no se sabe si el volumen cayó o nunca llegó a esa cifra.
- El tablero dice que la definición de la métrica "no está declarada", y por eso no se sabe si mide lo mismo que el caso de negocio.

**Afirmaciones numéricas que nadie mide:** "Retorno esperado en 24 meses". No trae cifra ni supuesto, y no hay serie que lo mida.

**No está dicho en ninguna parte**
- El criterio de éxito.
- En qué consiste la propuesta: solo dice "Propuesta principal".
- El monto del retorno y su base.
- Cómo se calculó el volumen de 272.424.
- El tamaño del segmento Hogares.
- Quién decide. El acta del 2026-10-13 no lo nombra, y el único asistente fue Diana Molina.
- Qué proyecto lo construye: la definición dice "Ninguno declarado".
- Qué pasa si el proveedor no cumple.

**Sostenida por un supuesto**
- *El proveedor cumple el tiempo pactado* lleva 70 días sin verificar. Para verificarlo hace falta el plazo pactado a la vista y un hito del proveedor contra esa fecha. Hoy ningún documento nombra al proveedor ni el plazo.
- El supuesto figura "declarado el 2026-08-08" dentro de una definición fechada el 2026-07-12, y la fecha real debería aclararla quien la escribió.

**Sostenida por evidencia y evidencia que envejeció**
- "Hogares no tiene tarjeta de la tienda" se apoya en una sola entrevista del 2025-08-24: *"Lo necesito y hoy no lo tengo."*
- Es evidencia débil: alguien dijo que lo necesita, pero nadie pagó ni se inscribió. La cita no nombra a Hogares ni a la tarjeta.
- Tiene 13 meses, y es la única evidencia que citan los requerimientos que tienen respaldo.

**Lo normativo que toca:** una tarjeta de tienda probablemente toca crédito o pago al consumidor, datos personales y retención de información. Estado: **no tengo la norma a la vista**, porque ningún documento dice el país. Eso no significa que no haya obligación ni que se cumpla, y esta parte va a revisión jurídica.

**Lo que falta para cerrar la definición:** el criterio de éxito y quién decide. El problema y el segmento sí están, aunque con evidencia débil y vieja.

**Después:** ofrezco convertir el supuesto del proveedor en riesgo con doliente. No corresponde ofrecer `/product-charter` porque la definición no está cerrada.

**Corrida registrada:** `2026-10-17-product-definition-1`, con 32 hallazgos en 32 segundos. La salida completa está en `estado-producto/PRD-309/corridas/salida-product-definition.md`.