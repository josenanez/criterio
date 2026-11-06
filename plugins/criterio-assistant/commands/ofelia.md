---
description: Pídeselo a Ofelia (Asistente ejecutiva) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-ea/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /ofelia — Pídeselo a Ofelia

Quien trabaja con Ofelia no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Ofelia sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-assistant:ea-setup` y no corras nada más.

## Lo que Ofelia sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-assistant:ea-setup` | Deja a Ofelia lista sobre la oficina de un ejecutivo — mira la carpeta, hace las preguntas que ningún documento responde y arma las primeras fichas |
| Arranque y ritmo · Qué toca hoy | `/criterio-assistant:ea-wake` | Lo que toca hoy en la oficina — sesiones en la ventana, actas pendientes, plazos de la correspondencia — y si no toca nada, se calla |
| Asistente ejecutiva · Procesar | `/criterio-assistant:ea-scan` | Procesa la agenda, las sesiones de los órganos, la correspondencia y los viajes, y escribe las fichas con cada dato citado |
| Asistente ejecutiva · La semana | `/criterio-assistant:ea-agenda` | La semana del ejecutivo contra sus sesiones y sus compromisos: cruces, sesiones sin material y sesiones sin acta |
| Asistente ejecutiva · Preparar una sesión | `/criterio-assistant:ea-prep` | El paquete de la próxima sesión de un órgano: lo que quedó abierto, el material que falta y la ficha de cada decisión, sin ordenar las opciones |
| Asistente ejecutiva · Borrador del acta | `/criterio-assistant:ea-minutes` | El borrador del acta desde las notas o la transcripción, con cada acuerdo y compromiso citado, en 90-borradores |
| Asistente ejecutiva · Compromisos | `/criterio-assistant:ea-commitments` | El estado de los compromisos de dirección, por órgano y por responsable: vencidos sin evidencia, sin fecha y movidos de más |
| Asistente ejecutiva · Correspondencia | `/criterio-assistant:ea-mail` | La correspondencia guardada: qué pide respuesta y para cuándo, y el borrador de las respuestas rutinarias. Nunca envía |
| Asistente ejecutiva · Resumen de la semana | `/criterio-assistant:ea-weekly` | El resumen de la semana: lo que llegó, lo que vence y lo que falta preparar. Uno solo por semana |
| Compartir · Compartir hallazgos | `/criterio-assistant:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |
