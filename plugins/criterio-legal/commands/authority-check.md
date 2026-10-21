---
description: Quién firmó cada contrato y con qué facultad según la matriz de atribuciones, qué no tiene la firma de las dos partes y qué certificado estaba vencido
argument-hint: "vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
---

# /authority-check — Firmas y facultades

> **Dónde está la configuración:** `.criterio/legal/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la del NIT o RUC que viene en el argumento. La escribe `/criterio-legal:legal-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo monto, plazo, día o conteo que muestres se copia de la salida de `legal.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **Sin opinión jurídica.** No interpretes una cláusula ni una norma, no califiques la validez de un contrato o de una firma y no recomiendes renovar ni terminar. Lo que es criterio jurídico queda como pregunta para la persona.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-legal:legal-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **signing-authority**. Cada firmante de la entidad contra la matriz de atribuciones a la fecha de firma: tipo de contrato y monto, otrosíes incluidos.

## Flujo

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" reporte --config <config> --what authority-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/contratos/reporte-authority-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

**Sin opinión sobre la validez.** Que alguien firmara sin facultad según la matriz de la organización es un hallazgo para quien decide; qué efecto tiene es criterio jurídico y queda como pregunta.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-authority-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/legal.py" corrida --config <config> --what authority-check \
    --salida <estado>/corridas/salida-authority-check.md \
    --caso <código del contrato, o «todos»> \
    --nota "firmas sin facultad, contratos sin firma, certificados vencidos"
```
