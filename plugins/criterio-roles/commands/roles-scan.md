---
description: Procesa lo que cambió en los perfiles de cargo, lleva cada perfil nuevo a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /roles-scan — Lo que cambió en los perfiles

> **Dónde está la configuración:** `.criterio/perfiles/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-roles:roles-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas un perfil, no fijas un salario ni un cargo y no evalúas a una persona.** Dices qué perfil no tiene su ocupación, qué le falta frente a su estándar, qué requisito no se apoya en una tarea y qué pide que la ley o la política no permiten pedir; la decisión es de una persona. **Del estándar solo usas su descarga oficial**: ninguna ocupación, destreza ni nivel se escribe de memoria.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-roles:roles-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **talent-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" inventario --config <config>
```

**2. La descarga del estándar en `00-referencia/` no se extrae:** la procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **profile-record**: cada perfil nuevo o cambiado de `10-perfiles/` con su ocupación, sus tareas, cada requisito con la tarea y el elemento del estándar que lo apoyan, sus estudios, lo que no aplica con su motivo y su revisión:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" convertir --config <config> --caso 10-perfiles
```

**3. Calcula y muestra.** Si `record_issues` trae un perfil que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" reporte --config <config> --period <AAAA-MM> --what roles-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/perfiles/<AAAA-MM>/reporte-roles-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-roles-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what roles-scan \
    --salida <estado>/corridas/salida-roles-scan.md \
    --caso <AAAA-MM> \
    --nota "perfiles llevados a la ficha, señales"
```
