---
description: Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía
argument-hint: "vacío"
allowed-tools: Read, Bash(python3:*)
---

# /share-findings — Compartir hallazgos, siempre preguntando

> **Cómo se trabaja sin pedir permiso a cada paso:** el script se llama por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/compartir.py" …`, una acción por llamada, sin `cd`, sin `&&` ni tuberías. **Y sin subagentes en paralelo:** todo pasa en esta misma conversación.

> **Nada se envía.** Este comando no publica, no sube y no manda nada a ninguna parte. Arma un resumen, te lo muestra y, si dices que sí, te da un enlace que abres tú (decisión 0025).

## Flujo

**1. El resumen.** Lo arma el código desde el rastro local de las corridas de este agente, en `.criterio/corridas/`, y solo con campos que no vienen de tus documentos: el plugin y su versión, cada comando con cuántas veces corrió y su duración mediana, y cada señal por su código con cuántas veces salió. No lleva nombres, identificaciones, cifras, rutas ni el texto de ningún reporte.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/compartir.py" resumen
```

Muéstralo **tal cual y entero**. No lo resumas, no le agregues datos y no lo redactes de nuevo.

**2. La pregunta, siempre.** Después del resumen, una sola línea: «¿Quieres compartir este resumen para mejorar el producto?». Espera la respuesta. **Sin un sí explícito, el comando termina ahí** y no guarda nada.

**3. Con un sí, el enlace.**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/compartir.py" enlace
```

Muestra el enlace tal cual y di en una línea que abre la plantilla de hallazgo del repositorio con el resumen ya escrito: la persona agrega con sus palabras qué encontró o qué no encontró, revisa que no haya datos de clientes, y decide si la publica. No abras el enlace por ella ni lo envíes a ninguna parte.
