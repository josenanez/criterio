# /criterio-product:product-setup documentos/productos/PRD-300

## Listo: Venta en línea (PRD-300)

**Lo que miré:** 5 documentos, todos legibles (3 .docx y 2 .md). Solo uno es de descubrimiento: una entrevista del 2025-08-30. Lo más reciente es el acta del comité del 2026-10-13.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-18 para la versión 1.1, y así quedó registrado. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.5.0-2026-10-18.md` y `.pdf`. Los primeros 16 caracteres del SHA-256 son 05a6d511835489a1…

**Preguntas:** nadie respondió, así que tomé la sugerida en las cuatro:
- **Producto:** PRD-300 «Venta en línea», con Diana Molina como gerente.
- **Quién decide:** el Comité de producto. Es solo una propuesta por defecto, porque ningún documento dice quién decide.
- **Dónde guardo el estado:** `estado-producto/PRD-300`, no en `estado/`.
- **Términos:** aceptados con el nombre que indicaste.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| El segmento Pequeños negocios no tiene venta en línea | Una sola entrevista: «Lo necesito y hoy no lo tengo». No dice quién es ni qué necesita | 2025-08-30 (13 meses) |
| El cliente paga por la entrega rápida | Un supuesto «confirmado» con un documento técnico del proveedor, que no dice qué paga el cliente | 2026-09-14 |
| volumen_mensual = 162.820 | Solo el caso de negocio, sin serie medida | 2026-05-30 |
| Retorno esperado en 24 meses | Solo el caso de negocio, sin cifra ni cálculo | 2026-05-30 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** no existe.
- **Quién decide qué se construye:** ningún documento lo nombra.
- **La propuesta:** la definición tiene el título «Propuesta principal» y nada debajo.
- **Qué proyecto construye el producto:** 0 de 15 requerimientos tienen proyecto (0,0 %).
- **Cuál es «el plan» que el comité mantuvo:** el acta dice «Se mantiene el plan» y no hay plan entre los documentos.
- **Medición de volumen_mensual:** no hay ninguna serie, así que nadie está midiendo lo que el negocio afirmó.
- **Qué pidió cada requerimiento:** los 15 se llaman «Requerimiento REQ-xxxx» y ninguno describe el problema.

### Supuestos sobre los que está escrita
Hay uno, el de la entrega rápida. Está marcado como verificado, pero con una fuente que no es de demanda.

### El registro
El acta acepta los 15 requerimientos. Los cálculos salen del script:
- **Sin evidencia de demanda:** 6 (REQ-4001, 4003, 4004, 4009, 4011, 4012). Los otros 9 tienen evidencia, el 60,0 %.
- **Con evidencia vencida:** 9. Todos apuntan a la misma entrevista, de hace 13 meses.
- **Sin criterio de aceptación:** 4 (REQ-2028, 4000, 4011, 4013).
- **Sin proyecto que los ejecute:** 15 de 15.

Esos 9 que citan evidencia comparten una sola entrevista de un cliente sin nombre. El acta dice «Cliente entrevistado» sin decir cuál, así que no pude vincular esa cita a cada requerimiento.

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas: hay una sola.
- La serie medida de volumen_mensual, con su fuente.
- Quién decidió cada aceptación, y si el comité descartó algo.
- Un criterio de éxito y la lista de proyectos.

### Una desviación del comando
El comando dice que aquí no va `corrida-inicio`, pero `sellar` se negó a correr sin una corrida abierta. La abrí solo para poder sellar y lo dejé anotado en la nota de la corrida.

La corrida quedó registrada como `2026-10-18-product-setup-1`, con la salida completa en `estado-producto/PRD-300/corridas/salida-product-setup.md`. No medí los minutos hasta el primer resultado; el script registró 31 segundos de ejecución. Lo siguiente sería `/product-discovery` sobre las entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.