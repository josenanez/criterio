---
description: Cada incidente contra el plazo de contención de su severidad y su revisión posterior contra los días de la política
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /incident-timeline — La línea de tiempo de cada incidente

> **Dónde está la configuración:** `.criterio/resiliencia/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-resilience:resilience-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, hora o conteo que muestres se copia de la salida de `seguridad.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No notificas a nadie, no declaras ni cierras un incidente y no ejecutas una prueba ni una restauración.** Dices qué incidente se contuvo fuera de plazo, qué notificación de la matriz se hizo tarde o no se hizo y qué prueba pasó su fecha; quién notifica y qué se hace es de una persona. **Nunca abres credenciales, llaves ni respaldos**: el motor los lista en `excluidos` y no se abren.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-resilience:resilience-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **incident-record**.

## Flujo

Cada incidente de la ficha: las horas de la detección a la contención contra el plazo de su severidad, y su revisión posterior contra los días de la política desde el cierre.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" reporte --config <config> --period <AAAA-MM> --what incident-timeline
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/resiliencia/<AAAA-MM>/reporte-incident-timeline.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-incident-timeline.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" corrida --config <config> --what incident-timeline \
    --salida <estado>/corridas/salida-incident-timeline.md \
    --caso <AAAA-MM> \
    --nota "incidentes contenidos fuera de plazo y sin revisión"
```
