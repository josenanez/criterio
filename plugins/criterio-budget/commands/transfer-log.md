---
description: Cada traslado, adición o reducción del presupuesto con el acta que lo aprueba, y los que no la tienen
argument-hint: "[AAAA-MM del corte] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /transfer-log — Traslados y actas

> **Dónde está la configuración:** `.criterio/presupuesto/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-budget:budget-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-budget:budget-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **transfer-control**. El motor compara cada versión de `10-aprobado/` con la anterior, línea por línea, y cruza cada cambio con el acta que lo aprueba.

## Flujo

**1.** Si hay actas nuevas en `40-actas/`, conviértelas y registra sus movimientos en `minutes` de la ficha aplicando **budget-record**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" convertir --config <config> --caso presupuesto-<AAAA>/40-actas
```

**2.** Calcula y muestra:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --year <AAAA> --period <AAAA-MM> --what transfer-log
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/presupuesto/<AAAA>/reporte-transfer-log.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

Un traslado deja igual el total; una adición o una reducción lo cambia, y el reporte las muestra aparte. Un acta cuyo movimiento no aparece en ninguna versión se lista como *acta sin cambio aplicado*.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-transfer-log.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what transfer-log \
    --salida <estado>/corridas/salida-transfer-log.md \
    --caso <AAAA-MM del corte> \
    --nota "cambios, con acta y sin acta"
```
