---
description: Pídeselo a Custodia (El gobierno de los datos) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cdo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /custodia — Pídeselo a Custodia

Quien trabaja con Custodia no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Custodia sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-data-governance:governance-setup` y no corras nada más.

## Lo que Custodia sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-data-governance:governance-setup` | Deja a Custodia lista sobre una entidad — mira la carpeta de datos, reconoce el catálogo y el registro de bases personales y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-data-governance:governance-wake` | Lo que toca hoy en el gobierno de los datos — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| El gobierno de los datos · Qué cambió en el gobierno | `/criterio-data-governance:governance-scan` | Procesa lo que cambió en el gobierno de los datos, lleva cada política, cada plazo y cada término nuevo a la ficha del periodo y dice qué señales nuevas aparecieron |
| El gobierno de los datos · Cada conjunto con su dueño | `/criterio-data-governance:catalog-check` | Cada conjunto del catálogo con su dueño de negocio y su clasificación de confidencialidad: los que no tienen quién responda por ellos |
| El gobierno de los datos · Las políticas y los plazos | `/criterio-data-governance:retention-check` | Cada política contra su fecha de revisión y cada conjunto contra el plazo de conservación de su tipo: lo vencido y lo que se conserva de más |
| El gobierno de los datos · El glosario y el registro | `/criterio-data-governance:glossary-check` | Cada término de los informes contra el glosario de negocio y cada base con datos personales contra el registro de la organización |
| Compartir · Compartir hallazgos | `/criterio-data-governance:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Ariadna · la calidad y el linaje de los datos | `/criterio-data-quality:ariadna` |
