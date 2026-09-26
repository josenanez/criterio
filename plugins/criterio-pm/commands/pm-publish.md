---
description: Publica la ficha del proyecto en su carpeta de gobierno, para que la PMO la lea como lee cualquier documento
argument-hint: "[confirmar] o vacío"
---

# /pm-publish — Publicar la ficha

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

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
python3 scripts/pmo.py compute --state <estado> --config <archivo>
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
