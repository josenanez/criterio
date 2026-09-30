---
description: Publica la ficha de tu producto donde los demás productos la puedan leer, con lo mínimo para cruzar y nada más
argument-hint: "[carpeta de productos publicados] o vacío para la configurada"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /product-publish — Publicar la ficha del producto

> **Dónde está la configuración:** `.criterio/producto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo producto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-product:product-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Alba trabaja sobre **un** producto. Y hay una pregunta que un producto solo no puede
responder: **¿nos estamos pisando con otro?**

La respuesta cómoda sería una base de datos de productos. Este diseño no la tiene y no la
va a tener, por la misma razón que no la tienen las dos fichas de un proyecto: cada
producto deja un documento, los demás lo leen, **y no hay almacenamiento compartido ni
consistencia distribuida que mantener.**

```
productos/
  publicados/
    PRD-QR.json           ← lo que este comando escribe
    PRD-COBROS.json       ← lo que publicó el otro gerente de producto
    PRD-TESORERIA.json
```

## Por qué es un comando y no pasa solo

Publicar expone tu producto a la lectura de los demás con una profundidad que antes no
tenía. Es deseable, y también es político: el día que dos productos comparten una métrica,
alguien va a tener que explicar por qué el comité vio las dos cifras sumadas. **Este diseño
no decide por tu organización — lo corres tú, sabiendo lo que haces.**

## Qué lleva, y qué no

Lo mínimo para poder cruzar:

| Va | No va |
|---|---|
| Código, nombre y gerente del producto | Las entrevistas y sus citas |
| A quién dice servir el producto | Los supuestos de la definición |
| Las métricas que la definición afirma, con su fuente | Las series medidas |
| Los proyectos que ejecutan sus requerimientos | El registro completo con su evidencia |
| El id, título y estado de cada requerimiento | Los criterios de aceptación |

**Lo que no hace falta para cruzar no se publica.** Un descubrimiento sin terminar, un
requerimiento que todavía se está discutiendo o el nombre del cliente que se quejó no son
asunto de los demás productos.

## Flujo

**Antes de escribir una cifra, recalcula.**

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" compute --state <estado> --config <config>
```

Toda cifra derivada —porcentaje, desviación, días, suma, conteo de señales— se copia de esa salida, con todos sus dígitos. Si el script no la da, no se escribe: se dice qué dato falta para poder calcularla.

**1. Recalcula antes de publicar.** Una ficha vieja publicada es peor que ninguna: alguien
la va a leer creyendo que es de hoy.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" publish --state <estado> --config <archivo>
```

**2. Di qué vas a publicar, antes de escribir nada.** Cuántos requerimientos van, cuántos
proyectos, qué métricas afirma tu definición con qué cifra, y a qué segmento dice servir.
**Eso último es lo que más se lee del otro lado.**

**3. Escríbelo en la carpeta de productos publicados**, con el nombre `<código>.json`. Es
el único sitio donde este comando escribe. Si la carpeta no existe, **pregunta antes de
crearla**, y si no está configurada, dilo: sin un sitio común acordado esto no sirve, y
acordarlo es una conversación de la organización, no un comando.

**4. Confirma con la ruta exacta y la fecha.**

## Lo que los demás van a poder ver, y conviene que sepas

Con tu ficha publicada, cualquier otro gerente de producto puede correr `/product-overlap`
y encontrar:

- **Que su producto y el tuyo afirman la misma métrica.** Si los dos casos de negocio
  cuentan las mismas transacciones, la suma que vio el comité no existe.
- **Que el mismo proyecto ejecuta requerimientos de los dos.**
- **Que los dos dicen servir al mismo segmento.**

Ninguna de las tres es una acusación. La primera suele ser el hallazgo más caro de un
portafolio de productos, y **casi siempre nadie lo hizo a propósito.**

## Lo que este comando no hace

- **No publica tu registro.** Ver la tabla de arriba.
- **No avisa a nadie.** El otro gerente la encontrará cuando cruce; si necesitas que la
  vean hoy, eso es una conversación.
- **No lee las de los demás.** Eso es `/product-overlap`.
- **No toca ningún otro archivo** de tu carpeta de documentación.

## Salida

```markdown
Publiqué la ficha en `[ruta exacta]`, con corte al [fecha].

**Lleva:** [N] requerimientos · [N] proyectos · [N] métricas afirmadas
**Segmento declarado:** [a quién dice servir]
**Métricas:** [nombre, cifra y de qué documento sale cada una]
```

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida --state <estado> --what product-publish \
    --salida <estado>/corridas/salida-product-publish.md \
    --caso <código del producto, el de la configuración> \
    --nota "qué quedó publicado para el portafolio"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-product-publish-<n>.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
