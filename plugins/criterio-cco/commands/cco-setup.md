---
description: Configura la familia CCO de una vez — Augusto y Valeria — en una sola conversación, con lo común preguntado una sola vez
argument-hint: "[ruta de la carpeta] o vacío"
allowed-tools: Skill, Read, Glob
---

# /cco-setup — La familia CCO, de una vez

Instalar `criterio-cco` instaló a Augusto (`criterio-sales`) y Valeria (`criterio-revenue`), y a Rostrum
(`criterio-server`). Este comando los deja listos en una sola conversación: lo que comparten se
pregunta una vez, y cada agente pregunta solo lo suyo.

**Este comando no escribe ninguna configuración.** La de cada agente la escribe su propio setup,
con su motor y sus validaciones. Aquí solo se ordena el recorrido.

## Flujo

**0. Preséntate, en una línea.**

> Vamos a dejar lista la familia CCO: Augusto, el pronóstico y Valeria, de la venta a la factura. Lo que comparten te lo pregunto una sola vez.

**1. Corre el setup de cada agente, en este orden**, uno después del otro y en esta misma conversación:

1. **Augusto** — `/criterio-sales:sales-setup`
2. **Valeria** — `/criterio-revenue:revenue-setup`

Invócalos tú, con la herramienta que corre los comandos. Si no puedes invocar un comando, dile a la
persona exactamente cuál escribir y espera a que termine. Si el argumento trae una ruta, pásasela
al primero.

**2. Lo que ya se respondió no se vuelve a preguntar.** El primer setup encuentra la carpeta, la
entidad y dónde guardar el estado. Antes de cada setup siguiente, di en una línea lo que ya quedó
fijado: ese setup lo toma de la conversación y solo pide confirmarlo.

**3. Los términos los muestra cada setup.** No los resumas, no los agrupes y no los aceptes por la
persona: cada agente pide su propio sí.

**4. Si la persona no quiere uno de los agentes, sáltalo.** Cada agente funciona solo. Dilo en una
línea y sigue con el siguiente.

**5. Al final, la familia en una tabla:** una fila por agente —configurado o saltado— con el primer
resultado que mostró su setup, en sus palabras. Y el siguiente paso, en una línea: para verlo fuera de
la conversación, `/criterio-server:server-setup` publica lo de la familia en Rostrum.
