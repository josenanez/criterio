---
description: Procesa lo que cambió en la selección, lleva cada hoja de vida nueva a la ficha del periodo y dice qué señales nuevas aparecieron
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /talent-scan — Lo que cambió en la selección

> **Dónde está la configuración:** `.criterio/seleccion/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-talent:talent-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Ninguna decisión sobre una persona es tuya.** No rechazas, no descartas, no das un puntaje y no ordenas candidatos por un número: presentas cada requisito con su evidencia, en el orden del identificador del candidato. **No usas la fotografía, la edad, el sexo, el estado civil, el origen, la religión ni la salud de nadie**: si llegan, la ficha registra solo su tipo y dónde, y el motor los excluye. **No entras a redes ni buscas personas** fuera de lo que la organización entrega.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-talent:talent-setup`, que registra la aceptación: este comando no produce nada sin ella.

## Flujo

**1. El inventario**, contra el de la corrida anterior. Aplica **talent-intake**:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" inventario --config <config>
```

**2. Las tablas de `20-vacantes/`, `40-autorizaciones/` y `50-ats/` no se extraen:** las procesa el motor. Lo que solo trae un documento escrito se extrae a la ficha del periodo, aplicando **cv-record**: cada hoja de vida nueva de `30-candidatos/` con cada título, certificación y empleo, su soporte y sus fechas, la evidencia de cada requisito del perfil y lo que llegó y no se debe tratar —solo su tipo y dónde—:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" convertir --config <config> --caso 30-candidatos
```

**Una fotografía no se abre.** Una imagen cuyo nombre dice que es un documento —`diploma`, `titulo`, `acta`, `certificado`, `tarjeta`, `certificacion`— es un soporte escaneado: ábrela solo para confirmar que es ese documento y cítala en `support` de lo que soporta. Cualquier otra imagen de la carpeta de un candidato es una fotografía: no se abre, va a `protected` como `fotografia` con su ruta, y el motor la excluye. El nombre del candidato no va a la ficha: va su identificador.

**3. Calcula y muestra.** Si `record_issues` trae un documento que no está en la ficha, llévalo o anótalo en `reviewed` con su motivo, y vuelve a calcular:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" compute --config <config> --period <AAAA-MM>
```

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" reporte --config <config> --period <AAAA-MM> --what talent-scan
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/seleccion/<AAAA-MM>/reporte-talent-scan.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-talent-scan.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what talent-scan \
    --salida <estado>/corridas/salida-talent-scan.md \
    --caso <AAAA-MM> \
    --nota "hojas de vida llevadas a la ficha, lo excluido, señales"
```
