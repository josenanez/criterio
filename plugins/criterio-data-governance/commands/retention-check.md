---
description: Cada política contra su fecha de revisión y cada conjunto contra el plazo de conservación de su tipo: lo vencido y lo que se conserva de más
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /retention-check — Las políticas y los plazos

> **Dónde está la configuración:** `.criterio/gobierno/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-data-governance:governance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `datos.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No asignas un dueño, no decides una clasificación y no borras nada.** Dices qué conjunto no tiene dueño ni clasificación, qué política se venció, qué dato pasó su plazo y qué término no está en el glosario; la decisión es del área de datos y del dueño de cada dato. **Nunca te conectas a una base ni procesas un dato personal**: procesas exportaciones, y de una base con datos personales solo sus metadatos.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-data-governance:governance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **data-policy**.

## Flujo

Cada política de la ficha contra su fecha de revisión, y cada conjunto del catálogo contra el plazo que la política de conservación fija para su tipo, desde su registro más antiguo. Qué se archiva o se borra lo decide el dueño del dato con la política.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" reporte --config <config> --period <AAAA-MM> --what retention-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/gobierno/<AAAA-MM>/reporte-retention-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-retention-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/datos.py" corrida --config <config> --what retention-check \
    --salida <estado>/corridas/salida-retention-check.md \
    --caso <AAAA-MM> \
    --nota "las políticas y los plazos"
```
