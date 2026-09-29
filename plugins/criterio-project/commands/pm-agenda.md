---
description: La estructura de tu reunión — solo los puntos que necesitan a alguien en la sala, en orden de quién se destraba primero
argument-hint: "[fecha de la reunión] o vacío para la próxima según la cadencia"
---

# /pm-agenda — La estructura de la reunión

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Una agenda de seguimiento casi nunca se escribe. Se hereda: el mismo orden del día de la
semana pasada, con los mismos puntos y los mismos nombres. Y la reunión se va en repasar
lo que ya está bien.

**Este comando construye la agenda al revés: empieza por lo que no se destraba solo.** Un
punto entra si hay alguien en esa sala que puede moverlo. Si nadie de los que van puede
hacer nada con un tema, el tema no es de esta reunión, y decirlo también es trabajo.

Es el comando de más apalancamiento de Samuel: cierra el ciclo. **El que arma la agenda
antes recibe la minuta después**, y esa minuta es el insumo principal de todo lo demás.

## Invocación

```
/pm-agenda                    la próxima reunión según la cadencia configurada
/pm-agenda 2026-11-27         una fecha concreta
/pm-agenda 20                 una agenda que no pase de veinte minutos
```

## Flujo

**1. Mira qué cambió desde la reunión anterior, no el estado completo.**

```
python3 scripts/portafolio.py diff  --state <estado>
python3 scripts/portafolio.py due   --config <archivo> --state <estado>
```

Lo que sigue igual desde la semana pasada y no está vencido **no es un punto de agenda**:
es el anexo. Una reunión que repasa todo es una reunión que no decide nada.

**2. Junta los candidatos, de cuatro sitios y no de más.**

- **Los compromisos reprogramados.** Del cálculo, `commitment_rescheduled`, con sus veces.
- **Los compromisos vencidos sin evidencia**, con doliente y desde cuándo.
- **Lo abierto que se movió o se venció**: riesgos, incidencias y dependencias con
  `raid-taxonomy`, y los entregables de proveedor vencidos o aceptados sin documento.
- **Lo que quedó pendiente de decidir** en la reunión anterior, y sigue pendiente.

**3. Descarta lo que esta reunión no puede mover.** Es el paso que hace la diferencia, y
el que un orden del día heredado nunca hace. Un punto se queda **solo si su doliente va a
estar**, o si lo que se necesita es precisamente que alguien de la sala lo consiga. Si
excede la autoridad del gerente, **no es punto de esta reunión: es punto de comité**, y se
dice así — ofrece `/pm-commitments` para formularlo o súbelo al material del comité.

**4. Ordena por lo que no se arregla solo, no por área ni por fecha.**

1. **Lo reprogramado tres veces.** Primero siempre: es lo único que el tiempo empeora.
2. **Lo vencido sin evidencia**, más viejo primero.
3. **Lo que se decide hoy o se atrasa**, con la consecuencia dicha.
4. **Lo que vence antes de la próxima reunión** — el único punto preventivo que vale.

**5. Ponle tiempo, y que la suma quepa.** Cada punto lleva minutos y lleva **qué tiene que
quedar resuelto al terminarlo**, que no es lo mismo que de qué se va a hablar. Si la suma
pasa del tiempo de la reunión, **corta por el final de la lista y dilo**: *«estos tres
quedaron fuera por tiempo»* es información; una agenda de noventa minutos para una
reunión de cuarenta es una agenda que se abandona a los veinte.

**6. Cada punto lleva su cita.** De qué minuta, de qué fecha. Un punto sin fuente se
discute de memoria, y la memoria es lo que este agente existe para reemplazar.

## Salida

```markdown
## Reunión de seguimiento — [proyecto] · [fecha]
[N] puntos · [N] minutos · [N] personas requeridas

### Lo que no se destraba solo
[Va primero. Si no hay nada aquí, la reunión es de seguimiento y se dice.]

> **[1] [Qué tiene que quedar resuelto]** · [N] min · **[quién]**
> Prometido para el [fecha], y antes para el [fecha], y antes para el [fecha].
> Fuente: [minuta y fecha]
> **Si no se resuelve hoy:** [consecuencia]

### Vencido sin evidencia
| Quién | Qué | Desde | Qué se necesita hoy | Min |

### Se decide hoy o se atrasa
| Qué | Quién decide | Si no se decide | Min |

### Vence antes de la próxima
| Quién | Qué | Para cuándo |

### No es de esta reunión
| Qué | Por qué | Dónde va |
[Lo que excede la autoridad del gerente, y lo que su doliente no va a atender aquí.]

### Anexo — sin cambios desde el [fecha]
[Una línea cada uno. No se repasa en la reunión.]
```

**Si no hay un solo punto que necesite a alguien, dilo en una línea y no armes agenda:**
*«nada vencido, nada reprogramado y nada pendiente de decidir desde el [fecha]»*. Una
reunión sin puntos es una decisión válida, y proponerla es más útil que llenar media hora.

## Lo que este comando no hace

- **No convoca a nadie.** Produce la agenda; citar a la reunión es del gerente.
- **No dirige la reunión.** La reunión es donde se destraba lo que está trabado, y eso
  necesita autoridad e información que no está en ningún documento.
- **No decide qué se pelea.** Cuando dos puntos compiten por el mismo tiempo, el orden que
  este comando propone sale de la evidencia; la prioridad real sale de la política del
  patrocinador, y esa la lee el gerente.
- **No inventa puntos para llenar la agenda.** Ver arriba.

## Después

Cuando la reunión termine, ofrece `/pm-minutes` sobre la transcripción o las notas: la
agenda y el acta son el mismo ciclo, y los compromisos que salgan de ahí entran derecho a
`/pm-commitments` con su cita.

## Deja la corrida registrada

Lo último, siempre:

```
python3 scripts/portafolio.py corrida --state <estado> --what pm-agenda \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-pm-agenda.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
