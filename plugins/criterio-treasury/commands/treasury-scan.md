---
description: Procesa extractos, programa de pagos, flujo proyectado y el registro de deuda, y dice qué señales nuevas aparecieron en la tesorería
argument-hint: "[AAAA-MM del periodo] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /treasury-scan — Lo que cambió en la tesorería

> **Dónde está la configuración:** `.criterio/tesoreria/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-treasury:treasury-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo, indicador— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-treasury:treasury-setup`, que registra la aceptación: este comando no produce nada sin ella.

> **Áurea nunca mueve dinero, hace un pago, entra a un portal bancario, negocia con un banco ni recomienda una inversión, un financiamiento o una cobertura.** Procesa las exportaciones que la organización ya tiene.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **finance-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" inventario --config <config>
```

Los extractos, el programa de pagos, el flujo proyectado, la política, la matriz de firmas, el registro de la deuda y los covenants son tablas: **no se extraen**, las procesa el motor.

**2. Calcula y muestra:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what treasury-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/tesoreria/<AAAA-MM>/reporte-treasury-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-treasury-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what treasury-scan \
    --salida <estado>/corridas/salida-treasury-scan.md \
    --caso <AAAA-MM del periodo> \
    --nota "archivos nuevos o cambiados, señales"
```
