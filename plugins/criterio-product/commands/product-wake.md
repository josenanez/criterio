---
description: Lo que toca hoy en tu producto — la revisión del registro, el comité, y lo que cruzó un umbral sin que nadie hiciera nada
argument-hint: "[AAAA-MM-DD para simular otro día]"
---

# /product-wake — Lo que toca hoy

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.
> Este es el comando que invoca el reloj, no la persona. Puede correr sin nadie mirando.

## Antes de leer nada

```
python3 scripts/producto.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Un comando espera a que lo llamen. **Un agente no.**

Y un registro de producto tiene una propiedad que ni un portafolio ni un proyecto tienen:
**sus hallazgos aparecen solos.** Nadie hace nada, el calendario se mueve, y el
requerimiento que llevaba cincuenta y nueve días sin decidirse llega a sesenta. El supuesto
de marzo sigue sin verificarse. La entrevista que sostenía la definición cumple doce meses.

Nadie va a abrir una sesión para preguntar si eso ya pasó. **Por eso este comando existe.**

## Flujo

**1. Pregunta qué toca.** La decisión es aritmética de fechas, así que no la tomes tú:

```
python3 scripts/producto.py due --state <estado> --config <archivo>
```

Devuelve `due`, `quiet`, `detail` y `next_wake`.

**2. Si `quiet` es verdadero, termina aquí.** Una línea: qué revisaste y cuándo vuelves.
**No produzcas un informe para decir que no hay novedad.**

**3. Si toca `crossed`** — es lo primero, y es lo único de este comando que no existiría si
alguien estuviera mirando. `detail.crossed` dice qué señales cruzaron desde el corte
anterior. Recalcula, y reporta **solo esas**:

```
python3 scripts/producto.py compute --state <estado> --config <archivo> --fichas <fichas>
```

Aplica el orden de lectura de **product-health**, y su regla: lo que ya estaba en el corte
anterior **no se vuelve a reportar**. Un agente que repite el mismo hallazgo cada semana
enseña a ignorarlo.

Para cada una, la acción concreta, no el diagnóstico:

- **`requirement_undecided`** → *quién tiene la facultad de decidirlo*, que casi siempre es
  el dato que falta. Ofrece llevarlo al comité.
- **`assumption_unverified`** → **qué haría falta para verificarlo**, y si ya pasó el punto
  en que conviene tratarlo como riesgo, dilo: aplica **assumption-tracking**.
- **`evidence_stale`** → qué afirmación de la definición se queda sin sustento, no solo qué
  documento envejeció.

**4. Si toca `review`** — la revisión del registro contra la carpeta. Aplica
**document-intake** para saber qué hay que releer. Si aparecieron documentos de
descubrimiento nuevos, ofrece `/product-discovery`; si cambió la definición, ofrece
`/product-definition`.

Y haz la única revisión que nadie hace por su cuenta: **confirma las trazas.** Con las
fichas a la vista, `trace_not_confirmed` dice si un proyecto que decía ejecutar tu producto
dejó de decirlo — y eso cambia sin que nadie te avise, porque lo escribe otro. **Sin la
carpeta de fichas, ninguna traza se da por confirmada, y se dice así.**

**5. Si toca `report`** — el comité de producto, con su anticipación. Lleva lo que necesita
decisión y nada más: lo que lleva meses sin decidirse, lo aceptado que nadie está
construyendo, y las contradicciones entre lo que el negocio declara y lo que los datos
miden. Lo demás va al anexo.

**6. Deja constancia de lo que corriste.** Sin esto, mañana vuelve a tocar lo mismo:

```
python3 scripts/producto.py ran --state <estado> --what review
python3 scripts/producto.py snapshot --state <estado>
```

**El corte es obligatorio**, no opcional: es contra él que la corrida siguiente sabe qué es
nuevo. Sin corte, `crossed` no puede existir y este comando pierde su razón de ser.

**7. Cierra diciendo cuándo vuelves**, con la fecha de `next_wake`.

## Salida cuando no hay novedad

```markdown
Revisé el registro: [N] requerimientos, nada cruzó un umbral desde el [fecha]. Vuelvo el [fecha].
```

## Salida cuando sí hay

```markdown
## [producto] · [fecha]

**Desde el [fecha del corte anterior]:** [N] señales nuevas

### Cruzó un umbral sin que nadie hiciera nada
| Qué | REQ | Cuánto lleva | Qué se necesita | Quién |

### Las trazas
[Solo lo que cambió del lado del proyecto. Si no cambió nada, se omite.]

### Del descubrimiento
[Documentos nuevos, y si traen algo que el registro no tiene.]

**Vuelvo el [fecha].**
```

## Lo que este comando no hace

- **No decide nada**, ni siquiera corriendo solo. Lo que lleva sesenta días sin decidirse
  sigue sin decidirse cuando este comando termina: lo que cambia es que ahora tiene nombre,
  días y un dueño a quien preguntarle.
- **No verifica supuestos.** Dice cuál falta y qué haría falta para verificarlo.
- **No le escribe a nadie**, ni al doliente de un requerimiento, ni al gerente del proyecto
  cuya ficha dejó de nombrar tu producto. Eso es una conversación.
- **No toca la ficha de ningún proyecto.** La lee, y cuando no coincide con tu registro
  reporta el desacuerdo.

## Cómo se programa

Esto no se programa solo: alguien tiene que ponerlo en un reloj, y ese reloj vive fuera del
plugin.

**Claude Cowork** — una tarea programada que invoque este comando con la cadencia que salió
de `/product-setup`. **Semanal alcanza**: los umbrales de un producto se miden en meses, y
una corrida diaria sobre un registro que se mueve poco es ruido con puntualidad.

**Claude Code** — el programador del sistema operativo invocando Claude en modo no
interactivo con este comando. Da la línea exacta para su sistema y **di qué se necesita
para que funcione sin nadie delante**: que la sesión pueda correr sin aprobar cada paso, y
que las carpetas del producto y de las fichas estén montadas cuando el reloj dispare.

**Si la organización no quiere corridas desatendidas**, dilo sin discutir: este comando
también sirve corrido a mano antes del comité, y la cadencia sigue diciendo qué toca. Lo
que se pierde es justo lo que más cuesta ver a mano — que algo cruzó un umbral mientras
nadie miraba.

## Deja la corrida registrada

Lo último, siempre:

```
python3 scripts/producto.py corrida --state <estado> --what product-wake \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-product-wake.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
