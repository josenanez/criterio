---
description: Pídeselo a Alexis (El gobierno y los controles) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-ciso/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /alexis — Pídeselo a Alexis

Quien trabaja con Alexis no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Alexis sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-security:security-setup` y no corras nada más.

## Lo que Alexis sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-security:security-setup` | Deja a Alexis listo sobre una entidad — mira la carpeta de seguridad, lista lo que excluye, reconoce la declaración de aplicabilidad y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-security:security-wake` | Lo que toca hoy en los controles — evidencia nueva, una revisión o una evaluación que vence — y si no toca nada, se calla |
| El gobierno y los controles · Qué cambió en la seguridad | `/criterio-security:security-scan` | Procesa lo que cambió en la carpeta de seguridad, lleva la evidencia nueva a la ficha del periodo y dice qué señales nuevas aparecieron |
| El gobierno y los controles · La declaración de aplicabilidad | `/criterio-security:soa-status` | Cada control de la declaración de aplicabilidad con si aplica, su estado y su responsable: el aplicable sin responsable |
| El gobierno y los controles · Los controles contra su evidencia | `/criterio-security:control-evidence` | Cada control aplicable contra la evidencia de que operó: el que no tiene ninguna y el que la tiene vencida |
| El gobierno y los controles · Las revisiones de acceso | `/criterio-security:access-reviews` | Cada sistema contra la frecuencia de su revisión de accesos: la vencida y la que nunca se hizo |
| El gobierno y los controles · Los terceros críticos | `/criterio-security:third-parties` | Cada tercero crítico contra la frecuencia de su evaluación de seguridad: la vencida y la que nunca se hizo |
| El gobierno y los controles · El registro de riesgos | `/criterio-security:risk-register` | Cada aceptación de riesgo contra su fecha de revisión: la que venció |
| Compartir · Compartir hallazgos | `/criterio-security:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Guillermo · las vulnerabilidades | `/criterio-vulnerability:guillermo` |
| Amparo · la respuesta y la recuperación | `/criterio-resilience:amparo` |
