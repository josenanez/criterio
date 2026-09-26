---
name: specification-draft
description: El borrador de especificación desde el registro de requerimientos, con criterios de aceptación verificables y los vacíos señalados en vez de rellenados. Se carga al redactar o revisar una especificación de producto.
---

# El borrador de especificación

Lo escribe el agente; **lo cierra el gerente de producto.** La diferencia no es de estilo:
una especificación decide qué se construye, y decidir es de quien tiene la autoridad.

Lo que el agente aporta es lo que cuesta tiempo y no cuesta juicio: recoger el registro,
redactar el criterio de aceptación en forma verificable, y **dejar los huecos a la vista en
vez de rellenarlos con lo razonable.**

## De dónde sale

Del registro, requerimiento por requerimiento. Aplica **requirement-record**. Una
especificación que no se puede rastrear al registro es una especificación donde alguien
agregó algo, y ese alguien no queda escrito en ninguna parte.

**Cada sección de la especificación cita los requerimientos que cubre.** Y al final, la
vuelta: qué requerimientos aceptados **no** quedaron cubiertos por ninguna sección. Ese
segundo listado es el que evita la conversación de *«¿y esto no iba?»* tres meses después.

## El criterio de aceptación

Es la parte que casi nunca está, y la que decide si la discusión de si quedó bien se tiene
antes o después de construirlo.

**Un criterio de aceptación es una frase que alguien puede verificar sin discutir.** La
prueba: dos personas distintas, mirando lo construido, tienen que llegar a la misma
respuesta.

| No sirve | Sirve |
|---|---|
| «La confirmación es rápida» | «La confirmación llega al comercio en menos de 3 s en el percentil 95» |
| «La interfaz es clara» | «Un comercio nuevo completa su primer cobro sin ayuda, en la primera sesión» |
| «Cumple con la normativa» | «Cada transacción queda con su trazabilidad según [la obligación citada]». Aplica **regulatory-sweep** |
| «Soporta alto volumen» | «300 transacciones por minuto sostenidas 10 min sin degradar el percentil 95» |

Y una regla que ahorra discusiones: **un criterio que no se puede medir con lo que la
organización ya tiene, se marca.** *«Percentil 95»* necesita que alguien esté midiendo
percentiles. Si nadie los mide, el criterio no es verificable todavía, y eso es un hallazgo,
no un detalle.

## Los vacíos se señalan, no se rellenan

Es la regla central de este skill, y va contra el instinto de un modelo que escribe bien.
Una especificación con los huecos rellenados de forma razonable es **peor** que una con los
huecos a la vista: se ve completa, se aprueba, y lo que nadie decidió queda decidido por el
agente.

Los huecos que hay que nombrar siempre:

- **Requerimientos sin criterio de aceptación.** El cálculo los trae
  (`requirement_without_acceptance`).
- **Comportamiento no definido en los casos borde.** Qué pasa si no hay conexión, si el pago
  se duplica, si el cliente se va antes de la confirmación.
- **Los supuestos sobre los que está escrita.** Aplica **assumption-tracking**: van
  listados, no incorporados como si fueran hechos.
- **Lo que otro equipo tiene que hacer** y todavía no se ha acordado con ese equipo.
- **Las obligaciones normativas que toca y no están resueltas.**

Cada hueco lleva **quién lo tendría que cerrar**. Un vacío sin dueño es un vacío que nadie
cierra.

## La forma

```markdown
# Especificación — [producto] · borrador del [fecha]

## Qué problema resuelve
[De la definición, con su cita. Si la definición no lo dice, se dice que no lo dice.]

## Alcance
### Entra
### No entra
[Esta segunda lista vale más que la primera, y casi nunca se escribe.]

## Comportamiento
[Por sección, citando los requerimientos que cubre.]

## Criterios de aceptación
| Criterio | Requerimiento | Cómo se verifica | ¿Se puede medir hoy? |

## Supuestos sobre los que está escrita
| Supuesto | Verificado | Quién lo verificaría |

## Vacíos
| Qué falta decidir | Consecuencia de no decidirlo | Quién lo cierra |

## Requerimientos aceptados que esta especificación no cubre
| ID | Título | Por qué no |
```

## Lo que no hace

- **No decide el alcance.** Propone el que sale del registro, y señala lo que queda fuera.
- **No diseña.** El requerimiento dice el problema; el diseño técnico es de quien construye.
  Una especificación que ya decide la arquitectura le quitó al equipo la decisión que le
  corresponde.
- **No estima.** Ni esfuerzo, ni costo, ni fecha. Eso nace con el plan, y el plan nace con
  el acta de constitución.
- **No aprueba.** El borrador se cierra con una firma que este agente no puede dar.
