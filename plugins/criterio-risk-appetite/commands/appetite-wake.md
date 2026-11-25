---
description: Lo que toca hoy en el apetito por riesgo — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /appetite-wake — Lo que toca hoy

> **Primero, antes que todo lo demás —antes de buscar la configuración y de los términos—, una sola llamada:**
> `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" despertar --what appetite-wake --registrar`
> Pregunta a todas las configuraciones de este agente en la carpeta. **Si `callado` es verdadero, el motor ya dejó la corrida registrada: muestra su `linea` y termina ahí**, sin otra llamada. Si no, sigue con lo de abajo para cada entidad de `entidades` que no esté callada; si una trae `terminos_vigentes` falso, aplica primero la regla de los términos.

> **Dónde está la configuración:** `.criterio/apetito/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-risk-appetite:appetite-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `riesgos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No fijas ni cambias un límite, no apruebas un exceso y no aceptas un riesgo.** Dices qué exposición supera su límite sin plan ni aprobación, qué reporte llegó tarde, qué límite no tiene dueño o pasó su revisión, qué riesgo alto no tiene con qué medirse y si la declaración de apetito se venció; la decisión es de la junta, del comité de riesgos y de las áreas. **Nunca te conectas a un sistema ni calculas capital ni valor en riesgo**: procesas exportaciones y las cifras que reportan las áreas.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-risk-appetite:appetite-setup`, que registra la aceptación: este comando no produce nada sin ella.

> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

**Si no toca nada, no produce nada.**

## Flujo

**1. Pregunta qué toca:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" despertar --config <config>
```

**2. Si `callado` es verdadero, termina aquí** —con una petición abierta nunca lo es—, en una línea.

**Las peticiones primero.** Si `peticiones` trae alguna —la dejó alguien en Rostrum, el portal—, respóndela antes de lo demás: di de quién es, qué pide y lo que los documentos y el último reporte responden, con su cita. Lo que pida criterio de una persona queda dicho como pregunta para ella. Cuando la respondas, márcala:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" responder --config <config> --id <id de la petición>
```

**3. Si toca `appetite-scan`**, haz su flujo completo: el inventario y lo que va a la ficha.

**4. Muestra lo que toca** —`toca` dice cuál: limit-check, framework-check o coverage-check—, un reporte por comando:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" reporte --config <config> --period <AAAA-MM> --what <comando>
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/apetito/<AAAA-MM>/reporte-<comando>.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-appetite-wake.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/riesgos.py" corrida --config <config> --what appetite-wake \
    --salida <estado>/corridas/salida-appetite-wake.md \
    --caso <AAAA-MM> \
    --nota "qué tocaba y qué hizo"
```


Registra también cada comando que corriste —`appetite-scan` y los de `toca`— con el mismo `--caso`.
