---
description: Cada candidato contra su autorización de tratamiento de datos y contra la conservación de la política; lo que llegó y no se debe tratar
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /privacy-check — La autorización y la conservación de los datos

> **Dónde está la configuración:** `.criterio/seleccion/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-talent:talent-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día o conteo que muestres se copia de la salida de `talento.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Ninguna decisión sobre una persona es tuya.** No rechazas, no descartas, no das un puntaje y no ordenas candidatos por un número: presentas cada requisito con su evidencia, en el orden del identificador del candidato. **No usas la fotografía, la edad, el sexo, el estado civil, el origen, la religión ni la salud de nadie**: si llegan, la ficha registra solo su tipo y dónde, y el motor los excluye. **No entras a redes ni buscas personas** fuera de lo que la organización entrega.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-talent:talent-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **selection-policy**.

## Flujo

Cada candidato de la ficha del periodo contra el registro de autorizaciones —que exista y sea anterior a recibir sus datos— y contra los días de conservación de la política cuando su proceso terminó; y lo que llegó y no se debe tratar, que se excluye.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" reporte --config <config> --period <AAAA-MM> --what privacy-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/seleccion/<AAAA-MM>/reporte-privacy-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

No borras ni mueves los datos de nadie: dices cuáles pasaron su conservación. La supresión la hace una persona.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-privacy-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/talento.py" corrida --config <config> --what privacy-check \
    --salida <estado>/corridas/salida-privacy-check.md \
    --caso <AAAA-MM> \
    --nota "autorizaciones, conservación y lo excluido"
```
