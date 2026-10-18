# /criterio-product:product-setup documentos/productos/PRD-309

## Listo — Tarjeta de la tienda (PRD-309)

**Lo que miré:** había 6 documentos del producto. Uno es de descubrimiento: una sola entrevista, del 2025-10-12. También hay una definición y un caso de negocio, ambos del 2026-02-23, un tablero de métricas y el acta del comité del 2026-10-11, que es lo más reciente. Pude leer todos los formatos. No hay transcripciones: solo una frase de la entrevista.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.4.0 (términos 1.1), el 2026-10-17. Tomé esa aceptación de tu instrucción. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.4.0-2026-10-17.md` y `.pdf`, con SHA-256 `38ea1d146bbd84f3…`.

**Configuración:** `.criterio/producto/PRD-309/config.json`, verificada (`ok`). El estado está en `estado-producto/PRD-309`, no en `estado/`, que es la carpeta del portafolio. Decide el Comité de producto. Es la respuesta sugerida: ningún documento dice quién decide. El acta solo lista como asistente a Ricardo Salas.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Hogares no tiene tarjeta de la tienda» | Una entrevista a un «cliente entrevistado»: «Lo necesito y hoy no lo tengo.» No dice quién es y no nombra Hogares ni la tarjeta, así que la sostiene poco. | 2025-10-12 (12 meses) |
| volumen_mensual = 278.242 | Solo el caso de negocio, que no dice cómo se calculó. El tablero mide 214.637 al corte 2026-10-09, así que el caso queda 22,9 % por encima de lo medido. | caso 2026-02-23; medición 2026-10-09 |
| «El cliente paga por la entrega rápida» | Un supuesto sin verificar desde hace 31 días. | declarado 2026-09-16 |
| «Retorno esperado en 24 meses» | Nada: hay un plazo, no una cifra. | 2026-02-23 |

### Lo que no está dicho en ninguna parte
- **La propuesta:** la definición solo dice «Propuesta principal».
- **El criterio de éxito.**
- **La cifra del retorno esperado.**
- **Cómo se calculó el volumen de 278.242** y qué cuenta el tablero como volumen.
- **Cuántos hogares son el segmento** y qué evidencia hay de que quieran la tarjeta.
- **Qué relación tiene la entrega rápida con una tarjeta de la tienda.**
- **Qué es cada uno de los 15 requerimientos:** el acta solo los lista por número.
- **Quién decidió cada aceptación:** el acta registra solo «Se mantiene el plan».
- **Qué proyecto construye algo de esto:** la definición dice «Ninguno declarado».

### Supuestos sobre los que está escrita
Declara uno: «El cliente paga por la entrega rápida», sin verificar. Está fechado el 2026-09-16 dentro de una definición fechada el 2026-02-23. Eso indica que la definición se editó después sin cambiar su encabezado.

### Registro de requerimientos
El acta del 2026-10-11 lista 15 requerimientos: 13 aceptados y 2 propuestos. 11 tienen evidencia de demanda (84,6 %) y ninguno tiene proyecto que lo ejecute (0,0 %). Las señales salen de `compute`:

| Señal | Cuántos | Cuáles |
|---|---|---|
| Evidencia envejecida (12 meses) | 13 | Todos los que citan al «cliente entrevistado». |
| Aceptado sin proyecto | 13 | Todos los aceptados. |
| Aceptado sin criterio de aceptación | 4 | REQ-4901, REQ-4907, REQ-4909, REQ-4913 |
| Aceptado sin evidencia de demanda | 2 | REQ-4901, REQ-4912 |
| Propuesto sin decidir | 2 | REQ-4905 (161 días), REQ-4908 (179 días) |

Los 11 requerimientos con evidencia citan la misma entrevista, de una frase genérica. La demanda es una voz, no once. REQ-4907 lo pidió su propio dueño, Ricardo Salas, y REQ-2035 sigue otra numeración que los demás (REQ-49xx).

### Qué le falta a tu carpeta
- Las transcripciones de las entrevistas, con quién habló y de qué producto.
- Una serie de la métrica principal con fuente y definición. Hoy hay un solo punto.
- Las decisiones del comité con su razón. Con «Se mantiene el plan», un requerimiento descartado se ve igual que uno que nadie miró.
- Un proyecto declarado para este producto.

### Para tener en cuenta
- **Preguntas:** no le hice ninguna a una persona. Contesté las cuatro con la respuesta sugerida.
- **Orden de los comandos:** `sellar` exigió abrir una corrida con `corrida-inicio` y que `producto.json` se escribiera después. El comando dice que aquí no va `corrida-inicio`, pero sin él no sellaba. Lo abrí y reescribí la ficha.
- **Conteo de documentos:** `sellar` reportó 5 documentos vistos y yo conté 6. No investigué la diferencia.
- **Tiempo:** `corrida` midió 28 segundos, de `corrida-inicio` a `corrida`.
- **Corrida registrada:** `2026-10-17-product-setup-1`. La salida completa está en `estado-producto/PRD-309/corridas/salida-product-setup.md`.

Sigue `/product-discovery` sobre las entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.