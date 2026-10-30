---
description: Lo que toca hoy en la respuesta — un incidente nuevo, una notificación pendiente, una prueba que vence — y si no toca nada, se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /resilience-wake — Lo que toca hoy

> **Dónde está la configuración:** `.criterio/resiliencia/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-resilience:resilience-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, hora o conteo que muestres se copia de la salida de `seguridad.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No notificas a nadie, no declaras ni cierras un incidente y no ejecutas una prueba ni una restauración.** Dices qué incidente se contuvo fuera de plazo, qué notificación de la matriz se hizo tarde o no se hizo y qué prueba pasó su fecha; quién notifica y qué se hace es de una persona. **Nunca abres credenciales, llaves ni respaldos**: el motor los lista en `excluidos` y no se abren.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-resilience:resilience-setup`, que registra la aceptación: este comando no produce nada sin ella.

> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

**Si no toca nada, no produce nada.**

## Flujo

**1. Pregunta qué toca:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" despertar --config <config>
```

**2. Si `callado` es verdadero, termina aquí** —con una petición abierta nunca lo es—, en una línea.

**Las peticiones primero.** Si `peticiones` trae alguna —la dejó alguien en Rostrum, el portal—, respóndela antes de lo demás: di de quién es, qué pide y lo que los documentos y el último reporte responden, con su cita. Lo que pida criterio de una persona queda dicho como pregunta para ella. Cuando la respondas, márcala:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" responder --config <config> --id <id de la petición>
```

**3. Si toca `resilience-scan`**, haz su flujo completo: el inventario, lo excluido y lo que va a la ficha.

**4. Muestra lo que toca** —`toca` dice cuál: incident-timeline, notifications o continuity-tests—, un reporte por comando:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" reporte --config <config> --period <AAAA-MM> --what <comando>
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/resiliencia/<AAAA-MM>/reporte-<comando>.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-resilience-wake.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" corrida --config <config> --what resilience-wake \
    --salida <estado>/corridas/salida-resilience-wake.md \
    --caso <AAAA-MM> \
    --nota "qué tocaba y qué hizo"
```


Registra también cada comando que corriste —`resilience-scan` y los de `toca`— con el mismo `--caso`.
