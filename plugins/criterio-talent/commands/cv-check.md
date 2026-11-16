---
description: Cada título, certificación y empleo de las hojas de vida contra su soporte: sin soporte, fechas que no coinciden y certificaciones vencidas
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /cv-check — Las hojas de vida contra sus soportes

> **Dónde está la configuración:** `.criterio/seleccion/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-talent:talent-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Ninguna decisión sobre una persona es tuya.** No rechazas, no descartas, no das un puntaje y no ordenas candidatos por un número: presentas cada requisito con su evidencia, en el orden del identificador del candidato. **No usas la fotografía, la edad, el sexo, el estado civil, el origen, la religión ni la salud de nadie**: si llegan, la ficha registra solo su tipo y dónde, y el motor los excluye. **No entras a redes ni buscas personas** fuera de lo que la organización entrega.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-talent:talent-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **cv-record**.

## Flujo

Cada afirmación de la ficha del periodo contra su soporte: el título, la certificación o el empleo que no tiene el documento que lo soporte, las fechas de un empleo que no son las de su certificado laboral, contadas al mes, y la certificación que el perfil exige y venció antes de la postulación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" reporte --config <config> --period <AAAA-MM> --what cv-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/seleccion/<AAAA-MM>/reporte-cv-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

Ninguna afirmación se da por falsa: se dice cuál no tiene soporte o no coincide. Una brecha entre dos empleos no es una señal.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-cv-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what cv-check \
    --salida <estado>/corridas/salida-cv-check.md \
    --caso <AAAA-MM> \
    --nota "afirmaciones sin soporte, fechas y certificaciones"
```
