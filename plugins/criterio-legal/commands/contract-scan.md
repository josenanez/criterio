---
description: Procesa lo que cambió en los contratos, actualiza la ficha de cada uno y dice qué señales nuevas aparecieron
argument-hint: "[código del contrato] o vacío para todos"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /contract-scan — Lo que cambió en los contratos

> **Dónde está la configuración:** `.criterio/legal/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-legal:legal-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-legal:legal-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **legal-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" inventario --config <config>
```

**2. Lo nuevo o cambiado se extrae a la ficha** de su contrato, aplicando **contract-record**: el contrato y sus otrosíes de `10-contrato/`, las pólizas de `20-garantias/`, el certificado de `30-contraparte/`. El registro, los pagos y la matriz de atribuciones son tablas: **no se extraen**, las procesa el motor.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" convertir --config <config> --caso contratos
```

**3. Calcula y muestra:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" compute --config <config>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --what contract-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/contratos/reporte-contract-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-contract-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what contract-scan \
    --salida <estado>/corridas/salida-contract-scan.md \
    --caso <código del contrato, o «todos»> \
    --nota "contratos nuevos o cambiados, señales"
```
