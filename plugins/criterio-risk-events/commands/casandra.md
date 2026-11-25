---
description: Pídeselo a Casandra (Los indicadores y los eventos) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cro/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /casandra — Pídeselo a Casandra

Quien trabaja con Casandra no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Casandra sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-risk-events:events-setup` y no corras nada más.

## Lo que Casandra sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-risk-events:events-setup` | Deja a Casandra lista sobre una entidad — mira la carpeta de riesgos, reconoce los indicadores clave, sus valores y la base de eventos y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-risk-events:events-wake` | Lo que toca hoy en los indicadores y los eventos — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| Los indicadores y los eventos · Qué cambió en los eventos | `/criterio-risk-events:events-scan` | Procesa lo que cambió en los indicadores y los eventos, lleva cada acción nueva de las actas a la ficha del periodo y dice qué señales nuevas aparecieron |
| Los indicadores y los eventos · Cada indicador contra su umbral | `/criterio-risk-events:kri-check` | Cada indicador clave contra sus umbrales: los que están en alerta sin una acción registrada y los que no tienen valor en el periodo |
| Los indicadores y los eventos · Cada evento con su registro | `/criterio-risk-events:event-check` | Cada evento de pérdida con su registro: los que no traen causa, monto o proceso, y los registrados fuera del plazo de la política |
| Los indicadores y los eventos · Lo que se repite | `/criterio-risk-events:pattern-check` | Lo que se repite: los eventos del mismo tipo en el mismo proceso dentro de la ventana de la política, y los eventos que no corresponden a ningún riesgo de la matriz |
| Compartir · Compartir hallazgos | `/criterio-risk-events:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Severo · el apetito por riesgo y sus límites | `/criterio-risk-appetite:severo` |
