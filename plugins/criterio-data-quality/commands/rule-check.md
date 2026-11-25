---
description: Cada regla de calidad contra su umbral y su corrida del periodo, y cada dato crítico contra las reglas que lo miden
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /rule-check — Las reglas de calidad

> **Dónde está la configuración:** `.criterio/calidad/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-data-quality:lineage-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `datos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No corriges una cifra ni decides cuál de dos cifras es la correcta.** Dices qué cifra no tiene fuente, cuál no coincide con su fuente al mismo corte, cuál sale de otro corte, dónde se corta el linaje y qué regla no pasa; la decisión es de quien firma el informe. **Nunca te conectas a una base ni procesas un dato personal**: procesas exportaciones.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-data-quality:lineage-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **data-policy**.

## Flujo

Cada regla de calidad contra su umbral y su resultado del periodo; la que mide un dato crítico y no corrió; y el dato crítico que ninguna regla mide. Los umbrales los fija la política de datos de la organización.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" reporte --config <config> --period <AAAA-MM> --what rule-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/calidad/<AAAA-MM>/reporte-rule-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-rule-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" corrida --config <config> --what rule-check \
    --salida <estado>/corridas/salida-rule-check.md \
    --caso <AAAA-MM> \
    --nota "las reglas de calidad"
```
