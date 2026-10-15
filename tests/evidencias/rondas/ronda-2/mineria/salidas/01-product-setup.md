# /criterio-product:product-setup documentos/productos/PRD-300

## Listo — Monitoreo de flota (PRD-300)

Soy Alba. Trabajo antes de que haya proyecto: miro qué sostiene tu definición y qué se sostiene solo.

Nadie podía responder, así que no hice preguntas y tomé la respuesta sugerida en cada una:
- **Producto y gerente:** PRD-300 «Monitoreo de flota», Beatriz Cuéllar, como dice la definición.
- **Quién decide qué se construye:** ningún documento lo dice, así que queda sin dato.
- **Dónde guardo el estado:** `estado-producto/PRD-300`, fuera de la documentación.
- **Términos:** aceptados por José Francisco Ñáñez, como indicaste. Los mostré tal cual antes de registrarlos.

**Lo que miré:** 5 documentos, y se pudieron leer todos. Solo 1 es de descubrimiento: una entrevista del 2025-09-28. La definición y el caso de negocio son del 2026-02-02. Lo más reciente es el acta del comité del 2026-10-11.

**Términos:** aceptados para la versión 1.1 (familia 0.3.8). El comprobante está en `.criterio/terminos/aceptacion-criterio-product-0.3.8-2026-10-15.md` y `.pdf`. SHA-256 del `.md`: d532cc0636d081a9…

Levanté la ficha del producto y los 4 requerimientos que nombra el acta del comité (REQ-1000, REQ-1001, REQ-1002, REQ-2017), solo con lo escrito. La configuración quedó en `.criterio/producto/PRD-300/config.json` y la verifiqué sin faltantes.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Gerencia no tiene monitoreo de flota» | Una sola cita: «Lo necesito y hoy no lo tengo». El cliente no tiene nombre y no dice que sea de Gerencia | 2025-09-28 |
| Volumen mensual de 164.808 | Nada. El tablero mide 102.629; el declarado está 37,7 % por encima | 2026-02-02 (caso de negocio) contra 2026-09-28 (tablero) |
| «El ahorro se sostiene sin inversión adicional» | Es un supuesto sin verificar, con 131 días | 2026-06-06 |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** la definición no trae ninguno.
- **Propuesta principal:** el título está y no hay texto debajo.
- **Retorno en 24 meses:** no hay cifra, base ni fuente.
- **Ahorro:** ningún documento da una cifra.
- **Autoridad:** nadie dice quién decide qué se construye. El acta solo lista a Beatriz Cuéllar como asistente.
- **Quién aceptó los 4 requerimientos y cuándo:** el acta dice «aceptado» con una fecha «desde» y «Se mantiene el plan». No hay decisión escrita ni quién decidió.
- **Qué necesita cada requerimiento:** los cuatro son un número y el nombre «Requerimiento REQ-xxxx». Ninguno dice el problema que resuelve.
- **REQ-2017 (Natalia Ospina):** nadie lo pidió según el acta, y está aceptado sin evidencia de demanda.
- **Proyecto que lo construye:** ninguno, para los 4. La definición dice «Ninguno declarado» y el acta tiene «—» en todos.

### Supuestos sobre los que está escrita
Declara uno: «El ahorro se sostiene sin inversión adicional», del 2026-06-06, sin verificar. No declara ningún otro.

### Lo que dicen las cifras
- **Evidencia de demanda:** 3 de 4 requerimientos aceptados (75,0 %) tienen una cita. Es la misma en los tres, de «Cliente entrevistado», con 12 meses de antigüedad. La entrevista no nombra ningún requerimiento; el vínculo viene solo del acta.
- **Criterio de aceptación:** los 4 dicen «se verifica en producción», que no se puede medir.
- **Con proyecto que los ejecute:** 0 de 4 (0,0 %).
- **Métricas:** `volumen_mensual` es la única a la vista, y es la que contradice al caso de negocio.

### Qué le falta a tu carpeta
Como hallazgo, no como requisito:
- **Transcripciones de las entrevistas:** hay una sola cita, de una persona sin nombre.
- **Serie de `volumen_mensual`:** hay un solo punto, el del 2026-09-28. Con una serie se vería si la brecha se cierra o se abre.
- **Decisiones del comité de producto:** con quién decidió y por qué. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.
- **Medición de retorno y ahorro:** no hay cifra ni medición.

Siguiente paso: `/product-discovery` sobre el material de entrevistas, para que los temas se vuelvan requerimientos con la cita de quién lo pidió.

La corrida quedó registrada como `2026-10-15-product-setup-1`. Tardó 26 segundos y dejó 14 hallazgos. El texto completo está en `estado-producto/PRD-300/corridas/salida-product-setup.md`.

**Detalles de la ejecución:**
- **`corrida-inicio` antes de los términos:** lo corrí antes de aceptarlos y no marcó. Tras la aceptación lo repetí y marcó.
- **Segunda escritura de la ficha:** `sellar` rechazó la ficha porque la había escrito antes de abrir la corrida. La reescribí dentro de la corrida y selló con 5 documentos vistos.
- **Entrevista y requerimientos:** guardé la cita de la entrevista como evidencia de los tres requerimientos que el acta atribuye a «Cliente entrevistado», y lo anoté en el campo.