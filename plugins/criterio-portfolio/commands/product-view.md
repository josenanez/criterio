---
description: El estado de un producto a través de todos los proyectos que lo construyen, y no de uno
argument-hint: "[nombre del producto]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /product-view — Por producto, no por proyecto

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el informe.
> Abre declarando de qué fichas sale y de cuándo. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/product-view                            todos los productos del portafolio
/product-view crédito de consumo         uno
```

## Por qué existe

Un proyecto termina; **un producto sobrevive a todos los proyectos que lo construyeron.**
La pregunta del dueño del producto no es *"¿cómo va el proyecto PRY-014?"* sino *"¿cómo va
el crédito de consumo?"*, y esa no se puede responder desde cuarenta fichas de proyecto
mirando una por una.

Es la vista que la PMO le debe a quien responde por el producto, y la que el comité de
producto pide y nadie prepara.

## Flujo

**1. Agrupa por `identity.product`.** Sale del cálculo, en `products`. Un proyecto sin
producto declarado no entra: **eso también se reporta**, porque un proyecto que nadie sabe a
qué producto sirve es un hallazgo de gobierno.

**2. Suma las señales del grupo**, sin promediarlas. Un producto con tres proyectos en los
que uno está en silencio no está «un tercio en silencio»: tiene un proyecto en silencio, y
así se dice.

**3. Cruza las dependencias dentro del producto.** Dos proyectos del mismo producto que
dependen uno del otro y no lo coordinaron es el caso más frecuente y el más caro.

**4. La fecha del producto es la del proyecto más tardío** que le sirve, no el promedio.
Aplica **baseline-variance** sobre cada uno y toma la última.

**5. El dinero se suma**, y se dice cuántos de los proyectos traen las cuatro cifras. Una
suma incompleta que no se declara incompleta es peor que no sumar.

## Salida

```markdown
## Productos al [fecha]

| Producto | Proyectos | Con alertas | Fecha más tardía | Aprobado | Comprometido |

### [Producto]
**Proyectos:** [códigos y nombres]
**Lo que hay que ver:** [las señales del grupo, por proyecto]
**Dependencias internas:** [entre proyectos del mismo producto]
**Fecha comprometida del producto:** [la más tardía, y de qué proyecto sale]

### Proyectos sin producto declarado
| Proyecto | Área dueña |
[Con la consecuencia: nadie puede responder por el conjunto al que sirven.]
```

## Después

Si un producto tiene un solo proyecto, dilo en una línea y no armes una sección: la vista
por producto no aporta nada ahí, y fingir que sí es ruido.

Si aparecieron dependencias internas sin confirmar, ofrece llevarlas al comité de producto
como una sola decisión, no como dos puntos de proyecto.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what product-view \
    --salida <estado>/corridas/salida-product-view.md \
    --caso <código del producto> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-product-view.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
