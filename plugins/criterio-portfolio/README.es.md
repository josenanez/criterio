# Vera · directora de proyectos

**Un segundo cerebro para quien responde por el portafolio completo.** Lee la documentación que tu PMO ya
tiene y dice qué cambió, qué se contradice y qué lleva semanas en silencio.

[English](README.md) · Apache 2.0 · Una instancia por oficina de proyectos · Se instala en cuatro clics

**Estado: los diecisiete comandos construidos**, los diez skills del método y la aritmética
verificada sobre un corpus con respuestas escritas a mano. **Lo que todavía no se ha probado:
la extracción sobre la documentación real de una organización.** Nada se anuncia como
terminado hasta que pasen los [criterios de aceptación](DISENO.es.md#criterios-de-aceptación).

**Esta página se lee sola.** Vera funciona sin sus hermanos: si solo te interesa el
portafolio, aquí está todo, incluidas sus pruebas. La familia —cómo se encuentra con Samuel y
con Alba— está en el [familia criterio-pmo](../../families/criterio-pmo/README.es.md), y **el servidor que publica su
informe**, en [SERVER.es.md](SERVER.es.md).

---

## Qué es

| | |
|---|---|
| **A quién extiende** | Al gerente de la PMO y a sus analistas |
| **Sobre qué trabaja** | **El portafolio completo.** Cuarenta proyectos, o setenta |
| **Qué mira** | La carpeta de documentación de todos ellos, como esté |
| **Cadencia** | Barrido diario si se configura, e informe con anticipación al comité |
| **Instancias** | Una por PMO |

## Qué hace

**Lo que hace y nadie más hace:** contrastar lo que cada gerente declara contra lo que
sustentan sus documentos, **en el conjunto y a la vez**. Un proyecto que reporta verde y
lleva cinco semanas sin un documento no lo detecta nadie mirando ese proyecto: lo detecta
quien mira los cuarenta con la misma vara.

**Lo que puede responder que hoy nadie responde sin días de trabajo:** qué cambió desde la
corrida anterior, qué se contradice entre dos documentos del mismo proyecto, qué lleva
semanas en silencio, cuántos de los que reportan verde tienen evidencia que ese verde no
explica, y a quién alcanza mover un proyecto.

### Los diecisiete comandos

> Se escriben con el prefijo del plugin: `/criterio-portfolio:` y autocompletar hace el resto. Es la única forma que resuelve en una sesión de Claude Code.

| Comando | Qué hace |
|---|---|
| `/criterio-portfolio:portfolio-setup` | **Lo primero que se corre.** Mira tus carpetas, hace cinco preguntas y produce el primer informe sobre tus propios documentos |
| `/criterio-portfolio:portfolio-wake` | **Lo que el reloj invoca.** Mira qué toca hoy, lo hace, y si no toca nada se calla |
| `/criterio-portfolio:portfolio-server` | Levanta **Rostrum**, el servidor: expone el informe para quien no abre una carpeta, y dice qué pedirle a la organización |
| `/criterio-portfolio:document-index` | Qué documentos cambiaron de verdad, qué hay que releer y qué citas dejaron de resolver |
| `/criterio-portfolio:portfolio-scan` | Lee la carpeta y produce o actualiza una ficha por proyecto. Puerta de entrada |
| `/criterio-portfolio:portfolio-report` | Informe consolidado: qué cambió, qué se contradice, qué está en silencio, qué no tiene sustento |
| `/criterio-portfolio:status-report` | Estado de un proyecto, y las señales que su semáforo declarado no explica |
| `/criterio-portfolio:health-check` | Diagnostica un proyecto desde cero contra la evidencia, sin asumir nada de su informe |
| `/criterio-portfolio:project-history` | Qué pasó en un proyecto, con la línea de tiempo y desde cuándo lo declarado no se sostiene |
| `/criterio-portfolio:steering-pack` | Material de comité como paquete de decisiones, no como informe de avance |
| `/criterio-portfolio:raid-log` | Riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron y nadie registró |
| `/criterio-portfolio:change-control` | Evalúa un cambio en alcance, tiempo y costo, calcula a quién alcanza, y crea línea base nueva sin borrar la anterior |
| `/criterio-portfolio:budget-tracking` | Aprobado, comprometido, ejecutado y proyección, con desviación contra las dos líneas base |
| `/criterio-portfolio:vendor-tracking` | Entregables contractuales contra evidencia de recibo y contra facturación |
| `/criterio-portfolio:product-view` | El estado de un producto a través de todos los proyectos que lo construyen |
| `/criterio-portfolio:project-charter` | Revisa o redacta el acta, señalando qué falta y qué consecuencia tiene |
| `/criterio-portfolio:project-closure` | Cierra contra el criterio de éxito pactado, con lecciones que se puedan sustentar |

### Los diez skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten, y se
pueden leer como se lee un manual.

| Skill | Qué encapsula | De quién es |
|---|---|---|
| `project-record` | La ficha: esquema, reglas de extracción, citación, estados de campo, qué hacer cuando dos documentos se contradicen | Propia · también en Samuel y Alba |
| `document-intake` | Qué documento hay que releer y cuál no, qué formatos se pueden leer y con qué, el renombrado, el borrado, y la cita que dejó de resolver | Propia · también en Samuel y Alba |
| `portfolio-health` | Las veintiuna señales con lo que significa cada una, los umbrales que las gobiernan, y las tres defensas contra el dato que dejó de ser cierto | Propia |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y contra la vigente, la replanificación contra lo que autorizó el comité, las cuatro cifras del presupuesto | Propia · también en Samuel |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, valoración, criterio de escalamiento | Propia · también en Samuel y Alba |
| `commitment-tracking` | Compromisos dichos en reuniones: extracción, estados, qué cuenta como evidencia, y el que se repite con fecha nueva cada vez | Propia · también en Samuel |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno y quién decide qué | Propia · también en Samuel y Alba |
| `vendor-control` | Contrato contra evidencia de recibo contra facturación, con monto por entregable | Propia · también en Samuel |
| `project-diagnosis` | El diagnóstico desde cero: en qué orden se lee y cuándo la respuesta es que no se puede diagnosticar | Propia · también en Samuel |
| `portfolio-history` | La historia de un proyecto desde sus documentos, y el punto donde la evidencia se separó de lo reportado | Propia |

## Para qué sirve

Mover un proyecto tiene consecuencias en proyectos que no son suyos, y esa cuenta no la hace
nadie porque exige mirar el grafo completo de dependencias del portafolio a la vez.

> **PRY-002 se mueve 60 días.**
> Alcanza a **PRY-001**, que depende de su entrega y **ya no alcanza a sostener su fecha de
> cierre: le faltan 121 días.**
> Nadie mirando PRY-002 lo habría visto, y el gerente de PRY-001 todavía no sabe que tiene
> que enterarse.

Ese caso sale del corpus sintético, con la respuesta escrita a mano **antes** de correr el
cálculo. Es la clase de pregunta que solo se puede responder desde arriba: `/criterio-portfolio:change-control`
la calcula, y dice además a quién hay que avisarle y qué dependencias están sin confirmar.

Y es la misma razón por la que Vera existe. Lo que hace no es leer mejor un proyecto —para eso
está su gerente— sino **aplicarle la misma vara a los cuarenta**, todos los días, sin
cansarse en el proyecto número treinta.

### Y para qué no sirve

Esto es lo que conviene tener claro antes de instalarlo, y no está en letra pequeña:

- **No escribe en tus carpetas.** Lee tus documentos; los informes y las fichas van a una
  carpeta de estado que tú eliges.
- **No decide.** Produce borradores de trabajo. Formula la decisión como pregunta con sus
  opciones; quién decide y asumiendo qué es de quien tiene la facultad.
- **No declara el estado de un proyecto.** Eso lo hace el gerente. El agente le muestra
  contra qué, y la diferencia entre las dos cosas es el hallazgo de más valor del sistema.
- **No sabe lo que no está escrito.** No conoce lo que se habló en el pasillo ni lo que se
  decidió en una llamada que nadie minutó. Todo hallazgo suyo es *«según los documentos»*, y
  lo declara.
- **No adivina.** Cada dato viene con la cita del documento de donde salió. *«No está dicho
  en ninguna parte»* es una respuesta válida y esperada.

**Y hay dos cosas que deliberadamente no están, aunque las pida un pliego: capacidad y
asignación de recursos, y materialización de beneficios.** No por poco importantes: porque los
datos no están en la carpeta. Capacidad exige horas reales y beneficios exige medición
posterior que casi ninguna organización tiene. Un skill que promete lo que el insumo no
permite quema la credibilidad del plugin entero. Tampoco trae contenido regulatorio: la
gestión de portafolio es método, no normativa, y funciona igual en Bogotá que en Santiago. Si
una obligación regulatoria toca un proyecto, la registra como restricción o como riesgo y no
opina sobre ella.

Y una que sí hay que decir en voz alta: **tus documentos se procesan en la infraestructura de
la plataforma de IA**, no solo en tu equipo. Confirma que sea admisible bajo tus políticas
antes de apuntarlo a material confidencial. Descargo completo en
[DISCLAIMER.es.md](../../DISCLAIMER.es.md), términos en [TERMS.es.md](../../TERMS.es.md).

## Instalación y configuración

![Instalación: cuatro clics, o dos comandos](../../docs/img/es/instalacion.png)

**Claude Code**

```
/plugin marketplace add josenanez-company/criterio
/plugin install criterio-portfolio@criterio
/criterio-portfolio:portfolio-setup
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez-company/criterio`.

Si gestionas un proyecto y no el portafolio, lo tuyo es
[Samuel](../criterio-project/README.es.md). Si defines un producto,
[Alba](../criterio-product/README.es.md).

### El primer resultado

![Los primeros quince minutos](../../docs/img/es/quince-minutos.png)

No hay archivo de configuración que editar, ni plantilla que llenar, ni carpeta que ordenar
antes de empezar. La configuración **es una conversación**, y termina con un resultado sobre
tus documentos.

| | |
|---|---|
| **0 – 2 min** | **Instalar.** Dos comandos en Claude Code, o cuatro clics en Cowork |
| **2 – 4 min** | **Mira antes de preguntar.** Le señalas la carpeta donde vive la documentación de proyectos, como esté. Lista lo que encontró: cuántos proyectos distingue, cuántos documentos, qué formatos, cuál es el más reciente, y cuáles no va a poder leer. Ahí sabes que está mirando tus cosas de verdad |
| **4 – 8 min** | **Cinco preguntas.** Quién eres, cuándo se reúne tu comité, quién recibe el informe y en qué forma, y los términos. Una a la vez, cada una con una respuesta sugerida a partir de lo que ya vio. *«No sé»* es una respuesta válida |
| **8 – 15 min** | **Un primer resultado.** Barre **tres proyectos**, no el portafolio completo, para que veas algo real en minutos: qué supo de cada uno, qué no está dicho en ninguna parte, y cualquier contradicción o compromiso vencido que haya aparecido de paso |

Al final te dice cuánto tomaría el portafolio completo, y qué le falta a tu carpeta para que
el análisis sea mejor. Pero como hallazgo, no como requisito: **esto funciona con lo que
haya.**

**Lo que queda configurado** lo escribe `/criterio-portfolio:portfolio-setup` a partir de lo que respondiste, en tu
equipo y en un archivo tuyo: dónde están los documentos, dónde vive el estado, tu cadencia de
comité, la forma del informe, los umbrales que le hacen levantar la voz, y el registro de que
aceptaste los términos, con tu nombre y la fecha. Todo eso se cambia **hablando**: si quieres
que el silencio se reporte a los diez días y no a los quince, se lo dices.

### Cada cuánto corre

![La cadencia: se activa solo, y casi siempre se calla](../../docs/img/es/cadencia.png)

Esta es la diferencia entre un comando y un agente. Un comando espera. **Este se programa y
corre solo.**

De las cinco preguntas del arranque sale una cadencia, y de la cadencia sale qué toca cada
día. La decisión es aritmética de fechas, así que la toma el código y no el criterio del
momento:

```
python3 scripts/portafolio.py due --state <estado> --config <archivo>
```

Y `/criterio-portfolio:portfolio-wake` es el comando que el reloj invoca: mira qué toca, lo hace, y **si no toca nada
no produce nada.** Callarse cuando no pasó nada no es una omisión — es la única razón por la
que un agente que corre todos los días sigue instalado el mes siguiente.

Tres cosas pueden tocar. El **barrido**, que mira qué cambió en la carpeta y solo recalcula
los proyectos tocados. El **informe de comité**, que aterriza con la anticipación que
configuraste para que alcances a reaccionar a lo que encuentre. Y la **confirmación**, cinco
campos por corrida — los que envejecen peor: patrocinador, gerente, presupuesto aprobado,
fecha de cierre y alcance.

Ponerlo en un reloj es del lado de tu organización: una tarea programada en Cowork, o el
programador del sistema en Claude Code. **Y si no quieren corridas desatendidas** —en un
banco es una respuesta razonable— la cadencia sigue diciendo qué toca, corrida a mano. Lo
que se pierde es que avise sin que nadie pregunte.

**Y si quieres que tu patrocinador lo vea sin pedírtelo**, `/criterio-portfolio:portfolio-server` levanta **Rostrum**,
el servidor de esta familia: un portal con tres secciones —informes de la PMO, proyectos y
productos— donde quien mira puede además **dejarle una pregunta escrita al agente**, que
queda en la cola y se atiende en la siguiente corrida. No autentica a nadie, y es a
propósito: se publica detrás del control de acceso que tu organización ya tiene.
→ **[Rostrum, con capturas de cada sección](SERVER.es.md)**

## Trabajo en equipo

Vera funciona sola. Si están los otros dos, **no hay nada que conectar**: se encuentran
por la ficha del proyecto, que es un documento más en la carpeta.

| Con quién | Qué pasa |
|---|---|
| **Samuel** | Publica la ficha de su proyecto con `/criterio-project:pm-publish`, y Vera la lee como lee cualquier documento. **Las dos fichas no se fusionan nunca**, y cuando las dos citan y no coinciden, alguien vio un papel que el otro no vio — con la fecha de cada fuente, para saber cuál es más reciente |
| **Alba** | Redacta el acta de constitución con la que nace la ficha del proyecto. Vera la recibe ya escrita y la revisa contra la evidencia |
| **Rostrum** | Publica el informe de Vera donde el equipo lo lea, y le devuelve las preguntas que deja quien lo mira. **No escribe nunca la ficha** |

## Pruebas

### Cómo está construido

![Cómo funciona: el modelo extrae, el código calcula](../../docs/img/es/como-funciona.png)

La espina es la **ficha de proyecto**: un contrato de datos que todos los comandos leen y
escriben, con la cita al documento fuente y a su fecha en cada campo. Ningún comando lee
documentos crudos por su cuenta. Eso permite consolidar cuarenta proyectos sin volver a
leerlos, **calcular en vez de opinar**, y comparar una corrida contra la anterior.

Tres scripts, que son lo único que no opina. [`scripts/texto.py`](scripts/texto.py) convierte
el documento a texto: `.docx`, `.xlsx` y `.pptx` con la librería estándar —son ZIP con XML
adentro—, `.eml` con el parser de correo, y el PDF con `pdftotext`. Lo que no se puede leer
se declara con la razón. [`scripts/portafolio.py`](scripts/portafolio.py) hace la aritmética, y su
subcomando `index` decide el costo de cada corrida: dos hashes por documento, uno para saber
si vale extraer y otro para saber si vale releer. Sobre ese índice, `plan-lectura` arma lo
que el agente va a leer —por lotes, con tope y con cuántos lotes a la vez, según el bloque
`execution` de la configuración— y `sellar` deja en cada ficha los hashes de lo leído,
calculados y no tecleados. El agente ejecuta el plan; no lo redacta, porque la única vez
que lo redactó lanzó cinco lectores en paralelo sobre un corpus sin cambios y agotó la
cuota. `workers` vale 1 por defecto, que es lo seguro con una ventana de cuota; una
organización que paga por uso lo sube, y el arnés marca en rojo la corrida que lo exceda. Y
[`scripts/informe.py`](scripts/informe.py) arma el informe impreso a partir de lo que los
otros dos produjeron, sin volver a leer un solo documento.

### Cómo se verifica

```
python3 scripts/portafolio.py selftest          la aritmética y la cadencia
python3 scripts/texto.py --selftest      la conversión de documentos
python3 scripts/informe.py --selftest    el informe: cifras, concordancia y nombres
python3 scripts/servidor.py --selftest   el servidor: qué sirve y qué nunca toca
```

Con la librería estándar, sin instalar nada. Sobre un corpus sintético con respuestas escritas
a mano leyendo los documentos — **incluido un control negativo**: un proyecto que no produce
ni un hallazgo. Un agente que encuentra algo ahí es un generador de ruido.

**Cómo salió la última corrida, generado desde la corrida misma:**
[`tests/criterio-portfolio/RESULTADOS.md`](../../tests/criterio-portfolio/RESULTADOS.md). Qué prueba cada
pieza del material y, con el mismo detalle, **qué no**, en
[`EVIDENCIA.md`](../../tests/criterio-portfolio/EVIDENCIA.md).

El diseño completo, con los criterios de aceptación y lo que sigue siendo de las personas, en
[`DISENO.es.md`](DISENO.es.md), que viaja con el plugin.

Y las pruebas del conjunto de la familia —lo que ningún agente puede responder solo— en el
[README de la familia](../../families/criterio-pmo/README.es.md#las-pruebas-de-la-familia).

