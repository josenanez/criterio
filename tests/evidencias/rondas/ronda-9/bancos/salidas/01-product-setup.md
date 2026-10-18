# /criterio-product:product-setup documentos/productos/PRD-307

## Listo — Remesas familiares (PRD-307)

**Lo que miré:** 6 documentos, y solo 1 es de descubrimiento: las entrevistas del 2025-10-10, un solo cliente y un solo tema. La definición y el caso de negocio son del 2025-10-02. Lo más reciente es del 2026-10-16 (acta del comité y tablero). Los puedo leer todos.

**Términos:** José Francisco Ñáñez aceptó la versión 1.1 el 2026-10-17. El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.4.0-2026-10-17.md` y `.pdf`. SHA-256: 38ea1d146bbd84f3…

**Quién decide:** el Comité de producto, que fue la respuesta sugerida. Ningún documento lo dice, y el acta del 2026-10-16 solo registra a Felipe Arango como asistente.

**Dónde guardo lo que encuentro:** `estado-producto/PRD-307`, hermana de la documentación. No toqué `estado/`, que es del portafolio.

**Preguntas:** hice 0. Tomé la respuesta sugerida en cada una y los términos con el sí que trae la sesión de prueba.

### Lo que tu definición afirma, y qué lo sostiene

| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Microcomercio no tiene remesas familiares» | Una entrevista: «Lo necesito y hoy no lo tengo». No dice a qué segmento pertenece el cliente. | 2025-10-10 (12 meses) |
| Volumen mensual de 108.635 | Solo el propio caso de negocio, que se cita a sí mismo. El tablero mide 76.086 (corte 2026-10-16), así que el caso está **30,0 % por encima**. | 2025-10-02 |
| «La regulación vigente lo permite» | Un supuesto marcado como verificado con la medición del piloto. Esa medición no dice qué permite la norma, y no hay concepto jurídico citado. | 2026-08-31 / 2026-09-11 |
| «Retorno esperado en 24 meses» | Nada: no trae cifra. | 2025-10-02 |

### Lo que no está dicho en ninguna parte
- **El criterio de éxito.** Ni la definición ni el caso de negocio lo escriben.
- **De dónde sale el 108.635,** ni qué cuenta exactamente el «volumen mensual».
- **Cuánto es el retorno** ni contra qué inversión.
- **Qué demanda hay en Microcomercio.** Hay una cita de un cliente, sin segmento, sin tamaño y sin relación con ningún requerimiento en particular.
- **La medición del piloto del 2026-09-11.** Se cita como prueba, pero no está en la carpeta.
- **Qué dice la regulación.** No hay ninguna norma ni concepto jurídico.
- **Quién decidió cada requerimiento aceptado.** El acta solo dice «Se mantiene el plan».
- **Ningún proyecto ejecuta nada.** La definición dice «Ninguno declarado» y el acta pone «—» en los 16 requerimientos. Nadie está construyendo los 9 aceptados, al menos por escrito.

Sobre el registro de requerimientos (16: 9 aceptados, 7 propuestos):
- **5 aceptados sin nadie que los haya pedido:** REQ-4702, 4703, 4706, 4707 y 4713.
- **Los otros 4 aceptados** (4705, 4709, 4711, 4714) se apoyan en la misma entrevista de hace 12 meses. En total, 10 requerimientos tienen evidencia envejecida, y ningún aceptado tiene demanda vigente.
- **2 aceptados sin criterio de aceptación:** REQ-4702 y 4705. En los demás el criterio es la misma frase, «se verifica en producción», que no permite decir cuándo quedó hecho.
- **2 sin doliente:** REQ-4708 y REQ-4714, este último ya aceptado.
- **Los 7 propuestos llevan más de 60 días sin decidirse.** El más viejo, REQ-4700, lleva 205 días.

### Supuestos sobre los que está escrita
La definición declara un solo supuesto: «La regulación vigente lo permite». Está marcado como verificado, pero con una medición que no corresponde a lo que afirma. La definición está fechada el 2025-10-02 y trae un supuesto declarado el 2026-08-31, así que se editó después y la fecha no se actualizó. Lo que sostiene el volumen y el retorno ni siquiera está dicho como supuesto.

### Qué le falta a tu carpeta
- Las **transcripciones** de las entrevistas. Hay una sola, resumida en una cita, y no nombra ningún requerimiento.
- La **serie de la métrica principal.** El tablero trae un único punto (2026-10-16), así que no se ve tendencia. Tampoco hay ninguna medición anterior a esa fecha que contraste lo que afirmó el caso de negocio.
- La **medición del piloto** del 2026-09-11 y el soporte regulatorio del supuesto.
- Las **decisiones del comité por requerimiento,** con quién las tomó y por qué. Hoy un requerimiento descartado se vería igual que uno que nadie miró.

**Lo que no pude hacer:** sellar la lectura. `sellar` falló con «no hay una corrida abierta: sellar va después de corrida-inicio», y este comando dice que aquí no va `corrida-inicio`. No lo forcé. La ficha del producto y los 16 registros sí quedaron escritos.

**Siguiente paso:** `/product-discovery` sobre el material de entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién los pidió.

La corrida quedó registrada como `2026-10-17-product-setup-1`. La salida completa está en `estado-producto/PRD-307/corridas/salida-product-setup.md`.