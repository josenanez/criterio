---
description: Cada plan de acción contra su responsable, su fecha y sus reprogramaciones: los que no tienen plan, los vencidos y los que se corren una y otra vez
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /action-status — Los planes contra su fecha

> **Dónde está la configuración:** `.criterio/seguimiento/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-remediation:remediation-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `auditoria.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No cierras un hallazgo, no validas una evidencia por tu cuenta, no aceptas un riesgo y no comunicas nada al comité.** Dices qué plan venció sin evidencia, qué cierre no tiene con qué sostenerse, qué hallazgo vuelve y qué riesgo aceptado no llegó a quien debía llegar; lo que se concluye es del responsable de auditoría. **Las Normas Globales de Auditoría Interna se citan por su número y su título**, nunca por su texto.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-remediation:remediation-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **follow-up-record** y **audit-methodology**.

## Flujo

Cada hallazgo comunicado del registro con su plan, su responsable y su fecha (norma 15.1); cada plan vencido con su evidencia o la explicación documentada del atraso, de la ficha (norma 15.2); y cada plan cuya fecha se corrió más veces de las que permite la metodología.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" reporte --config <config> --period <AAAA-MM> --what action-status
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/seguimiento/<AAAA-MM>/reporte-action-status.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-action-status.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/auditoria.py" corrida --config <config> --what action-status \
    --salida <estado>/corridas/salida-action-status.md \
    --caso <AAAA-MM> \
    --nota "los planes contra su fecha"
```
