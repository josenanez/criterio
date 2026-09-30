---
description: El borrador del acta de constitución desde el requerimiento aceptado — el momento en que un producto se vuelve proyecto, nace la ficha y el escritor cambia de manos
argument-hint: "<REQ-xxx o el conjunto de requerimientos que van al proyecto>"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /product-charter — El acta de constitución

> **Dónde está la configuración:** `.criterio/producto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo producto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-product:product-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Es **la costura del sistema**: el momento en que un problema definido se vuelve plan con
doliente, autoridad y criterio de éxito. Antes de esta línea no hay plan, ni línea base, ni
presupuesto contra los que medir. Después, sí — y empieza el trabajo de otro agente.

Conviene decir qué cambia exactamente, porque es la única frontera del diseño donde un
agente le entrega algo a otro:

| | Antes del acta | Después |
|---|---|---|
| **El objeto** | El registro de requerimiento | La ficha del proyecto |
| **Quién escribe** | Alba | El agente del proyecto, salvo el estado declarado |
| **Qué hace Alba** | Todo | **Solo leer**, para saber si su producto se está construyendo |

**Una ficha, un escritor.** Alba la crea con el acta y a partir de ahí no vuelve a
escribirla: si dos agentes la escribieran, el desacuerdo entre ellos dejaría de ser una señal
y sería una carrera.

## Invocación

```
/product-charter REQ-014
/product-charter REQ-014 REQ-017 REQ-021     varios en un proyecto
```

## Flujo

**1. Verifica que haya con qué, y si no, dilo y no escribas el acta.** Aplica
**requirement-record**. Un acta sobre un requerimiento a medias es un proyecto que arranca a
medias, y eso no se arregla después:

- **Está aceptado**, no propuesto. Quién decide qué se construye es el gerente de producto, y
  sin su decisión no hay acta.
- **Tiene criterios de aceptación** verificables. Son el criterio de éxito del proyecto, y
  sin ellos el cierre no se puede juzgar meses después.
- **Tiene evidencia de demanda**, con su cita. Aplica **demand-evidence**.
- **La definición tiene declarada la autoridad.** Es el campo que más se pierde y el que más
  cuesta después: un proyecto cuyo gerente no sabe qué puede decidir escala todo o no escala
  nada.

Di cuál falta, y **ofrece seguir sin él marcándolo como vacío del acta** — no lo rellenes.

**2. Redacta el borrador.** Aplica **governance-artifacts** para qué contiene un acta y quién
decide qué. Todo campo con su cita al registro o al documento de origen: **un acta con datos
sin fuente es la primera ficha con campos sin fuente**, y eso se arrastra todo el proyecto.

**3. Lista los supuestos que se llevan al proyecto.** Aplica **assumption-tracking**. Los
supuestos sin verificar de la definición **no desaparecen con el acta**: pasan a ser riesgos
del proyecto, con doliente, y se registran con **raid-taxonomy**. Que un supuesto del producto
se vuelva riesgo del proyecto es exactamente lo que tiene que pasar, y casi nunca pasa.

**4. Di qué no entra.** El alcance excluido, requerimiento por requerimiento, con la razón.
Es la lista que nadie escribe y la que evita la discusión del tercer mes.

**5. El acta la firma una persona.** Este comando produce el borrador y se detiene ahí.

**6. Solo después de firmada, crea la ficha.** No antes: una ficha creada sobre un acta sin
firma es un proyecto que existe en el sistema y no en la organización.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" init --state <estado del proyecto>
```

Aplica **project-record** para el esquema. Lo que se llena desde el acta: identidad,
`identity.product` con el código del producto —es lo que permite a la PMO mirar por producto y
lo que confirma la traza en los dos sentidos—, el criterio de éxito, la autoridad, los hitos
que el acta declare, y el presupuesto aprobado si lo declara.

**Y lo que no se llena, por diseño: `declared`.** El agente no declara el estado de un
proyecto; lo declara su gerente. Es la restricción que sostiene el hallazgo de más valor de
todo el sistema, y empieza a valer desde el primer día de la ficha.

**7. Di a quién le queda esto.** El proyecto necesita un gerente, y desde ese momento la ficha
es suya. Nombra qué instala —`criterio-project`— y qué corre primero: `/pm-setup`.

## Salida

```markdown
# Acta de constitución — [proyecto] · borrador del [fecha]
**Producto:** [código y nombre] · **Requerimientos:** [REQ-xxx, ...]

## Qué problema resuelve
[De la definición, con su cita.]

## Criterio de éxito
[De los criterios de aceptación del requerimiento. Con cómo se verifica cada uno.]

## Alcance
### Entra
| REQ | Título | Evidencia que lo sostiene |
### No entra
| REQ | Título | Por qué no |

## Gobierno
**Patrocinador:** · **Gerente propuesto:** · **Comité:** · **Autoridad del gerente:**
[Cada uno con su cita. Lo que no esté dicho, así.]

## Supuestos que se llevan al proyecto
| Supuesto | Verificado | Se convierte en riesgo de |

## Restricciones normativas sin resolver
| Qué toca | Obligación | Norma | Estado |

## Vacíos de este acta
| Qué falta | Consecuencia de firmar sin eso | Quién lo cierra |

---
**Esto es un borrador.** Lo firma [quién]. La ficha del proyecto se crea después de la firma.
```

## Lo que este comando no hace

- **No firma, y no da por firmado.** La ficha se crea en el paso 6, nunca antes.
- **No escribe el estado declarado.** Ni al crear la ficha ni nunca.
- **No planifica.** El acta no lleva cronograma: el plan y la línea base los hace el gerente
  del proyecto con su agente, y un acta que ya trae plan se lo impuso.
- **No nombra al gerente.** Propone; asignar a una persona es de quien tiene la autoridad.
- **No vuelve a escribir la ficha después de crearla.** Ver arriba: una ficha, un escritor.

## Después

Di en una línea qué sigue, y para quién: el gerente del proyecto instala `criterio-project` y corre
`/pm-setup`; cuando publique su ficha con `/pm-publish`, `/product-trace` va a poder confirmar
la traza contra ella, **y desde ahí Alba se entera de si su producto se está construyendo sin
tener que preguntarle a nadie.**

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida --state <estado> --what product-charter \
    --salida <estado>/corridas/salida-product-charter.md \
    --caso <código del producto, el de la configuración> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-product-charter.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
