# /criterio-product:product-spec 

> **Borrador de trabajo, no una especificación aprobada.** Lo escribe el agente; lo cierra Natalia Ospina (gerente de producto) y aprueba el Comité de producto. Este agente no puede dar esa firma.

# Especificación — Alerta de taludes (PRD-301) · borrador del 2026-10-17

**Resultado en una línea:** el registro permite listar el alcance por identificador, pero **no permite escribir el comportamiento de ningún requerimiento**. Los 17 llevan por título «Requerimiento REQ-xxxx» y ninguno tiene el problema (`need`) escrito. Inventarlo sería rellenar el hueco con lo razonable, así que la sección de comportamiento queda vacía a propósito.

## Qué problema resuelve

«El segmento Comunidad no tiene alerta de taludes.» (`00-definicion/2026-06-09-definicion-producto.docx`, 2026-06-09). Es todo lo que la definición dice. La «Propuesta principal» es un encabezado sin texto, y no hay criterio de éxito del producto en ninguna parte.

## Alcance

### Entra (provisional, solo por identificador)
Los 12 requerimientos en estado `aceptado`, según el acta del Comité de producto del 2026-10-09 (`30-decisiones/2026-10-09-comite-producto.docx`): REQ-2030, REQ-4100, REQ-4101, REQ-4104, REQ-4105, REQ-4106, REQ-4107, REQ-4108, REQ-4109, REQ-4111, REQ-4113, REQ-4114.

Ninguno dice qué es. Que «entren» significa que el comité los aceptó, no que se sepa qué se construye.

### No entra
- **Los 5 en estado `propuesto`**, que nadie ha decidido: REQ-4102 (Javier Hoyos), REQ-4103 (Jorge Medina), REQ-4110 (Óscar Ramírez), REQ-4112 (Liliana Torres), REQ-4115 (Diana Molina). Especificarlos sería escribir el documento dos veces.
- **Todo lo que no está en el registro.** La definición no declara canal de alerta, umbrales, zonas, destinatarios ni integración con la operación de la mina. No se proponen aquí porque serían decisiones de diseño.
- Diseño técnico, estimación de esfuerzo, costo y fechas: no son de este documento.

## Comportamiento

**No redactado.** Ninguno de los 12 requerimientos aceptados tiene `need` ni título descriptivo en el registro (`need: not_found` en los 12). Una sección de comportamiento escrita hoy saldría de mi redacción, no del registro, y no se podría rastrear a ninguna fuente. Se redacta cuando cada doliente diga qué problema resuelve su requerimiento.

## Criterios de aceptación

| Criterio | Requerimiento | Cómo se verifica | ¿Se puede medir hoy? |
|---|---|---|---|
| «se verifica en producción» (acta, 2026-10-09) | REQ-2030, REQ-4100, REQ-4106, REQ-4108, REQ-4111, REQ-4113 | **No es verificable.** Dos personas no llegan a la misma respuesta, porque no dice qué se observa ni con qué umbral. Es un lugar, no un criterio | No. No hay magnitud que medir |
| *(ninguno escrito)* | REQ-4101, REQ-4104, REQ-4105, REQ-4107, REQ-4109, REQ-4114 | — | — |

Hallazgo: **de los 12 aceptados, 6 no tienen criterio y 6 tienen uno que no pasa la prueba de verificabilidad. Ninguno es verificable hoy.** No propongo cifras de latencia, cobertura o tasa de falsos positivos, porque esos números los fija quien decide el riesgo aceptable de una alerta de taludes.

## Supuestos sobre los que está escrita

| Supuesto | Verificado | Quién lo verificaría |
|---|---|---|
| «La red de la mina soporta el volumen» (definición; declarado el 2026-08-20, sin verificar). El documento lleva fecha 2026-06-09 y el supuesto otra posterior, así que se editó después de su fecha | No, y lleva más de 30 días sin verificar (umbral configurado: 30) | Sin dueño en los documentos. Propongo a Natalia Ospina que asigne a quien opere la red de la mina |
| El «volumen mensual» de 191.637 es la base del caso (`2026-06-09-caso-de-negocio.md`). Sin unidad ni medición: la fuente que cita es el propio caso de negocio | No hay serie medida que lo contraste | Natalia Ospina (autora del caso) |
| Que la entrevista del 2025-08-30 («Lo necesito y hoy no lo tengo») represente la demanda de los 12 requerimientos aceptados | No. La entrevista no nombra ningún requerimiento | Natalia Ospina (realizó la entrevista) |

## Vacíos

| Qué falta decidir | Consecuencia de no decidirlo | Quién lo cierra |
|---|---|---|
| Qué es cada requerimiento (problema en palabras del doliente), los 12 aceptados | No se puede escribir comportamiento ni criterio; el equipo construiría lo que entienda | Cada doliente (ver tabla final) y Natalia Ospina |
| Criterio de aceptación verificable en los 12 (6 sin criterio, 6 con «se verifica en producción») | La discusión de «¿quedó bien?» ocurre después de construir | Cada doliente, con Natalia Ospina |
| Doliente de REQ-4100 («sin asignar» en el acta) | Un requerimiento aceptado sin persona que responda por él | Comité de producto |
| Proyecto que ejecuta cada requerimiento: el acta pone «—» en los 17; la definición dice «Ninguno declarado» | REQ-4105 está aceptado desde 2026-03-30 y sin proyecto a 2026-10-17; nada de esto se construye hasta el acta de constitución | Natalia Ospina / Comité de producto |
| Qué significa «Se mantiene el plan» (única decisión del acta del 2026-10-09): no hay plan en la carpeta | Una decisión que nadie puede rastrear | Natalia Ospina |
| Qué quiere decir exactamente el éxito del producto: la definición no lo trae | No hay forma de saber si el producto, en conjunto, funcionó | Natalia Ospina |
| Casos borde, sin ninguna definición en el registro: qué pasa si no hay conexión o la red de la mina cae, si la alerta no llega, si hay una falsa alarma, si hay alerta duplicada, o quién es responsable de actuar al recibirla | En un producto de alerta de seguridad, el caso borde es el caso importante. No lo relleno | Natalia Ospina con quien opere la mina |
| Lo que otro equipo debe hacer: la definición supone red de la mina y datos de taludes (origen sin declarar). No hay acuerdo escrito con ningún equipo | Dependencias no acordadas | Natalia Ospina |
| Obligaciones normativas (abajo) | Se descubren con el producto construido | Revisión jurídica de la organización |
| Demanda: la única evidencia es una entrevista del 2025-08-30 con 13,5 meses (umbral: 12), de un «Cliente entrevistado» sin nombre, y se repite sin cambio en 14 de los 17 registros. REQ-2030 y REQ-4108 no tienen evidencia alguna | Aceptados sobre una demanda que no se puede rastrear ni está vigente | Natalia Ospina |
| Aceptados «desde» antes de la definición: REQ-4105 (2026-03-30), REQ-4111 (2026-06-07) y REQ-4114 (2026-06-06) llevan fecha de aceptación anterior a la definición (2026-06-09) | O la definición no es la primera, o las fechas del acta no son las de la decisión | Comité de producto |

### Barrido normativo (primer barrido, sin dictamen de cumplimiento)

| Qué toca la definición | País | Obligación | Norma citada | Estado |
|---|---|---|---|---|
| Alertar a una comunidad: es probable que haya datos de contacto o ubicación de personas, pero **la definición no dice qué dato recoge** | No declarado en ningún documento | Posible tratamiento de datos personales; posible aviso/autorización | — | no tengo la norma a la vista (sin país ni dato declarado no cito ninguna) |
| Alerta de riesgo geotécnico a población: posibles deberes de aviso o de gestión de riesgo de quien opera la mina | No declarado | Desconocida | — | no tengo la norma a la vista |
| Retención de las alertas emitidas y su trazabilidad | No declarado | Desconocida | — | sin resolver |

No cito ninguna norma: sin país ni descripción de datos no puedo hacerlo sin inventar. Estos hallazgos deberían entrar al registro como restricción del requerimiento o como riesgo con doliente; ahora no pertenecen a ninguno.

## Requerimientos aceptados que esta especificación no cubre

Ninguno tiene sección de comportamiento (ver arriba). Están en el alcance solo por identificador.

| REQ | Título | Por qué no |
|---|---|---|
| REQ-2030 | «Requerimiento REQ-2030» · Diana Molina | Sin `need`, sin evidencia, criterio no verificable, sin proyecto |
| REQ-4100 | «Requerimiento REQ-4100» · **sin doliente** | Sin `need`, criterio no verificable, sin proyecto |
| REQ-4101 | «Requerimiento REQ-4101» · Rubén Cárdenas | Sin `need`, sin criterio, sin proyecto |
| REQ-4104 | «Requerimiento REQ-4104» · Beatriz Cuéllar | Sin `need`, sin criterio, sin proyecto |
| REQ-4105 | «Requerimiento REQ-4105» · Ricardo Salas | Sin `need`, sin criterio, sin proyecto |
| REQ-4106 | «Requerimiento REQ-4106» · Felipe Arango | Sin `need`, criterio no verificable, sin proyecto |
| REQ-4107 | «Requerimiento REQ-4107» · María Restrepo | Sin `need`, sin criterio, sin proyecto |
| REQ-4108 | «Requerimiento REQ-4108» · Mauricio Pérez | Sin `need`, sin evidencia, criterio no verificable, sin proyecto |
| REQ-4109 | «Requerimiento REQ-4109» · Gustavo Neira | Sin `need`, sin criterio, sin proyecto |
| REQ-4111 | «Requerimiento REQ-4111» · Óscar Ramírez | Sin `need`, criterio no verificable, sin proyecto |
| REQ-4113 | «Requerimiento REQ-4113» · Liliana Torres | Sin `need`, criterio no verificable, sin proyecto |
| REQ-4114 | «Requerimiento REQ-4114» · Javier Hoyos | Sin `need`, sin criterio, sin proyecto |

---
**Pie.** Sale del registro de requerimientos de PRD-301 (17 archivos en `estado-producto/PRD-301/requirements/`), actualizado el 2026-10-17, sobre el acta del 2026-10-09. Cubre 12 requerimientos aceptados por identificador y **0** con comportamiento redactado; deja fuera 5 propuestos. Términos vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17): https://www.josenanez.com/es/agents/criterio-pmo/legal

**Después:** no ofrezco `/product-charter`. Antes hace falta que los 12 tengan problema escrito, criterio verificable y proyecto que los ejecute.

---

Notas de la sesión:
- Los términos ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez (2026-10-17), así que no hubo nada que registrar.
- La corrida quedó registrada como `2026-10-17-product-spec-1`: 52 s, 17 requerimientos, 39 señales. Las señales son 14 de evidencia vencida, 12 de requerimientos sin proyecto, 6 sin criterio, 3 sin decidir, 2 aceptados sin evidencia, 1 sin doliente y 1 supuesto sin verificar.
- Los 3 `requirement_undecided` son REQ-4102, REQ-4103 y REQ-4112. El borrador los deja fuera del alcance como propuestos, pero no cita esa señal, que se reduce a que nadie los ha decidido.