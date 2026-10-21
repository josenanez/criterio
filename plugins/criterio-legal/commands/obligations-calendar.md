---
description: Los vencimientos, los preavisos de renovación y las obligaciones de cada contrato, con lo que venció sin evidencia
argument-hint: "vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /obligations-calendar — Vencimientos, preavisos y obligaciones

> **Dónde está la configuración:** `.criterio/legal/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-legal:legal-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-legal:legal-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **contract-calendar**. Para un contrato con renovación automática, **la fecha que importa es la del preaviso**: la terminación menos los días de preaviso que dice el contrato. Pasada esa fecha sin decisión, el contrato se prorroga en sus términos.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --what obligations-calendar
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/contratos/reporte-obligations-calendar.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

Una obligación está cumplida cuando un documento de `40-ejecucion/` lo prueba, con el id de la obligación al inicio del nombre. **La decisión de renovar o terminar es de una persona**: Fidel muestra la fecha y quién decide, no recomienda.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-obligations-calendar.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what obligations-calendar \
    --salida <estado>/corridas/salida-obligations-calendar.md \
    --caso <código del contrato, o «todos»> \
    --nota "vencimientos y preavisos en la ventana, obligaciones vencidas"
```
