---
description: Convierte entrevistas, tickets y notas en temas con la cita de quién lo dijo, y dice qué tema lleva meses dicho sin que nadie lo haya convertido en nada
argument-hint: "[carpeta o archivo de material de descubrimiento] o vacío para todo lo nuevo"
---

# /product-discovery — Sintetizar lo que dijo el cliente

> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Antes de leer nada

```
python3 scripts/producto.py corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Veinte entrevistas son doscientas páginas y tres días de trabajo. Ese trabajo es agrupar, y
agrupar es lo que un modelo hace bien.

Lo que este comando **no** hace, y es la razón de su forma, es concluir. *«Los comercios
quieren confirmación inmediata»* suena a síntesis y es una conclusión, porque ninguno de los
ocho lo dijo así.

## Invocación

```
/product-discovery                          todo lo que no se ha procesado
/product-discovery 10-entrevistas/          una carpeta
/product-discovery entrevista-comercio-3.md un archivo
```

## Flujo

**1. Lee el material y di de qué tamaño es.** Aplica **document-intake**. Cuántas piezas,
de qué fechas, y qué no vas a poder leer. Si ya se procesó antes, **solo lo nuevo**: releer
todo cada vez produce la misma síntesis con otra fecha.

**2. Agrupa por problema, no por solución pedida.** Aplica **discovery-synthesis**, y sus
cuatro reglas son las que deciden si esto sirve:

- **El título del tema es tuyo; todo lo demás va entre comillas con su fuente.** Un tema sin
  una sola cita no es un tema: es una opinión del agente, y se borra.
- **Cuenta cuántos y de cuántos.** «6 de 8», no «varios» y no «la mayoría».
- **Lo dicho una sola vez se registra como dicho una sola vez.** Ni se promueve ni se
  descarta: una sola voz puede ser la que importa, y eso lo decide el gerente.
- **Lo que contradice al tema va dentro del tema.** Una síntesis que esconde la disidencia
  fabrica consenso.

**3. Cruza contra el registro.** Aplica **requirement-record**. Para cada tema, mira si ya
existe un requerimiento que lo recoja:

- **Existe** → el tema entra como `evidence` de ese requerimiento, con la cita y la fecha de
  la entrevista. Y si la evidencia nueva contradice lo que el requerimiento dice, eso se
  nombra: no se reescribe el requerimiento en silencio.
- **No existe** → **es el hallazgo del comando.** Un tema con muchas citas y sin
  requerimiento es lo que el cliente viene diciendo y nadie ha convertido en nada. Ofrece
  crearlo en `propuesto`, con su doliente, y **no lo crees sin que alguien lo asuma**.

**4. Recalcula. No cuentes tú.**

```
python3 scripts/producto.py compute --state <estado> --config <archivo>
```

**5. Si entra material de fuentes públicas, entra citado y marcado como lo que es.**

Reseñas del producto propio, lo que un competidor publica de su producto, un informe de
mercado. Aplica **demand-evidence** y su jerarquía: **que un competidor lo tenga dice que
alguien apostó, no que tu cliente lo quiera**, y un informe de otra geografía se cita
diciendo de qué mercado habla.

Se recopila y se cita. **No se concluye posicionamiento**, no se compara con tu producto y
no se deriva una recomendación: eso es juicio de producto y necesita la estrategia, que no
está en ningún documento.

**6. Marca lo que es afirmación del entrevistado y no dato.** *«Perdemos como el 30% de las
ventas»* es una cita. Si el producto va a apoyarse en ese número, aplica **product-metrics**:
se busca la serie, o se declara que no existe.

## Salida

```markdown
## Descubrimiento — [producto] · [N] piezas nuevas al [fecha]

### Temas
> **[Título del tema]** — [N] de [N] piezas
> — *«[cita]»* · [quién], [fecha]
> — *«[cita]»* · [quién], [fecha]
> **En el registro:** [REQ-xxx | **ninguno**]

### Dicho y nunca convertido en nada
| Tema | Veces | Desde | Ningún requerimiento lo recoge |
[La sección que vale. Va con el tiempo que lleva dicho.]

### Dicho una sola vez
| Qué | Quién | Cuándo |
[No se promueve y no se descarta.]

### Afirmaciones numéricas de los entrevistados
| Lo que dijeron | Quién | ¿Hay serie que lo mida? |

### De fuentes públicas
| Qué | Fuente | De cuándo | Qué tan fuerte |
[Recopilación citada. No concluye posicionamiento. Si no entró ninguna, se omite.]

### Evidencia nueva que contradice el registro
| REQ | Decía | Dice la entrevista | Las dos fuentes |
```

**Si el material nuevo no produce ningún tema nuevo, una línea:** *«[N] piezas leídas,
ningún tema que el registro no tenga ya»*. Y se acaba.

## Lo que este comando no hace

- **No le pone intención al cliente.** *«Lo que en realidad quiere es...»* es la parte del
  trabajo que necesita estar frente a la persona.
- **No prioriza los temas.** La frecuencia se cuenta; la importancia se decide.
- **No corrige lo que dijeron.** Normaliza nombres y transcribe el resto.
- **No crea requerimientos solo.** Propone; el doliente lo asume una persona.

## Después

Si algún tema nuevo quedó como requerimiento, ofrece `/product-requirements` para ver el
registro completo con los vacíos. Y si la evidencia nueva contradice la definición, ofrece
`/product-definition`: eso ya no es descubrimiento, es que la definición envejeció.

## Deja la corrida registrada

Lo último, siempre:

```
python3 scripts/producto.py corrida --state <estado> --what product-discovery \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-product-discovery.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
