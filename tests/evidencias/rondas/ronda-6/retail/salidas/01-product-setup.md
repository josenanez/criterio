# /criterio-product:product-setup documentos/productos/PRD-302

## Listo: Autopago en tienda (PRD-302)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

**Lo que miré:** 5 documentos, y todos se pudieron leer. Hay una sola entrevista (2026-05-28), el tablero de métricas (2026-10-11), la definición y el caso de negocio (2025-10-25) y el acta del comité de producto (2026-10-10). El material de descubrimiento es escaso: una entrevista con una sola cita.

**Términos:** los acepté para la versión 0.3.12 (términos 1.1) a nombre de José Francisco Ñáñez, con fecha 2026-10-16, como indicaba la prueba. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.12-2026-10-16.md` y `.pdf`. El SHA-256 empieza por bbc944aafa669a50…

**Respuestas por defecto:**
- Gerente de producto: Elena Duarte.
- Quien decide: el Comité de producto. Ningún documento nombra a una persona.
- Estado guardado en `estado-producto/PRD-302`, separado de `estado/`.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| Pequeños negocios no tiene autopago | Nada directo. La entrevista dice «Lo necesito y hoy no lo tengo», pero no nombra el segmento ni el autopago | 2026-05-28 |
| `volumen_mensual` = 107.018 | El tablero mide 107.348, una diferencia de 0,3 % (el umbral es 20 %) | caso de negocio 2025-10-25; tablero 2026-10-11 |
| La regulación de datos lo permite | Un supuesto que el documento marca «verificado» sin citar con qué | 2026-08-20 |
| 12 requerimientos aceptados | 8 citan la misma entrevista y 4 no citan ninguna | acta 2026-10-10 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito.** La definición no lo trae.
- **Qué mide `volumen_mensual`.** Ningún documento lo define, y el problema dice que el segmento no tiene autopago.
- **Retorno.** El caso de negocio dice «Retorno esperado en 24 meses» sin cifra ni fuente.
- **Propuesta.** Dice solo «Propuesta principal».
- **Proyectos.** Ninguno declarado, y los 12 requerimientos aceptados tienen «—» como proyecto que los ejecuta.
- **Verificación de la regulación.** No se dice con qué se verificó.
- **Cuatro aceptados sin demanda citada:** REQ-2028, REQ-4203, REQ-4207 y REQ-4209.
- **Tres aceptados sin criterio de aceptación:** REQ-4204, REQ-4208 y REQ-4210.
- **Dos sin doliente:** REQ-4207 y REQ-4209.
- **Tres propuestos sin decidir hace más de 60 días:** REQ-4201 (135 días), REQ-4206 (130) y REQ-4213 (125).

### Supuestos sobre los que está escrita
Hay uno declarado: «La regulación de datos lo permite» (2026-08-20). Pasaron 57 días y no tiene cita que lo verifique, así que lo conté como no verificado.

### Qué le falta a tu carpeta
- Las transcripciones completas de las entrevistas. El acta atribuye 11 requerimientos a «Cliente entrevistado», pero la entrevista no nombra ninguno.
- La definición de la métrica y su serie con fuente. Hay un solo punto medido.
- Los títulos y el problema de cada requerimiento. El acta los llama «Requerimiento REQ-42xx».
- El criterio de éxito y el retorno con cifra.
- Confirmar que REQ-2028 es de este producto, porque tiene otro prefijo.
- Quién decidió cada estado y cuándo. Registré la fecha del acta, 2026-10-10.

**Registrado en `estado-producto/PRD-302`:** la ficha del producto, 15 requerimientos (12 aceptados y 3 propuestos) y la serie de la métrica, con la lectura sellada. La configuración está en `.criterio/producto/PRD-302/config.json`. La corrida quedó como `2026-10-16-product-setup-1`, con la salida completa en `corridas/salida-product-setup.md`. Hizo 25 hallazgos en 24 segundos, sin preguntas a la persona.

**Dos desvíos que conviene saber:**
- `sellar` exige una corrida abierta, así que usé `corrida-inicio` y reescribí la ficha antes de sellar. El comando decía que aquí no iba.
- Dejé el supuesto regulatorio como no verificado aunque el documento diga «verificado», porque no cita nada.

**Después:** te ofrezco `/product-discovery` sobre el material de entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.