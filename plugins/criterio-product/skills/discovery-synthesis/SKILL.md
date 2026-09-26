---
name: discovery-synthesis
description: Convertir entrevistas, tickets, encuestas y notas de campo en temas con la cita de quién lo dijo, sin que la síntesis se vuelva una conclusión propia. Se carga al procesar material de descubrimiento de producto.
---

# Sintetizar lo que dijo el cliente

Un gerente de producto sale de veinte entrevistas con doscientas páginas de notas y tres
días de trabajo por delante. Ese trabajo es agrupar, y agrupar es lo que un modelo hace
bien.

**Lo que un modelo hace mal es concluir**, y en descubrimiento la frontera entre las dos
cosas es fina: *«los comercios quieren confirmación inmediata»* suena a síntesis y es una
conclusión, porque ninguno de los ocho lo dijo así.

## La regla que sostiene todo esto

**Un tema es un conjunto de citas, no una afirmación.** Se escribe así:

> **Confirmar el pago sin llamar al call center** — 6 de 8 entrevistas
> — *«yo termino llamando para saber si entró»* · comercio 3, entrevista del 11 de sept.
> — *«el cliente ya se fue y yo todavía no sé»* · comercio 7, entrevista del 12 de sept.

El título del tema es de quien sintetiza. **Todo lo demás es de quien lo dijo, y va entre
comillas con su fuente.** Si un tema no tiene ni una cita, no es un tema: es una opinión
del agente, y se borra.

## Cómo se agrupa

1. **Por el problema, no por la solución pedida.** Tres personas pidiendo tres cosas
   distintas para no llamar al call center son un tema, no tres. Y dos personas pidiendo
   *«una app»* para dos problemas distintos son dos temas.
2. **Cuenta cuántos y de cuántos.** «6 de 8» no es lo mismo que «varios», y no es lo mismo
   que «la mayoría». El número va siempre, y el denominador también.
3. **Lo dicho una sola vez se registra como dicho una sola vez.** No se promueve a tema
   general, y no se descarta: una sola voz puede ser la que importa, y quien decide eso es
   el gerente.
4. **Lo que contradice al tema va en el tema.** Si 6 de 8 lo piden y 2 dicen lo contrario,
   los 2 se citan ahí mismo. Una síntesis que esconde la disidencia es una síntesis que
   fabrica consenso.

## Lo que no se hace

- **No se cuantifica lo que no fue cuantificado.** *«Perdemos como el 30% de las ventas»*
  dicho por un comerciante es una cita, no un dato. Se marca como afirmación del
  entrevistado, y si el producto va a apoyarse en ese número, aplica **product-metrics**:
  se busca la serie, o se declara que no existe.
- **No se corrige lo que dijeron.** Se normalizan nombres y se transcribe el resto.
- **No se le pone intención al cliente.** *«Lo que en realidad quiere es...»* no es
  síntesis: es la parte del trabajo que necesita estar frente a la persona, y es
  exactamente lo que el gerente de producto hace y este agente no.
- **No se priorizan los temas.** La frecuencia se cuenta; la importancia se decide.

## De tema a requerimiento

Un tema no es un requerimiento todavía. Se vuelve uno cuando alguien nombra **qué haría
falta** y alguien lo asume como doliente. Aplica **requirement-record**: el tema entra como
`evidence` del requerimiento, con la cita y la fecha de la entrevista, y el requerimiento
nace en `propuesto`.

**Un tema con muchas citas y sin requerimiento es un hallazgo**, y conviene decirlo: es lo
que el cliente viene diciendo y nadie ha convertido en nada.

## Lo que cuenta como material de descubrimiento

Entrevistas y sus transcripciones, tickets de soporte, encuestas con sus respuestas
abiertas, correos del área comercial, notas de campo, grabaciones de llamadas ya
transcritas, reseñas públicas del producto propio. Aplica **document-intake** para los
formatos y para saber qué hay que releer.

Y lo que no: el juicio del propio equipo sobre lo que el cliente quiere. Puede ser
correcto, y no es evidencia de demanda. Aplica **demand-evidence** para la diferencia, que
es la que decide si una definición se sostiene o se sostiene sola.
