---
description: Lo que el comité de auditoría tiene que saber: lo vencido, lo repetido, los riesgos aceptados sin escalar y los hallazgos externos fuera del registro
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /committee-brief — Lo que el comité tiene que saber

> **Dónde está la configuración:** `.criterio/seguimiento/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-remediation:remediation-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `auditoria.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No cierras un hallazgo, no validas una evidencia por tu cuenta, no aceptas un riesgo y no comunicas nada al comité.** Dices qué plan venció sin evidencia, qué cierre no tiene con qué sostenerse, qué hallazgo vuelve y qué riesgo aceptado no llegó a quien debía llegar; lo que se concluye es del responsable de auditoría. **Las Normas Globales de Auditoría Interna se citan por su número y su título**, nunca por su texto.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-remediation:remediation-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **follow-up-record**.

## Flujo

Lo vencido sin evidencia, lo que vuelve, cada riesgo aceptado por encima del apetito que no se discutió con la alta dirección o que, sin resolverse, no llegó al consejo (norma 11.5), y cada hallazgo de un informe externo que no está en el registro. Es el material: lo que se concluye y se comunica al comité es del responsable de auditoría.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" reporte --config <config> --period <AAAA-MM> --what committee-brief
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/seguimiento/<AAAA-MM>/reporte-committee-brief.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-committee-brief.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" corrida --config <config> --what committee-brief \
    --salida <estado>/corridas/salida-committee-brief.md \
    --caso <AAAA-MM> \
    --nota "el material del comité"
```
