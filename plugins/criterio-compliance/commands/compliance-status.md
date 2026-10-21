---
description: El estado del cumplimiento: cada obligación de la matriz contra su evidencia, declarado contra evidenciado
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /compliance-status — El estado del cumplimiento

> **Dónde está la configuración:** `.criterio/cumplimiento/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-compliance:compliance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-compliance:compliance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **obligations-matrix** y **compliance-record**. Una obligación está cumplida cuando una evidencia la prueba en la ventana de su periodicidad, con su id al inicio del nombre en `10-evidencias/`.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --period <AAAA-MM> --what compliance-status
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cumplimiento/<AAAA-MM>/reporte-compliance-status.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

**La diferencia entre lo declarado y lo evidenciado es el hallazgo.** Constanza no declara el estado del cumplimiento: lo declara su responsable.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-compliance-status.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what compliance-status \
    --salida <estado>/corridas/salida-compliance-status.md \
    --caso <AAAA-MM> \
    --nota "obligaciones con evidencia sobre el total, señales abiertas"
```
