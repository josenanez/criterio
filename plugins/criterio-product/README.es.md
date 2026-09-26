# criterio-product

**Alba te dice qué de tu definición se sostiene, y qué se sostiene solo.** Tú hablas con el
cliente, lees lo que el cliente no dice, decides qué se construye y pones el precio. Ella
llega con la cadena de evidencia armada y los huecos señalados.

[English](README.md) · Apache 2.0 · Una instancia por producto

**Estado: los siete comandos construidos**, doce skills, y la aritmética del registro
verificada con 44 comprobaciones. **Lo que todavía no se ha probado: el registro sobre la
documentación real de un producto** — la extracción desde entrevistas y casos de negocio no
se ha ejercitado fuera de material sintético. Nada se anuncia como terminado hasta que pasen
los [criterios de aceptación](ACCEPTANCE.md).

---

## Instalación

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-product@criterio
/product-setup
```

Si gestionas un proyecto y no un producto, lo tuyo es
[`criterio-pm`](../criterio-pm/README.es.md). Si gestionas el portafolio,
[`criterio-pmo`](../criterio-pmo/README.es.md).

## El primer resultado

`/product-setup` mira tu carpeta, hace cuatro preguntas —una a la vez, cada una con una
respuesta sugerida— y **toma la definición que ya tengas escrita y la parte en afirmaciones.**
Con eso te muestra, en menos de diez minutos, tres listas:

- **Lo que la evidencia sostiene**, con el documento y la fecha.
- **Lo que se sostiene en un supuesto** que nadie ha verificado.
- **Lo que no está dicho en ninguna parte.**

Esa tercera lista es la que ninguna revisión encuentra, **porque leyendo un documento bien
escrito todo parece sustentado.**

## La comparación, un paso antes del proyecto

En un proyecto se contrasta el **estado que el gerente declara** contra la evidencia
documental. En un producto se contrasta la **definición** contra la evidencia de demanda.

Es la misma comparación, aguas arriba, y falla igual: **nadie miente.** La definición se
escribió hace ocho meses con la evidencia que había, la evidencia envejeció, la cifra del caso
de negocio se quedó, y el documento sigue igual de convincente.

> **tx_mensuales** · el caso de negocio del 4 de marzo dice **250.000**
> El tablero transaccional mide **180.000** al 1 de septiembre — **28% de diferencia**
> No es que alguien se equivocó: es que la cifra con la que se está decidiendo es de marzo.

*«El negocio y los datos no coinciden»* no le permite a nadie hacer nada. Las dos fuentes y
las dos fechas, sí.

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

Y una que hay que decir en voz alta: **tus documentos se procesan en la infraestructura de la
plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus políticas antes
de apuntarlo a material confidencial. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

---

## Lo decidido que nadie está construyendo

Se decidió en un comité, se escribió en el acta, y no entró en el alcance de ningún proyecto.
Se descubre meses después, normalmente en otro comité.

`/product-trace` lo encuentra con un filtro, y encuentra además la brecha que nadie busca:
**el proyecto que dice ejecutar tu producto, y cuya ficha dice que ejecuta otro.** Alba no le
cree a su propio registro: lo confirma contra la ficha del proyecto, que tiene otro dueño y
otra cadencia.

Cuando las dos no coinciden, **el desacuerdo se reporta y no se arregla desde aquí.** Es la
misma regla que gobierna a las dos fichas de un proyecto, un nivel más arriba.

## Dónde termina Alba y empieza el proyecto

`/product-charter` es la costura del sistema: el momento en que un problema definido se vuelve
plan con doliente, autoridad y criterio de éxito.

| | Antes del acta | Después |
|---|---|---|
| **El objeto** | El registro de requerimiento | La ficha del proyecto |
| **Quién escribe** | Alba | El agente del proyecto, salvo el estado declarado |
| **Qué hace Alba** | Todo | **Solo leer**, para saber si su producto se está construyendo |

**Una ficha, un escritor.** Alba la crea con el acta firmada y a partir de ahí no vuelve a
escribirla: si dos agentes la escribieran, el desacuerdo entre ellos dejaría de ser una señal
y sería una carrera.

## Los siete comandos

| Comando | Qué hace |
|---|---|
| `/product-setup` | **Lo primero que se corre.** Mira tu carpeta, hace cuatro preguntas y contrasta la definición que ya tengas |
| `/product-discovery` | Entrevistas y tickets en temas con la cita de quién lo dijo, y el tema que lleva meses dicho sin que nadie lo convierta en nada |
| `/product-requirements` | El registro con sus vacíos: sin doliente, sin criterio, aceptado sin que nadie lo pidiera, y lo que nadie decide |
| `/product-definition` | La definición contra la evidencia de demanda, y dónde el negocio y los datos no coinciden |
| `/product-trace` | Requerimiento → decisión → proyecto → entregable, y las dos brechas de arriba |
| `/product-spec` | El borrador de especificación con criterios verificables y los vacíos señalados, no rellenados |
| `/product-charter` | El acta de constitución: donde nace la ficha y el escritor cambia de manos |

## Los doce skills

Se cargan solos cuando el tema aparece. Ocho son propios de producto; cuatro son copias
literales de `criterio-pmo`, porque son método y no rol.

| Skill | Qué encapsula |
|---|---|
| `requirement-record` | **El contrato de datos de Alba.** Esquema, extracción, citación, los cinco estados y qué exige cada uno |
| `product-health` | Las diez señales, los cuatro umbrales, en qué orden se leen y **cuál no es hallazgo** |
| `demand-evidence` | Qué cuenta como evidencia de que alguien pidió algo, qué no cuenta aunque lo parezca, y cómo envejece |
| `discovery-synthesis` | Entrevistas y tickets en temas con la cita. Un tema es un conjunto de citas, no una afirmación |
| `assumption-tracking` | El supuesto escrito de forma que puede resultar falso, y el día en que se vuelve riesgo registrado |
| `product-metrics` | La serie con su fuente y su definición, y el contraste entre lo declarado y lo medido |
| `specification-draft` | El criterio de aceptación verificable, y la regla de señalar el vacío en vez de rellenarlo |
| `regulatory-sweep` | Las obligaciones que toca la definición, citadas. **No opina sobre cumplimiento** |
| `project-record` | La ficha del proyecto: nace con el acta, y Alba es quien la crea |
| `governance-artifacts` | Qué contiene un acta de constitución y quién decide qué |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué |
| `raid-taxonomy` | A dónde se muda un supuesto el día que nadie lo verifica |

## Cómo se verifica

```
python3 tests/criterio-product/grade.py    sobre dos productos, con control negativo
python3 scripts/producto.py selftest      44 comprobaciones sobre la aritmética
```

Con la librería estándar, sin instalar nada. Sobre un corpus sintético con respuestas escritas
a mano leyendo los documentos — **incluido un control negativo**: un producto con definición,
entrevistas y registro que no produce ni un hallazgo. Un agente que encuentra algo ahí es un
generador de ruido.

Qué prueba esa corrida y, con el mismo detalle, **qué no**, en
[`tests/criterio-product/EVIDENCIA.md`](../../tests/criterio-product/EVIDENCIA.md).

El diseño completo, con las tres clases de función y lo que sigue siendo de la persona, en
[`docs/agents/product-manager.md`](../../docs/agents/product-manager.md).
