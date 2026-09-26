---
description: El borrador de especificación desde el registro, con criterios de aceptación verificables, los vacíos señalados en vez de rellenados, y lo que ninguna sección cubre
argument-hint: "[REQ-xxx, REQ-xxx] o vacío para todo lo aceptado"
---

# /product-spec — El borrador de especificación

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Para qué existe

Lo escribe el agente; **lo cierra el gerente de producto.** Lo que el agente aporta es lo
que cuesta tiempo y no cuesta juicio: recoger el registro, redactar el criterio de aceptación
en forma verificable, y **dejar los huecos a la vista en vez de rellenarlos con lo
razonable.**

Esa última parte va contra el instinto de un modelo que escribe bien, y es la regla central
del comando: **una especificación con los huecos rellenados de forma razonable es peor que
una con los huecos a la vista.** Se ve completa, se aprueba, y lo que nadie decidió queda
decidido por el agente.

## Invocación

```
/product-spec                        todo lo aceptado
/product-spec REQ-014 REQ-017        un subconjunto
/product-spec revisar 40-spec/v2.md  revisa una especificación que ya existe
```

## Flujo

**1. Toma el registro, no la memoria.** Aplica **requirement-record** y
**specification-draft**. Solo requerimientos en `aceptado` o `en_construccion`: especificar
lo que nadie decidió es escribir el documento dos veces.

**2. Cada sección cita los requerimientos que cubre.** Una especificación que no se puede
rastrear al registro es una donde alguien agregó algo, y ese alguien no queda escrito en
ninguna parte.

**3. Escribe el criterio de aceptación de forma que alguien pueda verificarlo sin discutir.**
La prueba: dos personas distintas, mirando lo construido, llegan a la misma respuesta.
*«La confirmación es rápida»* no pasa la prueba; *«llega en menos de 3 s en el percentil 95»*
sí.

Y **marca el criterio que la organización no puede medir hoy.** Un percentil necesita que
alguien esté midiendo percentiles; si nadie los mide, el criterio no es verificable todavía,
y eso es un hallazgo.

**4. Señala los vacíos, con dueño.** Los cinco que hay que nombrar siempre: requerimientos
sin criterio de aceptación, comportamiento no definido en los casos borde, los supuestos
sobre los que está escrita —aplica **assumption-tracking**—, lo que otro equipo tiene que
hacer y no se ha acordado con ese equipo, y las obligaciones normativas sin resolver —aplica
**regulatory-sweep**—.

**Cada vacío lleva quién lo tendría que cerrar.** Un vacío sin dueño es un vacío que nadie
cierra.

**5. Y la vuelta, que es la que evita la conversación de «¿y esto no iba?»:** qué
requerimientos aceptados **no** quedaron cubiertos por ninguna sección, y por qué.

**6. Si es una revisión de una especificación que ya existe**, no la reescribas. Di qué
afirma que el registro no sostiene, qué requerimiento aceptado no cubre, y qué criterio de
aceptación no es verificable. Es más útil y es honesto con el autor.

## Salida

La forma completa está en **specification-draft** y se sigue tal cual. Lo que no puede faltar:

```markdown
# Especificación — [producto] · borrador del [fecha]

## Alcance
### Entra
### No entra
[Esta segunda lista vale más que la primera, y casi nunca se escribe.]

## Criterios de aceptación
| Criterio | Requerimiento | Cómo se verifica | ¿Se puede medir hoy? |

## Supuestos sobre los que está escrita
| Supuesto | Verificado | Quién lo verificaría |

## Vacíos
| Qué falta decidir | Consecuencia de no decidirlo | Quién lo cierra |

## Requerimientos aceptados que esta especificación no cubre
| REQ | Título | Por qué no |
```

**Pie obligatorio:** de qué registro sale, de cuándo es, cuántos requerimientos cubre, y el
enlace a los términos. Y en la primera línea, que es un borrador y quién lo cierra.

## Lo que este comando no hace

- **No decide el alcance.** Propone el que sale del registro, y señala lo que queda fuera.
- **No diseña.** El requerimiento dice el problema; la arquitectura es de quien construye, y
  una especificación que ya la decide le quitó al equipo su decisión.
- **No estima.** Ni esfuerzo, ni costo, ni fecha: eso nace con el plan, y el plan nace con el
  acta de constitución.
- **No aprueba.** El borrador se cierra con una firma que este agente no puede dar.
- **No rellena un vacío con lo razonable.** Ver el paso 4. Es la regla que sostiene todo lo
  demás.

## Después

Si la especificación quedó con los vacíos cerrados y el requerimiento tiene criterio de
éxito, ofrece `/product-charter`: es el momento en que esto deja de ser producto y se vuelve
proyecto.
