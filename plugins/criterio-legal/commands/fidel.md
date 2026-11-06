---
description: Pídeselo a Fidel (Contratos) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-clo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /fidel — Pídeselo a Fidel

Quien trabaja con Fidel no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Fidel sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-legal:legal-setup` y no corras nada más.

## Lo que Fidel sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-legal:legal-setup` | Deja a Fidel listo sobre una entidad — mira la carpeta de contratos, hace las preguntas que ningún documento responde y arma las primeras fichas |
| Arranque y ritmo · Qué toca hoy | `/criterio-legal:legal-wake` | Lo que toca hoy en los contratos — vencimientos y preavisos que entran en la ventana, documentos nuevos — y si no toca nada, se calla |
| Contratos · Qué cambió en los contratos | `/criterio-legal:contract-scan` | Procesa lo que cambió en los contratos, actualiza la ficha de cada uno y dice qué señales nuevas aparecieron |
| Contratos · Registro de contratos | `/criterio-legal:contract-register` | El registro de contratos contra lo que dicen los documentos: contratos sin registro, registros sin documento, estados y valores que no cuadran |
| Contratos · Vencimientos, preavisos y obligaciones | `/criterio-legal:obligations-calendar` | Los vencimientos, los preavisos de renovación y las obligaciones de cada contrato, con lo que venció sin evidencia |
| Contratos · Firmas y facultades | `/criterio-legal:authority-check` | Quién firmó cada contrato y con qué facultad según la matriz de atribuciones, qué no tiene la firma de las dos partes y qué certificado estaba vencido |
| Contratos · Pagos y garantías | `/criterio-legal:contract-execution` | Lo pagado contra el valor pactado y sus otrosíes, los pagos después de la terminación y cada garantía contra la vigencia que exige el contrato |
| Compartir · Compartir hallazgos | `/criterio-legal:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Constanza · el cumplimiento | `/criterio-compliance:constanza` |
