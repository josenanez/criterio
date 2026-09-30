---
name: commitment-tracking
description: "Compromisos dichos en reuniones: extraerlos de minutas y transcripciones con doliente y fecha, y revisar en cada corrida cuáles vencieron sin evidencia. Úsalo al procesar una minuta o transcripción de voz, al preparar seguimiento, al revisar qué se acordó y no se cumplió, o al preparar comité. Meeting commitments, action items, overdue follow-ups."
---
<!-- COPIA · la fuente es plugins/criterio-portfolio/skills/commitment-tracking/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Compromisos

## Por qué esto solo

Las transcripciones y las minutas están llenas de *"yo lo tengo para el viernes"*, *"esta semana lo reviso", "me comprometo a mandarlo el lunes"*. Nadie los registra, nadie los revisa, y en la reunión siguiente se vuelve a acordar lo mismo.

Extraer compromisos y revisar cuáles vencieron sin evidencia es determinístico, barato, y no lo hace ninguna herramienta que use hoy un gerente de proyecto. Es la función que sola justifica instalar el plugin.

## Qué es un compromiso

Tres cosas juntas: **alguien**, **algo concreto** y **una fecha**. Si falta una, no es compromiso.

| Lo dicho | ¿Compromiso? |
|---|---|
| "Yo mando el documento el viernes" | Sí. Quién, qué, cuándo |
| "Habría que revisar el contrato" | No. Nadie se hizo cargo |
| "Juan queda encargado de hablar con el proveedor" | Sí, sin fecha. Se registra con fecha `no_declarada` y se marca |
| "Lo vemos la próxima" | No. Es un aplazamiento, no un compromiso |
| "Ya quedamos que eso se hacía" | No. Es una referencia a un compromiso anterior; búscalo en vez de crear uno nuevo |

**Tampoco inventes la fecha.** "Esta semana", "antes del comité", "pronto" no son
fechas: se copian tal cual en `due_date` y el compromiso queda `no_declarada` hasta que
alguien la ponga. En un acta real el agente escribió `~2026-10-04` para "esta semana" —con
tilde de aproximado y todo— y con eso el código lo habría dado por vencido el día 5 contra
una fecha que nadie prometió. Una fecha que el doliente no dijo es un dato inventado, aunque
el cálculo sea razonable; se pregunta en la reunión siguiente y se registra la respuesta.

**Nunca inventes el doliente.** Si en la transcripción no se distingue quién se comprometió, el compromiso se registra con `who: no_identificado` y se pregunta. Asignarle una tarea a la persona equivocada quema la confianza en el sistema entero, y se quema una sola vez.

## Cómo se registra

```yaml
- who: "Carlos Méndez"
  what: "Enviar la propuesta técnica revisada del proveedor"
  due_date: 2026-09-26
  stated_on: 2026-09-19
  source: "30-reuniones/2026-09-19-comite-tecnico.md"
  state: open
```

`stated_on` es la fecha de la reunión; `due_date` es la que se prometió. Las dos importan: un compromiso que se repite en tres reuniones seguidas con fecha nueva cada vez es un hallazgo distinto de uno vencido una sola vez.

## Los estados

- **open** — vigente, no ha llegado la fecha.
- **met** — hay evidencia de cumplimiento.
- **overdue** — pasó la fecha y no hay evidencia.
- **unknown** — pasó la fecha y no se puede determinar. Distinto de vencido.

## Qué cuenta como evidencia de cumplimiento

Un documento nuevo que corresponde a lo prometido, una mención explícita en una minuta posterior de que se entregó, o una confirmación del gerente.

**No cuenta** que el compromiso deje de mencionarse. El silencio no es cumplimiento; es silencio, y se reporta como `unknown`.

## El compromiso que se repite

Cuando el mismo doliente promete lo mismo en varias reuniones con fechas sucesivas, no son varios compromisos: es uno con historial. Se registra una vez, con las reprogramaciones listadas.

Un compromiso reprogramado tres veces es información distinta de tres compromisos vencidos, y es la que le sirve al gerente: no tiene un problema de seguimiento, tiene un bloqueo que nadie ha nombrado.

## Tono al reportar

Se reporta el hecho, no la persona. *"El compromiso de enviar la propuesta venció el 26 de septiembre sin evidencia"* — no *"Carlos incumplió"*.

La diferencia no es cortesía. Un compromiso vencido casi siempre tiene una causa que el registro no ve: le faltó un insumo, cambió la prioridad, nadie lo desbloqueó. El informe abre esa conversación; no la cierra con un juicio.
