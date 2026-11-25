---
description: Procesa lo que cambió en los informes y en la calidad, lleva cada cifra nueva a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /lineage-scan — Lo que cambió en la calidad

> **Dónde está la configuración:** `.criterio/calidad/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-data-quality:lineage-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `datos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No corriges una cifra ni decides cuál de dos cifras es la correcta.** Dices qué cifra no tiene fuente, cuál no coincide con su fuente al mismo corte, cuál sale de otro corte, dónde se corta el linaje y qué regla no pasa; la decisión es de quien firma el informe. **Nunca te conectas a una base ni procesas un dato personal**: procesas exportaciones.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-data-quality:lineage-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **data-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" inventario --config <config>
```

**2. El linaje, las cifras de la fuente, las reglas, sus resultados y los datos críticos no se extraen: los procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **figure-record**: cada cifra de los informes de `20-informes/`, con su indicador, su valor y la fecha de corte que el informe declara:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" convertir --config <config> --caso 20-informes
```

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" reporte --config <config> --period <AAAA-MM> --what lineage-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/calidad/<AAAA-MM>/reporte-lineage-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-lineage-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" corrida --config <config> --what lineage-scan \
    --salida <estado>/corridas/salida-lineage-scan.md \
    --caso <AAAA-MM> \
    --nota "cifras llevadas a la ficha, señales"
```
