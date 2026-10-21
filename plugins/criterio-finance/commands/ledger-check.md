---
description: El cuadre del balance de comprobación y del libro mayor, cuenta por cuenta, y los saldos contrarios a su naturaleza
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /ledger-check — El cuadre

> **Dónde está la configuración:** `.criterio/finanzas/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-finance:finance-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-finance:finance-setup`, que registra la aceptación: este comando no produce nada sin ella.

Débitos contra créditos; saldo inicial más movimientos contra saldo final; el mayor contra el balance, cuenta por cuenta; y los saldos contrarios a la naturaleza que declara el plan de cuentas de la organización. Aplica **ledger-tieout**.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --period <AAAA-MM> --what ledger-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/cierre/<AAAA-MM>/reporte-ledger-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

Un saldo contrario a la naturaleza no es una señal: se lista para que alguien lo mire, porque puede tener explicación. Clara no registra asientos ni los corrige.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-ledger-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what ledger-check \
    --salida <estado>/corridas/salida-ledger-check.md \
    --caso <AAAA-MM> \
    --nota "diferencia general, cuentas con diferencia"
```
