# /criterio-product:product-setup documentos/productos/PRD-301

## Listo — Alerta de taludes (PRD-301)

**Lo que miré:** 5 documentos, de los cuales 1 es de descubrimiento (una entrevista del 2025-10-06). Leí la definición del 2026-06-01 completa. Lo más reciente es el acta del comité del 2026-10-12.

**Términos:** quedaron aceptados para la versión 0.3.12 (términos 1.1) a nombre de José Francisco Ñáñez, con fecha 2026-10-16. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-product-0.3.12-2026-10-16.md` y `.pdf`. El SHA-256 del .md empieza por bbc944aafa669a50 y el del .pdf por 089f4fb48989f62f.

**Preguntas:** no hice ninguna, porque nadie podía responder. Tomé la respuesta sugerida en cada una:
- **Producto y gerente:** Alerta de taludes, Mauricio Pérez, tal como salen de la definición.
- **Quién decide:** «Comité de producto». El acta no lo dice, así que esto hay que confirmarlo.
- **Dónde guardo el estado:** `estado-producto/PRD-301`, no la carpeta `estado/` de otro agente.
- **Términos:** usé el sí que venía en la instrucción de la prueba.

### Lo que tu definición afirma, y qué lo sostiene
| Afirmación | Sostenida por | De cuándo |
|---|---|---|
| «El segmento Mantenimiento no tiene alerta de taludes» | Una sola entrevista: «Lo necesito y hoy no lo tengo». El cliente no tiene nombre y no dice segmento ni qué necesita. | 2025-10-06, hace 12 meses |
| Volumen mensual de 169.380 | Lo declara el caso de negocio. El tablero mide 106.047, un 37,4 % por debajo de lo declarado. | Caso 2026-06-01; medición 2026-10-08 |
| «El proveedor cumple el tiempo pactado» | Es un supuesto sin verificar desde hace 54 días. No dice qué proveedor ni qué tiempo. | 2026-08-23 |
| Retorno esperado en 24 meses | Nada: no hay cifra, cálculo ni fuente. | — |

### Lo que no está dicho en ninguna parte
- **Criterio de éxito:** ningún documento lo escribe.
- **Qué se propone:** la definición dice «Propuesta principal» y nada más.
- **Cuánto retorna:** «Retorno esperado en 24 meses» no trae monto.
- **Qué problema resuelve cada requerimiento:** el acta nombra REQ-4100 a REQ-4113 sin describirlos.
- **Quién decidió:** el acta solo lista a Mauricio Pérez como asistente. La única decisión escrita es «Se mantiene el plan».
- **Qué proyecto construye algo:** la definición dice «Ninguno declarado» y los 14 requerimientos tienen «—».

### Registro de requerimientos (14: 13 aceptados, 1 propuesto)
- **Sin proyecto:** los 13 aceptados no tienen proyecto que los ejecute.
- **Sin evidencia de demanda:** 6 aceptados (REQ-4100, 4102, 4103, 4104, 4108, 4113).
- **Evidencia vieja:** 7 requerimientos (53,8 % del registro) se apoyan en la misma entrevista de hace 12 meses. Esa entrevista no nombra ninguno; el acta solo dice «Cliente entrevistado».
- **Sin doliente:** 5 figuran «sin asignar» (REQ-4106, 4107, 4108, 4109, 4113).
- **Sin criterio de aceptación:** 1 aceptado (REQ-4105).
- **Sin decidir:** 1 propuesto lleva 167 días (REQ-4111, desde 2026-05-02).
- **Una sola persona en todo:** Mauricio Pérez es el gerente, autor del caso de negocio, entrevistador, único asistente al comité y doliente de REQ-4110.

### Supuestos sobre los que está escrita
La definición declara uno solo: «El proveedor cumple el tiempo pactado» (2026-08-23, sin verificar, 54 días). El volumen y el retorno también son supuestos, pero no están declarados como tales.

### Qué le falta a tu carpeta
- Las transcripciones completas de las entrevistas. Hay una sola, de tres líneas.
- Una serie de la métrica: hay un único punto medido, sin historia para ver si 106.047 sube o baja.
- Las decisiones del comité con quién decidió y por qué. Sin ellas, un requerimiento descartado se ve igual que uno que nadie miró.
- Una métrica para el retorno, porque nadie lo está midiendo.

**Siguiente paso:** `/product-discovery` sobre el material de entrevistas, para convertir los temas en requerimientos con la cita de quién los pidió.

### Nota sobre el proceso
`sellar` falló al principio porque exige una corrida abierta y una ficha escrita dentro de ella. Abrí la corrida con `corrida-inicio`, aunque el comando dice que aquí no va, y reescribí la ficha dentro de esa corrida. El sellado quedó bien, con 5 documentos vistos.

La corrida quedó registrada como `2026-10-16-product-setup-1` y el texto completo está en `estado-producto/PRD-301/corridas/salida-product-setup.md`. La configuración está en `.criterio/producto/PRD-301/config.json` y el comando `config` la verificó.