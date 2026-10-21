---
description: El índice del paquete del auditor: cada requerimiento con su respuesta, su soporte y su estado; no mueve ni copia archivos
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /audit-pack — El paquete del auditor

> **Dónde está la configuración:** `.criterio/finanzas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-finance:finance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-finance:finance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **audit-support**. El índice de requerimientos llega como una tabla del auditor en `50-auditoria/requerimientos/`; las respuestas van en `50-auditoria/respuestas/`, con el id del requerimiento al inicio del nombre.

## Flujo

**1.** Si un requerimiento llegó en Word, PDF o correo y no está en la tabla, conviértelo y extráelo a `audit_requests` de la ficha aplicando **close-record**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" convertir --config <config> --caso <AAAA-MM>/50-auditoria
```

**2.** Calcula y muestra:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what audit-pack
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cierre/<AAAA-MM>/reporte-audit-pack.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

El índice cita dónde está cada archivo; no lo mueve ni lo copia.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-audit-pack.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what audit-pack \
    --salida <estado>/corridas/salida-audit-pack.md \
    --caso <AAAA-MM> \
    --nota "requerimientos, respondidos con soporte, vencidos"
```
