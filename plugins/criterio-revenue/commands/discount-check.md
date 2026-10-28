---
description: Cada descuento contra el nivel de la matriz que lo cubre y la aprobación que ese nivel pide
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /discount-check — Los descuentos contra su política

> **Dónde está la configuración:** `.criterio/ingresos/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RFC que viene en el argumento. La escribe `/criterio-revenue:revenue-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, porcentaje, día o conteo que muestres se copia de la salida de `ventas.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No escribes en el CRM ni contactas a nadie, y no calificas personas.** No cambies una oportunidad, no apruebes un descuento, no fijes una meta y no liquides una comisión. Dices qué oportunidad, qué cotización o qué liquidación no tiene lo que la sostiene, nunca quién vende mejor. Los datos de contacto de los clientes —correos, teléfonos— no entran a la ficha.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-revenue:revenue-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **discount-policy**.

## Flujo

Cada cotización de la ficha contra la matriz de descuentos de `00-referencia/`. **Ningún descuento lo apruebas tú**: dices cuál no tiene la aprobación que pide su nivel.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" reporte --config <config> --period <AAAA-MM> --what discount-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/ingresos/<AAAA-MM>/reporte-discount-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-discount-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" corrida --config <config> --what discount-check \
    --salida <estado>/corridas/salida-discount-check.md \
    --caso <AAAA-MM> \
    --nota "descuentos fuera de la política"
```
