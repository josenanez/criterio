---
description: Pídeselo a Áurea (Tesorería) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cfo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /aurea — Pídeselo a Áurea

Quien trabaja con Áurea no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Áurea sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-treasury:treasury-setup` y no corras nada más.

## Lo que Áurea sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-treasury:treasury-setup` | Deja a Áurea lista sobre la tesorería de una entidad — mira la carpeta, hace las preguntas que ningún documento responde y muestra la primera posición de caja |
| Arranque y ritmo · Qué toca hoy | `/criterio-treasury:treasury-wake` | Lo que toca hoy en la tesorería: pagos de los próximos días, obligaciones por vencer y una revisión semanal; si no toca nada, se calla |
| Tesorería · Qué cambió en la tesorería | `/criterio-treasury:treasury-scan` | Procesa extractos, programa de pagos, flujo proyectado y el registro de deuda, y dice qué señales nuevas aparecieron en la tesorería |
| Tesorería · La posición de caja | `/criterio-treasury:cash-position` | La caja de cada cuenta contra su mínimo y su proyección, la consolidada y la exposición en otras monedas contra su límite |
| Tesorería · Los pagos y quién los aprueba | `/criterio-treasury:payment-check` | Cada pago programado contra los aprobadores que pide la política para su monto y contra la matriz de firmas |
| Tesorería · La deuda y sus covenants | `/criterio-treasury:debt-watch` | La deuda y las inversiones contra su vencimiento, y cada covenant calculado desde el balance del periodo que cierra Clara |
| Compartir · Compartir hallazgos | `/criterio-treasury:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Clara · el cierre | `/criterio-finance:clara` |
| Tomás · el presupuesto | `/criterio-budget:tomas` |
