<picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/img/marca/es/criterio-pmo-oscuro.svg"><img src="../../docs/img/marca/es/criterio-pmo-claro.svg" alt="Criterio PMO · Gobierno de proyectos" height="48"></picture>

# criterio-pmo · la familia de gobierno de proyectos

**Tres agentes y un servidor, alrededor de un solo contrato de datos.** Cada uno extiende
a una persona distinta de la cadena —quien define el producto, quien ejecuta el proyecto,
quien vigila el portafolio— y ninguno habla con otro directamente: se hablan por la ficha.

[English](README.md) · [← Criterio](../../README.es.md) · Apache 2.0

![Vera, Samuel, Alba y Rostrum](../../docs/img/es/robots.gif)

[Video de la familia (MP4, 4:5)](../../docs/video/criterio-pmo-familia-es.mp4)

| | |
|---|---|
| **Alcance** | El gobierno de un portafolio, de cada proyecto que lo compone y de cada producto que esos proyectos construyen |
| **Objetivo** | Que lo declarado y lo evidenciado se puedan comparar, todos los días y sobre el conjunto — que es lo que hoy no se puede |
| **Compuesta por** | [Vera](../../plugins/criterio-portfolio/README.es.md) · [Samuel](../../plugins/criterio-project/README.es.md) · [Alba](../../plugins/criterio-product/README.es.md) · [Rostrum](../../plugins/criterio-server/README.es.md) |
| **El soporte** | El marco de trabajo que define cada rol y lo que cuesta hoy a una organización, con su fuente, su año y su muestra: [`FUENTES.es.md`](FUENTES.es.md) |
| **Estado** | Los tres agentes construidos y verificados sobre corpus sintético. **La extracción sobre documentación real no se ha probado** |
| **Enfoque** | Estrategia y ejecución |
| **Compromiso** | Generar, difundir y conservar el conocimiento es una obligación profesional |
| **Qué no es** | No reemplaza a tu PMO ni decide por ella: procesa lo que tu equipo ya escribió y dice qué no se sostiene |
| **Licencia** | [Apache 2.0](../../LICENSE) |
| **Qué viene** | Más capacidades para mejorar los entornos laborales |

---

## Qué hace la familia

![La familia: tres agentes, un solo contrato de datos](../../docs/img/es/familia.png)

La capacidad tiene más de un agente porque la organización tiene más de un rol. Llevan nombre
de persona porque **son capacidades extendidas de personas**, y el significado de cada
nombre apunta a lo que hace: **Vera** —de *verus*, lo verdadero— dice lo que los documentos
dicen y no lo que se reporta; **Samuel** —«el que escuchó»— recuerda el viernes lo que se
dijo en la reunión; **Alba** trabaja antes de que amanezca el proyecto.

**Los tres se instalan hoy**, cada uno con su propio plugin, y comparten el mismo contrato
de datos. Los tres tienen también la misma deuda, y está escrita en su página: construidos y
verificados sobre corpus sintético, **no probados todavía sobre la documentación real de una
organización.**

**Samuel**, el agente del gerente de proyecto, no va a las reuniones — el gerente va. Lo que hace es que el gerente llegue
con la semana preparada: la agenda armada antes, la minuta redactada después, el plan al día
contra la evidencia y el informe listo salvo una línea. Su función central no la hace ninguna
herramienta que un gerente use hoy: **el compromiso dicho y no cumplido.** Las reuniones están
llenas de *«yo lo tengo para el viernes»* y nadie los registra.

**Alba** trabaja antes de que exista el proyecto, y entrega el acta con la
que el proyecto nace.

---

## Cómo operan los tres

![Cómo operan los tres agentes](../../docs/img/es/flujo.png)

El orden temporal es lo que los hace un sistema y no tres herramientas. **Dos ciclos cerrados, y ninguno pasa por una base de datos compartida.** El acta baja una
vez, y con ella nace la ficha. La ficha del gerente sube publicada como un documento más del
proyecto, y Vera la lee como lee todo lo demás. El informe sale al equipo, y del equipo vuelve
una petición. Y el lazo de arriba: Alba lee las fichas de los proyectos para confirmar que el
que dice estar construyendo su producto de verdad lo esté.

Lo que **no** hay en ese dibujo es tan importante como lo que hay:

- **Ninguna flecha entre dos agentes.** Todas pasan por un documento. Dos agentes que se
  hablan directo son dos agentes que hay que desplegar juntos.
- **Ninguna flecha de vuelta desde Rostrum a la ficha.** El servidor no escribe.
- **Ninguna flecha que escriba el estado declarado.** Esa la escribe una persona, en los tres
  sitios donde aparece.

**Y las personas están en el mismo dibujo, abajo.** El insumo de cada agente lo produce el trabajo no delegable de su persona.** Quitar a la
persona no deja al agente solo: lo deja sin comida.

## Los tres agentes y el único contrato

Nada se habla con nada directamente. **La ficha de proyecto es el único contrato.**

![El único contrato: quién escribe la ficha y quién solo la publica](../../docs/img/es/contrato.png)

El Product Manager trabaja antes de que exista plan: no escribe en la ficha, **la crea**. Su
entrega cierra con el acta de constitución, que es el certificado de nacimiento de la ficha.

### Las siete invariantes

1. **Los agentes no se hablan entre sí.** Se hablan por la ficha.
2. **Rostrum, el servidor, no escribe.**
3. **La fuente puede cambiar; la ficha no.** Un adaptador nuevo llena los mismos campos.
4. **Declarado y evidenciado nunca se fusionan**, venga de archivo o de base de datos.
5. **El modelo extrae, el código calcula.**
6. **Ningún agente escribe la declaración.** El estado declarado lo escribe una persona.
7. **Una ficha, un escritor.** Dos agentes que leen los mismos documentos escriben dos
   fichas, y no se fusionan nunca. La diferencia entre las dos es el hallazgo.

La sexta es la más fácil de romper por conveniencia y la que se lleva el sistema entero si se
rompe: si el agente declara, la comparación entre declaración y evidencia compara al sistema
consigo mismo, y todo esto se vuelve un generador de informes bonitos. No es una recomendación
de la documentación: es una restricción del camino de escritura, y falla si se intenta.

La séptima es la cuarta un nivel más arriba, y aparece en cuanto hay más de un agente sobre
el mismo proyecto. La forma cómoda de resolverlo —una ficha y un dueño— obliga a elegir mal
en las dos direcciones: si manda el gerente, la PMO no puede leer por su cuenta cuando duda;
si manda la PMO, entra en el camino crítico de setenta proyectos. Dos fichas quitan el
problema en vez de arbitrarlo, y **lo que era un conflicto de escritura se vuelve la señal.**
Ver [Samuel · las dos fichas](../../plugins/criterio-project/DISENO.es.md#las-dos-fichas).

## Lo que sigue siendo de las personas

Los tres roles siguen existiendo completos. Esto extiende capacidad; no sustituye función. Y el
argumento no es de cortesía, es estructural:

> **El insumo de cada agente lo produce el trabajo no delegable de su persona.**

El agente PM necesita que alguien dirija la reunión, porque de ahí sale la minuta que lo
alimenta. El agente PMO necesita que alguien persiga lo que el informe pide, porque si nadie
actúa el informe siguiente dice lo mismo. El agente de producto necesita que alguien hable con
el cliente, porque no hay síntesis sin entrevista.

Quitar a la persona no deja al agente solo: lo deja sin comida. Cada hoja documenta qué se
rompe primero si se intenta, y en qué orden.

## La estructura de carpetas recomendada

<!-- carpetas: generado por scripts/carpetas.py desde carpetas.json; no se edita a mano -->

Recomendada, no obligatoria: los agentes procesan la carpeta como esté, y las pruebas lo comprueban con cuatro disposiciones distintas. Con esta estructura cada documento llega a su lugar sin que el agente tenga que deducirlo.

Una carpeta por proyecto y una por producto, cada una empezando por su código: `PRY-101-originacion-digital`, `PRD-301-pagos-qr`.

**Cada proyecto**

| Carpeta | Qué va |
|---|---|
| `00-gobierno/` | Acta de constitución, contratos con proveedores y la ficha que publica el gerente del proyecto |
| `10-plan/` | Cronogramas y líneas base, cada versión con su fecha en el nombre |
| `20-seguimiento/` | Informes de avance, actas de recibo de entregables, facturas de proveedores, solicitudes de cambio y su aprobación |
| `30-reuniones/` | Minutas, actas de comité y notas de reunión, con la fecha en el nombre |

**Cada producto**

| Carpeta | Qué va |
|---|---|
| `00-definicion/` | Definición del producto y caso de negocio |
| `10-descubrimiento/` | Entrevistas, visitas, tickets y notas de clientes |
| `20-metricas/` | Tableros y series de las métricas del producto |
| `30-decisiones/` | Actas de los comités de producto |

<!-- /carpetas -->

## Instalación de la familia

Cada agente es un plugin y se instala solo. **No hace falta instalar los tres**: se instala el
que resuelve el rol que tienes.

```
/plugin marketplace add josenanez/criterio

/plugin install criterio-portfolio@criterio      si gestionas el portafolio
/plugin install criterio-project@criterio       si gestionas un proyecto
/plugin install criterio-product@criterio  si defines un producto
```

**En Claude Cowork** — Personalizar → Explorar plugins → Personal → **+** → Agregar
marketplace desde GitHub → `josenanez/criterio`.

Después de instalar, cada agente tiene su propio comando de instalación que mira tus carpetas,
hace unas pocas preguntas y produce un primer resultado sobre tus propios documentos. **Nadie
edita un archivo de configuración a mano.**

Y si instalas más de uno, se encuentran solos: **no hay nada que conectar.** Se hablan por la
ficha, que es un documento en la carpeta del proyecto.

## De qué responde cada agente, y dónde está su detalle

Las cuatro piezas, con lo mismo para cada una: de qué responde, qué no hace, y dónde está todo
su detalle. **Cada página de agente se lee sola** — alguien puede instalar uno sin los otros.

| | De qué responde | Lo que nunca hace | Su página | Sus pruebas |
|---|---|---|---|---|
| **Vera** · el portafolio | El portafolio completo: consolidar, contrastar lo declarado contra la evidencia, y armar el material del comité | No declara el estado de ningún proyecto, y no prioriza la demanda | [criterio-portfolio](../../plugins/criterio-portfolio/README.es.md) · 16 comandos, 10 skills | [resultados](../../tests/criterio-portfolio/RESULTADOS.md) |
| **Samuel** · un proyecto | Lo que la reunión deja escrito: el compromiso dicho y no cumplido, el plan contra la evidencia, y el informe listo salvo una línea | No declara el estado de su proyecto, y no va a la reunión | [criterio-project](../../plugins/criterio-project/README.es.md) · 9 comandos, 8 skills | [resultados](../../tests/criterio-project/RESULTADOS.md) |
| **Alba** · un producto | Lo que hay antes del proyecto: la definición contra la evidencia de demanda, el registro de requerimientos, y el acta con la que nace la ficha | No decide qué se construye, y no habla con el cliente | [criterio-product](../../plugins/criterio-product/README.es.md) · 11 comandos, 12 skills | [resultados](../../tests/criterio-product/RESULTADOS.md) |
| **Rostrum** · el servidor | Publicar el informe donde el equipo lo lea, y recibir la petición de quien no abre una carpeta | **No escribe nunca la ficha**, y no decide nada | [criterio-server](../../plugins/criterio-server/README.es.md) · 2 comandos, uno para todas las familias | [resultados](../../tests/criterio-server/RESULTADOS.md) |

Los 36 comandos de la familia y los 2 de Rostrum, uno por uno —qué hacen, qué reciben, qué leen y qué escriben— están en el [manual de los comandos](../../docs/manual.es.md), y las respuestas a lo que más se pregunta, en las [preguntas frecuentes](PREGUNTAS.es.md).

**La frontera es la misma para los tres y no es una recomendación: es una restricción del
camino de escritura.** Ninguno escribe el estado declarado de un proyecto. Esa línea la escribe
una persona, y sin ella la comparación entre lo declarado y lo evidenciado —que es de lo que
vive todo esto— compararía al sistema consigo mismo.

## En Rostrum, el portal de todas las familias

Hasta aquí el resultado de la familia son archivos en el equipo de quien corrió los agentes. **Un
patrocinador no abre una carpeta de archivos**: abre un enlace, o no abre nada. Para eso está
**Rostrum**, un plugin aparte, `criterio-server`, que sirve a la PMO junto con las demás familias.

**Cómo entra la PMO al portal.** Cada agente deja su configuración al correr su setup:
`/criterio-portfolio:portfolio-setup` en `.criterio/portafolio/`, `/criterio-project:pm-setup` en
`.criterio/proyecto/<PRY>/` y `/criterio-product:product-setup` en `.criterio/producto/<PRD>/`, con
la carpeta raíz de sus documentos marcada (`_CRITERIO_PORTAFOLIO.txt`, `_CRITERIO_PROYECTO.txt`,
`_CRITERIO_PRODUCTO.txt`). Después, `/criterio-server:server-setup` encuentra esas configuraciones,
las muestra para que digas que sí y guarda el mapa; `/criterio-server:server-start` levanta el
portal. Un proyecto nuevo entra volviendo a correr `server-setup`.

**Lo que la PMO tiene en Rostrum:**

| Dónde | Qué |
|---|---|
| Inicio | La tarjeta **Criterio PMO**: cuántos proyectos y productos tienen informe, y las señales del último barrido de Vera con su fecha |
| Menú › PMO | Las cuatro vistas del informe de Vera —cómo va el portafolio, lo que necesita una decisión, proyectos y productos—, la página de cada agente y **Dónde trabaja** |
| Lo que vence | El próximo comité, junto a los vencimientos de las otras familias |
| `/caso/<PRY>` | Todo lo que los agentes hicieron sobre un proyecto, también lo que encontró Tomás en su presupuesto |
| Dónde trabaja | La ruta completa de la carpeta raíz, de los documentos con su marca, del estado y de la configuración de Vera, Samuel y Alba |
| Preguntar a un agente | La pregunta queda en `peticiones/` de quien elijas y se atiende en su siguiente corrida |

Ahí está lo que ninguna otra página puede decir: cuando un producto lo construyen proyectos que
reportan a comités distintos, cada comité ve su proyecto y **ninguno ve el producto**. Y *«esto no
coincide con lo que yo sé»* es la petición de más valor del sistema: es una persona diciendo qué
documento falta.

**No autentica a nadie, y es a propósito**: se publica detrás del control de acceso que la
organización ya tiene. No escribe nunca la ficha.

→ **[Rostrum: instalación, configuración y uso con todas las familias](https://www.josenanez.com/es/agents/rostrum)** ·
[su README, con las rutas y qué pedirle a tu organización](../../plugins/criterio-server/README.es.md)

## Cómo se configura y cada cuánto corre cada uno

Esta es la tabla que responde tres preguntas a la vez: **dónde se ve cada agente, qué le
hace falta configurado, y cada cuánto tiene sentido que corra.**

| | Vera | Samuel | Alba |
|---|---|---|---|
| **Se instala** | `criterio-portfolio` | `criterio-project` | `criterio-product` |
| **Instancias** | Una por PMO | **Una por proyecto** | **Una por producto** |
| **Se configura con** | `/criterio-portfolio:portfolio-setup` | `/criterio-project:pm-setup` | `/criterio-product:product-setup` |
| **Cuánto tarda eso** | Quince minutos | Diez | Diez |
| **Qué le tienes que decir** | Dónde está la documentación, cuándo es el comité, quién eres | Dónde está tu proyecto, cuándo es tu reunión, quién eres | Dónde está la definición, quién decide qué se construye, quién eres |
| **Dónde queda** | Un archivo de la persona, escrito por el comando | Igual | Igual |
| **El que se le pone a un reloj** | `/criterio-portfolio:portfolio-wake` | `/criterio-project:pm-wake` | `/criterio-product:product-wake` |
| **Cadencia que tiene sentido** | Diaria si el barrido está activo; y el informe con su anticipación al comité | Diaria con barrido, o el día antes y el día después de la reunión | **Semanal alcanza** |
| **Qué lo despierta además del reloj** | Una petición que alguien dejó en Rostrum | Una minuta nueva en la carpeta | Que algo cruzara un umbral solo |

**Nadie edita un archivo de configuración a mano.** Es una regla de los tres comandos de
instalación, no una cortesía: si para cambiar un umbral hay que abrir un JSON, el umbral se
queda como vino y la configuración deja de describir a la organización. Se dice en la
conversación y el comando lo reescribe.

Cada plugin trae su `scripts/config.example.json` para ver la forma completa sin instalar
nada.

### Por qué las tres cadencias son distintas

No es una preferencia: **cada agente mide contra otra cosa.**

- **Vera** mide contra la carpeta. Un documento nuevo puede cambiar el estado de un
  proyecto hoy, así que el barrido diario tiene sentido y el informe se entrega con
  anticipación al comité — para que el gerente de la PMO alcance a reaccionar a lo que
  encuentre, no para que se entere cuando ya está enviado.
- **Samuel** mide contra la reunión. Su ciclo no es el calendario: es *antes de la reunión*
  y *después de la reunión*, y por eso `/criterio-project:pm-wake` mira de qué lado estás antes de ofrecer
  nada.
- **Alba** mide contra el paso del tiempo, y eso cambia todo. Sus umbrales se cuentan en
  meses, así que una corrida diaria sobre un registro que se mueve poco es ruido con
  puntualidad. **Pero es la única de los tres cuyos hallazgos aparecen sin que nadie haga
  nada**: el requerimiento que llevaba cincuenta y nueve días sin decidirse llega a
  sesenta, y nadie va a abrir una sesión para preguntar si eso ya pasó.

### Los tres se callan cuando no hay nada

Es la regla que decide si un agente sigue instalado el mes siguiente. Los tres comandos de
reloj devuelven `quiet` cuando no toca nada, y con `quiet` la salida es una línea: qué se
revisó y cuándo vuelve.

Un agente que produce un informe para decir que no hay novedad enseña a ignorarlo, y el día
que sí hay novedad ya nadie lo abre.

### Qué es lo que **no** está programado

Conviene decirlo aquí y no en una nota al pie: **ninguno de los tres se programa solo.**
Los tres traen el comando que un reloj invoca, y el reloj vive fuera del plugin — una tarea
programada de Claude Cowork, o el programador del sistema operativo invocando Claude en
modo no interactivo. Alguien tiene que ponerlo, una vez, y cada comando de reloj explica
cómo.

Y para que corra sin nadie delante hacen falta dos cosas que no dependen de este
repositorio: **que la sesión pueda correr sin aprobar cada paso**, y **que la carpeta esté
montada cuando el reloj dispare.**

**Si la organización no quiere corridas desatendidas** —y en un banco es una respuesta
razonable— los tres comandos sirven corridos a mano, y la cadencia sigue diciendo qué toca.
Lo que se pierde es que avisen sin que nadie pregunte, que es justamente lo que más cuesta
ver a mano.

## Las pruebas de la familia

**Una sola puerta corre todo lo que este repositorio verifica**, de los tres agentes a la vez:

```
python3 scripts/verificar.py
```

Es el equivalente de una prueba integral: no verifica un agente, verifica **que la familia
siga siendo una familia.** Lo propio de cada agente —su aritmética, su corpus, sus respuestas
escritas a mano— lo responde su página; aquí se verifica lo que ninguno puede responder solo:

| Qué se verifica del conjunto | Por qué es de la familia y no de un agente |
|---|---|
| Que la documentación y el código digan lo mismo | Una señal que un agente calcula y su skill no explica rompe la promesa de todos |
| Que el marketplace y cada plugin estén completos | Un plugin que se instala sin su README es un agente que llega mudo |
| **Que las copias compartidas no se hayan separado** | Los tres comparten aritmética por copia, no por importación. Dos copias que se separan calculan distinto sobre los mismos documentos, y nadie sabría a cuál creerle |
| Que cada agente tenga su análisis de pruebas y esté enlazado | Un resultado que nadie puede abrir es un resultado que no existe |

**El resultado del conjunto, generado desde la corrida**, en
[`docs/pruebas.md`](../../docs/pruebas.md) — y con gráficas, para abrir en un navegador, en
[`pruebas.html`](../../docs/pruebas.html).

**Y el de cada agente, en su propia página**, porque cada uno responde por lo suyo:
[Vera](../../tests/criterio-portfolio/RESULTADOS.md) ·
[Samuel](../../tests/criterio-project/RESULTADOS.md) ·
[Alba](../../tests/criterio-product/RESULTADOS.md).

Todo corre con la librería estándar y sin instalar nada. Qué prueba cada corpus y, con el mismo
detalle, **qué no**, en las tres páginas de evidencia bajo [`tests/`](../../tests/).

**El análisis estadístico de las rondas con los agentes** —precisión, cobertura y margen del 95 %
de cada uno, su evolución ronda a ronda, por industria, por tipo de alerta y los defectos con su
origen— en [`analisis/ANALISIS.es.md`](analisis/ANALISIS.es.md). Lo genera
[`scripts/analisis.py`](../../scripts/analisis.py) desde [`tests/evidencias/`](../../tests/evidencias/)
con cada ronda, y `verificar.py` comprueba que diga lo que dice la evidencia.

## Las industrias de prueba

<!-- industrias: generado por scripts/industrias.py desde industrias.json; no se edita a mano -->

Probada en 6 industrias de Suramérica, con 13 proyectos por industria en la última ronda. Las siguientes entran de dos en dos, cada una con su versión y su ronda completa.

| Industria | Estado | Qué trae a las pruebas |
|---|---|---|
| Entidades financieras · bancos | Probada · rondas 1–11 | Core de depósitos, originación digital, nube y Open Banking; comités de transformación, arquitectura y riesgos |
| Entidades financieras · cooperativas | Probada · rondas 1–11 | Consejo de Administración y comité de crédito; core cooperativo, libranza y aportes; asociados urbanos y rurales |
| Retail | Probada · rondas 1–11 | Tienda en línea, fidelización y centros de distribución; integración con el ERP y congelamiento de cambios en temporada alta |
| Minería (oro y cobre) | Probada · rondas 1–11 | Ingeniería, licencias y permisos, montaje; paradas de planta; proveedores de ingeniería y montaje |
| Construcción e infraestructura | Probada · rondas 11 | Cronogramas de MS Project, órdenes de cambio, contratistas, avance físico contra financiero |
| Oil & gas | Probada · rondas 11 | Megaproyectos de capital, contratistas, permisos y seguridad industrial |
| Telecomunicaciones | Incremento 5 · versión 0.12.0 | Muchos despliegues en paralelo, proveedores y permisos: la escala del portafolio |
| Logística | Incremento 5 · versión 0.12.0 | Implantaciones en varios centros con una operación que no se detiene |

<!-- /industrias -->

## Hoja de ruta

<!-- hoja de ruta: generado por scripts/hoja.py desde hoja-de-ruta.json; no se edita a mano -->

La familia crece por incrementos. Cada uno es una versión con su prueba completa y su análisis estadístico publicados, con las mismas métricas, para que la evolución se pueda comparar.

| Versión | Estado | Qué entra | Prueba |
|---|---|---|---|
| 0.6.0 | Liberada | **Material más amplio**<br>· Las correcciones D058 a D060<br>· 20 proyectos por industria en el material de prueba<br>· Las industrias desde una sola fuente | La verifica la prueba de la 0.7.0 |
| 0.7.0 | Liberada | **Cronogramas de Microsoft Project**<br>· El XML de Project como cronograma: tareas, hitos, línea base, avance, predecesoras y recursos; el .mpp donde haya Java y MPXJ<br>· La estructura de carpetas recomendada<br>· El contraste entre la ficha del gerente y la de la PMO como lo define el skill<br>· El análisis estadístico, regenerado con cada prueba<br>· Esta hoja de ruta, desde una sola fuente | 4 industrias, 80 proyectos |
| 0.8.0 | Liberada | **Rostrum para todas las familias, y la CFO y la CLO**<br>· Rostrum, un plugin propio para todas las familias, con un menú por familia y un inicio que dice qué pide atención hoy, WCAG 2.2 AA comprobado con axe-core<br>· La carpeta raíz que cada agente busca y, con permiso, marca<br>· Las familias CFO y CLO, con el motor probado y una primera ronda con el agente | La verifica la prueba de la 0.9.0 |
| 0.9.0 | Liberada | **Construcción e infraestructura, y oil & gas**<br>· Dos industrias nuevas, con sus propios proyectos, documentos y situaciones | 6 industrias |
| 0.12.0 | Siguiente | **Telecomunicaciones y logística**<br>· Dos industrias nuevas: la escala del portafolio y la operación que no se detiene | 8 industrias |
| 0.13.0 | Siguiente | **Rostrum**<br>· Gantt de línea base contra vigente, hitos y curva de avance | 8 industrias |
| 1.0.0 | Reservada | **El despliegue en una organización**<br>· El esquema de la ficha, sostenido en el primer despliegue en una organización | La documentación de esa organización |

<!-- /hoja de ruta -->

## Los dieciocho skills de la familia

Dieciocho skills distintos entre los tres agentes. **Los que comparten son copias literales, no un módulo importado**: un plugin instalado tiene que correr solo, y un `import` a la ruta del otro funciona aquí y falla en el equipo de quien lo instaló.

`scripts/sincronizar.py` las copia y `tests/coherencia.py` falla si se separan.

| Skill | Vera | Samuel | Alba |
|---|:--:|:--:|:--:|
| `assumption-tracking` | · | · | ● |
| `baseline-variance` | ● | ● | · |
| `commitment-tracking` | ● | ● | · |
| `demand-evidence` | · | · | ● |
| `discovery-synthesis` | · | · | ● |
| `document-intake` | ● | ● | ● |
| `governance-artifacts` | ● | ● | ● |
| `portfolio-health` | ● | · | · |
| `portfolio-history` | ● | · | · |
| `product-health` | · | · | ● |
| `product-metrics` | · | · | ● |
| `project-diagnosis` | ● | ● | · |
| `project-record` | ● | ● | ● |
| `raid-taxonomy` | ● | ● | ● |
| `regulatory-sweep` | · | · | ● |
| `requirement-record` | · | · | ● |
| `specification-draft` | · | · | ● |
| `vendor-control` | ● | ● | · |

## Estado

**Los tres están construidos y se pueden instalar hoy**, y los tres tienen la misma deuda,
que conviene no esconder: **verificados sobre corpus sintético, no probados sobre la
documentación real de una organización.**

| Agente | Se instala | Tablas A y B de su diseño |
|---|---|---|
| **Vera** · PMO | `criterio-portfolio` · 16 comandos, 10 skills | **sin filas abiertas** |
| **Samuel** · proyecto | `criterio-project` · 9 comandos, 8 skills | **sin filas abiertas** |
| **Alba** · producto | `criterio-product` · 11 comandos, 12 skills | **sin filas abiertas** |
| **Rostrum** · el servidor | `criterio-server` · 2 comandos, para todas las familias | — |

**Ninguna de las tres hojas de diseño tiene ya una fila en «Falta» o en «Parcial».** Lo que
sigue pendiente no es construcción.

La cadena documento → modelo → ficha se prueba en rondas con el agente: los tres agentes corren
sus 38 comandos, en el orden de una PMO, sobre la documentación de una organización por
industria, y lo que escriben se califica contra una clave que no ven. La ronda 11 corrió sobre
seis industrias y 78 proyectos: Vera 381 de 381 alertas sin una de más, Samuel y Alba al 100 %.
Su detalle, en el [análisis estadístico](analisis/ANALISIS.es.md). Lo que no prueba es la
documentación de una organización real.

La corrida que sostiene estos estados, con lo que prueba y lo que no, está en las tres
páginas de evidencia bajo [`tests/`](../../tests/) y el conjunto en
[`docs/pruebas.md`](../../docs/pruebas.md) — con gráficas, para el navegador, en
[`pruebas.html`](../../docs/pruebas.html). La quinta decisión de la tabla siguiente salió de
ahí y no de una conversación.

