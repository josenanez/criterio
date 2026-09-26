---
description: La cadena requerimiento → decisión → proyecto → entregable, y las dos brechas que nadie encuentra solo — lo decidido que nadie construye, y el proyecto cuya ficha dice que está haciendo otro producto
argument-hint: "[REQ-xxx o código de proyecto] o vacío para toda la cadena"
---

# /product-trace — La trazabilidad

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Para qué existe

*«¿Qué falta para tener el producto completo?»* es una pregunta que hoy se responde
preguntándole a la gente. Con el registro y las fichas de los proyectos, **es un filtro.**

Y al hacerlo aparecen dos brechas que nadie encuentra por su cuenta:

1. **Lo que se decidió construir y nadie está construyendo.** Se decidió en un comité, se
   escribió en el acta, y no entró en el alcance de ningún proyecto. Se descubre meses
   después, normalmente en otro comité.
2. **El proyecto que dice ejecutar tu producto, y cuya ficha dice que ejecuta otro.**
   **Alba no le cree a su propio registro:** lo confirma contra la ficha del proyecto, que
   tiene otro dueño y otra cadencia.

## Invocación

```
/product-trace                  toda la cadena, con las dos brechas
/product-trace REQ-014          un requerimiento, hasta su entregable
/product-trace PRY-101          qué de tu producto está en ese proyecto
```

## Flujo

**1. Recalcula, y pásale las fichas.** Sin la carpeta de fichas **ninguna traza se da por
confirmada**, y eso sale dicho en la salida: es mejor que dar por bueno lo que no se verificó.

```
python3 scripts/producto.py compute --state <estado> --config <archivo> --fichas <fichas>
```

Las fichas son las de los proyectos que ejecutan el producto. Pueden venir de la PMO, o de
lo que cada gerente publique con `/pm-publish` en la carpeta de gobierno de su proyecto.
**Si no tienes acceso a ninguna, dilo y sigue**: la cadena hasta la decisión se puede armar
igual, y la parte que falta queda declarada.

**2. Arma la cadena, requerimiento por requerimiento.** Aplica **requirement-record**:

```
REQ-014 → decisión del comité del 8-oct → PRY-101 → [entregables]
```

Cada eslabón con su cita. Un eslabón sin cita rompe la cadena, y se dice dónde se rompió.

**3. Confirma cada traza contra la ficha.** El cálculo emite `trace_not_confirmed` con el
motivo, y hay tres motivos distintos que no se mezclan:

| Motivo | Qué significa |
|---|---|
| No hay ficha de ese proyecto | No se puede confirmar. Puede ser que el proyecto exista y su ficha no esté publicada |
| La ficha no dice qué producto ejecuta | El campo está vacío en el otro lado. **Es un hallazgo del otro lado**, y se dice así |
| La ficha dice otro producto | El desacuerdo real. Uno de los dos registros está mirando mal, y hay que ir a ver |

**4. Lee la cobertura del producto, y no la infles.** De lo decidido, cuánto tiene proyecto,
cuánto tiene entregable con evidencia, cuánto está entregado. **Lo que está entregado no
necesita traza** — es historia, no hallazgo.

**5. Y la vuelta: qué está construyendo un proyecto que tu registro no tiene.** Si una ficha
dice que ejecuta tu producto y ninguno de tus requerimientos la nombra, **alguien está
construyendo algo que no está en el registro.** Es la brecha en la otra dirección, y es la
que hace que el registro sirva como inventario y no solo como intención.

## Salida

```markdown
## Trazabilidad — [producto] · al [fecha]
[N] decididos · [N] con proyecto · [N] confirmados contra la ficha · [N] entregados

### Decidido y nadie lo está construyendo
| REQ | Título | Decidido el | Por quién |
[Va primero.]

### La traza no se confirma
| REQ | Dice ejecutarlo | La ficha dice | Motivo |

### Lo que un proyecto construye y el registro no tiene
| Proyecto | Su ficha dice que ejecuta este producto | Ningún REQ lo nombra |

### La cadena completa
| REQ | Estado | Decisión | Proyecto | Confirmado | Entregables |

### Sin fichas a la vista
[Qué proyectos no se pudieron confirmar y por qué. Si hay todas, se omite.]
```

**Si todo lo decidido tiene proyecto y toda traza está confirmada, una línea:** *«[N]
requerimientos decididos, todos con proyecto y todos confirmados contra su ficha.»* Y se
acaba.

## Lo que este comando no hace

- **No escribe en la ficha del proyecto.** Es de otro dueño. Cuando los dos no coinciden, el
  desacuerdo se reporta; no se arregla desde aquí. **Es la misma regla que gobierna a las dos
  fichas del proyecto, un nivel más arriba.**
- **No le pide nada a ningún gerente de proyecto.** Produce la lista; pedir que publiquen su
  ficha es una conversación.
- **No decide quién tiene razón** cuando el registro y la ficha difieren. Dice qué dice cada
  uno, con su documento y su fecha, y la mitad de las veces el que tiene razón es el otro.
- **No cuenta avance.** Cuántos entregables hay no es cuánto avanzó el producto, y confundir
  las dos cosas es el informe que a nadie le sirve.

## Después

Si hay decididos sin proyecto, ofrece `/product-charter` para el que ya esté listo para
serlo. Si hay trazas que no se confirman, la salida es una conversación con ese gerente de
proyecto, y conviene decirlo así en vez de proponer un comando.
