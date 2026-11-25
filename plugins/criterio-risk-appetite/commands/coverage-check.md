---
description: Cada riesgo alto o crítico de la matriz con su límite o su indicador clave: los que no tienen con qué medirse
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /coverage-check — Cada riesgo alto con su límite

> **Dónde está la configuración:** `.criterio/apetito/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-risk-appetite:appetite-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `riesgos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No fijas ni cambias un límite, no apruebas un exceso y no aceptas un riesgo.** Dices qué exposición supera su límite sin plan ni aprobación, qué reporte llegó tarde, qué límite no tiene dueño o pasó su revisión, qué riesgo alto no tiene con qué medirse y si la declaración de apetito se venció; la decisión es de la junta, del comité de riesgos y de las áreas. **Nunca te conectas a un sistema ni calculas capital ni valor en riesgo**: procesas exportaciones y las cifras que reportan las áreas.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-risk-appetite:appetite-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **risk-policy**.

## Flujo

Cada riesgo calificado alto o crítico en la matriz contra los límites del marco y los indicadores clave que lo miden. Si un riesgo necesita un límite o un indicador lo decide el comité de riesgos: aquí se dice cuál no tiene ninguno.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" reporte --config <config> --period <AAAA-MM> --what coverage-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/apetito/<AAAA-MM>/reporte-coverage-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-coverage-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" corrida --config <config> --what coverage-check \
    --salida <estado>/corridas/salida-coverage-check.md \
    --caso <AAAA-MM> \
    --nota "la cobertura de la matriz"
```
