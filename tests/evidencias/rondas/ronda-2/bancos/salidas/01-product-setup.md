# /criterio-product:product-setup documentos/productos/PRD-303

## Listo: Cuenta PyME (PRD-303)

**Lo que miré:** 5 documentos. Uno es de descubrimiento: una sola entrevista, del 2025-08-11. La definición y el caso de negocio son del 2026-02-02, y lo más reciente es el tablero de métricas del 2026-10-09. Los leí todos, incluidos los dos `.docx`.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-15 para la versión 0.3.8 (términos 1.1). Lo registré con la aceptación que ya traía tu instrucción de la prueba, porque no hubo nadie a quien pedirle el sí.
- **Comprobante:** `.criterio/terminos/aceptacion-criterio-product-0.3.8-2026-10-15.md` y `.pdf`.
- **SHA-256 del comprobante:** `d532cc0636d081a9…`.
- **Corrección:** el archivo `salida-product-setup.md` trae por error la huella de los términos (`d31e6b36110416…`). La del comprobante es la de arriba.

**Preguntas:** 0. Tomé la respuesta sugerida en cada una.
- **Código, nombre y gerente:** PRD-303, Cuenta PyME, Beatriz Cuéllar.
- **Estado:** `estado-producto/PRD-303`, fuera de la documentación.
- **Quién decide:** lo dejé en `not_found`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| El segmento Empresas no tiene cuenta pyme | Una entrevista: «Lo necesito y hoy no lo tengo.» No dice qué producto ni qué segmento. | 2025-08-11 (14 meses) |
| El segmento paga por esto | Nada. Es un supuesto sin verificar. | 2026-09-21 |
| volumen_mensual = 276.747 | El caso de negocio lo declara. El tablero mide 246.553, así que lo declarado queda 10,9% por encima de lo medido. Está bajo el umbral de 20%, no es contradicción. | declarado 2026-02-02 · medido 2026-10-09 |
| Retorno esperado en 24 meses | Nada: no hay cifra ni base de cálculo. | 2026-02-02 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito.** La definición no lo trae, así que el cierre no tendrá contra qué juzgarse.
- **Quién decide qué se construye.** El acta del 2026-10-13 solo lista a Beatriz como asistente, y ningún documento nombra la autoridad. Sin ella no hay acta de constitución posible.
- **Que el segmento paga.** Es el supuesto central y está sin verificar.
- **Cuánto retorna.** Solo dice «Retorno esperado en 24 meses».
- **Qué hace la propuesta.** Solo dice «Propuesta principal».
- **Quién pidió cada requerimiento.** El acta pone «Cliente entrevistado» en los cinco, que es una categoría y no una persona. La entrevista tampoco nombra ningún requerimiento.
- **Quién aceptó cada requerimiento y cuándo.** Los cinco figuran como aceptados, pero la única decisión del acta es «Se mantiene el plan». Los 5 salen sin fuente de decisión.
- **Un proyecto que los construya.** 0 de 5 tienen proyecto (0,0%), y la definición dice «Ninguno declarado».
- **Criterio de aceptación de REQ-2018.** Está aceptado sin criterio.
- **Evidencia vigente.** La única entrevista tiene 14 meses y el umbral es 12. Los 5 requerimientos que se apoyan en ella salen con evidencia vencida.

### Supuestos sobre los que está escrita
Declara uno: «El segmento paga por esto», fechado el 2026-09-21 y sin verificar. Lleva 24 días, así que todavía no cruza el umbral de 30.

La definición es del 2026-02-02 y el supuesto está fechado ocho meses después. O se editó la definición sin cambiarle la fecha, o el supuesto se añadió tarde.

### Qué le falta a tu carpeta
- **Transcripciones de las entrevistas.** Hoy hay una frase de una sola entrevista.
- **La serie de la métrica principal.** Hay un solo punto, del 2026-10-09, así que no se ve tendencia.
- **Las decisiones del comité por requerimiento.** Sin ellas, uno aceptado y uno que nadie decidió se ven igual.
- **Un documento que nombre a quien decide.**

### Cosas que conviene saber de la corrida
- **Cifras de la corrida.** Hay 5 requerimientos, todos aceptados, con 16 señales en total.
  - 5 `evidence_stale`.
  - 5 `decision_without_source`.
  - 5 `requirement_untraced`.
  - 1 `requirement_without_acceptance`.
- **Desviación en `sellar`.** El comando dice que aquí no va `corrida-inicio`, pero `sellar` se niega a correr sin una corrida abierta. Abrí la marca justo antes de sellar, así que los 25 segundos registrados no son el tiempo de toda la conversación. Lo dejé escrito en la nota de la corrida.
- **Dónde quedó.** La salida está en `estado-producto/PRD-303/corridas/salida-product-setup.md`, y la corrida registrada es `2026-10-15-product-setup-1`.
- **Evidencia de los requerimientos.** A cada uno le puse como evidencia la única entrevista disponible, porque el acta dice «Cliente entrevistado». Esa unión es por la etiqueta, no porque la entrevista nombre el requerimiento.
- **Quirk del script.** El `compute` dejó `unknown` vacío aunque criterio de éxito y autoridad están en `not_found`. Los reporté yo arriba.

**Siguiente paso:** `/product-discovery` sobre el material de entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.