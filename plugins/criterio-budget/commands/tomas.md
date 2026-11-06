---
description: Pídeselo a Tomás (FP&A) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cfo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /tomas — Pídeselo a Tomás

Quien trabaja con Tomás no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Tomás sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-budget:budget-setup` y no corras nada más.

## Lo que Tomás sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-budget:budget-setup` | Deja a Tomás listo sobre el presupuesto de una entidad — mira la carpeta, hace las preguntas que ningún documento responde y muestra la primera ejecución contra lo aprobado |
| Arranque y ritmo · Qué toca hoy | `/criterio-budget:budget-wake` | Lo que toca hoy en el presupuesto — contabilidad nueva, comité cerca o la revisión semanal de compromisos — y si no toca nada, se calla |
| FP&A · Qué cambió en el presupuesto | `/criterio-budget:budget-scan` | Procesa presupuesto, ejecución, compromisos, proyecciones y actas, actualiza cada ficha y dice qué señales nuevas aparecieron |
| FP&A · Ejecución contra aprobado | `/criterio-budget:variance-report` | Aprobado, ejecutado, comprometido, disponible y desviación por área y línea, contra la versión aprobada |
| FP&A · Proyección al cierre del año | `/criterio-budget:forecast` | La proyección al cierre del año: la del área y dos calculadas, al ritmo y al plan, cada una con su supuesto escrito |
| FP&A · Traslados y sus actas | `/criterio-budget:transfer-log` | Cada traslado, adición o reducción del presupuesto con el acta que lo aprueba, y los que no la tienen |
| FP&A · Paquete del comité de presupuesto | `/criterio-budget:budget-committee-pack` | El material del comité de presupuesto como paquete de decisiones: cada una con su cifra, su cita y quién la toma |
| Compartir · Compartir hallazgos | `/criterio-budget:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Clara · el cierre | `/criterio-finance:clara` |
| Áurea · la tesorería | `/criterio-treasury:aurea` |
