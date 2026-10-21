---
description: Lo que toca hoy en los contratos — vencimientos y preavisos que entran en la ventana, documentos nuevos — y si no toca nada, se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /legal-wake — Lo que toca hoy

> **Dónde está la configuración:** `.criterio/legal/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-legal:legal-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-legal:legal-setup`, que registra la aceptación: este comando no produce nada sin ella.

> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

**Si no toca nada, no produce nada.**

## Flujo

**1. Pregunta qué toca:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" despertar --config <config>
```

**2. Si `callado` es verdadero, termina aquí**, en una línea.

**3. Si toca `contract-scan`**, aplica **legal-intake** y haz el barrido:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" inventario --config <config>
```

**4. Muestra el calendario** si hay vencimientos, preavisos u obligaciones en la ventana:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --what obligations-calendar
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/contratos/reporte-obligations-calendar.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-legal-wake.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what legal-wake \
    --salida <estado>/corridas/salida-legal-wake.md \
    --caso <código del contrato, o «todos»> \
    --nota "qué tocaba y qué hizo"
```


Registra también cada comando que corriste —`contract-scan`, `obligations-calendar`— con el mismo `--caso`: así la cadencia sabe que ya corrió hoy.
