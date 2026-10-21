---
description: Aprobado, ejecutado, comprometido, disponible y desviación por área y línea, contra la versión aprobada
argument-hint: "[AAAA-MM del corte] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /variance-report — Ejecución contra presupuesto

> **Dónde está la configuración:** `.criterio/presupuesto/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-budget:budget-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-budget:budget-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **variance-analysis**. Por área y línea: aprobado en el año, aprobado al corte —con la distribución mensual si la versión la trae; si no, el reporte lo dice—, ejecutado, comprometido, disponible y desviación.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --year <AAAA> --period <AAAA-MM> --what variance-report
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/presupuesto/<AAAA>/reporte-variance-report.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

Si un área declaró que está dentro del presupuesto y los números no lo sostienen, el reporte lo muestra como señal: **la diferencia entre lo declarado y lo calculado es el hallazgo**. Tomás no declara el estado del presupuesto de nadie.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-variance-report.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what variance-report \
    --salida <estado>/corridas/salida-variance-report.md \
    --caso <AAAA-MM del corte> \
    --nota "líneas sobre el umbral, gasto sin línea"
```
