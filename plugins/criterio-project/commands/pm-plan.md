---
description: El primer borrador del plan y la WBS desde el acta, con los supuestos declarados como supuestos y sin comprometer ninguna fecha
argument-hint: "[ruta del acta de constitución] o vacío para la configurada"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /pm-plan — El primer borrador del plan

> **Dónde está la configuración:** `.criterio/proyecto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo proyecto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-project:pm-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

El acta está firmada y hay que planificar. Ese primer borrador cuesta dos o tres días de
un gerente, y casi todo ese tiempo se va en lo mecánico: descomponer, ordenar, y escribir
un cronograma que después se discute entero en la primera reunión.

Lo mecánico es lo que este comando hace. **Lo que no hace es comprometer una fecha**, y
esa no es una limitación: es la sexta invariante del diseño. Una fecha comprometida es un
acto de autoridad, y la autoridad es tuya.

## Invocación

```
/pm-plan
/pm-plan 00-gobierno/2026-11-03-acta-constitucion.md
/pm-plan revisar 10-plan/wbs-v2.md      revisa un plan que ya existe
```

## Flujo

**1. Parte del acta, y si falta algo dilo antes de descomponer nada.** Aplica
**governance-artifacts**. Un plan construido sobre un acta incompleta hereda el hueco y lo
esconde:

- **Sin criterio de éxito** no se puede saber qué entra en el alcance. Es el vacío más
  caro y el más frecuente.
- **Sin autoridad declarada** no se sabe qué puedes decidir tú al planificar y qué hay que
  subir.
- **Sin patrocinador** no hay a quién llevarle las excepciones.

Dilo como hallazgo con su consecuencia, ofrece seguir marcándolo, y **no lo rellenes.**

**2. Descompón por entregable, no por área ni por fase.** Es la regla que decide si una
WBS sirve: cada nodo terminal tiene que ser algo que **alguien recibe y acepta**. *«Análisis»*
no es un entregable; *«el documento de requerimientos firmado por el negocio»* sí.

Y un nodo terminal que nadie puede aceptar es un nodo que nadie va a cerrar.

**3. Marca cada nodo con lo que se sabe y lo que no.** Tres estados y nada más:

| Estado | Qué significa |
|---|---|
| **Del acta** | Está escrito en el acta, con su cita |
| **Supuesto** | Lo estás asumiendo tú. Va declarado como supuesto, no como hecho |
| **Sin definir** | Nadie lo ha dicho. **No se completa con lo razonable** |

La tercera columna es el producto de este comando. Un plan que se ve completo porque el
agente rellenó los huecos con lo sensato es peor que uno con los huecos a la vista: se
aprueba, y lo que nadie decidió queda decidido por un modelo.

**4. Ordena por dependencia, no por calendario.** Qué necesita qué. Sin fechas todavía: el
orden es una propiedad del trabajo, las fechas son una decisión.

**5. Mira proyectos análogos del portafolio, si los hay.** Si tu configuración apunta a la
carpeta de fichas de la PMO, busca proyectos con el mismo producto o con entregables del
mismo tipo, y trae **lo que les pasó**, con la cita: cuánto se corrió el cierre, cuántas
replanificaciones tuvieron, qué hitos vencieron sin evidencia.

**Eso es referencia, no estimación.** *«El proyecto análogo PRY-014 se corrió 74 días
entre su línea base original y la vigente»* es un dato; *«esto va a tomar 74 días más»* es
un número inventado con aspecto de cálculo. Si no hay proyectos análogos a la vista, dilo:
es la respuesta correcta y la que evita una falsa precisión.

**6. Propón la estructura del cronograma, y deja las fechas en blanco.** Duración
propuesta por nodo **solo si sale de algo citable** —el contrato del proveedor, el acta,
un análogo—. Donde no haya de dónde sacarla, va vacía y con la pregunta: *«¿cuánto toma
esto?»*. Esa lista de preguntas es lo que el gerente lleva a su equipo, y es la mitad del
valor del comando.

**7. Di qué falta para poder comprometer una fecha.** Normalmente: la disponibilidad real
del equipo, la fecha del proveedor, y la ventana de la sala de producción. Ninguna de las
tres está en un documento.

## Salida

```markdown
# Plan — [proyecto] · borrador del [fecha]
**Desde:** [el acta, con su fecha] · **Criterio de éxito:** [o «no está declarado»]

## Lo que le falta al acta
| Qué | Consecuencia de planificar sin eso |
[Si no falta nada, una línea diciéndolo.]

## WBS
| # | Entregable | Quién lo acepta | De dónde sale | Duración |
| 1 | ... | ... | del acta · supuesto · sin definir | [vacía si no hay de dónde] |

## Orden
[Qué necesita qué. Sin fechas.]

## Supuestos sobre los que está construido
| Supuesto | Qué pasa si resulta falso |
[Estos pasan a riesgos del proyecto en cuanto el plan se apruebe.]

## Sin definir
| Qué | Quién lo define |

## Proyectos análogos
| Proyecto | Qué le pasó | Fuente |
[Referencia, no estimación. Si no hay ninguno a la vista, se dice.]

## Preguntas para el equipo
[Una por cada duración vacía. Es lo que el gerente lleva a la primera reunión.]

## Para comprometer una fecha falta
[Lo que no está en ningún documento.]
```

## Lo que este comando no hace

- **No compromete ninguna fecha.** Propone estructura y orden; la fecha la compromete el
  gerente, y ese es un acto de autoridad.
- **No estima por analogía.** Trae lo que les pasó a los análogos, con la cita, y ahí se
  detiene.
- **No rellena un nodo sin definir.** Ver el paso 3.
- **No crea la línea base.** La línea base nace cuando alguien aprueba el plan, y eso es
  otra cosa y otro momento.
- **No asigna personas.** Dice quién acepta cada entregable si el acta lo dice; repartir el
  trabajo es juicio sobre personas.

## Después

Cuando el plan se apruebe, ofrece registrarlo como **línea base original** —la primera, la
que después permite medir desviación contra dos referencias— y pasar los supuestos al RAID
con doliente, aplicando **raid-taxonomy**. Un supuesto que se queda en el documento del
plan es un riesgo que nadie va a volver a mirar.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what pm-plan \
    --salida <estado>/corridas/salida-pm-plan.md \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-pm-plan.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
