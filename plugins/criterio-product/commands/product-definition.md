---
description: Contrasta la definición del producto contra la evidencia de demanda que exista — qué se sostiene, qué se sostiene en un supuesto, qué no está dicho en ninguna parte, y dónde el negocio y los datos no coinciden
argument-hint: "[ruta del documento de definición] o vacío para la configurada"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /product-definition — La definición contra la evidencia

> **Dónde está la configuración:** `.criterio/producto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo producto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-product:product-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos. **Y sin subagentes en paralelo:** se leen hasta `execution.workers` proyectos a la vez según la configuración —1 si no lo dice, que es uno tras otro en esta misma conversación—; nunca más por decisión propia. El arnés cuenta los subagentes de cada corrida y marca la que se exceda.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.


## Lo primero, antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Es la tesis de Criterio un paso aguas arriba. En un proyecto se contrasta el **estado que el
gerente declara** contra la evidencia documental. En un producto se contrasta la
**definición** contra la evidencia de demanda.

Y falla igual: **nadie miente.** La definición se escribió hace ocho meses con la evidencia
que había, la evidencia envejeció, la cifra del caso de negocio se quedó, y el documento
sigue igual de convincente.

## Invocación

```
/product-definition
/product-definition 00-definicion/caso-de-negocio-v3.md
```

## Flujo

**1. Parte la definición en afirmaciones.** Cada frase que dice algo sobre el mundo —quién
tiene el problema, qué tan grande es, qué haría el cliente, cuánto pagaría— es una afirmación
aparte. Una definición de dos páginas suele tener entre quince y treinta.

**2. Para cada una, busca qué la sostiene, y clasifícala en tres.** Aplica
**demand-evidence** y su jerarquía —alguien ya pagó pesa más que alguien dijo que usaría—:

- **Sostenida**, y se dice por qué documento y de qué fecha.
- **Sostenida por un supuesto**, que se declara como tal. Va a **assumption-tracking**.
- **No está dicha en ninguna parte.** **Esta es la categoría del comando.** Nadie la afirmó
  ni la negó, y leyendo un documento bien escrito no se nota.

**Lo que la evidencia contradice va aparte**, con las dos fuentes y las dos fechas. No se
mezcla con lo que no está dicho: es otra cosa y se resuelve de otra manera.

**3. Contrasta las cifras.** Aplica **product-metrics**. El cálculo compara lo declarado
contra el punto más reciente de cada serie:

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" compute --state <estado> --config <archivo>
```

`claim_vs_metric` llega con las dos fuentes, las dos fechas y la dirección. **Cítala, no la
vuelvas a juzgar a ojo.** Y cuando no hay serie para una afirmación numérica, **dilo**: no es
contradicción, es que nadie está midiendo lo que el negocio afirmó, y es el caso más común.

**4. Revisa los supuestos.** Aplica **assumption-tracking**. Los de la definición sostienen
el producto entero. Para cada uno sin verificar: cuántos días lleva, y **qué haría falta para
verificarlo** — que es lo único accionable que este comando puede entregar sobre un supuesto.

Un supuesto escrito de forma que no se puede desmentir se marca así: *«el comercio está
digitalizado»* no se puede verificar, y por eso nadie lo va a verificar.

**5. Barre lo normativo.** Aplica **regulatory-sweep**, con su regla dura: **nombra y cita,
no dice si cumple.** Y usa el estado *«no tengo la norma a la vista»* cuando sea el caso, para
que un vacío del agente no se lea como un cumplimiento.

**6. Di qué falta para cerrar la definición.** Los campos que el cálculo trae en `unknown`:
el problema, para quién, el criterio de éxito y quién decide. **Sin criterio de éxito
declarado el producto no se puede cerrar**, porque el cierre se juzga contra él meses
después, y no haberlo escrito es la razón por la que nadie cierra nada.

## Salida

```markdown
## Definición — [producto] · contrastada al [fecha]
**Documento:** [cuál] · **del** [fecha] · [N] afirmaciones

### Lo que la evidencia contradice
| Afirma | Dice la evidencia | Las dos fuentes y sus fechas |
[Va primero. Si no hay nada, se dice en una línea.]

### El negocio y los datos
| Métrica | Declarado | Medido | Diferencia | Las dos fuentes y fechas |
[Solo las que pasan del umbral. Lo de abajo es imprecisión, no contradicción.]

### Afirmaciones numéricas que nadie mide
| Afirma | De qué documento | No hay serie |

### No está dicho en ninguna parte
[La sección que vale. Una línea cada una.]

### Sostenida por un supuesto
| Supuesto | Días sin verificar | Qué haría falta para verificarlo |

### Sostenida por evidencia
| Afirmación | Sostenida por | De cuándo | Qué tan fuerte |

### Evidencia que ya envejeció
| Afirmación | Lo más nuevo que la sostiene | Hace |

### Lo normativo que toca
| Qué toca | País | Obligación | Norma | Estado |
[Nombrado y citado. Esto va a revisión jurídica, no la reemplaza.]

### Lo que falta para cerrar la definición
[Problema, para quién, criterio de éxito, quién decide: los que no estén.]
```

## Lo que este comando no hace

- **No decide si la demanda alcanza.** Que ocho de ochenta lo pidan es un dato; si eso
  justifica construirlo depende del costo, de la estrategia y de la política.
- **No juzga si va a gustar.** No está en ningún documento.
- **No dice si el producto cumple la norma.** Ver el paso 5.
- **No reescribe la definición.** Produce el contraste; la definición es de su autor.
- **No inventa el supuesto que el autor «obviamente tenía».** Si el documento no lo dice, la
  categoría es *no está dicho en ninguna parte*.

## Después

Si hay supuestos que llevan meses sin verificarse, ofrece convertirlos en riesgo con doliente
— aplica **raid-taxonomy** — porque a partir de cierto punto eso es lo que son. Y si la
definición quedó cerrada, con criterio de éxito y con autoridad, ofrece `/product-charter`.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida --state <estado> --what product-definition \
    --salida <estado>/corridas/salida-product-definition.md \
    --caso <código del producto, el de la configuración> \
    --nota "qué de la definición sostiene la evidencia"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` cuenta lo que hay que contar y deja `<estado>/corridas/<fecha>-product-definition-<n>.md`: qué encontró por señal, cuánto tardó, y cuántos hallazgos más o menos que la vez anterior.
