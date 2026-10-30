---
description: Procesa lo que cambió en el periodo, actualiza la ficha del cierre y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío para el periodo configurado"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /close-scan — Lo que cambió en el periodo

> **Dónde está la configuración:** `.criterio/finanzas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-finance:finance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-finance:finance-setup`, que registra la aceptación: este comando no produce nada sin ella.

El barrido del periodo. Solo se reprocesa lo que cambió: el inventario guarda la huella de cada archivo y dice cuál es nuevo, cuál cambió y cuál se borró.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **finance-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" inventario --config <config>
```

Reporta en dos líneas qué es nuevo, qué cambió y qué está fuera de su lugar, con el destino sugerido. No muevas nada.

**2. Lo que solo trae un documento escrito.** Si entre lo nuevo hay un correo, un informe o un acta que declara el estado del cierre, o un requerimiento del auditor que llegó en Word o PDF, conviértelo y extráelo a la ficha aplicando **close-record**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" convertir --config <config> --caso <parte de la ruta, por ejemplo 2026-09/50-auditoria>
```

Las tablas —balance, mayor, extractos, auxiliares, checklist, índice del auditor— y las facturas electrónicas en XML **no se extraen**: las procesa el motor directamente. **La excepción es Honduras**, que no tiene un esquema de factura: cada factura nueva o cambiada de `30-facturacion/` se convierte y se extrae a `invoices` de la ficha aplicando **close-record** y **einvoice-matching**, con su CAI, su rango autorizado y su fecha límite de emisión (decisión 0024).

**3. Calcula y muestra:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what close-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cierre/<AAAA-MM>/reporte-close-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga. Antes del reporte, una línea: cuántos archivos nuevos o cambiados y cuántas señales nuevas respecto de la corrida anterior.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-close-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what close-scan \
    --salida <estado>/corridas/salida-close-scan.md \
    --caso <AAAA-MM> \
    --nota "cuántos archivos nuevos o cambiados, cuántas señales"
```
