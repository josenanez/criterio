---
description: Las normas nuevas con su evaluación de impacto, y las que aplican sin obligación en la matriz
argument-hint: "vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /regulatory-watch — Las normas nuevas

> **Dónde está la configuración:** `.criterio/cumplimiento/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-compliance:compliance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-compliance:compliance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **regulatory-change**. Las normas llegan al registro normativo de `30-normativa/`; las que aparecen en un boletín y no están en el registro se extraen a la ficha aplicando **compliance-record**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" convertir --config <config> --caso 30-normativa
```

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --period <AAAA-MM> --what regulatory-watch
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cumplimiento/<AAAA-MM>/reporte-regulatory-watch.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

**Si una norma aplica y qué exige lo decide la organización**, con su evaluación de impacto. Constanza no opina sobre el alcance de ninguna.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-regulatory-watch.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what regulatory-watch \
    --salida <estado>/corridas/salida-regulatory-watch.md \
    --caso <AAAA-MM> \
    --nota "normas sin evaluar, normas que aplican sin obligación"
```
