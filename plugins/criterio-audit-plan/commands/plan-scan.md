---
description: Procesa lo que cambió en el plan, lleva cada acta nueva a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /plan-scan — Lo que cambió en el plan

> **Dónde está la configuración:** `.criterio/plan/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-audit-plan:plan-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `auditoria.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas el plan, no decides qué se audita y no emites una opinión.** Dices qué riesgo alto no tiene un trabajo, qué unidad pasó su ciclo, qué cambio no tiene su acta y si las horas alcanzan; la decisión es del responsable de auditoría con el consejo. **Las Normas Globales de Auditoría Interna se citan por su número y su título**, nunca por su texto.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-audit-plan:plan-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **audit-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" inventario --config <config>
```

**2. El universo, la matriz, el plan, el equipo y las asignaciones no se extraen: los procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **plan-record**: cada acta nueva de `10-plan/` con el trabajo que agrega, cancela o aplaza y quién lo aprobó, y la razón documentada si el plan no considera un área:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" convertir --config <config> --caso 10-plan
```

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" reporte --config <config> --period <AAAA-MM> --what plan-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/plan/<AAAA-MM>/reporte-plan-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-plan-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" corrida --config <config> --what plan-scan \
    --salida <estado>/corridas/salida-plan-scan.md \
    --caso <AAAA-MM> \
    --nota "actas llevadas a la ficha, señales"
```
