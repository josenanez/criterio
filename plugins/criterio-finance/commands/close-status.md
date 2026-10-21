---
description: El estado del cierre: lo declarado contra lo evidenciado, tarea por tarea del checklist, con la ruta crítica
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /close-status — El estado del cierre

> **Dónde está la configuración:** `.criterio/finanzas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-finance:finance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-finance:finance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Cruza cada tarea del checklist con su evidencia en `40-soportes/`, su fecha y sus dependencias, y pone al lado el estado que alguien declaró. **La diferencia entre los dos es el hallazgo.** Aplica **close-checklist** para leer el checklist y **close-record** para lo declarado.

## Flujo

**1.** Si desde la última corrida llegó una declaración del estado del cierre —«septiembre quedó cerrado»—, regístrala en `declared` de la ficha con su cita y su fecha.

**2.** Calcula y muestra:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what close-status
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cierre/<AAAA-MM>/reporte-close-status.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

**Una tarea está cumplida cuando un soporte lo prueba.** Que el checklist la marque cumplida no la cierra: queda como *cumplida sin evidencia*. La evidencia es un archivo de `40-soportes/` cuyo nombre empieza por el id de la tarea.

## Lo que Clara no hace

No declara el estado del cierre: lo declara el contralor. Clara muestra contra qué.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-close-status.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what close-status \
    --salida <estado>/corridas/salida-close-status.md \
    --caso <AAAA-MM> \
    --nota "tareas con evidencia sobre el total, señales abiertas"
```
