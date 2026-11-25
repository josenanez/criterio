---
description: Cada resultado del informe de mercadeo contra la exportación de la plataforma al mismo corte: el que no se sostiene
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /result-check — Cada resultado contra la plataforma

> **Dónde está la configuración:** `.criterio/campanas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-campaigns:campaigns-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `mercadeo.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas un presupuesto, no juzgas una campaña y no decides cuál cifra es la correcta.** Dices qué campaña pasó su presupuesto, qué factura de pauta no tiene campaña ni orden, qué campaña no tiene meta, cuál siguió después de su fin y qué resultado no coincide con la plataforma; la decisión es del área de mercadeo y de quien firma el informe. **Nunca te conectas a una plataforma de pauta ni de analítica**: procesas sus exportaciones.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-campaigns:campaigns-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **marketing-policy**.

## Flujo

Cada resultado de la ficha contra el valor de la plataforma para la misma campaña, el mismo indicador y el mismo corte, con la tolerancia de la política. Cuál cifra es la correcta lo decide quien firma el informe: aquí se dice cuál no coincide.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" reporte --config <config> --period <AAAA-MM> --what result-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/campanas/<AAAA-MM>/reporte-result-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-result-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" corrida --config <config> --what result-check \
    --salida <estado>/corridas/salida-result-check.md \
    --caso <AAAA-MM> \
    --nota "los resultados contra la plataforma"
```
