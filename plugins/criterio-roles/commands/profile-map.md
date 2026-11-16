---
description: Los perfiles de la organización por ocupación: los que se solapan y las ocupaciones afines que no tienen perfil
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /profile-map — El mapa de los perfiles

> **Dónde está la configuración:** `.criterio/perfiles/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-roles:roles-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas un perfil, no fijas un salario ni un cargo y no evalúas a una persona.** Dices qué perfil no tiene su ocupación, qué le falta frente a su estándar, qué requisito no se apoya en una tarea y qué pide que la ley o la política no permiten pedir; la decisión es de una persona. **Del estándar solo usas su descarga oficial**: ninguna ocupación, destreza ni nivel se escribe de memoria.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-roles:roles-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **occupation-standard**.

## Flujo

Los perfiles de la ficha del periodo agrupados por su ocupación: los que comparten la ocupación y la mayor parte de sus requisitos, y las ocupaciones afines a las de la organización, según el estándar, que no tienen perfil.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" reporte --config <config> --period <AAAA-MM> --what profile-map
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/perfiles/<AAAA-MM>/reporte-profile-map.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-profile-map.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what profile-map \
    --salida <estado>/corridas/salida-profile-map.md \
    --caso <AAAA-MM> \
    --nota "perfiles que se solapan y ocupaciones sin perfil"
```
