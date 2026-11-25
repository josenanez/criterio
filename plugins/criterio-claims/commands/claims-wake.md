---
description: Lo que toca hoy en las piezas — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /claims-wake — Lo que toca hoy

> **Primero, antes que todo lo demás —antes de buscar la configuración y de los términos—, una sola llamada:**
> `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" despertar --what claims-wake --registrar`
> Pregunta a todas las configuraciones de esta agente en la carpeta. **Si `callado` es verdadero, el motor ya dejó la corrida registrada: muestra su `linea` y termina ahí**, sin otra llamada. Si no, sigue con lo de abajo para cada entidad de `entidades` que no esté callada; si una trae `terminos_vigentes` falso, aplica primero la regla de los términos.

> **Dónde está la configuración:** `.criterio/piezas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-claims:claims-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `mercadeo.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas una pieza, no juzgas la creatividad y no dices si una afirmación es verdadera.** Dices qué afirmación no tiene soporte, qué comparativa no cita su fuente, qué promoción no publica sus condiciones, qué pieza salió sin aprobación o sin identificarse como publicidad y qué base se usó sin autorización; la decisión es de legal y del área de mercadeo. **Nunca te conectas a una plataforma ni procesas los datos de una persona**: de una base de contactos procesas solo su registro.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-claims:claims-setup`, que registra la aceptación: este comando no produce nada sin ella.

> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

**Si no toca nada, no produce nada.**

## Flujo

**1. Pregunta qué toca:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" despertar --config <config>
```

**2. Si `callado` es verdadero, termina aquí** —con una petición abierta nunca lo es—, en una línea.

**Las peticiones primero.** Si `peticiones` trae alguna —la dejó alguien en Rostrum, el portal—, respóndela antes de lo demás: di de quién es, qué pide y lo que los documentos y el último reporte responden, con su cita. Lo que pida criterio de una persona queda dicho como pregunta para ella. Cuando la respondas, márcala:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" responder --config <config> --id <id de la petición>
```

**3. Si toca `claims-scan`**, haz su flujo completo: el inventario y lo que va a la ficha.

**4. Muestra lo que toca** —`toca` dice cuál: claim-check, promo-check o approval-check—, un reporte por comando:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" reporte --config <config> --period <AAAA-MM> --what <comando>
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/piezas/<AAAA-MM>/reporte-<comando>.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-claims-wake.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" corrida --config <config> --what claims-wake \
    --salida <estado>/corridas/salida-claims-wake.md \
    --caso <AAAA-MM> \
    --nota "qué tocaba y qué hizo"
```


Registra también cada comando que corriste —`claims-scan` y los de `toca`— con el mismo `--caso`.
