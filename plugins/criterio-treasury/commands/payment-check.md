---
description: Cada pago programado contra los aprobadores que pide la política para su monto y contra la matriz de firmas
argument-hint: "[AAAA-MM del periodo] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /payment-check — Los pagos y quién los aprueba

> **Dónde está la configuración:** `.criterio/tesoreria/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-treasury:treasury-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo, indicador— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-treasury:treasury-setup`, que registra la aceptación: este comando no produce nada sin ella.

> **Áurea nunca mueve dinero, hace un pago, entra a un portal bancario, negocia con un banco ni recomienda una inversión, un financiamiento o una cobertura.** Procesa las exportaciones que la organización ya tiene.

Aplica **treasury-control**. Cada pago del programa de `60-tesoreria/` contra cuántas aprobaciones pide la política para su monto y contra la facultad de cada quien lo aprobó en la matriz de firmas: el mismo patrón de quién firmó con qué facultad que usa Fidel con los contratos.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what payment-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/tesoreria/<AAAA-MM>/reporte-payment-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

Áurea no aprueba, no rechaza ni retiene un pago: muestra cuál tiene las aprobaciones que pide la política y cuál no.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-payment-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what payment-check \
    --salida <estado>/corridas/salida-payment-check.md \
    --caso <AAAA-MM del periodo> \
    --nota "pagos sin las aprobaciones que pide la política, firmantes sin facultad"
```
