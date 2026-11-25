---
description: Pídeselo a Lucía (Lo que se anuncia) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cmo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /lucia — Pídeselo a Lucía

Quien trabaja con Lucía no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Lucía sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-claims:claims-setup` y no corras nada más.

## Lo que Lucía sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-claims:claims-setup` | Deja a Lucía lista sobre una entidad — mira la carpeta de mercadeo, reconoce el registro de piezas, el de bases de contactos y el plan, y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-claims:claims-wake` | Lo que toca hoy en las piezas — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| Lo que se anuncia · Qué cambió en las piezas | `/criterio-claims:claims-scan` | Procesa lo que cambió en las piezas, lleva cada afirmación con su soporte y cada promoción con sus condiciones a la ficha del periodo y dice qué señales nuevas aparecieron |
| Lo que se anuncia · Cada afirmación con su soporte | `/criterio-claims:claim-check` | Cada afirmación de una pieza con su soporte, y cada comparativa con su fuente: lo que se anunció sin con qué sostenerlo |
| Lo que se anuncia · Cada promoción con sus condiciones | `/criterio-claims:promo-check` | Cada promoción con su vigencia y sus condiciones de modo y lugar: las que no dicen cuándo ni cómo |
| Lo que se anuncia · La aprobación y la autorización | `/criterio-claims:approval-check` | Cada pieza con su aprobación y su identificación como publicidad, y cada base de contactos con su autorización: lo que salió sin el sí de la política |
| Compartir · Compartir hallazgos | `/criterio-claims:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Próspero · lo que se invierte en las campañas | `/criterio-campaigns:prospero` |
