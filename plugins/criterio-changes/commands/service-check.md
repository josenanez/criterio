---
description: Cada servicio del catálogo contra el nivel que se acordó con el negocio: el que no lo cumplió
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /service-check — Cada servicio contra su nivel

> **Dónde está la configuración:** `.criterio/cambios/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-changes:changes-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `tecnologia.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas un cambio, no decides una arquitectura y no calificas un incidente.** Dices qué cambio llegó a producción sin aprobación o sin su revisión, qué despliegue no corresponde a ningún cambio, qué incidente mayor no tiene su causa y qué servicio quedó por debajo de su nivel; la decisión es del comité de cambios y del área de tecnología. **Nunca te conectas a una herramienta ni a un servidor, y no procesas la seguridad**, que es de la familia CISO.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-changes:changes-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **technology-policy**.

## Flujo

La disponibilidad de cada servicio en el periodo contra el nivel acordado en el catálogo de servicios. El nivel lo acuerda el área con el negocio: aquí se dice qué servicio no lo cumplió.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" reporte --config <config> --period <AAAA-MM> --what service-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cambios/<AAAA-MM>/reporte-service-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-service-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" corrida --config <config> --what service-check \
    --salida <estado>/corridas/salida-service-check.md \
    --caso <AAAA-MM> \
    --nota "los servicios contra su nivel"
```
