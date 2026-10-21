---
description: Procesa presupuesto, ejecución, compromisos, proyecciones y actas, actualiza cada ficha y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM del corte] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /budget-scan — Lo que cambió en el presupuesto

> **Dónde está la configuración:** `.criterio/presupuesto/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-budget:budget-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-budget:budget-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **finance-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" inventario --config <config>
```

**2. Lo que solo trae un documento escrito.** Las actas de `40-actas/` —aprobaciones, traslados, adiciones y reducciones—, lo que un área declara sobre su presupuesto y la versión que usa un informe se extraen a la ficha del presupuesto aplicando **budget-record**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" convertir --config <config> --caso presupuesto-<AAAA>/40-actas
```

El presupuesto, la contabilidad, los compromisos y las proyecciones son tablas: **no se extraen**, las procesa el motor.

**3. Calcula y muestra:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" compute --config <config> --year <AAAA> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --year <AAAA> --period <AAAA-MM> --what budget-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/presupuesto/<AAAA>/reporte-budget-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-budget-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what budget-scan \
    --salida <estado>/corridas/salida-budget-scan.md \
    --caso <AAAA-MM del corte> \
    --nota "archivos nuevos o cambiados, señales"
```
