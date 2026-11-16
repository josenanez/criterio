---
description: Pídeselo a Cándido (La selección) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-chro/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /candido — Pídeselo a Cándido

Quien trabaja con Cándido no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Cándido sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-talent:talent-setup` y no corras nada más.

## Lo que Cándido sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-talent:talent-setup` | Deja a Cándido listo sobre una entidad — mira la carpeta de talento, reconoce los registros de la selección y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-talent:talent-wake` | Lo que toca hoy en la selección — hojas de vida nuevas, una vacante que vence o un reporte con señales abiertas — y si no toca nada, se calla |
| La selección · Qué cambió en la selección | `/criterio-talent:talent-scan` | Procesa lo que cambió en la selección, lleva cada hoja de vida nueva a la ficha del periodo y dice qué señales nuevas aparecieron |
| La selección · La búsqueda de una vacante | `/criterio-talent:talent-search` | Arma la búsqueda de una vacante: las cadenas para el buscador de quien recluta y las personas de la base interna con la misma ocupación |
| La selección · Las hojas de vida contra sus soportes | `/criterio-talent:cv-check` | Cada título, certificación y empleo de las hojas de vida contra su soporte: sin soporte, fechas que no coinciden y certificaciones vencidas |
| La selección · Cada candidato contra el perfil | `/criterio-talent:candidate-fit` | Cada candidato de una vacante contra el perfil, requisito por requisito y con la cita; sin puntaje y sin orden por número |
| La selección · La autorización y la conservación de los datos | `/criterio-talent:privacy-check` | Cada candidato contra su autorización de tratamiento de datos y contra la conservación de la política; lo que llegó y no se debe tratar |
| La selección · Las vacantes contra su plazo | `/criterio-talent:vacancy-status` | Cada vacante abierta contra el plazo de cobertura de la política: las que lo pasaron |
| Compartir · Compartir hallazgos | `/criterio-talent:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Norma · los perfiles de cargo | `/criterio-roles:norma` |
