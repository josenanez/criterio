---
description: El informe de cada trabajo contra sus papeles: el hallazgo que falta o sobra, la prioridad y las cifras que no coinciden
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /report-check — El informe contra los papeles

> **Dónde está la configuración:** `.criterio/trabajos/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-audit-work:work-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `auditoria.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No emites una opinión, no firmas ni apruebas un informe, no cambias la prioridad de un hallazgo y no editas un papel de trabajo.** Dices qué hallazgo no tiene su criterio, su causa o su papel, qué paso no se ejecutó, qué papel no se revisó y en qué no coincide el informe con los papeles; la decisión es del auditor. **No calificas a las personas.** **Las Normas Globales de Auditoría Interna se citan por su número y su título**, nunca por su texto.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-audit-work:work-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **finding-record**.

## Flujo

Cada hallazgo del informe contra el de sus papeles, en la ficha: que esté en los dos, con la misma prioridad y las mismas cifras. Cada diferencia va con las dos citas.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" reporte --config <config> --period <AAAA-MM> --what report-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/trabajos/<AAAA-MM>/reporte-report-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-report-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" corrida --config <config> --what report-check \
    --salida <estado>/corridas/salida-report-check.md \
    --caso <AAAA-MM> \
    --nota "el informe contra los papeles"
```
