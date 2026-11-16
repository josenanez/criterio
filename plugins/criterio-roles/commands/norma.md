---
description: Pídeselo a Norma (Los perfiles de cargo) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-chro/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /norma — Pídeselo a Norma

Quien trabaja con Norma no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Norma sabe hacer —los grupos de la tabla de abajo,
con sus etiquetas y sin nombres de comando— y pregunta qué necesita la persona.

**2. Con argumento, elige de la tabla el comando que lo resuelve.** Antes de elegir, busca en la
tabla **todos** los que encajan, no solo el primero:

- **Dos o más posibles:** pregunta cuál, con sus etiquetas, y no corras nada. Un pedido general
  —«revisa», «qué pasa con», «cómo va»— que no nombra lo que distingue a dos comandos es de dos
  posibles aunque uno parezca más probable. No adivines: correr el equivocado cuesta más que una
  pregunta.
- **Pero si el pedido nombra lo que distingue a uno** —«el embudo», «el banco», «las facturas»,
  la palabra de su etiqueta—, es ese, aunque otro toque el mismo tema: no preguntes.
- **Uno solo:** di en una línea cuál vas a correr y por qué —«Esto es *<etiqueta>*: corro
  `/<comando>`»— y córrelo con la herramienta que corre los comandos, pasándole como argumento lo que
  del pedido le sirva. Si no puedes invocarlo, dile a la persona exactamente qué escribir.
- **Es de otro agente de la familia:** dilo en una línea y da su entrada, de la segunda tabla.
- **Ninguno:** dilo en una línea. No improvises el trabajo con lo que hay en la conversación.

**Un comando a la vez, sin subagentes en paralelo.**

**3. Lo que el pedido no dice no se inventa.** Si el comando necesita un dato que el pedido no trae —un
periodo, un proyecto, una ruta—, lo pide el propio comando.

**4. Si el comando elegido responde que falta la configuración**, ofrece
`/criterio-roles:roles-setup` y no corras nada más.

## Lo que Norma sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-roles:roles-setup` | Deja a Norma lista sobre una entidad — mira la carpeta de talento, reconoce el estándar de ocupaciones y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-roles:roles-wake` | Lo que toca hoy en los perfiles — perfiles nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| Los perfiles de cargo · Qué cambió en los perfiles | `/criterio-roles:roles-scan` | Procesa lo que cambió en los perfiles de cargo, lleva cada perfil nuevo a la ficha del periodo y dice qué señales nuevas aparecieron |
| Los perfiles de cargo · Un perfil nuevo desde su ocupación | `/criterio-roles:profile-build` | Arma el borrador de un perfil de cargo desde la ocupación de su estándar, con cada requisito atado a una tarea, para que una persona lo apruebe |
| Los perfiles de cargo · Los perfiles contra su ocupación | `/criterio-roles:profile-check` | Cada perfil de cargo contra la ocupación de su estándar: sin ocupación, lo que no recoge, requisitos sin tarea, estudios que no corresponden y la revisión vencida |
| Los perfiles de cargo · Lo que un perfil no puede pedir | `/criterio-roles:profile-language` | Cada requisito de los perfiles contra los datos sensibles de la ley del país y lo que la política prohíbe pedir |
| Los perfiles de cargo · El mapa de los perfiles | `/criterio-roles:profile-map` | Los perfiles de la organización por ocupación: los que se solapan y las ocupaciones afines que no tienen perfil |
| Compartir · Compartir hallazgos | `/criterio-roles:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Cándido · la selección | `/criterio-talent:candido` |
