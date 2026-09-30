---
description: El registro de requerimientos con sus vacíos — sin doliente, sin criterio de aceptación, aceptado sin que nadie lo haya pedido, y lo que lleva meses sin que nadie lo decida
argument-hint: "[REQ-xxx] o vacío para todo el registro"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /product-requirements — El registro

> **Dónde está la configuración:** `.criterio/producto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo producto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-product:product-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Un backlog en una hoja de cálculo tiene trescientas filas, y nadie sabe cuáles de esas
trescientas alguien pidió, cuáles tienen dueño, y cuáles llevan un año ahí porque nadie se
atreve a cerrarlas.

Este comando no ordena el backlog: **muestra los cuatro vacíos que hacen que un registro no
sirva**, y el quinto, que es el que nadie mira — lo que lleva meses propuesto sin que nadie
lo decida. Un registro que solo crece es un registro donde no se está decidiendo.

## Invocación

```
/product-requirements              todo el registro, con sus vacíos
/product-requirements REQ-014      uno solo, con su cadena de evidencia
/product-requirements aceptados    un estado
```

## Flujo

**1. Recalcula. No cuentes tú.**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" compute --state <estado> --config <archivo> --fichas <fichas>
```

Devuelve, por requerimiento, sus señales; y en total, cuántos hay por estado, qué porcentaje
de lo decidido tiene evidencia y qué porcentaje tiene un proyecto que lo ejecute. **Si un
número de tu salida no sale de ahí, está inventado.**

**2. Aplica el orden de lectura de **product-health**, no el del cálculo.** Primero lo que se
va a construir y nadie pidió; después lo que se decidió y nadie construye; al final los
vacíos de forma, que son los más fáciles de cerrar y por eso engañan.

**3. Respeta lo que no es hallazgo.** Aplica **requirement-record**: a un requerimiento
`propuesto` **no se le exige evidencia ni criterio de aceptación** — nadie dijo todavía que
se hace, y exigírselo convierte el registro en un trámite. A un `entregado` sin traza
tampoco: es historia.

**4. Para cada vacío, di quién lo cerraría.** Un vacío sin dueño es un vacío que nadie
cierra. Y para lo que lleva meses sin decidirse, **di quién tiene la facultad de decidir**,
porque casi siempre el problema no es que nadie lo mire: es que nadie sabe a quién le toca.

**5. Cierra lo que ya se decidió y nadie registró.** Aplica **requirement-record**: un
requerimiento descartado con su documento es información valiosa, y es el estado que más se
pierde. Sin él, la misma discusión vuelve cada seis meses.

## Salida

```markdown
## Registro — [producto] · al [fecha]
[N] requerimientos · [N] decididos · [N]% con evidencia · [N]% con proyecto que lo ejecuta

### Se va a construir y nadie lo pidió
| REQ | Título | Estado | Doliente |
[Sin una sola cita de quien lo pidió. Va primero.]

### Decidido y nadie lo está construyendo
| REQ | Título | Decidido el | |

### Sin doliente, o con un área en vez de una persona
| REQ | Título | Dice |

### Sin criterio de aceptación
| REQ | Título | Estado |
[Solo los decididos. La discusión de si quedó bien se está dejando para el final.]

### Decidido sin documento que lo respalde
| REQ | Quién decidió | Cuándo |

### Lleva meses y nadie lo decide
| REQ | Título | Propuesto hace | Quién tiene la facultad |

### Evidencia vieja
| REQ | Lo más nuevo que lo sostiene | Hace |

## Por estado
| propuesto | aceptado | en construcción | entregado | descartado |
```

**Si el registro no tiene ni un vacío, una línea:** *«[N] requerimientos, todos con
doliente, con criterio y con evidencia.»* Y se acaba. No produzcas un informe para decir que
no hay novedad.

## Cuando se pide uno solo

La cadena completa, que es lo que vuelve *«¿por qué estamos haciendo esto?»* una pregunta con
respuesta:

```markdown
## REQ-014 — [título]
**Estado:** [estado] · **Doliente:** [quién] · **Dicho el:** [fecha]

**El problema:** [en las palabras de quien lo tiene, con su cita]
**Quién lo pidió:** [cada evidencia, con su fuente y su fecha]
**Criterios de aceptación:** [cada uno, y si se puede medir hoy]
**Supuestos:** [con verificado o no, y quién lo verificaría]
**Decisión:** [qué, quién, cuándo, con qué documento]
**Lo ejecuta:** [proyecto, y si su ficha lo confirma]
```

## Lo que este comando no hace

- **No prioriza.** El orden lo pone el gerente de producto, y cuando hay conflicto de
  intereses ese orden no sale de ningún documento.
- **No decide qué se hace.** Muestra qué lo sostiene.
- **No le escribe a nadie.** Produce la lista; cerrar un vacío es una conversación.
- **No cierra requerimientos por viejos.** Propone decidirlos, que no es lo mismo.

## Después

Si hay requerimientos decididos que nadie está construyendo, ofrece `/product-trace`. Y si
hay uno aceptado, con evidencia y con criterio, ofrece `/product-charter`: ahí es donde deja
de ser un registro y se vuelve un proyecto.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida --state <estado> --what review \
    --salida <estado>/corridas/salida-review.md \
    --nota "qué requerimientos quedaron sin sustento"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-review.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
