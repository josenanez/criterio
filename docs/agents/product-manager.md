# Caliper · el agente Product Manager

Mide antes de trazar. Extiende al **gerente de producto**: la persona que define qué se va a construir, antes de que
exista un proyecto.

Marco general, definición de las clases y de las columnas: [README](README.md).

| | |
|---|---|
| **Instancia** | Una por producto |
| **Alcance** | El producto a lo largo de su vida, no un proyecto |
| **Escribe** | Su propio registro previo. **Crea la ficha** con el acta de constitución |
| **Lee** | Su registro, y las fichas de los proyectos que ejecutan su producto |
| **Estado** | Sin construir |

---

## Por qué este agente no encaja todavía

La espina de la ficha es `plan` + `baseline` + `money`. En investigación y definición **ninguno
de los tres existe**, así que este agente no escribe en la ficha: trabaja antes, con su propio
registro.

**La costura con el agente Project Manager es el acta de constitución** — el momento en que un
problema definido se vuelve plan con doliente, autoridad y criterio de éxito. Ya está en el
plugin, en `governance-artifacts` y `/project-charter`: el traspaso no necesita inventar nada.

Y el PMO no vigila proyectos sueltos: vigila **todos los proyectos que tienen producto**, y para
eso necesita la dimensión `producto` en la ficha, que hoy no existe.

---

## El flujo

```
GERENTE DE PRODUCTO  (clase C)                 AGENTE PRODUCT  (clases A y B)
──────────────────────────────────────────────────────────────────────────────────
habla con el cliente
lee lo que el cliente no dice
   └─► entrevistas, notas, tickets ──────────►  sintetiza en temas, con la cita
                                               de quién lo dijo
                                          ┌──  contrasta la definición contra la
                                          │    evidencia de demanda que existe
   ◄──── qué se sostiene, qué no, ◄───────┘     marca los supuestos no verificados
         qué no está dicho

decide qué se construye
pone el precio
   └─► la decisión ──────────────────────────►  entra al registro de requerimientos
                                               con estado, doliente y evidencia

   ◄──── borrador de especificación ◄─────────  y el borrador del acta
firma el acta de constitución
   └─► acta ─────────────────────────────────►  nace la ficha · pasa al agente PM

firma el go / no-go
   └─► criterio de éxito y fecha ────────────►  referencia del cierre, meses después
```

---

## A · Lo que haría, y hoy consume tiempo de alguien

Ninguna está construida. Todas dependen primero del registro de requerimiento.

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Sintetizar entrevistas y retroalimentación en temas | Entrevistas, notas, tickets, encuestas | Temas con la cita de quién lo dijo, nunca como conclusión propia | Falta |
| Inventario de requerimientos | La definición y los documentos que la soportan | Un registro por requerimiento, con estado, doliente y evidencia | Falta |
| Trazabilidad requerimiento → decisión → entregable | El registro y las fichas de los proyectos que lo ejecutan | La cadena completa, que vuelve *"qué falta"* un filtro y no una corrida de modelo | Falta |
| Detectar requerimientos sin criterio de aceptación o sin doliente | El registro | La lista de vacíos; igual que un riesgo sin doliente, es decoración | Falta |
| Recopilar análisis competitivo de fuentes públicas | Fuentes públicas | Recopilación citada. No concluye posicionamiento | Falta |
| Consolidar las métricas del producto | El sistema donde viven | La serie al día, con su fuente y fecha | Falta |
| Borrador de la especificación | Lo ya decidido y el registro de requerimientos | Borrador con criterios de aceptación y vacíos señalados | Falta |
| Producir el borrador del acta de constitución | La definición cerrada | El acta que el gerente firma, y con la que nace la ficha | Falta |

## B · Lo que haría, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Contrastar la definición contra la evidencia de demanda | La definición y todo lo que la organización tenga escrito sobre demanda | Qué se sostiene, con qué documento, y qué no está dicho en ninguna parte | Falta |
| Detectar contradicción entre lo que dice el negocio y lo que dicen los datos | Documentos del negocio y las métricas | El conflicto con las dos fuentes y sus fechas | Falta |
| Identificar los supuestos no verificados de la definición | La definición | Los supuestos declarados como tales, para validarlos o convertirlos en riesgo | Falta |
| Primer barrido de obligaciones normativas que toca el producto | La definición y la norma aplicable | Las obligaciones citadas. **No opina sobre cumplimiento** | Falta |
| Estructurar el caso de negocio | Lo que el negocio entregue | La estructura y los vacíos. Las cifras son del negocio | Falta |
| Análisis de canibalización | Datos internos de los productos existentes | El solapamiento, con su fuente | Falta |

La primera fila traslada la tesis de Criterio aguas arriba: en un proyecto se contrasta el
**estado declarado** contra la evidencia documental; en un producto se contrasta la
**definición** contra la evidencia de demanda. Es la misma comparación, un paso antes.

## C · Lo que el agente no hace

Lista de acciones que el agente no ejecuta. No es una evaluación de riesgo ni pretende ser
exhaustiva: **la responsabilidad de uso y ejecución es de la organización que lo despliega.**
Ver [README](README.md#c--lo-que-el-agente-no-hace).

| Función | Requiere | Qué le entrega al agente |
|---|---|---|
| Decidir qué se construye y qué no | Autoridad | La decisión: sin ella no hay acta, y sin acta no nace la ficha |
| Hablar con el cliente | Información fuera de los documentos | La entrevista, que es el insumo de toda la síntesis |
| Leer lo que el cliente no dice | Información fuera de los documentos | La definición |
| Definir precio y modelo de negocio | Autoridad | El caso de negocio con sus cifras |
| Juzgar deseabilidad: si esto va a gustar | Información fuera de los documentos | La priorización del registro |
| Firmar el go / no-go de lanzamiento | Autoridad | La fecha y el criterio de éxito, que son la referencia del cierre |
| Retirar un producto | Autoridad | El cierre del ciclo de vida |
| Asumir el riesgo regulatorio de una definición | Autoridad | Las restricciones que el agente registra |
| Priorizar el backlog cuando hay conflicto de intereses | Autoridad · información fuera de los documentos | El orden |

Este es el agente con **la peor cobertura de información de los tres**, y conviene decirlo en voz
alta. La verdad de un portafolio vive en documentos; la de un proyecto, en conversación que deja
minuta; la de un producto, en clientes, mercado y juicio — de lo cual casi nada queda escrito
antes de la decisión.

---

## Lo que sigue siendo del gerente de producto persona

**Habla con el cliente, lee lo que el cliente no dice, juzga si algo va a gustar, decide qué se
construye, pone el precio y firma el go / no-go.** Nada de eso se toca.

Lo que cambia es que llega a esa decisión con la cadena de evidencia armada y los huecos
señalados: qué de la definición está sustentado y por qué documento, qué supuestos no se han
verificado, dónde el negocio y los datos dicen cosas distintas, y qué obligaciones normativas
toca lo que va a definir.

Si una organización quitara al gerente de producto y dejara solo al agente, se rompe antes que
en los otros dos casos: **no hay descubrimiento, y sin descubrimiento no hay nada que
sintetizar.** Un agente de producto sin gerente de producto sintetiza el vacío.

---

## Antes de construir nada

1. **El registro de requerimiento**, que es la dependencia bloqueante.
2. **El campo `producto` en la ficha**, para que el PMO pueda mirar por producto.
3. **Que la ficha tenga dos escritores y el contrato haya aguantado** — es decir, que el agente
   PM esté corriendo sobre documentación real.

El tercero no es una formalidad. Definir este agente antes diluye la única tesis que hoy es
medible, y el proyecto ya pagó una vez el costo de abrir dos líneas a la vez: está escrito en
[`docs/decisions/0005`](../decisions/0005-scope-pmo-only.md).
