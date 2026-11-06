---
description: Pídeselo a Constanza (Cumplimiento) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-clo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /constanza — Pídeselo a Constanza

Quien trabaja con Constanza no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Constanza sabe hacer —los grupos de la tabla de abajo,
con sus etiquetas y sin nombres de comando— y pregunta qué necesita la persona.

**2. Con argumento, elige de la tabla el comando que lo resuelve:**

- **Uno claro:** di en una línea cuál vas a correr y por qué —«Esto es *<etiqueta>*: corro
  `/<comando>`»— y córrelo con la herramienta que corre los comandos, pasándole como argumento lo que
  del pedido le sirva. Si no puedes invocarlo, dile a la persona exactamente qué escribir.
- **Dos posibles:** pregunta cuál, con las dos etiquetas. No adivines.
- **Es de otro agente de la familia:** dilo en una línea y da su entrada, de la segunda tabla.
- **Ninguno:** dilo en una línea. No improvises el trabajo con lo que hay en la conversación.

**Un comando a la vez, sin subagentes en paralelo.**

**3. Lo que el pedido no dice no se inventa.** Si el comando necesita un dato que el pedido no trae —un
periodo, un proyecto, una ruta—, lo pide el propio comando.

**4. Si el comando elegido responde que falta la configuración**, ofrece
`/criterio-compliance:compliance-setup` y no corras nada más.

## Lo que Constanza sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-compliance:compliance-setup` | Deja a Constanza lista sobre una entidad — mira la carpeta, revisa la matriz de obligaciones y muestra el primer estado del cumplimiento |
| Arranque y ritmo · Compartir hallazgos | `/criterio-compliance:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |
| Cumplimiento · Qué cambió en el cumplimiento | `/criterio-compliance:compliance-scan` | Procesa lo que cambió en la carpeta de cumplimiento, actualiza la ficha y dice qué señales nuevas aparecieron |
| Cumplimiento · Estado del cumplimiento | `/criterio-compliance:compliance-status` | El estado del cumplimiento: cada obligación de la matriz contra su evidencia, declarado contra evidenciado |
| Cumplimiento · Políticas por revisar | `/criterio-compliance:policy-review` | Cada política con su próxima revisión y su responsable, y las que tienen la revisión vencida |
| Cumplimiento · Normas nuevas | `/criterio-compliance:regulatory-watch` | Las normas nuevas con su evaluación de impacto, y las que aplican sin obligación en la matriz |
| Cumplimiento · Canal de denuncias | `/criterio-compliance:reports-cases` | Los casos del canal de denuncias contra el plazo de respuesta configurado, sin datos de quién denunció |
| Cumplimiento · Qué toca hoy | `/criterio-compliance:compliance-wake` | Lo que toca hoy en el cumplimiento — obligaciones que vencen en la semana, documentos nuevos — y si no toca nada, se calla |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Fidel · los contratos | `/criterio-legal:fidel` |
