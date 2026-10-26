---
description: Todas las facturas electrónicas del periodo contra la contabilidad —no una muestra—: sin registro, registros sin factura, diferencias y duplicados
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /einvoice-check — Facturas contra contabilidad

> **Dónde está la configuración:** `.criterio/finanzas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-finance:finance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-finance:finance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Cada XML de `30-facturacion/` se procesa con la estructura oficial —el anexo técnico de la DIAN (F-01), la ficha técnica del SRI (F-04, F-09) o la guía UBL 2.1 de la SUNAT (F-13)— y se cruza con los registros de las cuentas de ventas, compras e IVA de la configuración. Aplica **einvoice-matching**.

## Flujo

Si una factura no se pudo procesar y la persona pregunta por qué, el motor la muestra campo por campo:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" factura --file <ruta del XML>
```

El cruce del periodo:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what einvoice-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cierre/<AAAA-MM>/reporte-einvoice-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

**Sin opinión fiscal.** Clara no dice si un gasto es deducible, qué tarifa aplica ni cómo se trata una diferencia: lo que es criterio tributario queda como pregunta para la persona. Tampoco dice de memoria una tarifa, un plazo ni el valor de una unidad tributaria.

En Ecuador, los comprobantes que no son factura —notas, retenciones, guías— se identifican por su clave de acceso, y en Perú la nota de crédito, por su serie y número; sus valores no se cruzan en esta versión: el reporte los cuenta aparte.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-einvoice-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what einvoice-check \
    --salida <estado>/corridas/salida-einvoice-check.md \
    --caso <AAAA-MM> \
    --nota "facturas procesadas, cruzadas y señales"
```
