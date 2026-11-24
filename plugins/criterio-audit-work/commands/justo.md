---
description: Pídeselo a Justo (Los trabajos de auditoría) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cae/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /justo — Pídeselo a Justo

Quien trabaja con Justo no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Justo sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-audit-work:work-setup` y no corras nada más.

## Lo que Justo sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-audit-work:work-setup` | Deja a Justo listo sobre una entidad — mira la carpeta de auditoría, reconoce los trabajos y el equipo y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-audit-work:work-wake` | Lo que toca hoy en los trabajos — documentos nuevos de un trabajo o un reporte con señales abiertas — y si no toca nada, se calla |
| Los trabajos de auditoría · Qué cambió en los trabajos | `/criterio-audit-work:work-scan` | Procesa lo que cambió en los trabajos, lleva cada hallazgo nuevo o cambiado a la ficha del periodo y dice qué señales nuevas aparecieron |
| Los trabajos de auditoría · Cada hallazgo y sus elementos | `/criterio-audit-work:finding-check` | Cada hallazgo con su criterio, su condición, su causa, su efecto y su prioridad, y su prioridad contra la que da la metodología |
| Los trabajos de auditoría · El programa y los papeles | `/criterio-audit-work:workpaper-check` | El programa de cada trabajo y su aprobación, cada paso con su papel, cada papel con su revisión y cada hallazgo con un papel que existe |
| Los trabajos de auditoría · El informe contra los papeles | `/criterio-audit-work:report-check` | El informe de cada trabajo contra sus papeles: el hallazgo que falta o sobra, la prioridad y las cifras que no coinciden |
| Los trabajos de auditoría · Las asignaciones y la objetividad | `/criterio-audit-work:objectivity-check` | Cada auditor asignado a un trabajo de aseguramiento contra lo que tuvo a su cargo en los doce meses anteriores |
| Compartir · Compartir hallazgos | `/criterio-audit-work:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Prudencia · el plan de auditoría | `/criterio-audit-plan:prudencia` |
| Remedios · el seguimiento de los hallazgos | `/criterio-remediation:remedios` |
