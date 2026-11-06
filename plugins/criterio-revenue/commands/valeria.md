---
description: Pídeselo a Valeria (De la venta a la factura) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-cco/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /valeria — Pídeselo a Valeria

Quien trabaja con Valeria no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Valeria sabe hacer —los grupos de la tabla de abajo,
con sus etiquetas y sin nombres de comando— y pregunta qué necesita la persona.

**2. Con argumento, elige de la tabla el comando que lo resuelve:**

- **Uno claro:** di en una línea cuál vas a correr y por qué —«Esto es *<etiqueta>*: corro
  `/<comando>`»— y córrelo con la herramienta que corre los comandos, pasándole como argumento lo que
  del pedido le sirva. Si no puedes invocarlo, dile a la persona exactamente qué escribir.
- **Dos posibles:** pregunta cuál, con las dos etiquetas. No adivines.
- **Es de otro agente de la familia:** dilo en una línea y da su entrada, de la segunda tabla.
- **Ninguno:** dilo en una línea. No improvises el trabajo con lo que hay en la conversación.

**Un comando a la vez, sin subagentes en paralelo.**

**3. Lo que el pedido no dice no se inventa.** Si el comando necesita un dato que el pedido no trae —un
periodo, un proyecto, una ruta—, lo pide el propio comando.

**4. Si el comando elegido responde que falta la configuración**, ofrece
`/criterio-revenue:revenue-setup` y no corras nada más.

## Lo que Valeria sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-revenue:revenue-setup` | Deja a Valeria lista sobre una entidad — mira la carpeta comercial, reconoce cada exportación del CRM y muestra el primer resultado |
| Arranque y ritmo · Compartir hallazgos | `/criterio-revenue:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |
| De la venta a la factura · Qué cambió en lo vendido | `/criterio-revenue:deal-scan` | Procesa las cotizaciones y los pedidos nuevos, actualiza la ficha del periodo y dice qué señales nuevas aparecieron |
| De la venta a la factura · Los descuentos contra su política | `/criterio-revenue:discount-check` | Cada descuento contra el nivel de la matriz que lo cubre y la aprobación que ese nivel pide |
| De la venta a la factura · De lo ganado a la factura | `/criterio-revenue:won-to-invoice` | De lo ganado a lo firmado y a lo facturado: lo ganado sin contrato en las fichas de Fidel y lo firmado sin factura en las de Clara |
| De la venta a la factura · Las comisiones contra el plan | `/criterio-revenue:commission-check` | Cada comisión liquidada contra la que da el plan sobre lo ganado y facturado |
| De la venta a la factura · Qué toca hoy | `/criterio-revenue:revenue-wake` | Lo que toca hoy de la venta a la factura — cotizaciones nuevas, un contrato o una factura que no llegó, la liquidación — y si no toca nada, se calla |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Augusto · el pronóstico | `/criterio-sales:augusto` |
