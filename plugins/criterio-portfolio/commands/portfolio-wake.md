---
description: Mira qué toca hoy según la cadencia configurada, lo hace, y si no toca nada se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
---

# /portfolio-wake — Lo que toca hoy

> **Dónde está la configuración:** `.criterio/portafolio/config.json`, en la carpeta donde corre la sesión. La escribe `/criterio-portfolio:portfolio-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla.
> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Un comando espera a que lo llamen. **Un agente no.**

Esto es lo que se programa para que corra solo: revisa la cadencia que la persona declaró
en `/portfolio-setup`, hace lo que toque, y **si no toca nada no produce nada.** Callarse cuando
no pasó nada no es una omisión: es la única razón por la que un agente que corre todos los
días sigue instalado el mes siguiente.

## Flujo

**1. Pregunta qué toca.** La decisión es aritmética de fechas, así que no la tomes tú:

```
python3 scripts/portafolio.py due --state <estado> --config <archivo>
```

Devuelve `due` con lo que toca, `quiet` si no toca nada, y `next_wake` con la próxima vez
que hay que mirar.

**2. Si `quiet` es verdadero, termina aquí.** Una línea: qué se revisó y cuándo vuelves.
**No produzcas un informe para decir que no hay novedad.**

**3. Si toca `sweep`** — el barrido diario. Aplica **document-intake**:

```
python3 scripts/portafolio.py index --state <estado> --docs <documentos>
```

Si `to_read` es cero y no hay citas rotas, no hay nada que releer: dilo en una línea. Si
hay documentos cambiados, corre `/portfolio-scan` **solo sobre los proyectos de
`projects_to_recompute`**, nunca sobre el portafolio completo.

Después del barrido, recalcula y mira si algo cruzó un umbral. Si nada cruzó, cállate
igual: el barrido corrió y no había noticia.

**4. Si toca `report`** — el informe de comité, que aterriza con la anticipación
configurada para que alcance a reaccionar a lo que encuentre. Corre `/portfolio-report`, y
si el comité es el que viene, ofrece también `/steering-pack`.

**5. Si toca `confirmation`** — la confirmación periódica. Aplica **portfolio-health**:
**cinco campos por corrida**, elegidos por importancia y no por antigüedad. Si preguntas
por cuarenta, no responde nadie.

Las preguntas se hacen una vez. Si la anterior no se respondió, **no la repitas**: reporta
*«preguntada el 12, sin respuesta»*, que es un hallazgo por sí solo.

**6. Si toca `requests`** — alguien dejó una petición en el servidor. Esto **no es
cadencia**: es la única cosa que rompe el silencio sin ser aritmética de fechas, y la
razón es simple — una persona preguntó y está esperando.

```
python3 scripts/portafolio.py requests --state <estado>
```

Atiéndelas **de la más vieja a la más nueva**. Cada una lleva su asunto, y el asunto
dice qué hacer: *revisar* es `/health-check` sobre ese proyecto; *explicar* es rastrear
el dato hasta su documento y citarlo; *corregir* es lo más valioso de todas — alguien
está diciendo que la evidencia no cuenta toda la historia. Eso **no se escribe en la
ficha**: se registra como hallazgo, con quién lo dijo y cuándo, y el documento que
falta es la pregunta que queda abierta. Ningún agente escribe la declaración.

Solo después de responderla, márcala. Una petición sin marcar vuelve a aparecer mañana,
y eso es correcto:

```
python3 scripts/portafolio.py answered --state <estado> --id <identificador>
```

Si no pudiste responder una, **déjala sin marcar y dilo**. Es mejor que vuelva a
aparecer a que se pierda.

**7. Deja constancia de lo que corriste.** Sin esto, mañana vuelve a tocar lo mismo:

```
python3 scripts/portafolio.py ran --state <estado> --what sweep
```

Una llamada por cada cosa que hiciste. **Solo por las que hiciste de verdad.**

**8. Cierra diciendo cuándo vuelves**, con la fecha de `next_wake`.

## Salida cuando no hay novedad

```markdown
Revisé la carpeta: [N] documentos, ninguno cambió. Vuelvo el [fecha].
```

Eso es todo. Sin encabezados, sin tablas, sin resumen de lo que no pasó.

## Salida cuando sí hay

```markdown
## [fecha]

**Revisé:** [N] documentos · [N] cambiaron · [N] proyectos recalculados

### Lo que cruzó un umbral
[Solo lo que cruzó. Con el proyecto, la señal y la cita.]

### Peticiones atendidas
[Quién preguntó qué, y la respuesta. Ninguna si no había.]

### Preguntas
[Máximo cinco, una por campo, con la fuente y la fecha del dato actual.]

**Vuelvo el [fecha].**
```

## Cómo se programa

Esto no se programa solo: alguien tiene que ponerlo en un reloj, y ese reloj vive fuera del
plugin. Ofrece el camino que corresponda:

**Claude Cowork** — una tarea programada que invoque este comando con la cadencia que salió
de `/portfolio-setup`. Si el barrido diario está activo, diaria.

**Claude Code** — el programador del sistema operativo invocando Claude en modo no
interactivo con este comando. Da la línea exacta para su sistema y **di qué se necesita
para que funcione sin nadie delante**: que la sesión pueda correr sin aprobar cada paso, y
que la carpeta de documentación esté montada cuando el reloj dispare.

**Si la organización no quiere corridas desatendidas** —y en un banco es una respuesta
razonable—, dilo sin discutir: este comando también sirve corrido a mano, y la cadencia
sigue diciendo qué toca. Lo que se pierde es que avise sin que nadie pregunte.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what portfolio-wake \
    --salida <estado>/corridas/salida-portfolio-wake.md \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-portfolio-wake.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
