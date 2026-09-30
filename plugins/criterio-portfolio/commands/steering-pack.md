---
description: Material de comité — un paquete de decisiones, no un informe de avance
argument-hint: "[fecha del comité] o vacío para el próximo configurado"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /steering-pack — Material de comité

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes el material.
> Abre declarando qué fichas cargó y su fecha. Cierra con el pie: versión, fichas aplicadas, campos inciertos y enlace a los términos.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/steering-pack
/steering-pack 2026-10-08
```

## El principio

Un comité decide lo que excede la autoridad del gerente de proyecto. Su material **no es un informe de avance**: es un paquete de decisiones.

Todo lo que no requiere decisión va al anexo. Si el paquete no tiene decisiones, el comité no tiene por qué reunirse, y eso también se dice.

## Flujo

**Antes de escribir una cifra, recalcula.**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" compute --state <estado> --config <config>
```

Toda cifra derivada —porcentaje, desviación, días, suma, conteo de señales— se copia de esa salida, con todos sus dígitos. Si el script no la da, no se escribe: se dice qué dato falta para poder calcularla.

**1. Junta lo que escala.** Aplica **raid-taxonomy** y su criterio de escalamiento: excede autoridad, afecta a otro proyecto, dos períodos sin movimiento, doliente fuera del proyecto sin responder, mitigación vencida sin evidencia.

Suma las solicitudes de cambio pendientes de decisión y las contradicciones de portafolio que ningún gerente puede resolver solo.

**2. Formula cada punto como decisión.** Aplica **governance-artifacts**. Cada punto lleva cuatro cosas, y si falta alguna el punto no está listo:

- La decisión, como pregunta cerrada.
- Las opciones, con su implicación en alcance, tiempo y costo.
- Qué se recomienda y por qué.
- Qué pasa si no se decide hoy.

**3. Verifica quién decide.** Un punto dirigido a quien no tiene la facultad se devuelve. Si no está claro quién aprueba, ese es el primer punto del comité.

**4. Cierra el ciclo anterior.** Qué se decidió en el comité pasado, qué se hizo con esa decisión y qué sigue abierto. Sin esto el comité decide sobre el vacío.

## Salida

```markdown
# Comité de proyectos — [fecha]
[N] decisiones · [N] escalamientos · [N] proyectos con hallazgos

## Decisiones del comité anterior
| Decisión | Fecha | Qué pasó | Estado |

## Decisiones de hoy

### [1] [La pregunta, cerrada]
**Proyecto:** · **Quién decide:** · **Si no se decide hoy:**
| Opción | Alcance | Tiempo | Costo |
**Recomendación:** [cuál y por qué]

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |

## Para conocimiento
[Una línea por proyecto. Sin detalle: el detalle va al anexo.]

## Anexo
[Estado de cada proyecto, contradicciones abiertas, vacíos de información.]
```

## Después

Ofrece registrar las decisiones en las fichas una vez el comité sesione — ahí es donde el ciclo se cierra y el material del próximo comité empieza a construirse solo.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what steering-pack \
    --salida <estado>/corridas/salida-steering-pack.md \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-steering-pack.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
