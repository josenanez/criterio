---
description: La proyección al cierre del año: la del área y dos calculadas, al ritmo y al plan, cada una con su supuesto escrito
argument-hint: "[AAAA-MM del corte] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /forecast — La proyección al cierre del año

> **Dónde está la configuración:** `.criterio/presupuesto/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-budget:budget-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-budget:budget-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **forecast-method**. Dos proyecciones calculadas, cada una con su supuesto, al lado de la que entregó cada área en `30-proyecciones/`. **Ninguna es la correcta por definición**: la decisión de cuál usar es de una persona, y el reporte deja los supuestos escritos para que pueda tomarla.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --year <AAAA> --period <AAAA-MM> --what forecast
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/presupuesto/<AAAA>/reporte-forecast.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-forecast.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what forecast \
    --salida <estado>/corridas/salida-forecast.md \
    --caso <AAAA-MM del corte> \
    --nota "áreas sobre lo aprobado, proyecciones vencidas"
```
