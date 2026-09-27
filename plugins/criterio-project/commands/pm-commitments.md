---
description: Quién prometió qué y para cuándo, qué venció sin evidencia, y qué se viene reprogramando reunión tras reunión
argument-hint: "[ruta de una minuta] o vacío para revisar todo lo abierto"
---

# /pm-commitments — El compromiso dicho y no cumplido

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Para qué existe

**Ninguna herramienta que un gerente de proyecto use hoy hace esto.** Las reuniones
están llenas de *«yo lo tengo para el viernes»*, y el viernes no se acuerda nadie. No
está en el plan, porque no es una tarea del cronograma. No está en el acta, porque el
acta la escribió alguien de memoria dos días después. Está dicho, y se perdió.

Esta es la función central de Samuel y la razón por la que existe.

## Invocación

```
/pm-commitments                          revisa todo lo abierto
/pm-commitments 30-reuniones/2026-11-13-comite.md   extrae de una minuta
/pm-commitments Rubén                    lo de una persona
```

## Flujo

**1. Si hay una minuta en el argumento, extrae de ahí.** Aplica
**commitment-tracking**. De cada compromiso sacas **cuatro cosas, y las cuatro llevan
cita**: quién, qué, para cuándo, y de qué documento salió.

Reglas que no se negocian, todas del skill:

- **Quién es una persona, no un área.** *«Tecnología lo revisa»* no es un compromiso:
  es una intención. Regístrala como tal o déjala fuera, pero no le inventes doliente.
- **Un compromiso sin fecha se registra con `due_date: no_declarada`**, no se descarta y
  no se le inventa una. No puede estar vencido, y **por eso mismo es el que desaparece
  de los informes** — se cuenta aparte, siempre.
- **No conviertas en compromiso lo que es una decisión.** *«Se acordó usar el switch
  interoperable»* es una decisión; *«Rubén entrega el documento el 9»* es un compromiso.

**2. Si el compromiso ya existía, no lo dupliques: actualízalo.** El mismo doliente
sobre lo mismo con fecha nueva **es el mismo compromiso reprogramado**, y la fecha
anterior entra en su historial:

```json
"reschedules": [{"due_date": ..., "stated_on": ...}]
```

Esto es lo que separa un seguimiento útil de una lista que crece. Tres entradas sueltas
son tres compromisos vencidos; **una entrada con tres reprogramaciones es un bloqueo que
nadie ha nombrado**, y es información distinta.

**3. Recalcula. No cuentes tú.**

```
python3 scripts/portafolio.py compute --state <estado> --config <archivo>
```

Devuelve `commitments_overdue`, `commitments_undated` y `commitments_rescheduled` con
las veces y las fechas. **Si un número de tu salida no sale de ahí, está inventado.**

**4. Ordena por lo que necesita a alguien, no por fecha.**

El orden es: lo reprogramado tres veces primero —porque es lo único que no se arregla
solo—, después lo vencido sin evidencia, después lo que vence esta semana, y al final lo
que no tiene fecha.

**5. Cierra lo que tenga evidencia.**

Un compromiso se marca cumplido **contra un documento**, no contra la palabra de nadie:
un acta de recibo, un correo de entrega, el entregable en el expediente. Sin documento
sigue abierto, y eso se dice: *«Rubén dice que lo entregó; no hay nada en el expediente
que lo respalde»*.

## Salida

```markdown
## Compromisos — [proyecto] · al [fecha]

### Se viene reprogramando
[Solo si hay. Con las veces, las fechas y quién. Esto va primero.]

> **[Quién]** · [qué]
> Prometido para el [fecha], y antes para el [fecha], y antes para el [fecha].
> **Tres veces no es un problema de seguimiento: es un bloqueo que nadie ha nombrado.**

### Vencidos sin evidencia
| Quién | Qué | Prometido para | Hace |

### Vencen esta semana
| Quién | Qué | Para cuándo |

### Sin fecha
| Quién | Qué | Dicho el |
[No pueden estar vencidos. Se cuentan aparte para que no desaparezcan.]

### Cerrados desde la última revisión
[Con el documento que los cierra. Si no hay ninguno, se omite la sección.]
```

**Si no hay nada en ninguna categoría, una línea:** *«[N] compromisos abiertos, ninguno
vencido y ninguno reprogramado.»* Y se acaba. No produzcas un informe para decir que no
hay novedad.

## Lo que este comando no hace

- **No le escribe a nadie.** Produce la lista; quien persigue un compromiso es el
  gerente, porque perseguirlo es una conversación y no un recordatorio.
- **No juzga por qué no se cumplió.** *«El equipo estaba atendiendo una incidencia»* es
  una razón que puede ser buena, y valorarla es del gerente.
- **No marca cumplido lo que nadie documentó.** Ver el paso 5.

## Después

Si hay algo reprogramado tres veces, **ofrece formularlo como decisión para el comité**:
qué se pide, qué pasa si no se decide, y quién tiene la facultad. Eso excede la
autoridad del gerente y por eso sube.

Y si algún compromiso cambió lo que la ficha decía, ofrece `/pm-publish` para que la PMO
lo vea.
