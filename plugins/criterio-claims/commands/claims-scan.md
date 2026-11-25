---
description: Procesa lo que cambió en las piezas, lleva cada afirmación con su soporte y cada promoción con sus condiciones a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /claims-scan — Lo que cambió en las piezas

> **Dónde está la configuración:** `.criterio/piezas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-claims:claims-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `mercadeo.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas una pieza, no juzgas la creatividad y no dices si una afirmación es verdadera.** Dices qué afirmación no tiene soporte, qué comparativa no cita su fuente, qué promoción no publica sus condiciones, qué pieza salió sin aprobación o sin identificarse como publicidad y qué base se usó sin autorización; la decisión es de legal y del área de mercadeo. **Nunca te conectas a una plataforma ni procesas los datos de una persona**: de una base de contactos procesas solo su registro.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-claims:claims-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **marketing-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" inventario --config <config>
```

**2. El registro de piezas, el de bases de contactos y el plan no se extraen: los procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **claim-record**: cada afirmación de las piezas de `10-piezas/` con el soporte de `20-soportes/` que trata de lo mismo, si es comparativa y la fuente que cita, y cada promoción de `30-promociones/` con su vigencia y sus condiciones:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" convertir --config <config> --caso 10-piezas
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" convertir --config <config> --caso 30-promociones
```

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" reporte --config <config> --period <AAAA-MM> --what claims-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/piezas/<AAAA-MM>/reporte-claims-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-claims-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" corrida --config <config> --what claims-scan \
    --salida <estado>/corridas/salida-claims-scan.md \
    --caso <AAAA-MM> \
    --nota "afirmaciones y promociones llevadas a la ficha, señales"
```
