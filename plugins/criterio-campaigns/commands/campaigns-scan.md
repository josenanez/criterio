---
description: Procesa lo que cambió en las campañas, lleva cada resultado nuevo del informe a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /campaigns-scan — Lo que cambió en las campañas

> **Dónde está la configuración:** `.criterio/campanas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-campaigns:campaigns-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `mercadeo.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas un presupuesto, no juzgas una campaña y no decides cuál cifra es la correcta.** Dices qué campaña pasó su presupuesto, qué factura de pauta no tiene campaña ni orden, qué campaña no tiene meta, cuál siguió después de su fin y qué resultado no coincide con la plataforma; la decisión es del área de mercadeo y de quien firma el informe. **Nunca te conectas a una plataforma de pauta ni de analítica**: procesas sus exportaciones.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-campaigns:campaigns-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **marketing-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" inventario --config <config>
```

**2. El plan, las facturas de pauta y la exportación de la plataforma no se extraen: los procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **result-record**: cada resultado del informe de mercadeo de `50-campanas/`, con su campaña, su indicador, su valor y la fecha de corte que el informe declara:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" convertir --config <config> --caso 50-campanas
```

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" reporte --config <config> --period <AAAA-MM> --what campaigns-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/campanas/<AAAA-MM>/reporte-campaigns-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-campaigns-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" corrida --config <config> --what campaigns-scan \
    --salida <estado>/corridas/salida-campaigns-scan.md \
    --caso <AAAA-MM> \
    --nota "resultados llevados a la ficha, señales"
```
