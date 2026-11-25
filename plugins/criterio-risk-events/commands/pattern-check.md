---
description: Lo que se repite: los eventos del mismo tipo en el mismo proceso dentro de la ventana de la política, y los eventos que no corresponden a ningún riesgo de la matriz
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /pattern-check — Lo que se repite

> **Dónde está la configuración:** `.criterio/eventos/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-risk-events:events-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `riesgos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No fijas un umbral, no calificas un riesgo y no cierras un evento.** Dices qué indicador está en alerta sin acción, cuál no se reportó, qué evento está incompleto o se registró tarde, qué se repite en el mismo proceso y qué evento no está en la matriz; la decisión es del comité de riesgos y de las áreas. **Nunca te conectas a un sistema ni calculas una pérdida esperada ni capital**: procesas exportaciones.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-risk-events:events-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **risk-policy**.

## Flujo

Los eventos del mismo tipo en el mismo proceso dentro de la ventana de la política, con su monto, y cada evento contra el riesgo de la matriz al que corresponde. Si un evento cambia la calificación de un riesgo lo decide el área de riesgos: aquí se dice qué se repite y qué no está en la matriz.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" reporte --config <config> --period <AAAA-MM> --what pattern-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/eventos/<AAAA-MM>/reporte-pattern-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-pattern-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" corrida --config <config> --what pattern-check \
    --salida <estado>/corridas/salida-pattern-check.md \
    --caso <AAAA-MM> \
    --nota "los eventos repetidos y fuera de la matriz"
```
