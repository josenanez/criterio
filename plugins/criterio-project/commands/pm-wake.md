---
description: Lo que toca hoy en tu proyecto según la cadencia de tu reunión — y si no toca nada, se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /pm-wake — Lo que toca hoy

> **Dónde está la configuración:** `.criterio/proyecto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo proyecto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-project:pm-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos. **Y sin subagentes en paralelo:** se leen hasta `execution.workers` proyectos a la vez según la configuración —1 si no lo dice, que es uno tras otro en esta misma conversación—; nunca más por decisión propia. El arnés cuenta los subagentes de cada corrida y marca la que se exceda.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.
> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Un comando espera a que lo llamen. **Un agente no.**

Y la cadencia de un proyecto no es la de un comité: **gira alrededor de la reunión.** La
agenda tiene que estar antes, el acta después, y el informe con la anticipación que le
sirva al gerente para reaccionar a lo que encuentre, no para enterarse cuando ya está
enviado.

**Si no toca nada, no produce nada.** Callarse cuando no pasó nada es la única razón por
la que un agente que corre todos los días sigue instalado el mes siguiente.

## Flujo

**1. Pregunta qué toca.** La decisión es aritmética de fechas, así que no la tomes tú:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" due --state <estado> --config <archivo>
```

Devuelve `due` con lo que toca, `quiet` si no toca nada, y `next_wake`.

**2. Si `quiet` es verdadero, termina aquí.** Una línea: qué revisaste y cuándo vuelves.

**3. Si toca `sweep`** — el barrido diario de la carpeta. Aplica **document-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" index --state <estado> --docs <documentos>
```

**Lo que importa aquí no es lo mismo que en un portafolio.** En un proyecto el documento
que aparece suele ser una minuta, y una minuta nueva significa compromisos nuevos: si el
índice trae una, corre la extracción de **commitment-tracking** sobre ella. Si lo que
cambió no es una minuta, recalcula y cállate si nada cruzó un umbral.

**4. Si el comité está cerca, mira de qué lado de la reunión estás.** Es lo propio de este
agente, y sale del `detail.committee` que devuelve `due`:

- **Falta un día o menos** → la reunión es lo siguiente. Ofrece `/pm-agenda`, y ofrécela
  una sola vez: si ya la armaste para esta reunión, no la vuelvas a proponer.
- **La reunión ya pasó y no hay acta** → es lo que más se pierde y lo que más cuesta
  después. Ofrece `/pm-minutes`, y **di qué necesitas**: la transcripción o las notas.
  Sin insumo no se redacta un acta, y decirlo es parte del trabajo.
- **Toca `report`** → `/pm-report`, con su anticipación. Ármalo completo **salvo el
  estado**, y pídele la declaración al gerente **después** de mostrarle la evidencia.

**5. Revisa lo que se venció solo.** Nadie hizo nada y el hallazgo está: compromisos que
vencieron desde la corrida anterior, hitos vencidos sin evidencia, y los reprogramados que
llegaron al umbral. Recalcula y reporta **solo lo que cruzó**, no el estado completo.

**6. Mira si tu ficha publicada se quedó vieja.** Si `/pm-publish` corrió hace más de un
ciclo de comité y la ficha cambió desde entonces, **la PMO está leyendo una foto vieja de
tu proyecto.** Dilo y ofrece publicar. Es el único aviso de este comando que no es sobre
tu proyecto sino sobre cómo te ven.

**7. Deja constancia de lo que corriste.** Sin esto, mañana vuelve a tocar lo mismo:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" ran --state <estado> --what sweep
```

Una llamada por cada cosa que hiciste. **Solo por las que hiciste de verdad.**

**8. Cierra diciendo cuándo vuelves**, con la fecha de `next_wake`.

## Salida cuando no hay novedad

```markdown
Revisé la carpeta: [N] documentos, ninguno cambió. Nada venció. Vuelvo el [fecha].
```

Eso es todo. Sin encabezados y sin resumen de lo que no pasó.

## Salida cuando sí hay

```markdown
## [proyecto] · [fecha]

**Revisé:** [N] documentos · [N] cambiaron · [N] minutas nuevas

### Lo que se venció solo
[Compromisos, hitos y reprogramados que cruzaron desde la corrida anterior, con su cita.]

### La reunión
[De qué lado estás: la agenda que falta, o el acta que nadie escribió.]

### Tu ficha publicada
[Solo si se quedó vieja. De cuándo es y qué cambió desde entonces.]

**Vuelvo el [fecha].**
```

## Lo que este comando no hace

- **No le escribe a nadie.** Ni a los dolientes de los compromisos vencidos, ni al
  patrocinador. Perseguir un compromiso es una conversación.
- **No declara el estado**, ni siquiera corriendo solo y sin nadie a quien preguntarle. Si
  toca informe y el gerente no está, el informe sale con esa línea en blanco y lo dice.
- **No publica tu ficha solo.** Avisa que se quedó vieja; publicarla sigue siendo un acto
  explícito tuyo.

## Cómo se programa

Esto no se programa solo: alguien tiene que ponerlo en un reloj, y ese reloj vive fuera del
plugin.

**Claude Cowork** — una tarea programada que invoque este comando con la cadencia que salió
de `/pm-setup`. Con el barrido diario activo, diaria; si no, el día anterior a la reunión y
el día después.

**Claude Code** — el programador del sistema operativo invocando Claude en modo no
interactivo con este comando. Da la línea exacta para su sistema y **di qué se necesita
para que funcione sin nadie delante**: que la sesión pueda correr sin aprobar cada paso, y
que la carpeta del proyecto esté montada cuando el reloj dispare.

**Si la organización no quiere corridas desatendidas** —y en un banco es una respuesta
razonable—, dilo sin discutir: este comando también sirve corrido a mano el lunes en la
mañana, y la cadencia sigue diciendo qué toca. Lo que se pierde es que avise sin que nadie
pregunte.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/portafolio.py" corrida --state <estado> --what pm-wake \
    --salida <estado>/corridas/salida-pm-wake.md \
    --caso <código del proyecto, el de la configuración> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-pm-wake.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
