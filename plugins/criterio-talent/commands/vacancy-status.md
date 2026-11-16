---
description: Cada vacante abierta contra el plazo de cobertura de la política: las que lo pasaron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /vacancy-status — Las vacantes contra su plazo

> **Dónde está la configuración:** `.criterio/seleccion/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-talent:talent-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Ninguna decisión sobre una persona es tuya.** No rechazas, no descartas, no das un puntaje y no ordenas candidatos por un número: presentas cada requisito con su evidencia, en el orden del identificador del candidato. **No usas la fotografía, la edad, el sexo, el estado civil, el origen, la religión ni la salud de nadie**: si llegan, la ficha registra solo su tipo y dónde, y el motor los excluye. **No entras a redes ni buscas personas** fuera de lo que la organización entrega.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-talent:talent-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **selection-policy**.

## Flujo

Cada vacante del registro contra el plazo de cobertura de la política, o el suyo si el registro lo trae, contado desde su apertura.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" reporte --config <config> --period <AAAA-MM> --what vacancy-status
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/seleccion/<AAAA-MM>/reporte-vacancy-status.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-vacancy-status.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what vacancy-status \
    --salida <estado>/corridas/salida-vacancy-status.md \
    --caso <AAAA-MM> \
    --nota "vacantes contra su plazo"
```
