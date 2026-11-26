---
description: Pídeselo a Fausto (Los cambios y el servicio) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cto/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /fausto — Pídeselo a Fausto

Quien trabaja con Fausto no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Fausto sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-changes:changes-setup` y no corras nada más.

## Lo que Fausto sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-changes:changes-setup` | Deja a Fausto listo sobre una entidad — mira la carpeta de tecnología, reconoce el catálogo de servicios, los cambios, los despliegues, los incidentes y la disponibilidad, y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-changes:changes-wake` | Lo que toca hoy en los cambios — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| Los cambios y el servicio · Qué cambió en los cambios | `/criterio-changes:changes-scan` | Procesa lo que cambió en los cambios, lleva cada aprobación y cada revisión de las actas a la ficha del periodo y dice qué señales nuevas aparecieron |
| Los cambios y el servicio · Cada cambio con su aprobación | `/criterio-changes:change-check` | Cada cambio en producción con su aprobación y su revisión, y cada despliegue con su cambio: lo que llegó a producción sin el sí del comité |
| Los cambios y el servicio · Cada incidente mayor con su causa | `/criterio-changes:incident-check` | Cada incidente mayor con su problema y su causa: la falla grande que todavía no tiene su porqué |
| Los cambios y el servicio · Cada servicio contra su nivel | `/criterio-changes:service-check` | Cada servicio del catálogo contra el nivel que se acordó con el negocio: el que no lo cumplió |
| Compartir · Compartir hallazgos | `/criterio-changes:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Domingo · los activos, las licencias, los proveedores y la nube | `/criterio-assets:domingo` |
