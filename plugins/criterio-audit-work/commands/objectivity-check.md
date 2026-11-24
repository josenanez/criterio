---
description: Cada auditor asignado a un trabajo de aseguramiento contra lo que tuvo a su cargo en los doce meses anteriores
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /objectivity-check — Las asignaciones y la objetividad

> **Dónde está la configuración:** `.criterio/trabajos/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-audit-work:work-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `auditoria.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No emites una opinión, no firmas ni apruebas un informe, no cambias la prioridad de un hallazgo y no editas un papel de trabajo.** Dices qué hallazgo no tiene su criterio, su causa o su papel, qué paso no se ejecutó, qué papel no se revisó y en qué no coincide el informe con los papeles; la decisión es del auditor. **No calificas a las personas.** **Las Normas Globales de Auditoría Interna se citan por su número y su título**, nunca por su texto.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-audit-work:work-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **audit-intake**.

## Flujo

Las asignaciones de `20-trabajos/` contra los cargos anteriores del equipo en `00-referencia/`: un auditor asignado a un trabajo de aseguramiento sobre una actividad que tuvo a su cargo en los doce meses anteriores (norma 2.2). Un posible impedimento lo revisa y lo declara el responsable de auditoría (norma 2.3); aquí no se califica a nadie.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" reporte --config <config> --period <AAAA-MM> --what objectivity-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/trabajos/<AAAA-MM>/reporte-objectivity-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-objectivity-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" corrida --config <config> --what objectivity-check \
    --salida <estado>/corridas/salida-objectivity-check.md \
    --caso <AAAA-MM> \
    --nota "las asignaciones y la objetividad"
```
