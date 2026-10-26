---
description: Lo que toca hoy en la tesorería: pagos de los próximos días, obligaciones por vencer y una revisión semanal; si no toca nada, se calla
argument-hint: "vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /treasury-wake — Qué toca hoy

> **Dónde está la configuración:** `.criterio/tesoreria/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-treasury:treasury-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo, indicador— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-treasury:treasury-setup`, que registra la aceptación: este comando no produce nada sin ella.

> **Áurea nunca mueve dinero, hace un pago, entra a un portal bancario, negocia con un banco ni recomienda una inversión, un financiamiento o una cobertura.** Procesa las exportaciones que la organización ya tiene.

> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

**Si no toca nada, no produce nada.**

## Flujo

**1. Pregunta qué toca:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" despertar --config <config>
```

**2. Si `callado` es verdadero, termina aquí** —con una petición abierta nunca lo es—, en una línea.

**Las peticiones primero.** Si `peticiones` trae alguna —la dejó alguien en Rostrum, el portal—, respóndela antes de lo demás: di de quién es, qué pide y lo que los documentos y el último reporte responden, con su cita. Lo que pida criterio de una persona queda dicho como pregunta para ella. Cuando la respondas, márcala:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" responder --config <config> --id <id de la petición>
```

**3. Si toca `treasury-scan`**, aplica **finance-intake** y calcula:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" compute --config <config> --period <AAAA-MM>
```

**4. Muestra lo que toca**, con el reporte del comando que corresponda —`payment-check`, `cash-position` o `debt-watch`—:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what payment-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/tesoreria/<AAAA-MM>/reporte-payment-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

Registra también cada comando que corriste —`treasury-scan`, `payment-check`, `cash-position`, `debt-watch`— con el mismo `--caso`: así la cadencia sabe qué ya procesó.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-treasury-wake.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what treasury-wake \
    --salida <estado>/corridas/salida-treasury-wake.md \
    --caso <AAAA-MM del periodo> \
    --nota "qué tocaba y qué hizo"
```
