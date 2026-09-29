---
description: Evalúa una solicitud de cambio en alcance, tiempo y costo, y deja la línea base nueva sin borrar la anterior
argument-hint: "<código del proyecto> <qué se quiere cambiar>"
---

# /change-control — Control de cambios

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide aceptación explícita y ofrece guardarla. Sin eso, responde preguntas pero no generes la solicitud.
> Abre declarando de qué ficha sale. Cierra con el pie de rigor.

## Antes de leer nada

```
python3 scripts/portafolio.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Invocación

```
/change-control PRY-014 sumar el módulo de firma electrónica
/change-control PRY-014 mover el cierre a marzo
```

## Flujo

**1. Parte de la línea base vigente.** Aplica **baseline-variance**. Sin línea base no hay cambio que evaluar: hay un plan que nunca se aprobó, y eso es lo que se reporta.

**2. Evalúa las tres dimensiones, siempre las tres.** Aplica **governance-artifacts**.

Un cambio que declara impacto en una sola dimensión casi siempre está mal evaluado. Ampliar alcance sin mover fecha ni presupuesto significa que alguien lo va a absorber en calidad o en horas no pagadas, y eso se dice explícitamente.

**3. Busca el efecto en el portafolio. No lo mires a ojo: cálculalo.**

```
python3 scripts/portafolio.py impact --state <estado> --code <proyecto> --days <días que se mueve>
```

Recorre las dependencias declaradas y devuelve a quién alcanza el cambio —**directa e indirectamente**, con el camino por el que quedó alcanzado—, el gerente de cada uno, y las dos cosas que importan:

- **Quién no puede sostener su fecha** (`cannot_hold_date`): un proyecto que depende de este y cierra antes de la fecha nueva tiene un problema que todavía no sabe que tiene, y `days_short` dice por cuántos días.
- **Qué dependencia nunca se confirmó** con el otro lado. Una dependencia declarada y no acordada es la que se descubre el día que se incumple.

**Lo que este cálculo no dice, y no hay que inventarlo: cuántos días se mueve cada uno.** Eso necesita holgura por actividad, y la ficha de portafolio no la tiene. Decir *«se mueve 21 días»* sin holgura es un número con aspecto de cálculo.

**4. Determina quién decide.** Contra la autoridad declarada en el acta. Si el cambio excede esa autoridad, el paquete va a comité. Si no hay autoridad declarada, ese es el hallazgo de fondo.

**5. Si se aprueba, crea línea base nueva.** Registro nuevo con su fecha, su motivo y el documento que la aprobó. **La anterior no se toca.** El conteo de replanificaciones sube, y desde ahí toda desviación se reporta contra dos referencias.

Y desde ahora se reconcilia: el script resta los días que la línea base se movió menos los días que autorizaron los cambios aprobados (`changes.baseline_moved_days`, `changes.approved_time_days`, `changes.unauthorized_days`). Si sobran días, `rebaseline_unauthorized` los nombra. No es una acusación: es que **ningún documento de la carpeta autoriza esa diferencia**, y eso es exactamente el hallazgo. Un cambio aprobado que movió fechas y no dejó línea base nueva sale en `approved_without_new_baseline`, y un impacto de tiempo escrito en meses queda en `time_impact_unreadable` en vez de convertirse en un número inventado.

## Salida

```markdown
## Solicitud de cambio — [proyecto] — [fecha]

**Qué se pide:** · **Quién lo pide:** · **Por qué:**

### Impacto
| Dimensión | Hoy | Con el cambio | Diferencia |
| Alcance | | | |
| Tiempo | | | |
| Costo | | | |

[Si alguna dimensión queda sin impacto declarado, decir quién lo absorbe.]

### Efecto en el portafolio
| Proyecto afectado | Cómo | Gerente |

### Quién decide
**Autoridad requerida:** · **Según:** [acta, cláusula] · **Va a comité:** [sí | no]

### Si no se aprueba
[Qué pasa con el proyecto tal como está.]

### Si se aprueba
Línea base [N+1] — cierre [fecha] · presupuesto [monto] · motivo: [texto]
Desviación acumulada contra la línea base original: [tiempo] · [costo]
```

**El último número es el que importa y el que se suele omitir.** Un proyecto en su cuarta línea base se ve sano contra la vigente y lleva un año de atraso contra la original.

## Después

Ofrece llevarlo a comité si excede la autoridad, o registrar la nueva línea base si ya fue aprobado por quien podía aprobarlo.

## Deja la corrida registrada

Lo último, siempre:

```
python3 scripts/portafolio.py corrida --state <estado> --what change-control \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-change-control.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
