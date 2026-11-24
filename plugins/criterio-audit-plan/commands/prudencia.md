---
description: Pídeselo a Prudencia (El plan de auditoría) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cae/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /prudencia — Pídeselo a Prudencia

Quien trabaja con Prudencia no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Prudencia sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-audit-plan:plan-setup` y no corras nada más.

## Lo que Prudencia sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-audit-plan:plan-setup` | Deja a Prudencia lista sobre una entidad — mira la carpeta de auditoría, reconoce el universo, la matriz y el plan y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-audit-plan:plan-wake` | Lo que toca hoy en el plan — actas nuevas o un reporte con señales abiertas — y si no toca nada, se calla |
| El plan de auditoría · Qué cambió en el plan | `/criterio-audit-plan:plan-scan` | Procesa lo que cambió en el plan, lleva cada acta nueva a la ficha del periodo y dice qué señales nuevas aparecieron |
| El plan de auditoría · El plan contra los riesgos | `/criterio-audit-plan:plan-coverage` | El plan contra la matriz de riesgos y el universo auditable: riesgos altos sin trabajo, unidades fuera de su ciclo, la evaluación de riesgos vencida y las áreas que el plan no considera |
| El plan de auditoría · El avance y los cambios del plan | `/criterio-audit-plan:plan-status` | Cada trabajo del plan contra sus fechas y cada cambio al plan contra el acta que lo aprueba |
| El plan de auditoría · Las horas del plan | `/criterio-audit-plan:plan-capacity` | Las horas del plan contra la capacidad del equipo, y el requisito temático vigente de cada trabajo de aseguramiento |
| El plan de auditoría · La evaluación externa de calidad | `/criterio-audit-plan:quality-status` | La última evaluación externa de calidad y cuándo toca la siguiente, contra los cinco años de la norma 8.4 |
| Compartir · Compartir hallazgos | `/criterio-audit-plan:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Justo · los trabajos de auditoría | `/criterio-audit-work:justo` |
| Remedios · el seguimiento de los hallazgos | `/criterio-remediation:remedios` |
