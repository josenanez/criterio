---
description: Publica la ficha del proyecto en su carpeta de gobierno, para que la PMO la lea como lee cualquier documento
argument-hint: "[confirmar] o vacío"
---

# /pm-publish — Publicar la ficha

> **Dónde está la configuración:** `.criterio/proyecto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo proyecto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-project:pm-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Samuel escribe la ficha de tu proyecto en **su** carpeta de estado. Vera, el agente de
la PMO, no la alcanza: son dos instalaciones distintas, probablemente en dos equipos
distintos, y **está bien que así sea**.

Este comando pone una copia de tu ficha en la carpeta de gobierno del proyecto, con el
nombre `ficha-pm.json`. Desde ahí Vera **la lee como lee cualquier otro documento**, sin
almacenamiento compartido y sin que nadie tenga que sincronizar nada.

```
PRY-101-pasarela-qr/
  00-gobierno/
    2026-08-03-acta-constitucion.md
    ficha-pm.json          ← lo que este comando escribe
```

## Por qué es un comando y no pasa solo

**Es el único archivo que Samuel escribe fuera de su estado**, y esa lista no crece sin
que quede escrito en el diseño. Publicar expone tu proyecto a la lectura de la PMO con
una profundidad que antes no tenía: es deseable, y también es político. Este diseño no
decide por tu organización — **lo corres tú, sabiendo lo que haces.**

## Flujo

**1. Recalcula antes de publicar.** Una ficha vieja publicada es peor que ninguna:
alguien la va a leer creyendo que es de hoy.

```
python3 scripts/portafolio.py compute --state <estado> --config <archivo>
```

**2. Di qué vas a publicar, antes de escribir nada.** Cuántos campos van con dato,
cuántos van como *no está dicho en ninguna parte*, de cuándo es el más viejo, y **qué
declara el estado del proyecto** — que es lo primero que la PMO va a mirar.

**3. Escribe `ficha-pm.json`** en la carpeta de gobierno del proyecto. Es el único sitio
donde este comando escribe. Si esa carpeta no existe, **pregunta antes de crearla**.

**4. Confirma con la ruta exacta** y con la fecha, para que quede en la conversación.

## Lo que la PMO va a ver, y conviene que sepas

Vera contrasta **ocho campos** de tu ficha contra su propia lectura de los mismos
documentos:

```
identity.sponsor   identity.manager    identity.committee
identity.product   plan.end_date       money.approved
declared.status    declared.as_of
```

**Cuando los dos citan y no coinciden, alguien vio un documento que el otro no vio.** Es
el hallazgo de más valor del sistema, y la mitad de las veces el que tiene razón eres
tú: tú estuviste en la reunión donde cambió el patrocinador, y el acta de constitución
no se actualizó nunca.

Lo que tú tienes y la PMO no —los compromisos de cada reunión, el riesgo que alguien
dijo al pasar— **no es una contradicción**: es diferencia de profundidad, y no se
reporta como hallazgo.

## Lo que este comando no hace

- **No publica tu declaración de estado como si fuera de la PMO.** Sigue siendo tuya, y
  la ficha la marca como declarada.
- **No toca ningún otro archivo** de la carpeta de documentación.
- **No avisa a nadie.** Vera la encontrará en su próximo barrido. Si necesitas que la
  vean hoy, eso es una conversación, no un comando.

## Salida

```markdown
Publiqué la ficha en `[ruta exacta]`, con corte al [fecha].

**Lleva:** [N] campos con dato · [N] sin decir en ninguna parte · declara **[estado]** al [fecha]

**Lo más viejo que va ahí:** [campo], del [fecha] — [si pasa de un año, dilo]
```

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 scripts/portafolio.py corrida --state <estado> --what confirmation \
    --salida <estado>/corridas/salida-confirmation.md \
    --nota "qué quedó publicado para el portafolio"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-confirmation.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
