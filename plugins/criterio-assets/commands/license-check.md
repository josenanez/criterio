---
description: Cada software con sus licencias contra las que están en uso: lo que se usa sin licencia y lo que se paga sin usar
argument-hint: "[AAAA-MM] o vacío"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*)
model: sonnet
---

# /license-check — Cada licencia contra su uso

> **Dónde está la configuración:** `.criterio/activos/<entidad>/config.json`, en la carpeta donde corre la sesión; con una sola entidad configurada es esa, con varias la de la identificación fiscal que viene en el argumento. La escribe `/criterio-assets:assets-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** el motor se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. **Y sin subagentes en paralelo:** se procesa una entidad a la vez, en esta misma conversación, salvo que `execution.workers` de la configuración diga otra cosa; nunca más por decisión propia.

> **Las cifras y las fechas las calcula el código.** Todo plazo, día, diferencia o conteo que muestres se copia de la salida de `tecnologia.py`. Si el motor no lo da, no se escribe: se dice qué dato falta para calcularlo.

> **No eliges un proveedor, no decides renovar o retirar un activo y no interpretas un contrato.** Dices qué activo no tiene dueño o soporte, qué software se usa sin licencia o se paga sin uso, qué proveedor incumplió sin su crédito en la factura y qué cuenta de la nube se pasó de su presupuesto; la decisión es del área de tecnología, del comité de arquitectura y de legal. **Nunca te conectas a la nube, a una herramienta de inventario ni a un servidor, y no procesas la seguridad**, que es de la familia CISO.

> **Antes de producir nada:** corre `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" terminos --config <config>`. Si no está vigente, muestra tal cual su `en_corto` con el enlace a la nota legal y pide correr `/criterio-assets:assets-setup`, que registra la aceptación: este comando no produce nada sin ella.

Aplica **technology-policy**.

## Flujo

Las licencias compradas de cada software contra las que están en uso, y las que sobran contra el umbral de la política. Si se compran o se devuelven licencias lo decide el área: aquí se dice cuáles faltan y cuáles sobran.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" reporte --config <config> --period <AAAA-MM> --what license-check
```

**El reporte lo escribe el motor**, en el formato común —encabezado, lo que hay que atender, el resultado, lo que no se pudo procesar, las preguntas que hiciste y las fuentes— y queda en `<estado>/activos/<AAAA-MM>/reporte-license-check.md`. Muéstralo tal cual. Lo que agregues va antes del encabezado, en dos o tres líneas, y no lleva cifras ni fechas que el reporte no traiga.

## Deja la corrida registrada

Lo último, siempre. Escribe en `<estado>/corridas/salida-license-check.md` **lo que le mostraste a la persona, tal cual y entero**, y registra la corrida:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/tecnologia.py" corrida --config <config> --what license-check \
    --salida <estado>/corridas/salida-license-check.md \
    --caso <AAAA-MM> \
    --nota "las licencias contra su uso"
```
