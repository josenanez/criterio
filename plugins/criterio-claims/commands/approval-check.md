---
description: Cada pieza con su aprobación y su identificación como publicidad, y cada base de contactos con su autorización: lo que salió sin el sí de la política
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /approval-check — La aprobación y la autorización

> **Dónde está la configuración:** `.criterio/piezas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-claims:claims-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `mercadeo.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No apruebas una pieza, no juzgas la creatividad y no dices si una afirmación es verdadera.** Dices qué afirmación no tiene soporte, qué comparativa no cita su fuente, qué promoción no publica sus condiciones, qué pieza salió sin aprobación o sin identificarse como publicidad y qué base se usó sin autorización; la decisión es de legal y del área de mercadeo. **Nunca te conectas a una plataforma ni procesas los datos de una persona**: de una base de contactos procesas solo su registro.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-claims:claims-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **marketing-policy**.

## Flujo

Cada pieza publicada contra su fecha de aprobación; cada pieza pagada a un influenciador contra su identificación como publicidad; y cada base de contactos que usa una campaña contra su autorización para mercadeo en el registro de bases. Quién aprueba lo fija la política: aquí se dice qué salió sin aprobación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" reporte --config <config> --period <AAAA-MM> --what approval-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/piezas/<AAAA-MM>/reporte-approval-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-approval-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/mercadeo.py" corrida --config <config> --what approval-check \
    --salida <estado>/corridas/salida-approval-check.md \
    --caso <AAAA-MM> \
    --nota "la aprobación de las piezas y la autorización de las bases"
```
