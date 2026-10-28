---
description: De lo ganado a lo firmado y a lo facturado: lo ganado sin contrato en las fichas de Fidel y lo firmado sin factura en las de Clara
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /won-to-invoice — De lo ganado a la factura

> **Dónde está la configuración:** `.criterio/ingresos/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RFC que viene en el argumento. La escribe `/criterio-revenue:revenue-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, porcentaje, día o conteo que muestres se copia de la salida de `ventas.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No escribes en el CRM ni contactas a nadie, y no calificas personas.** No cambies una oportunidad, no apruebes un descuento, no fijes una meta y no liquides una comisión. Dices qué oportunidad, qué cotización o qué liquidación no tiene lo que la sostiene, nunca quién vende mejor. Los datos de contacto de los clientes —correos, teléfonos— no entran a la ficha.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-revenue:revenue-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **won-to-cash**.

## Flujo

Los contratos son los de las fichas de Fidel y las facturas, las de las de Clara: **no vuelvas a procesar un contrato ni una factura**. Una cuenta sin identificación en la tabla de cuentas se dice, no se completa.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" reporte --config <config> --period <AAAA-MM> --what won-to-invoice
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/ingresos/<AAAA-MM>/reporte-won-to-invoice.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-won-to-invoice.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ventas.py" corrida --config <config> --what won-to-invoice \
    --salida <estado>/corridas/salida-won-to-invoice.md \
    --caso <AAAA-MM> \
    --nota "lo ganado sin contrato y lo firmado sin factura"
```
