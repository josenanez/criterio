---
description: Pídeselo a Remedios (El seguimiento de los hallazgos) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cae/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /remedios — Pídeselo a Remedios

Quien trabaja con Remedios no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Remedios sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-remediation:remediation-setup` y no corras nada más.

## Lo que Remedios sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-remediation:remediation-setup` | Deja a Remedios lista sobre una entidad — mira la carpeta de auditoría, reconoce el registro de hallazgos y el de riesgos aceptados y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-remediation:remediation-wake` | Lo que toca hoy en el seguimiento — evidencias o informes nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| El seguimiento de los hallazgos · Qué cambió en el seguimiento | `/criterio-remediation:remediation-scan` | Procesa lo que cambió en el seguimiento, lleva cada evidencia, explicación y hallazgo externo a la ficha del periodo y dice qué señales nuevas aparecieron |
| El seguimiento de los hallazgos · Los planes contra su fecha | `/criterio-remediation:action-status` | Cada plan de acción contra su responsable, su fecha y sus reprogramaciones: los que no tienen plan, los vencidos y los que se corren una y otra vez |
| El seguimiento de los hallazgos · Cada cierre contra su evidencia | `/criterio-remediation:closure-check` | Cada cierre contra su evidencia y su validación, y los hallazgos que vuelven en el mismo proceso |
| El seguimiento de los hallazgos · Lo que el comité tiene que saber | `/criterio-remediation:committee-brief` | Lo que el comité de auditoría tiene que saber: lo vencido, lo repetido, los riesgos aceptados sin escalar y los hallazgos externos fuera del registro |
| Compartir · Compartir hallazgos | `/criterio-remediation:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Prudencia · el plan de auditoría | `/criterio-audit-plan:prudencia` |
| Justo · los trabajos de auditoría | `/criterio-audit-work:justo` |
