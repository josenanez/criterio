---
description: Pídeselo a Amparo (La respuesta y la recuperación) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-ciso/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /amparo — Pídeselo a Amparo

Quien trabaja con Amparo no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Amparo sabe hacer —los grupos de la tabla de abajo,
con sus etiquetas y sin nombres de comando— y pregunta qué necesita la persona.

**2. Con argumento, elige de la tabla el comando que lo resuelve.** Antes de elegir, busca en la
tabla **todos** los que encajan, no solo el primero:

- **Dos o más posibles:** pregunta cuál, con sus etiquetas, y no corras nada. Un pedido general
  —«revisa», «qué pasa con», «cómo va»— que no nombra lo que distingue a dos comandos es de dos
  posibles aunque uno parezca más probable. No adivines: correr el equivocado cuesta más que una
  pregunta.
- **Uno solo:** di en una línea cuál vas a correr y por qué —«Esto es *<etiqueta>*: corro
  `/<comando>`»— y córrelo con la herramienta que corre los comandos, pasándole como argumento lo que
  del pedido le sirva. Si no puedes invocarlo, dile a la persona exactamente qué escribir.
- **Es de otro agente de la familia:** dilo en una línea y da su entrada, de la segunda tabla.
- **Ninguno:** dilo en una línea. No improvises el trabajo con lo que hay en la conversación.

**Un comando a la vez, sin subagentes en paralelo.**

**3. Lo que el pedido no dice no se inventa.** Si el comando necesita un dato que el pedido no trae —un
periodo, un proyecto, una ruta—, lo pide el propio comando.

**4. Si el comando elegido responde que falta la configuración**, ofrece
`/criterio-resilience:resilience-setup` y no corras nada más.

## Lo que Amparo sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-resilience:resilience-setup` | Deja a Amparo listo sobre una entidad — mira la carpeta de seguridad, lista lo que excluye, toma los plazos de la política de respuesta y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-resilience:resilience-wake` | Lo que toca hoy en la respuesta — un incidente nuevo, una notificación pendiente, una prueba que vence — y si no toca nada, se calla |
| La respuesta y la recuperación · Qué cambió en la respuesta | `/criterio-resilience:resilience-scan` | Procesa los incidentes, las revisiones y las pruebas nuevas, los lleva a la ficha del periodo y dice qué señales nuevas aparecieron |
| La respuesta y la recuperación · La línea de tiempo de cada incidente | `/criterio-resilience:incident-timeline` | Cada incidente contra el plazo de contención de su severidad y su revisión posterior contra los días de la política |
| La respuesta y la recuperación · Las notificaciones | `/criterio-resilience:notifications` | Cada notificación que pide la matriz, contra la que se hizo: a tiempo, tarde o sin hacer |
| La respuesta y la recuperación · Las pruebas de continuidad | `/criterio-resilience:continuity-tests` | Cada prueba de continuidad, de recuperación y de restauración contra su calendario |
| Compartir · Compartir hallazgos | `/criterio-resilience:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Alexis · el gobierno y los controles | `/criterio-security:alexis` |
| Guillermo · las vulnerabilidades | `/criterio-vulnerability:guillermo` |
