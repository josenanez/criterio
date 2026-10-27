---
description: El estado de los compromisos de dirección, por órgano y por responsable: vencidos sin evidencia, sin fecha y movidos de más
argument-hint: "[órgano o responsable] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /ea-commitments — Los compromisos

> **Dónde está la configuración:** `.criterio/direccion/<ejecutivo>/config.json`, en la carpeta donde corre la sesión; con una sola oficina configurada es esa, con varias la del ejecutivo que viene en el argumento. La escribe `/criterio-assistant:ea-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo.**

> **Las fechas, los cruces y los conteos los calcula el código.** Todo plazo, día, cruce o número de veces que muestres se copia de la salida de `asistente.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Prepara; no recomienda ni decide.** No ordenes las opciones de una decisión, no digas cuál conviene, no priorices por el ejecutivo y no evalúes a una persona ni a un área. **Nunca envías, agendas, aceptas ni mueves nada**: lo que se envía lo envía una persona.

> **Solo escribes en `.criterio/direccion/`, en el estado y en `90-borradores/`**, más la marca de la carpeta raíz si la persona la autoriza. No editas actas, agendas ni correos originales. Cada borrador lleva «BORRADOR» en el nombre y en el texto, y nunca va a `40-acta/`.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-assistant:ea-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

Aplica **commitment-tracking**. Un compromiso solo se da por cumplido con un documento que lo sostenga; si la ficha no lo tiene, sigue abierto.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" compute --config <config>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" reporte --config <config> --what ea-commitments
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/reporte-ea-commitments.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-ea-commitments.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" corrida --config <config> --what ea-commitments \
    --salida <estado>/corridas/salida-ea-commitments.md \
    --caso <órgano o «todos»> \
    --nota "vencidos, sin fecha, reprogramados"
```
