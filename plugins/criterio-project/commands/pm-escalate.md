---
description: Convierte lo que excede tu autoridad en una decisión formulada — pregunta cerrada, opciones con su costo, y qué pasa si nadie decide
argument-hint: "[qué se escala] o vacío para lo que ya está marcado"
---

# /pm-escalate — El escalamiento con la decisión formulada

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Para qué existe

Un escalamiento mal formulado vuelve. *«Necesitamos definición sobre el proveedor»* no es
una decisión: es un tema, y un comité no decide temas — los discute veinte minutos y los
deja para la próxima sesión.

Este comando convierte lo que excede tu autoridad en **algo que se puede responder con
una palabra.** Es la diferencia entre subir un problema y subir una decisión, y es lo que
hace que el comité sirva para algo.

## Invocación

```
/pm-escalate                       lo que ya está marcado como escalable
/pm-escalate el switch del proveedor
/pm-escalate cambio 2026-11-18     un cambio, con su efecto calculado
```

## Qué escala, y qué no

No todo lo que molesta escala. Aplica **raid-taxonomy** y su criterio, que es el mismo de
la PMO para que las dos partes usen la misma vara:

| Escala | No escala |
|---|---|
| Excede la autoridad declarada del gerente en el acta | Lo que puedes decidir tú, aunque sea incómodo |
| Afecta a otro proyecto o a otra área | Lo que solo te afecta a ti y tiene solución dentro del proyecto |
| Dos períodos sin movimiento con doliente fuera del proyecto | Lo que se movió esta semana |
| Mitigación vencida sin evidencia | Un riesgo abierto que todavía tiene plan vigente |
| Compromiso reprogramado tres veces | Un vencido que se destraba con una llamada |

**Si no encuentras la autoridad declarada en el acta, ese es el primer punto que escala**,
y no el que venías a subir: un gerente que no sabe qué puede decidir escala todo o no
escala nada.

## Flujo

**1. Formula la decisión como pregunta cerrada.** Es el paso entero. Si la pregunta no se
puede responder con *sí*, *no* o *la opción B*, no está lista.

> No: *«Necesitamos definición sobre el proveedor.»*
> Sí: *«¿Se acepta la propuesta del proveedor a 45 días con sobrecosto de X, o se cambia
> de proveedor y el cierre se corre al 30 de abril?»*

**2. Pon las opciones con lo que cuesta cada una**, en las tres dimensiones. Aplica
**governance-artifacts**. Una opción sin costo declarado es una opción que alguien va a
elegir por conveniencia.

**3. Si lo que se escala mueve una fecha, calcula el efecto. No lo describas.**

```
python3 scripts/portafolio.py impact --state <estado> --code <tu proyecto> --days <días>
```

Devuelve **los hitos tuyos por los que pasa el cambio**, y **qué otros proyectos quedan
alcanzados** —directa e indirectamente—, con su gerente, cuáles no pueden sostener su
fecha y por cuántos días, y qué dependencia nunca se confirmó con el otro lado.

Eso último es lo que convierte un escalamiento en una conversación corta: llegar al comité
sabiendo **a quién hay que llamar** vale más que llegar con el problema bien descrito.

**Lo que ese cálculo no dice, y no se inventa: cuántos días se mueve cada proyecto
alcanzado.** Necesita holgura por actividad, y la ficha no la tiene.

**4. Di quién tiene la facultad.** Contra la autoridad declarada. Un punto dirigido a
quien no puede decidirlo se devuelve, y haber perdido el comité es lo de menos: lo caro es
que se decidió y no valía.

**5. Di qué pasa si no se decide hoy**, con fecha. *«Se atrasa»* no sirve; *«el 27 de
noviembre vence la oferta y el precio se renegocia»* sí. **Sin esta línea el punto se
aplaza, siempre.**

**6. Di qué recomiendas, y por qué.** Escalar no es abstenerse. El comité decide, y tú
eres quien conoce el proyecto: una recomendación con su razón acelera la decisión y deja
escrito qué se sabía en ese momento.

## Salida

```markdown
## Para decisión — [proyecto] · [fecha]

### [La pregunta, cerrada]

**Quién decide:** [según el acta] · **Si no se decide hoy:** [consecuencia, con fecha]

| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|

**Recomiendo:** [cuál] — [por qué, en una línea]

### A quién alcanza
| Proyecto | Gerente | ¿Sostiene su fecha? | Dependencia confirmada |

### Mis hitos por los que pasa
| Hito | Fecha vigente | En cuántos días |

### De dónde sale esto
[La cita de cada dato: el acta que declara la autoridad, la minuta donde se dijo, el
documento del proveedor.]
```

**Si lo que traías no escala, dilo y no armes el paquete:** *«esto está dentro de tu
autoridad según el acta del [fecha]»*. Es más útil que subirlo, y evita el escalamiento que
vuelve con un *«eso lo decide usted»*.

## Lo que este comando no hace

- **No escala solo.** Produce el paquete; llevarlo al comité es tuyo.
- **No decide**, y tampoco decide por omisión: si el comité no responde, el punto sigue
  abierto y vuelve a aparecer con los días que lleva.
- **No estima los días que se mueve cada proyecto alcanzado.** Ver el paso 3.
- **No le escribe al gerente del otro proyecto.** Te dice su nombre; la llamada es tuya, y
  casi siempre esa llamada resuelve el punto antes del comité.

## Después

Si el comité decide, ofrece registrarlo: la decisión con su fecha y su documento entra a la
ficha, y con ella se cierra el ítem del RAID que la originó. Y si el cambio mueve la línea
base, eso es control de cambios, no un escalamiento: se registra aparte y **la línea base
anterior no se toca.**
