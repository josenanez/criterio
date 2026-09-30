---
description: La estructura del caso de negocio y sus vacíos, con cada cifra citada al documento del que sale — las cifras son del negocio, no del agente
argument-hint: "[ruta del caso de negocio] o vacío para armar la estructura desde cero"
allowed-tools: Read, Glob, Grep, Write, Edit, Bash(python3:*), Bash(ls:*), Bash(mkdir:*), Bash(mv -n:*)
---

# /product-business-case — El caso de negocio

> **Dónde está la configuración:** `.criterio/producto/<código>/config.json`, en la carpeta donde corre la sesión; con un solo producto configurado es ese, con varios el del código que viene en el argumento. La escribe `/criterio-product:product-setup`. Si no existe, dilo en una línea y para: no la busques en otro sitio ni la inventes.

> **Cómo se trabaja sin pedir permiso a cada paso:** los scripts se llaman por su ruta absoluta, `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/…"`, uno por llamada, sin `cd`, sin `&&` ni tuberías; y los documentos se leen con Read, Glob y Grep, no con `cat` ni `find`. Un comando compuesto o un script buscado por el disco pide una aprobación cada vez, y en un barrido eso son cientos. **Y sin subagentes en paralelo:** se leen hasta `execution.workers` proyectos a la vez según la configuración —1 si no lo dice, que es uno tras otro en esta misma conversación—; nunca más por decisión propia. El arnés cuenta los subagentes de cada corrida y marca la que se exceda.
> **Antes de producir nada:** verifica `terms_accepted` en la configuración local. Si
> falta, o su versión es anterior a la de `TERMS.md`, muestra el descargo corto, pide
> aceptación explícita y ofrece guardarla.

## Antes de leer nada

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida-inicio --state <estado>
```

Marca el arranque para que **el tiempo lo mida la corrida**. Un tiempo que alguien escribe al final es un recuerdo, no una medición.

## Para qué existe

Un caso de negocio se aprueba o se rechaza por sus cifras, y casi ninguna de esas cifras
tiene de dónde salió escrito al lado. Seis meses después nadie puede reconstruir por qué se
esperaban 250.000 transacciones, y para entonces el número ya está en tres presentaciones.

Este comando hace **la estructura y la trazabilidad**: cada cifra con su fuente, y cada
hueco nombrado. **Las cifras son del negocio.** El agente no proyecta ingresos, no calcula
retorno y no estima beneficios — y esa no es una limitación de capacidad, es la línea que
hace que el documento se pueda defender.

## Invocación

```
/product-business-case                          arma la estructura desde cero
/product-business-case 00-definicion/caso-v2.md revisa uno que ya existe
```

## Flujo

**1. Toma lo que ya está escrito, y no empieces por una plantilla.** El problema, a quién
sirve y el criterio de éxito salen de la definición, con su cita. Aplica
**requirement-record** para el alcance: lo que entra al caso de negocio son los
requerimientos decididos, no el registro entero.

**2. Cada cifra, con el documento del que sale y su fecha.** Es la regla del comando. Una
cifra sin fuente **no entra al caso de negocio**: entra a la lista de vacíos con la
pregunta de quién la produce.

Aplica **product-metrics** para las que sí tienen serie medida: si el caso afirma un número
y la serie mide otro, **eso va dentro del caso**, con las dos cifras y las dos fechas. Un
caso de negocio que ignora su propia métrica es el que se cae en la primera pregunta del
comité.

**3. Separa las tres clases de cifra, y no las mezcles nunca:**

| Clase | Qué es | Quién la produce |
|---|---|---|
| **Medida** | Sale de una serie, con su fuente y su corte | El sistema donde el producto vive |
| **Declarada** | Alguien del negocio la afirmó, con su documento | El negocio |
| **Supuesta** | Nadie la ha afirmado; está implícita en el razonamiento | Nadie todavía — va a **assumption-tracking** |

La tercera columna es la que decide si el caso se sostiene. Un caso de negocio construido
sobre cifras supuestas que parecen declaradas es el que se aprueba y después no se cumple.

**4. Los costos, igual: con su fuente o en la lista de vacíos.** Contratos, cotizaciones,
el costo declarado del equipo. Si el costo de construir no está en ningún documento, **ese
es el primer vacío**, y sin él no hay caso de negocio que evaluar: hay una propuesta.

**5. Nombra lo que el caso no dice.** Normalmente: qué pasa si no se hace, qué alternativas
se consideraron, y cuándo se sabrá si funcionó. La última es la que más se olvida y la que
convierte el criterio de éxito en algo verificable meses después.

**6. Mira si otro producto afirma las mismas cifras.** Si hay productos publicados a la
vista, aplica el cruce de `/product-overlap` antes de cerrar: **dos casos de negocio que
cuentan las mismas transacciones producen una suma que no existe**, y el sitio donde eso
se detecta es aquí, no en el comité.

## Salida

```markdown
# Caso de negocio — [producto] · borrador del [fecha]
**Desde:** [la definición, con su fecha] · **Cifras con fuente:** [N] de [N]

## Qué problema resuelve, y para quién
[De la definición, con su cita.]

## Qué se construye
| Requerimiento | Estado | Evidencia de demanda |
[Los decididos. Con la cita de quién lo pidió.]

## Las cifras
| Cifra | Valor | Clase | De dónde sale | De cuándo |
[Medida · declarada · supuesta. Nunca mezcladas.]

### Donde la cifra declarada y la medida no coinciden
| Métrica | Declarada | Medida | Las dos fuentes y fechas |

## Los costos
| Concepto | Valor | De dónde sale |

## Supuestos sobre los que se sostiene
| Supuesto | Qué pasa si resulta falso | Quién lo verificaría |

## Vacíos
| Qué falta | Por qué importa | Quién lo produce |

## Cómo se sabrá si funcionó
[El criterio de éxito con su métrica y su fecha de corte. Si no está declarado, se dice:
sin esto el producto no se puede cerrar meses después.]

## Si hay otros productos publicados
[Métricas que otro producto también afirma. Si no hay ninguno publicado, se dice.]
```

## Lo que este comando no hace

- **No produce cifras.** Ni ingresos, ni retorno, ni beneficios, ni ahorro. Las trae con su
  fuente o las pone en vacíos.
- **No calcula rentabilidad ni periodo de recuperación.** Con cifras cuya fuente es un
  supuesto, cualquiera de esos números es una opinión con dos decimales.
- **No recomienda aprobar ni rechazar.** Arma el documento; decidir es de quien tiene la
  autoridad.
- **No rellena un vacío con un valor de referencia del sector.** Si entra una cifra de
  fuente pública, entra citada y marcada como externa, nunca como propia.

## Después

Ofrece pasar los supuestos al seguimiento con **assumption-tracking** —un supuesto que se
queda dentro del caso de negocio es el que nadie vuelve a mirar— y, si el caso se aprueba,
`/product-charter`: ahí es donde deja de ser un caso y se vuelve un proyecto.

## Deja la corrida registrada

Lo último, siempre. Antes de correrlo, escribe en `<estado>/corridas/salida-<qué>.md` **lo que le mostraste a la persona, tal cual y entero**: es lo que la corrida guarda como evidencia y lo que Rostrum muestra en la página de esa corrida. Sin ese archivo la corrida registra las cifras y declara que el resultado se quedó en la conversación.

```
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/producto.py" corrida --state <estado> --what product-business-case \
    --salida <estado>/corridas/salida-product-business-case.md \
    --caso <código del producto, el de la configuración> \
    --nota "qué produjo, y qué dijo que no sabía"
```

Sin esto la corrida no se puede compartir ni comparar, y cualquier estadística sobre ella tendría que teclearla una persona — que es medir su transcripción y no la corrida. `corrida` deja `<estado>/corridas/<fecha>-product-business-case.md`: cuánto tardó, sobre cuántos casos, qué señales estaban abiertas, y la nota.
