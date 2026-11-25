---
description: Pídeselo a Ariadna (La calidad y el linaje) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cdo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /ariadna — Pídeselo a Ariadna

Quien trabaja con Ariadna no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Ariadna sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-data-quality:lineage-setup` y no corras nada más.

## Lo que Ariadna sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-data-quality:lineage-setup` | Deja a Ariadna lista sobre una entidad — mira la carpeta de datos, reconoce el linaje, las cifras de la fuente y las reglas de calidad y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-data-quality:lineage-wake` | Lo que toca hoy en la calidad de los datos — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| La calidad y el linaje · Qué cambió en la calidad | `/criterio-data-quality:lineage-scan` | Procesa lo que cambió en los informes y en la calidad, lleva cada cifra nueva a la ficha del periodo y dice qué señales nuevas aparecieron |
| La calidad y el linaje · Cada cifra contra su fuente | `/criterio-data-quality:figure-check` | Cada cifra de los informes contra la de su fuente al mismo corte: las que no tienen fuente, las que no coinciden y las que salen de otro corte |
| La calidad y el linaje · El linaje de cada cifra | `/criterio-data-quality:lineage-check` | El linaje de cada cifra, paso a paso: dónde se corta porque un paso no tiene su sistema de origen |
| La calidad y el linaje · Las reglas de calidad | `/criterio-data-quality:rule-check` | Cada regla de calidad contra su umbral y su corrida del periodo, y cada dato crítico contra las reglas que lo miden |
| Compartir · Compartir hallazgos | `/criterio-data-quality:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Custodia · el gobierno de los datos | `/criterio-data-governance:custodia` |
