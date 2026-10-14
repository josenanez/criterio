# /criterio-product:product-setup documentos/productos/PRD-303

## Listo — Gemelo digital (PRD-303)

**Lo que miré:** 5 documentos, y solo uno es de descubrimiento: una ronda de entrevistas del 2026-08-31 con una sola cita. También leí la definición del 2025-12-09, el tablero del 2026-10-12 y el acta del comité del 2026-10-10. Pude leer todo. No hay transcripciones, tickets ni encuestas.

**Configuración:** no hubo nadie a quien preguntar, así que tomé las respuestas sugeridas en las cuatro preguntas.
- **Producto y gerente:** Gemelo digital (PRD-303), gerente Camilo Beltrán, tomado del caso de negocio.
- **Quién decide:** Comité de producto. Es una propuesta mía, porque ningún documento dice quién decide.
- **Dónde guardo lo que encuentre:** `estado/`, hermana de `documentos/` y fuera de la carpeta de documentación.
- **Términos:** TERMS.md v1.0 aceptado por José Francisco Ñáñez el 2026-10-14.
- **Archivo:** quedó en `.criterio/producto/PRD-303/config.json`. La ruta de fichas (`estado/fichas`) es provisional, y dejé sin fecha el próximo comité.

**Lo que tu definición afirma, y qué lo sostiene**

| Afirmación | Sostenida por |
|---|---|
| Gerencia no tiene gemelo digital | Una cita anónima de un cliente, sin segmento: «Lo necesito y hoy no lo tengo» (2026-08-31) |
| Volumen mensual 198.346 | Solo el propio caso de negocio. El tablero mide 179.966, por debajo de lo declarado |
| La red de la mina soporta el volumen | Solo su etiqueta «verificado». No hay prueba de esa verificación en la carpeta |

**Lo que no está dicho en ninguna parte**
- **Propuesta:** la definición dice solo «Propuesta principal».
- **Cliente:** no se nombra persona, empresa ni rol dentro de Gerencia.
- **Éxito:** no hay criterio de éxito.
- **Volumen:** no se explica cómo se calculó 198.346.
- **Retorno:** «Retorno esperado en 24 meses» no trae monto ni fuente.
- **Autoridad:** el acta solo lista a Camilo Beltrán como asistente y no dice quién decide.
- **Plan:** la decisión del comité es «Se mantiene el plan», y en la carpeta no hay ningún plan.
- **Requerimientos aceptados sin sustento:** REQ-1032 no tiene quién lo pidió. REQ-2026 no tiene ni quién lo pidió ni criterio de aceptación.
- **Proyectos:** los 6 requerimientos del acta están aceptados y ninguno tiene proyecto que lo construya.

**Supuestos:** la definición declara uno, el de la red. Dice «declarado el 2026-06-11», seis meses después de la definición. No declara los demás de los que depende, como que Gerencia es el segmento o que el retorno llega en 24 meses.

**Cifras:** no calculé la brecha entre 198.346 y 179.966, porque el script no la da. El registro de métricas y de requerimientos está vacío y `compute` devolvió cero requerimientos. Armé un snapshot desde los documentos y siguió vacío. No lo llené a mano. Cuando la serie esté registrada, la brecha sale del script y se compara con el umbral de 20 % configurado.

**Qué le falta a tu carpeta**
- Las transcripciones de las entrevistas.
- La serie de la métrica principal con su fuente: hoy hay un solo punto.
- Las decisiones del comité con su motivo.
- El plan que el comité mantiene.

**Siguiente paso:** `/product-discovery` sobre las entrevistas. Ahí los temas se vuelven requerimientos con la cita de quién los pidió, y se llena el registro que hoy está vacío.

**Aviso:** esto es un borrador de trabajo, no asesoría ni certificación. Verifícalo antes de decidir con él, porque Alba solo conoce lo que está en los documentos.

**Registro de la corrida:** el texto completo quedó en `estado/corridas/salida-product-setup.md` y la corrida en `2026-10-14-product-setup-1`. El script la registró con `producto: "?"`, `requerimientos: 0` y `segundos: null`, porque el estado está vacío y este comando no lleva `corrida-inicio`. El código PRD-303 sí quedó en el registro.