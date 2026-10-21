---
description: El registro de contratos contra lo que dicen los documentos: contratos sin registro, registros sin documento, estados y valores que no cuadran
argument-hint: "vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /contract-register — El registro contra los documentos

> **Dónde está la configuración:** `.criterio/legal/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-legal:legal-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-legal:legal-setup`, que registra la aceptación: este comando no produce nada sin ella.

Cruza el registro que lleva la organización con las carpetas y con las fichas. Aplica **contract-record**.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --what contract-register
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/contratos/reporte-contract-register.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

**El estado de un contrato lo dicen sus fechas**, no la columna del registro: un contrato que el registro dice vigente y cuya terminación pasó es un hallazgo. Con renovación automática y sin decisión de terminar, el contrato se prorroga en sus términos y el motor lo cuenta así.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-contract-register.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what contract-register \
    --salida <estado>/corridas/salida-contract-register.md \
    --caso <código del contrato, o «todos»> \
    --nota "contratos sin registro, registros sin documento, diferencias"
```
