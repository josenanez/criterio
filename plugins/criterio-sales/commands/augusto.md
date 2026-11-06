---
description: Pídeselo a Augusto (El pronóstico) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cco/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /augusto — Pídeselo a Augusto

Quien trabaja con Augusto no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Augusto sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-sales:sales-setup` y no corras nada más.

## Lo que Augusto sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-sales:sales-setup` | Deja a Augusto listo sobre una entidad — mira la carpeta comercial, reconoce cada exportación del CRM y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-sales:sales-wake` | Lo que toca hoy en el embudo — una exportación nueva, un acta del comité, el cierre del periodo — y si no toca nada, se calla |
| El pronóstico · Qué cambió en el embudo | `/criterio-sales:pipeline-scan` | Procesa lo que cambió en las exportaciones del CRM y en la evidencia, actualiza la ficha del periodo y dice qué señales nuevas aparecieron |
| El pronóstico · El embudo contra su evidencia | `/criterio-sales:pipeline-check` | Cada oportunidad contra la evidencia de su etapa: la que no la tiene, la detenida y la que corre su cierre |
| El pronóstico · El pronóstico contra su respaldo | `/criterio-sales:forecast-check` | El pronóstico comprometido contra lo que lo sostiene: lo cerrado y lo ponderado con evidencia, oportunidad por oportunidad |
| El pronóstico · La meta contra lo cerrado | `/criterio-sales:target-check` | La meta del periodo contra lo cerrado al corte, por línea y nunca por persona |
| Compartir · Compartir hallazgos | `/criterio-sales:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Valeria · de la venta a la factura | `/criterio-revenue:valeria` |
