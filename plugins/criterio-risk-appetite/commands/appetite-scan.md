---
description: Procesa lo que cambió en el apetito por riesgo, lleva la revisión de la declaración y cada exceso aprobado a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /appetite-scan — Lo que cambió en el apetito

> **Dónde está la configuración:** `.criterio/apetito/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-risk-appetite:appetite-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `riesgos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No fijas ni cambias un límite, no apruebas un exceso y no aceptas un riesgo.** Dices qué exposición supera su límite sin plan ni aprobación, qué reporte llegó tarde, qué límite no tiene dueño o pasó su revisión, qué riesgo alto no tiene con qué medirse y si la declaración de apetito se venció; la decisión es de la junta, del comité de riesgos y de las áreas. **Nunca te conectas a un sistema ni calculas capital ni valor en riesgo**: procesas exportaciones y las cifras que reportan las áreas.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-risk-appetite:appetite-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **risk-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" inventario --config <config>
```

**2. La matriz, los límites, los indicadores, la exposición y los planes de acción no se extraen: los procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **appetite-record**: la declaración de apetito de `00-marco/` con la fecha de su última revisión por la junta, y cada exceso de un límite que el comité o la junta aprobó en las actas de `40-actas/`:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" convertir --config <config> --caso 00-marco
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" convertir --config <config> --caso 40-actas
```

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" reporte --config <config> --period <AAAA-MM> --what appetite-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/apetito/<AAAA-MM>/reporte-appetite-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-appetite-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" corrida --config <config> --what appetite-scan \
    --salida <estado>/corridas/salida-appetite-scan.md \
    --caso <AAAA-MM> \
    --nota "declaración y excesos aprobados llevados a la ficha, señales"
```
