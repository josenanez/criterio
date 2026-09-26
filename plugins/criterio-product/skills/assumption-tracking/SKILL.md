---
name: assumption-tracking
description: El supuesto no verificado de una definición de producto: cómo se declara, cómo se verifica, cuándo se convierte en riesgo registrado y cuándo deja de importar. Se carga al revisar supuestos de un producto o de un requerimiento.
---

# El supuesto que nadie verificó

Toda definición de producto se para sobre supuestos. Eso no es un defecto: en definición no
se puede saber todo, y esperar a saberlo es no lanzar nunca.

**El defecto es que el supuesto no esté escrito**, porque entonces nadie lo puede verificar
y nadie lo puede desmentir. Seis meses después alguien descubre que el comercio no tenía
datos en el punto de venta, y eso no aparece como un supuesto que falló: aparece como un
proyecto atrasado.

## Cómo se declara

Un supuesto se escribe **en forma de algo que puede resultar falso**. Es la única prueba
que necesita:

| Escrito así, no sirve | Escrito así, sí |
|---|---|
| «El comercio está digitalizado» | «El comercio tiene conexión de datos en el punto de venta al momento del pago» |
| «Hay apetito de mercado» | «Al menos 1 de cada 5 comercios visitados acepta cambiar de recaudo si no paga instalación» |
| «El switch aguanta» | «El switch responde en menos de 2 s con 300 transacciones por minuto» |

Lo de la izquierda no se puede verificar, así que no se va a verificar. **Un supuesto que
no se puede desmentir no es un supuesto: es una frase.**

Y lleva, como todo en este sistema, **quién lo dijo y cuándo.** Un supuesto sin fecha no
puede envejecer, y por eso mismo no vuelve a mirarse.

## Dónde vive

- **Los supuestos de la definición** van en `producto.json`, en `definition.assumptions`.
  Sostienen el producto entero.
- **Los supuestos de un requerimiento** van en su registro, en `assumptions`. Aplica
  **requirement-record**.

La diferencia importa: el de la definición cae y se cae todo; el del requerimiento cae y se
cae un requerimiento.

## Cómo se verifica

`verified: true` **solo contra algo que se pueda citar**: una medición, un piloto, una
entrevista donde se preguntó exactamente eso, un documento técnico del proveedor. La
palabra de alguien del equipo no lo verifica, y *«lo dimos por hecho porque nadie dijo lo
contrario»* menos.

Verificar un supuesto tiene tres resultados, y los tres son buenos:

1. **Se confirmó.** Se marca verificado con su cita, y deja de contarse. Ya hizo su trabajo.
2. **Se desmintió.** **Este es el resultado valioso**, y el que la organización trata como
   mala noticia: la definición cambia antes de que haya presupuesto comprometido.
3. **No se pudo verificar.** Se dice así, y se dice qué haría falta para verificarlo. Es
   información sobre lo que la organización no puede saber todavía.

## Cuándo se convierte en riesgo

Pasado `assumption_unverified_days` el cálculo emite `assumption_unverified`. Eso no es un
recordatorio: es la frontera.

**Un supuesto que nadie verifica es un riesgo sin registrar**, y a partir de ahí se
gestiona como riesgo: aplica **raid-taxonomy**, con doliente, valoración y criterio de
escalamiento. Si el proyecto ya existe, el riesgo vive en la ficha del proyecto y no en el
registro de producto — es el mismo objeto, y tenerlo en los dos sitios es tenerlo en
ninguno.

**El supuesto que se convierte en riesgo no se borra del registro de producto.** Queda, con
la marca de que se escaló y a dónde. Es lo que permite, en el cierre, leer qué supuesto de
la definición original resultó falso, que es la lección que sirve y la que nunca se escribe.

## Lo que no se hace

- **No se verifica solo.** Este agente no llama a nadie ni hace pruebas: señala qué haría
  falta para verificarlo, y quién lo haría.
- **No se asumen supuestos que nadie declaró.** Si el documento no lo dice, la categoría es
  *«no está dicho en ninguna parte»*, y va a **demand-evidence**, no aquí. Inventar el
  supuesto que el autor «obviamente tenía» es ponerle palabras a alguien.
- **No se valora la probabilidad.** *«Es poco probable que esto falle»* no sale de ningún
  documento. La valoración es del gerente de producto, y la taxonomía de riesgo dice cómo
  se escribe.
