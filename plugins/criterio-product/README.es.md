# Alba · el agente de un producto

**Alba te dice qué de tu definición se sostiene, y qué se sostiene solo.** Tú hablas con el
cliente, lees lo que el cliente no dice, decides qué se construye y pones el precio. Ella
llega con la cadena de evidencia armada y los huecos señalados.

[English](README.md) · `criterio-product` · Apache 2.0 · Una instancia por producto

**Estado: los once comandos construidos**, doce skills, y la aritmética del registro
verificada con 62 comprobaciones. **Lo que todavía no se ha probado: el registro sobre la
documentación real de un producto** — la extracción desde entrevistas y casos de negocio no
se ha ejercitado fuera de material sintético. Nada se anuncia como terminado hasta que pasen
los [criterios de aceptación](DISENO.es.md#criterios-de-aceptación).

**Esta página se lee sola.** Alba funciona sin sus hermanos: si solo defines productos, aquí
está todo, incluidas sus pruebas. La familia —cómo se encuentra con Vera y con Samuel— está en
el [README de `criterio-pmo`](../criterio-pmo/README.es.md).

---

## El alcance

| | |
|---|---|
| **A quién extiende** | Al gerente de producto |
| **Sobre qué trabaja** | **Un producto, antes de que exista el proyecto** |
| **Qué mira** | La definición, las entrevistas, los tickets y las métricas |
| **Cadencia** | Por temporadas: una ronda de entrevistas, un comité de producto, una definición que se cierra |
| **Instancias** | Una por producto |

**Lo que hace y nadie más hace: contrastar la definición contra la evidencia de demanda.**
Es la misma comparación que sostiene a toda la familia —lo declarado contra lo evidenciado—
pero **un paso antes de que haya plan**, cuando todavía no hay línea base ni presupuesto
contra los que medir.

**Lo que puede responder que hoy nadie responde:** qué afirmación de tu definición **no está
dicha en ninguna parte**, qué supuesto lleva meses sin verificarse, dónde el caso de negocio
afirma un número que la métrica no sostiene, y qué se decidió construir que **nadie está
construyendo**.

## Dónde se superpone con los otros dos, y dónde no

La superposición es mínima **a propósito**: lo de Alba ocurre antes del proyecto, lo de
Samuel durante, lo de Vera por encima. Donde dos pueden tocar lo mismo, lo que cambia es **el
momento y quién responde**.

| Lo que también toca otro | Quién más | Qué hace Alba, y qué no |
|---|---|---|
| **El acta de constitución** | Samuel · Vera | **Alba la redacta, y con ella nace la ficha del proyecto.** De ahí en adelante no la vuelve a escribir: una ficha, un escritor. Samuel la escribe desde entonces; Vera la lee |
| **Los requerimientos** | Samuel | Alba lleva el registro **antes** de que haya proyecto y con su evidencia de demanda. Lo que entra al alcance de un proyecto ya es de Samuel |
| **Las métricas del producto** | Vera | Alba las contrasta contra lo que el negocio **declara** en su caso de negocio. Vera mira el producto a través de **los proyectos que lo construyen**, que es otra pregunta |
| **Saber si el producto se está construyendo** | Samuel | Alba no le pregunta a nadie: **lee la ficha que el proyecto publica** y confirma si de verdad ejecuta su producto. Cuando no coincide, lo reporta y no lo arregla |

**Si solo instalas a Alba, no pierdes nada de tu producto.** Lo que no tendrás es la ficha del
proyecto publicada para confirmar las trazas, y eso la página lo dice en vez de darlo por
bueno.

## Instalación

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-product@criterio
/product-setup
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez-company/criterio`.

Si gestionas un proyecto y no un producto, lo tuyo es
[Samuel](../criterio-pm/README.es.md). Si gestionas el portafolio,
[Vera](../criterio-pmo/VERA.es.md).

## El primer resultado

`/product-setup` mira tu carpeta, hace cuatro preguntas —una a la vez, cada una con una
respuesta sugerida— y **toma la definición que ya tengas escrita y la parte en afirmaciones.**
Con eso te muestra, en menos de diez minutos, tres listas:

- **Lo que la evidencia sostiene**, con el documento y la fecha.
- **Lo que se sostiene en un supuesto** que nadie ha verificado.
- **Lo que no está dicho en ninguna parte.**

Esa tercera lista es la que ninguna revisión encuentra, **porque leyendo un documento bien
escrito todo parece sustentado.**

**Lo que queda configurado** lo escribe `/product-setup` a partir de lo que respondiste, en tu
equipo y en un archivo tuyo: dónde está la documentación del producto, dónde vive tu registro,
cada cuánto se revisa, los cuatro umbrales, y el registro de que aceptaste los términos con tu
nombre y la fecha. Todo eso se cambia **hablando**.

## El hallazgo que nadie más produce

En un proyecto se contrasta el **estado que el gerente declara** contra la evidencia
documental. En un producto se contrasta la **definición** contra la evidencia de demanda.

Es la misma comparación, aguas arriba, y falla igual: **nadie miente.** La definición se
escribió hace ocho meses con la evidencia que había, la evidencia envejeció, la cifra del caso
de negocio se quedó, y el documento sigue igual de convincente.

> **tx_mensuales** · el caso de negocio del 4 de marzo dice **250.000**
> El tablero transaccional mide **180.000** al 1 de septiembre — **28% de diferencia**
> No es que alguien se equivocó: es que la cifra con la que se está decidiendo es de marzo.

*«El negocio y los datos no coinciden»* no le permite a nadie hacer nada. Las dos fuentes y
las dos fechas, sí. Ese caso sale del corpus sintético, con la respuesta escrita a mano
**antes** de correr el cálculo.

Y hay un segundo hallazgo de la misma clase: **lo decidido que nadie está construyendo.** Se
decidió en un comité, se escribió en el acta, y no entró en el alcance de ningún proyecto; se
descubre meses después, normalmente en otro comité. `/product-trace` lo encuentra, y encuentra
además la brecha que nadie busca: **el proyecto que dice ejecutar tu producto, y cuya ficha
dice que ejecuta otro.** Alba no le cree a su propio registro: lo confirma contra la ficha del
proyecto, que tiene otro dueño y otra cadencia. Cuando las dos no coinciden, **el desacuerdo se
reporta y no se arregla desde aquí.**

## No espera a que lo llamen

Esta es la diferencia entre un comando y un agente. Un comando espera. **Este se programa y
corre solo.**

Su cadencia es por temporadas, y de ahí sale qué toca. La decisión es aritmética de fechas, así
que la toma el código y no el criterio del momento:

```
python3 scripts/producto.py due --state <estado> --config <archivo>
```

Y `/product-wake` es el comando que el reloj invoca: mira qué cruzó un umbral mientras nadie
miraba —un supuesto que lleva demasiado sin verificarse, una evidencia que envejeció, un
requerimiento que nadie decide— y **si no cruzó nada no produce nada.** Callarse cuando no pasó
nada no es una omisión — es la única razón por la que un agente que corre todas las semanas
sigue instalado el mes siguiente.

Ponerlo en un reloj es del lado de tu organización: una tarea programada en Cowork, o el
programador del sistema en Claude Code. **Y si no quieren corridas desatendidas** —en un banco
es una respuesta razonable— la cadencia sigue diciendo qué toca, corrida a mano. Lo que se
pierde es que avise sin que nadie pregunte.

**Y si quieres que el comité de producto lo vea sin pedírtelo**, la familia tiene un servidor
que lo publica con una sección para productos, y quien mira puede dejarle una pregunta escrita
al agente. → **[Rostrum](../criterio-pmo/SERVER.es.md)**

## Lo que nunca hace

- **No decide qué se construye.** Eso lo decides tú. Alba te muestra qué lo sostiene, y si
  ella decidiera, la comparación compararía al sistema consigo mismo.
- **No habla con tu cliente**, y no lee lo que el cliente no dice. Es la parte del oficio que
  ningún agente va a tener, y es la que alimenta todo lo demás.
- **No juzga si algo va a gustar.**
- **No dice si tu producto cumple la norma.** Nombra y cita las obligaciones que toca; el
  juicio es jurídico y la responsabilidad es de tu organización.
- **No rellena un vacío con lo razonable.** Una especificación con los huecos rellenados se ve
  completa, se aprueba, y lo que nadie decidió queda decidido por el agente.
- **No escribe en tu carpeta de documentación.**
- **No adivina.** Cada dato lleva la cita del documento de donde salió. *«No está dicho en
  ninguna parte»* es una respuesta válida y esperada.

**Y hay una cosa que deliberadamente deja de hacer el día del acta: escribir la ficha del
proyecto.** La crea con el acta firmada y a partir de ahí solo la lee. Si dos agentes la
escribieran, el desacuerdo entre ellos dejaría de ser una señal y sería una carrera.

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura de la
plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus políticas antes
de apuntarlo a material confidencial. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

---

De aquí para abajo es para quien quiera auditarlo antes de instalarlo. **Todo esto se puede
leer sin ejecutar nada**, y eso es deliberado.

## Cómo se trabaja con Alba

Los tres agentes comparten cinco conductas, y ninguna es estilo: son las que hacen que el
resultado se pueda poner frente a un comité. **Cada dato lleva la cita** del documento y su
fecha · **«no está dicho en ninguna parte» es una respuesta válida** · **se callan cuando no
hay novedad** · **ninguno declara** · **ninguno le escribe a nadie**. Están explicadas en el
[README de la familia](../criterio-pmo/README.es.md#lo-que-comparten-los-tres).

Lo que cambia entre uno y otro es **el ritmo de la conversación**, y eso conviene saberlo
antes de instalar.

**Con Alba se conversa por temporadas.** Trabaja antes de que exista el proyecto, y ese trabajo
no es semanal: viene por rachas —una ronda de entrevistas, un comité de producto, una
definición que hay que cerrar— con semanas tranquilas en medio.

**El ritmo:** `/product-setup` una vez; `/product-discovery` cada vez que termina una ronda de
entrevistas; `/product-definition` cuando la definición se va a cerrar o cuando alguien la va a
discutir; `/product-charter` el día que se vuelve proyecto. `/product-wake` semanal avisa de lo
que cruzó un umbral mientras nadie miraba.

**Lo que te va a pedir a ti:** **hablar con el cliente.** Es la parte del oficio que ningún
agente va a tener, y sin ella no hay nada que sintetizar. Y **decidir**: lo que lleva sesenta
días sin decidirse sigue sin decidirse cuando Alba termina; lo que cambia es que ahora tiene
nombre, días y alguien a quien preguntarle.

**Lo que no le pidas:** que te diga si algo va a gustar. Eso no está en ningún documento.

## Cómo funciona

La espina es el **registro de requerimiento**: un contrato de datos que todos los comandos leen
y escriben, con la cita al documento fuente y a su fecha en cada campo, y con cinco estados que
dicen qué exige cada uno. Ningún comando lee documentos crudos por su cuenta. Eso permite
recorrer la traza —requerimiento → decisión → proyecto → entregable— sin volver a leer nada, y
**calcular en vez de opinar**.

Y hay una costura con el proyecto, porque el objeto cambia de manos:

| | Antes del acta | Después |
|---|---|---|
| **El objeto** | El registro de requerimiento | La ficha del proyecto |
| **Quién escribe** | Alba | El agente del proyecto, salvo el estado declarado |
| **Qué hace Alba** | Todo | **Solo leer**, para saber si su producto se está construyendo |

Tres scripts, que son lo único que no opina. [`scripts/producto.py`](scripts/producto.py) hace
la aritmética propia de Alba: las once señales, los cuatro umbrales, la cadencia y el
solapamiento entre dos productos. [`scripts/texto.py`](scripts/texto.py) convierte el documento
a texto, y [`scripts/pmo.py`](scripts/pmo.py) aporta la parte de la ficha de proyecto que Alba
crea con el acta. **Los dos últimos son copias literales de los de Vera, no importaciones**,
porque un plugin instalado tiene que correr solo; en el repositorio,
`scripts/sincronizar.py --check` falla si las copias se separaron.

## Los once comandos

| Comando | Qué hace |
|---|---|
| `/product-setup` | **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y contrasta la definición que ya tengas |
| `/product-discovery` | Entrevistas y tickets en temas con la cita de quién lo dijo, y el tema que lleva meses dicho sin que nadie lo convierta en nada |
| `/product-requirements` | El registro con sus vacíos: sin doliente, sin criterio, aceptado sin que nadie lo pidiera, y lo que nadie decide |
| `/product-definition` | La definición contra la evidencia de demanda, y dónde el negocio y los datos no coinciden |
| `/product-trace` | Requerimiento → decisión → proyecto → entregable, y las dos brechas de arriba |
| `/product-spec` | El borrador de especificación con criterios verificables y los vacíos señalados, no rellenados |
| `/product-charter` | El acta de constitución: donde nace la ficha y el escritor cambia de manos |
| `/product-business-case` | La estructura del caso de negocio con cada cifra citada, y los vacíos con quién los produce |
| `/product-publish` | Publica tu ficha donde los demás productos la puedan leer |
| `/product-overlap` | Dónde te pisas con otro producto: la misma métrica contada dos veces, el mismo proyecto, el mismo segmento |
| `/product-wake` | **El que se le pone a un reloj.** Lo que cruzó un umbral sin que nadie hiciera nada |

## Los doce skills

Se cargan solos cuando el tema aparece. Ocho son propios de producto; cuatro son copias
literales de `criterio-pmo`, porque son método y no rol.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `requirement-record` | **El contrato de datos de Alba.** Esquema, extracción, citación, los cinco estados y qué exige cada uno | Propia de Alba |
| `product-health` | Las once señales, los cuatro umbrales, en qué orden se leen y **cuál no es hallazgo** | Propia de Alba |
| `demand-evidence` | Qué cuenta como evidencia de que alguien pidió algo, qué no cuenta aunque lo parezca, y cómo envejece | Propia de Alba |
| `discovery-synthesis` | Entrevistas y tickets en temas con la cita. Un tema es un conjunto de citas, no una afirmación | Propia de Alba |
| `assumption-tracking` | El supuesto escrito de forma que puede resultar falso, y el día en que se vuelve riesgo registrado | Propia de Alba |
| `product-metrics` | La serie con su fuente y su definición, y el contraste entre lo declarado y lo medido | Propia de Alba |
| `specification-draft` | El criterio de aceptación verificable, y la regla de señalar el vacío en vez de rellenarlo | Propia de Alba |
| `regulatory-sweep` | Las obligaciones que toca la definición, citadas. **No opina sobre cumplimiento** | Propia de Alba |
| `project-record` | La ficha del proyecto: nace con el acta, y Alba es quien la crea | Copia de Vera · también en Samuel |
| `governance-artifacts` | Qué contiene un acta de constitución y quién decide qué | Copia de Vera · también en Samuel |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué | Copia de Vera · también en Samuel |
| `raid-taxonomy` | A dónde se muda un supuesto el día que nadie lo verifica | Copia de Vera · también en Samuel |

## Cómo se verifica

```
python3 tests/criterio-product/grade.py    sobre dos productos, con control negativo
python3 scripts/producto.py selftest      62 comprobaciones sobre la aritmética
```

Con la librería estándar, sin instalar nada. Sobre un corpus sintético con respuestas escritas
a mano leyendo los documentos — **incluido un control negativo**: un producto con definición,
entrevistas y registro que no produce ni un hallazgo. Un agente que encuentra algo ahí es un
generador de ruido.

**Cómo salió la última corrida, generado desde la corrida misma:**
[`tests/criterio-product/RESULTADOS.md`](../../tests/criterio-product/RESULTADOS.md). Qué
prueba cada pieza del material y, con el mismo detalle, **qué no**, en
[`EVIDENCIA.md`](../../tests/criterio-product/EVIDENCIA.md).

El diseño completo, con los criterios de aceptación y lo que sigue siendo de la persona, en
[`DISENO.es.md`](DISENO.es.md), que viaja con el plugin.

Y las pruebas del conjunto de la familia —lo que ningún agente puede responder solo— en el
[README de la familia](../criterio-pmo/README.es.md#las-pruebas-de-la-familia).
