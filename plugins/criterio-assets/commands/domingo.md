---
description: Pídeselo a Domingo (Los activos y los proveedores) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cto/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /domingo — Pídeselo a Domingo

Quien trabaja con Domingo no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Domingo sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-assets:assets-setup` y no corras nada más.

## Lo que Domingo sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-assets:assets-setup` | Deja a Domingo listo sobre una entidad — mira la carpeta de tecnología, reconoce el inventario, las licencias, el cumplimiento y las facturas de los proveedores y la nube, y muestra el primer resultado |
| Arranque y ritmo · Qué toca hoy | `/criterio-assets:assets-wake` | Lo que toca hoy en los activos y los proveedores — documentos nuevos o un reporte con señales abiertas — y si no toca nada, se calla |
| Los activos y los proveedores · Qué cambió en los activos | `/criterio-assets:assets-scan` | Procesa lo que cambió en los activos y los proveedores, lleva cada excepción y cada nivel de servicio de un contrato a la ficha del periodo y dice qué señales nuevas aparecieron |
| Los activos y los proveedores · Cada activo con su dueño y su soporte | `/criterio-assets:asset-check` | Cada activo con su dueño, y cada activo en producción con el soporte de su fabricante o su excepción: lo que corre sin quién responda o sin quién lo soporte |
| Los activos y los proveedores · Cada licencia contra su uso | `/criterio-assets:license-check` | Cada software con sus licencias contra las que están en uso: lo que se usa sin licencia y lo que se paga sin usar |
| Los activos y los proveedores · Cada proveedor contra su nivel | `/criterio-assets:vendor-check` | Cada proveedor contra el nivel de servicio de su contrato, y el incumplimiento contra el crédito en su factura: lo que se pagó completo sin cumplir |
| Los activos y los proveedores · La nube contra su presupuesto | `/criterio-assets:cloud-check` | La factura de la nube de cada cuenta contra su presupuesto: la cuenta que se pasó |
| Compartir · Compartir hallazgos | `/criterio-assets:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Fausto · los cambios en producción y el nivel de servicio | `/criterio-changes:fausto` |
