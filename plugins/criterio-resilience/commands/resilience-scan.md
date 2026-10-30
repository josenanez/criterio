---
description: Procesa los incidentes, las revisiones y las pruebas nuevas, los lleva a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /resilience-scan — Lo que cambió en la respuesta

> **Dónde está la configuración:** `.criterio/resiliencia/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-resilience:resilience-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, hora o conteo que muestres se copia de la salida de `seguridad.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No notificas a nadie, no declaras ni cierras un incidente y no ejecutas una prueba ni una restauración.** Dices qué incidente se contuvo fuera de plazo, qué notificación de la matriz se hizo tarde o no se hizo y qué prueba pasó su fecha; quién notifica y qué se hace es de una persona. **Nunca abres credenciales, llaves ni respaldos**: el motor los lista en `excluidos` y no se abren.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-resilience:resilience-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior, y lo que no se abre. Aplica **security-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" inventario --config <config>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" excluidos --config <config>
```

**2. Lo que solo trae un documento escrito se extrae a la ficha del periodo**, aplicando **incident-record**: cada incidente nuevo de `70-incidentes/` con su severidad, la detección, la contención y el cierre con su hora, si hubo datos personales o clientes afectados y cada notificación con su destinatario, su hora y su constancia; cada revisión de `80-revisiones/`; y, con **continuity-record**, cada prueba de `90-continuidad/` con su fecha y su resultado:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" convertir --config <config> --caso 70-incidentes
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" convertir --config <config> --caso 80-revisiones
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" convertir --config <config> --caso 90-continuidad
```

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" reporte --config <config> --period <AAAA-MM> --what resilience-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/resiliencia/<AAAA-MM>/reporte-resilience-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-resilience-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/seguridad.py" corrida --config <config> --what resilience-scan \
    --salida <estado>/corridas/salida-resilience-scan.md \
    --caso <AAAA-MM> \
    --nota "incidentes, revisiones y pruebas llevados a la ficha, señales"
```
