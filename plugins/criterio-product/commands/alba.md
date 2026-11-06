---
description: Pídeselo a Alba (Gerente de producto) en tus palabras — dice qué comando lo resuelve y lo corre
argument-hint: "[lo que necesitas, en tus palabras] o vacío"
allowed-tools: Skill, Read, Glob
---
<!-- generado desde families/criterio-pmo/familia.json y la descripción de cada comando, por scripts/familias.py; no se edita a mano -->

# /alba — Pídeselo a Alba

Quien trabaja con Alba no tiene que saber cómo se llama cada comando: dice lo que necesita y este
comando lo lleva al que corresponde. **No hace el trabajo por su cuenta y no escribe nada**: lo hace
el comando elegido, con su motor y sus reglas.

## Flujo

**1. Sin argumento**, muestra en una pantalla lo que Alba sabe hacer —los grupos de la tabla de abajo,
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
`/criterio-product:product-setup` y no corras nada más.

## Lo que Alba sabe hacer

| Para | Comando | Qué hace |
|---|---|---|
| Arranque y ritmo · Instalación | `/criterio-product:product-setup` | Deja a Alba lista para trabajar sobre un producto — mira qué hay escrito, hace cuatro preguntas, y contrasta la definición contra la evidencia que exista |
| Arranque y ritmo · Qué toca hoy | `/criterio-product:product-wake` | Lo que toca hoy en tu producto — la revisión del registro, el comité, y lo que cruzó un umbral sin que nadie hiciera nada |
| Descubrimiento · Descubrimiento: entrevistas | `/criterio-product:product-discovery` | Convierte entrevistas, tickets y notas en temas con la cita de quién lo dijo, y dice qué tema lleva meses dicho sin que nadie lo haya convertido en nada |
| Descubrimiento · Requerimientos | `/criterio-product:product-requirements` | El registro de requerimientos con sus vacíos — sin doliente, sin criterio de aceptación, aceptado sin que nadie lo haya pedido, y lo que lleva meses sin que nadie lo decida |
| Definición del producto · Definición | `/criterio-product:product-definition` | Contrasta la definición del producto contra la evidencia de demanda que exista — qué se sostiene, qué se sostiene en un supuesto, qué no está dicho en ninguna parte, y dónde el negocio y los datos no coinciden |
| Definición del producto · Especificación | `/criterio-product:product-spec` | El borrador de especificación desde el registro, con criterios de aceptación verificables, los vacíos señalados en vez de rellenados, y lo que ninguna sección cubre |
| Definición del producto · Caso de negocio | `/criterio-product:product-business-case` | La estructura del caso de negocio y sus vacíos, con cada cifra citada al documento del que sale — las cifras son del negocio, no del agente |
| Definición del producto · Acta de constitución | `/criterio-product:product-charter` | El borrador del acta de constitución desde el requerimiento aceptado — el momento en que un producto se vuelve proyecto, nace la ficha y el escritor cambia de manos |
| Trazas con proyectos · Trazas con proyectos | `/criterio-product:product-trace` | La cadena requerimiento → decisión → proyecto → entregable, y las dos brechas que nadie encuentra solo — lo decidido que nadie construye, y el proyecto cuya ficha dice que está haciendo otro producto |
| Trazas con proyectos · Solapamientos entre productos | `/criterio-product:product-overlap` | Dónde tu producto y otro se pisan — la misma métrica contada dos veces, el mismo proyecto construyendo para dos dueños, y el mismo segmento |
| Publicar a la PMO · Publicar la ficha | `/criterio-product:product-publish` | Publica la ficha de tu producto donde los demás productos la puedan leer, con lo mínimo para cruzar y nada más |
| Compartir · Compartir hallazgos | `/criterio-product:share-findings` | Arma un resumen sin datos de lo que corrió este agente en esta carpeta y pregunta si quieres compartirlo; nada se envía |

## Los otros agentes de la familia

| Agente | Su entrada |
|---|---|
| Vera · la PMO | `/criterio-portfolio:vera` |
| Samuel · gerente de proyecto | `/criterio-project:samuel` |
