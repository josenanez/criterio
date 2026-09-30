---
name: requirement-record
description: El registro de requerimiento: esquema, extracción, citación, estados, y qué hacer cuando dos documentos piden cosas distintas. Se carga al inventariar, registrar o revisar requerimientos de un producto.
---

# El registro de requerimiento

Es el contrato de datos de Alba, y la dependencia de la que cuelga todo lo demás: sin
registro no hay trazabilidad, no hay especificación y no hay acta de constitución.

**Un requerimiento por archivo**, en `<estado>/requirements/<id>.json`. No un backlog en
una hoja de cálculo: un registro, con las mismas reglas que la ficha de un proyecto.

## Las tres reglas que lo gobiernan

1. **Todo campo lleva su cita o queda en `not_found`.** Un valor sin fuente es un defecto
   del registro, no un caso degradado. *«No está dicho en ninguna parte»* es una respuesta
   válida y esperada.
2. **El requerimiento dice el problema, no la solución.** *«Que el comercio confirme el
   pago sin llamar»* es un requerimiento; *«un webhook»* es un diseño. Si lo que está
   escrito ya decide cómo, la conversación de qué se necesita no se tuvo.
3. **El doliente es una persona.** Un área no es un doliente.

## El esquema

```json
{
  "id": "REQ-014",
  "title":  {"value": "...", "source": "...", "source_date": "2026-09-11"},
  "product": "PRD-QR",
  "state": "propuesto",
  "owner": {"value": "Marcela Ruiz", "kind": "person", "source": "..."},
  "stated_on": "2026-09-11",
  "need": {"value": "el problema, en las palabras de quien lo tiene", "source": "..."},
  "acceptance": [{"value": "la confirmación llega en menos de 3 s", "source": "..."}],
  "evidence":   [{"value": "entrevista con 8 comercios", "source": "...",
                  "source_date": "2026-09-01"}],
  "assumptions": [{"value": "el comercio tiene datos en el punto de venta",
                   "verified": false, "stated_on": "2026-09-11"}],
  "priority": {"value": "alta", "source": "..."},
  "decision": {"what": {"value": "se hace", "source": "comite-2026-10-08.md"},
               "who": "Marcela Ruiz", "on": "2026-10-08"},
  "traces": {"project": "PRY-101", "deliverables": ["..."]}
}
```

`kind` en el doliente es lo único que el modelo decide y el código no puede: **si eso es
una persona o un área.** El código compara; esta distinción se lee.

## Los cinco estados, y qué exige cada uno

| Estado | Qué significa | Qué se le exige |
|---|---|---|
| `propuesto` | Alguien lo pidió. Nadie decidió nada | Nada más que doliente y cita. **No se le exige evidencia ni criterio** |
| `aceptado` | Se decidió que se hace | Criterio de aceptación, evidencia de demanda, y un proyecto que lo ejecute |
| `en_construccion` | Hay un proyecto haciéndolo | Lo mismo, y la traza confirmada contra la ficha del proyecto |
| `entregado` | Está entregado | Lo mismo, menos la traza: ya es historia |
| `descartado` | Se decidió que no se hace | **La decisión con su documento.** Es el estado que más se pierde, y el que evita volver a discutirlo |

Un estado que no esté en esta lista el cálculo lo deja en `desconocido` y no le inventa
otro. Un registro con veinte estados propios es un registro que nadie puede comparar.

## Cómo se extrae

**De documentos, y siempre con la cita.** Entrevistas, tickets, correos del área
comercial, actas de comité, el caso de negocio. Aplica **discovery-synthesis** para
convertir lo que se dijo en temas, y **demand-evidence** para decidir qué de eso sostiene
un requerimiento y qué no.

- **Lo mismo pedido por dos personas distintas es un requerimiento con dos evidencias**,
  no dos requerimientos. Dos entradas duplicadas son dos discusiones separadas sobre la
  misma cosa.
- **Lo mismo pedido por la misma persona con otro alcance es otro requerimiento.** El
  alcance es lo que cambia, y fusionarlo pierde la diferencia.
- **Cada evidencia lleva `source_date`, siempre.** Es la fecha del documento de donde
  salió —la del nombre del archivo, `AAAA-MM-DD-tema.ext`, o la de dentro si el nombre no
  la trae—, y es el único campo que el código mira para saber si la evidencia envejeció.
  La primera medición real lo mostró: el agente escribió en su nota que la única
  entrevista tenía trece meses, y en el registro dejó `source` sin `source_date`. El
  código no lee notas; leyó cinco requerimientos con evidencia sin fecha y no levantó
  `evidence_stale` en ninguno. La fecha que sabes y no escribes en el campo no existe.
- **Una evidencia es una cita concreta, no una categoría.** «Cliente entrevistado» no
  dice quién pidió qué; «entrevista con Almacenes Rey, 2025-08-13: pide conciliación el
  mismo día» sí. El `value` lleva lo que se dijo, en las palabras de quien lo dijo.
- **Una queja no es un requerimiento** hasta que alguien nombra qué haría falta. Se
  registra como evidencia, no como registro propio.

## Cuando dos documentos piden cosas distintas

La misma regla que en la ficha del proyecto: **no se fusionan y no se elige por
plausibilidad.** Se registran las dos versiones con su fuente y su fecha, y se nombra la
contradicción. Quién decide es el gerente de producto.

Y una que es propia de producto: **cuando el negocio y los datos no coinciden, ninguno de
los dos gana por defecto.** Aplica **product-metrics**: la señal lleva las dos fuentes y
las dos fechas, y la conversación que sigue es del gerente.

## La costura con el resto de la familia

**El acta de constitución es el momento en que un requerimiento aceptado se vuelve
proyecto**, y donde nace la ficha. Aplica **governance-artifacts** para el acta y
**project-record** para la ficha. Es la única frontera del sistema donde Alba escribe algo
que otro agente va a leer, y por eso es la única que conviene tener escrita con esta
precisión.

Y la vuelta: `traces.project` apunta a un proyecto, y **la ficha de ese proyecto dice qué
producto ejecuta.** Si las dos no coinciden, el cálculo lo dice (`trace_not_confirmed`).
Alba no le cree a su propio registro.

## Lo que este registro no es

- **No es un backlog priorizado.** El orden lo pone el gerente de producto, y cuando hay
  conflicto de intereses ese orden no sale de ningún documento.
- **No es una especificación.** Aplica **specification-draft** para eso: la especificación
  se redacta desde el registro, y el registro sobrevive a la especificación.
- **No es un sistema de tickets.** No hay flujo, no hay asignación y no se le escribe a
  nadie.
