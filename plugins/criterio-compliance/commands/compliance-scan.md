---
description: Procesa lo que cambió en la carpeta de cumplimiento, actualiza la ficha y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /compliance-scan — Lo que cambió

> **Dónde está la configuración:** `.criterio/cumplimiento/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-compliance:compliance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-compliance:compliance-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **legal-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" inventario --config <config>
```

**2. Lo que solo trae un documento escrito** —lo que declara el informe de `20-reportes/`, las normas nuevas de un boletín de `30-normativa/`— se extrae a la ficha aplicando **compliance-record**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" convertir --config <config> --caso 30-normativa
```

La matriz, el índice de políticas, el registro normativo y el de casos son tablas: las procesa el motor.

**3. Calcula y muestra:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --period <AAAA-MM> --what compliance-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cumplimiento/<AAAA-MM>/reporte-compliance-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-compliance-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what compliance-scan \
    --salida <estado>/corridas/salida-compliance-scan.md \
    --caso <AAAA-MM> \
    --nota "archivos nuevos o cambiados, señales"
```
