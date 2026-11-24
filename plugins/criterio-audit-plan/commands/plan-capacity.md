---
description: Las horas del plan contra la capacidad del equipo, y el requisito temático vigente de cada trabajo de aseguramiento
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /plan-capacity — Las horas del plan

> **Dónde está la configuración:** `.criterio/plan/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-audit-plan:plan-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `auditoria.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas el plan, no decides qué se audita y no emites una opinión.** Dices qué riesgo alto no tiene un trabajo, qué unidad pasó su ciclo, qué cambio no tiene su acta y si las horas alcanzan; la decisión es del responsable de auditoría con el consejo. **Las Normas Globales de Auditoría Interna se citan por su número y su título**, nunca por su texto.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-audit-plan:plan-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **audit-methodology**.

## Flujo

La suma de las horas de los trabajos activos contra las horas disponibles del equipo en el periodo, y cada trabajo de aseguramiento sobre ciberseguridad o terceros contra el requisito temático que rige desde antes de su inicio (F-02).

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" reporte --config <config> --period <AAAA-MM> --what plan-capacity
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/plan/<AAAA-MM>/reporte-plan-capacity.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-plan-capacity.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" corrida --config <config> --what plan-capacity \
    --salida <estado>/corridas/salida-plan-capacity.md \
    --caso <AAAA-MM> \
    --nota "las horas y los requisitos temáticos"
```
