---
description: El material del comité de presupuesto como paquete de decisiones: cada una con su cifra, su cita y quién la toma
argument-hint: "[AAAA-MM del corte] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /budget-committee-pack — El material del comité

> **Dónde está la configuración:** `.criterio/presupuesto/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-budget:budget-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras las calcula el código.** Toda cifra que muestres —saldo, diferencia, porcentaje, días, conteo— se copia de la salida de `finanzas.py`, con todos sus dígitos. Si el motor no la da, no se escribe: se dice qué dato falta para calcularla.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-budget:budget-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **committee-pack**. Los puntos de decisión son las líneas sobre el umbral, las proyecciones sobre lo aprobado, los traslados sin acta y los compromisos del comité anterior con su evidencia.

## Flujo

**1.** Del acta del comité anterior en `40-actas/`, registra sus compromisos en `committee_commitments` de la ficha aplicando **budget-record**, con su estado y la evidencia que lo prueba.

**2.** Calcula y muestra:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" reporte --config <config> --year <AAAA> --period <AAAA-MM> --what budget-committee-pack
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/presupuesto/<AAAA>/reporte-budget-committee-pack.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras que el reporte no traiga.

**El paquete no recomienda la decisión.** Presenta cada punto con su cifra y su cita, y deja escrito quién decide; la decisión es del comité.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-budget-committee-pack.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/finanzas.py" corrida --config <config> --what budget-committee-pack \
    --salida <estado>/corridas/salida-budget-committee-pack.md \
    --caso <AAAA-MM del corte> \
    --nota "puntos de decisión, compromisos del comité anterior"
```
