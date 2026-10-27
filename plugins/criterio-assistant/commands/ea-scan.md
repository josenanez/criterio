---
description: Procesa la agenda, las sesiones de los órganos y la correspondencia, y escribe las fichas con cada dato citado
argument-hint: "[órgano o fecha] o vacío para todo"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /ea-scan — Procesar

> **Dónde está la configuración:** `.criterio/direccion/<ejecutivo>/config.json`, en la carpeta donde corre la sesión; con una sola oficina configurada es esa, con varias la del ejecutivo que viene en el argumento. La escribe `/criterio-assistant:ea-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo.**

> **Las fechas, los cruces y los conteos los calcula el código.** Todo plazo, día, cruce o número de veces que muestres se copia de la salida de `asistente.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Prepara; no recomienda ni decide.** No ordenes las opciones de una decisión, no digas cuál conviene, no priorices por el ejecutivo y no evalúes a una persona ni a un área. **Nunca envías, agendas, aceptas ni mueves nada**: lo que se envía lo envía una persona.

> **Solo escribes en `.criterio/direccion/`, en el estado y en `90-borradores/`**, más la marca de la carpeta raíz si la persona la autoriza. No editas actas, agendas ni correos originales. Cada borrador lleva «BORRADOR» en el nombre y en el texto, y nunca va a `40-acta/`.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-assistant:ea-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **ea-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" inventario --config <config>
```

**2. La agenda la procesa el código**, no tú: eventos, repeticiones y zonas horarias.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" agenda --config <config>
```

Si la exportación es más vieja que el umbral, el motor lo avisa y no calcula cruces: dilo así.

**3. Lo nuevo o cambiado se extrae a la ficha de su sesión**, `<estado>/reuniones/<órgano>-<AAAA-MM-DD>.json`, aplicando **meeting-record**: de la convocatoria, el orden del día; del acta firmada, los acuerdos y los compromisos; y de cada punto que pide una decisión, su ficha con **decision-brief**. Los compromisos siguen **commitment-tracking**: cada uno es del acta donde nació, uno movido lleva su historia en `reschedules` y uno vencido se busca en el material antes de dejarlo abierto. Los de proyecto son de Samuel: se citan, no se copian.

**4. Cada correo guardado tiene su ficha**, `<estado>/correspondencia/<nombre del archivo sin extensión>.json`, aplicando **correspondence-record**: si pide respuesta, qué pide y para cuándo, con su cita. Los encabezados —quién, cuándo, a qué responde— los procesa el motor.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" convertir --config <config>
```

**5. Calcula y muestra:**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" compute --config <config>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" reporte --config <config> --what ea-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/reporte-ea-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

Si trae `record_issues`, corrige esa parte de la ficha y vuelve a calcular.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-ea-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/asistente.py" corrida --config <config> --what ea-scan \
    --salida <estado>/corridas/salida-ea-scan.md \
    --caso <órgano o «todo»> \
    --nota "sesiones y correos nuevos o cambiados, señales"
```
