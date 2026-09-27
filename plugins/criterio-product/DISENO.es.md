# Alba · el agente Product Manager

**Alba**, el amanecer: la luz que hay antes de que se vea nada. Trabaja antes de que el
proyecto exista, cuando todavía no hay plan, ni línea base, ni presupuesto contra los que
medir.

Extiende al **gerente de producto**: la persona que define qué se va a construir, antes de
que exista un proyecto.

Marco general, definición de las clases y de las columnas:
[`FAMILIA.es.md`](../criterio-pmo/FAMILIA.es.md).

| | |
|---|---|
| **Instancia** | Una por producto |
| **Alcance** | El producto a lo largo de su vida, no un proyecto |
| **Cadencia** | Semanal. Sus umbrales se miden en meses, y es el único de los tres cuyos hallazgos aparecen sin que nadie haga nada |
| **Escribe** | Su propio registro previo. **Crea la ficha** con el acta de constitución |
| **Lee** | Su registro, y las fichas de los proyectos que ejecutan su producto |
| **Se distribuye** | Como `criterio-product`, plugin aparte, con `pmo.py` y `texto.py` copiados de `criterio-pmo` |
| **Estado** | Los once comandos construidos, doce skills, corpus propio y 28 comprobaciones. **La extracción sobre documentación real no se ha corrido** |
| **Evidencia** | [`tests/criterio-product/EVIDENCIA.md`](../../tests/criterio-product/EVIDENCIA.md) |

---

## Por qué no encaja en la ficha, y con qué trabaja entonces

La espina de la ficha es `plan` + `baseline` + `money`. En investigación y definición **ninguno
de los tres existe**, así que este agente no escribe en la ficha: trabaja antes, con su propio
registro — **el registro de requerimiento**, que es su contrato de datos y era la dependencia
bloqueante de todo lo demás. Está construido, con su aritmética aparte en `producto.py`: diez
señales, cuatro umbrales, y el contraste de la definición contra la evidencia de demanda, que
es la tesis de Criterio un paso aguas arriba.

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

Todas dependían primero del registro de requerimiento, que hoy existe.

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Sintetizar entrevistas y retroalimentación en temas | Entrevistas, notas, tickets, encuestas | Temas con la cita de quién lo dijo, nunca como conclusión propia | **Construido**: `/product-discovery` |
| Inventario de requerimientos | La definición y los documentos que la soportan | Un registro por requerimiento, con estado, doliente y evidencia | **Construido**: `/product-requirements`, sobre el registro |
| Trazabilidad requerimiento → decisión → entregable | El registro y las fichas de los proyectos que lo ejecutan | La cadena completa, que vuelve *"qué falta"* un filtro y no una corrida de modelo | **Construido**: `/product-trace`, y confirma cada traza contra la ficha del proyecto |
| Detectar requerimientos sin criterio de aceptación o sin doliente | El registro | La lista de vacíos; igual que un riesgo sin doliente, es decoración | **Construido**, en código: dos señales, y un área no cuenta como doliente |
| Recopilar análisis competitivo de fuentes públicas | Fuentes públicas | Recopilación citada, con su fecha y con qué tan fuerte es. No concluye posicionamiento | **Construido** · dentro de `/product-discovery`, porque una reseña pública es material de descubrimiento y no una categoría aparte |
| Consolidar las métricas del producto | El sistema donde viven | La serie al día, con su fuente y fecha | **Construido**: el skill `product-metrics` y la serie en el estado. No se conecta a ningún sistema |
| Borrador de la especificación | Lo ya decidido y el registro de requerimientos | Borrador con criterios de aceptación y vacíos señalados | **Construido**: `/product-spec`, con la regla de señalar el vacío en vez de rellenarlo |
| Producir el borrador del acta de constitución | La definición cerrada | El acta que el gerente firma, y con la que nace la ficha | **Construido**: `/product-charter`, y la ficha se crea después de la firma, nunca antes |

## B · Lo que haría, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Contrastar la definición contra la evidencia de demanda | La definición y todo lo que la organización tenga escrito sobre demanda | Qué se sostiene, con qué documento, y qué no está dicho en ninguna parte | **Construido**: `/product-definition`. Es la función que justifica al agente |
| Detectar contradicción entre lo que dice el negocio y lo que dicen los datos | Documentos del negocio y las métricas | El conflicto con las dos fuentes y sus fechas | **Construido**, en código: `claim_vs_metric`, con las dos fuentes, las dos fechas y la dirección |
| Identificar los supuestos no verificados de la definición | La definición | Los supuestos declarados como tales, para validarlos o convertirlos en riesgo | **Construido**: `assumption_unverified` con su umbral, y la frontera a la que se vuelve riesgo |
| Primer barrido de obligaciones normativas que toca el producto | La definición y la norma aplicable | Las obligaciones citadas. **No opina sobre cumplimiento** | **Construido**: el skill `regulatory-sweep`, dentro de `/product-definition` |
| Estructurar el caso de negocio | Lo que el negocio entregue | La estructura, cada cifra con su fuente, las tres clases de cifra sin mezclar, y los vacíos con quién los produce | **Construido** · `/product-business-case`. No calcula retorno: con cifras supuestas eso es una opinión con dos decimales |
| Análisis de canibalización | Lo que los demás productos publicaron | La métrica que dos casos de negocio cuentan dos veces, el proyecto con dos dueños, y el segmento repetido | **Construido** · `/product-publish` y `/product-overlap`. La instalación sigue mirando un producto: los demás **publican**, como el gerente de proyecto publica su ficha |

La primera fila traslada la tesis de Criterio aguas arriba: en un proyecto se contrasta el
**estado declarado** contra la evidencia documental; en un producto se contrasta la
**definición** contra la evidencia de demanda. Es la misma comparación, un paso antes.

## C · Lo que el agente no hace

Lista de acciones que el agente no ejecuta. No es una evaluación de riesgo ni pretende ser
exhaustiva: **la responsabilidad de uso y ejecución es de la organización que lo despliega.**
Ver [FAMILIA.es.md](../criterio-pmo/FAMILIA.es.md#c--lo-que-el-agente-no-hace).

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

## Los tres prerrequisitos, y cómo quedaron

1. ~~**El registro de requerimiento**, la dependencia bloqueante~~ — **construido**, con su
   aritmética aparte y 52 comprobaciones.
2. ~~**El campo `producto` en la ficha**~~ — **construido**, y hoy sirve en las dos
   direcciones: la PMO mira por producto, y Alba confirma contra él que el proyecto que dice
   ejecutar su producto sea de verdad el suyo.
3. **Que la ficha tenga dos escritores y el contrato haya aguantado.** El contrato existe y
   aguantó en la prueba: Samuel publica, Vera lee, y el desacuerdo sale como `pm_vs_pmo` con
   sus dos citas. **Lo que no ha pasado es que corra sobre documentación real de una
   organización**, y eso no se puede construir desde aquí.

Así que el estado honesto de este agente es **construido y verificado sobre corpus, no
probado sobre documentación real** — la misma frase que aplica a los otros dos, y la que
protege a quien instale esto. La razón por la que el tercer prerrequisito estaba escrito
sigue en pie y está en [`docs/decisions/0005`](../../docs/decisions/0005-scope-pmo-only.md): definir
este agente antes de que hubiera algo medible habría diluido la única tesis que se puede
probar. Hoy hay con qué medirlo, y lo que falta es una carpeta de verdad.
