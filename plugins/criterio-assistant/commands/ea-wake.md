---
description: Lo que toca hoy en la oficina — sesiones en la ventana, actas pendientes, plazos de la correspondencia — y si no toca nada, se calla
argument-hint: "[AAAA-MM-DD para simular otro día]"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /ea-wake — Lo que toca hoy

> **Dónde está la configuración:** `.criterio/direccion/<ejecutivo>/config.json`, en la carpeta donde corre la sesión; con una sola oficina configurada es esa, con varias la del ejecutivo que viene en el argumento. La escribe `/criterio-assistant:ea-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo.**

> **Las fechas, los cruces y los conteos los calcula el código.** Todo plazo, día, cruce o número de veces que muestres se copia de la salida de `asistente.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Prepara; no recomienda ni decide.** No ordenes las opciones de una decisión, no digas cuál conviene, no priorices por el ejecutivo y no evalúes a una persona ni a un área. **Nunca envías, agendas, aceptas ni mueves nada**: lo que se envía lo envía una persona.

> **Solo escribes en `.criterio/direccion/`, en el estado y en `90-borradores/`**, más la marca de la carpeta raíz si la persona la autoriza. No editas actas, agendas ni correos originales. Cada borrador lleva «BORRADOR» en el nombre y en el texto, y nunca va a `40-acta/`.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-assistant:ea-setup`, que registra la aceptación: este comando no produce nada sin ella.

> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

**Si no toca nada, no produce nada.**

## Flujo

**1. Pregunta qué toca:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" despertar --config <config>
```

**2. Si `callado` es verdadero, termina aquí** —con una petición abierta nunca lo es—, en una línea.

**Las peticiones primero.** Si `peticiones` trae alguna —la dejó alguien en Rostrum—, respóndela antes de lo demás con lo que los documentos y el último reporte dicen, con su cita. Cuando la respondas, márcala:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" responder --config <config> --id <id de la petición>
```

**3. Corre lo que toca**, en el orden que da el motor, siguiendo cada comando: `ea-scan`, `ea-prep`, `ea-minutes`, `ea-mail` o `ea-weekly`.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-ea-wake.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" corrida --config <config> --what ea-wake \
    --salida <estado>/corridas/salida-ea-wake.md \
    --caso lo que tocó \
    --nota "qué corrió y qué encontró"
```
