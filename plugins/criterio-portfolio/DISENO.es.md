# Vera · el agente PMO

**Vera**, del latín *verus*: lo verdadero. Dice lo que los documentos dicen, no lo que se
reporta — y cuando las dos cosas no coinciden, esa diferencia es el hallazgo.

Extiende a la **oficina de proyectos**: la función que responde por el conjunto de los
proyectos, no por uno.

Esta hoja es la referencia completa de la capacidad: el flujo, las piezas que la componen y
qué hace cada una, las tres clases de función, y lo que falta. Marco general y definiciones:
[el README del plugin](README.es.md).

| | |
|---|---|
| **Instancia** | Una por organización |
| **Alcance** | Todos los proyectos. Barrido amplio, cadencia de comité |
| **Escribe** | Hallazgos. Estándar: umbrales, versión del esquema, convenciones |
| **No escribe** | La declaración de ningún gerente — sexta invariante |
| **Lee** | Todas las fichas, y la carpeta de documentación |
| **Estado** | Disponible. Clase A cerrada; de la B queda una fila |
| **Evidencia** | [`tests/criterio-portfolio/EVIDENCIA.md`](../../tests/criterio-portfolio/EVIDENCIA.md) |

---

## El flujo

```
DIRECTOR / ANALISTA DE PMO  (clase C)          AGENTE PMO  (clases A y B)
──────────────────────────────────────────────────────────────────────────────────
prioriza y admite la demanda
   └─► portafolio aprobado ──────────────────► define qué fichas existen
                                          ┌──  convierte los documentos a texto
                                          │    calcula qué cambió y qué hay que releer
                                          │    llena la ficha, con cita y fecha
                                          │    calcula alertas y desviaciones
                                          │    contrasta declaración contra evidencia
                                          │    cruza dependencias entre proyectos
   ◄── informe · preguntas · paquete ◄─────┘
       de decisión (borrador)

persigue lo que el informe pide
decide qué escala y qué se pelea
   └─► acuerdos y decisiones en acta ────────► entran como evidencia fechada

aprueba línea base, cambios
y excepciones
   └─► decisión fechada ─────────────────────► referencia de todo el cálculo

responde ante comité, auditoría
y regulador
   └─► requerimientos del auditor ───────────► entran como restricción o riesgo
```

El ciclo se cierra por la izquierda: **si nadie persigue lo que el informe pide, el informe
siguiente dice lo mismo**, y en un mes se ignora.

---

## La subestructura

Cuatro capas, y **cada una tiene un solo dueño documental.** Aquí no se repite lo que vive
en otro sitio: una tabla copiada es una tabla que se desactualiza en el documento que nadie
mira, y eso ya pasó una vez con la lista de señales.

| Capa | Qué es | Dueño |
|---|---|---|
| **Los valores** | Los ocho umbrales por defecto | `DEFAULT_THRESHOLDS` en [`scripts/portafolio.py`](../../plugins/criterio-portfolio/scripts/portafolio.py) |
| **El método** | Qué significa cada una de las 18 señales y cuándo merece alarma | el skill [`portfolio-health`](../../plugins/criterio-portfolio/skills/portfolio-health/SKILL.md) |
| **El inventario** | Los 15 comandos y los 10 skills, con lo que hace cada uno | el [README del plugin](../../plugins/criterio-portfolio/README.md), porque el plugin se distribuye solo y su README tiene que sostenerse solo |
| **El diseño** | El flujo, las tres clases, qué es de las personas, qué falta | esta hoja |

Y cuatro scripts, que son lo único que no opina:

**`scripts/texto.py`** convierte el documento a Markdown para que se pueda leer barato y para
que el hash del texto sea estable. **No extrae campos.** `.docx`, `.xlsx` y `.pptx` se leen
con la librería estándar porque son ZIP con XML adentro; `.eml` con el parser de correo; el
PDF con `pdftotext` si está, y si no se declara. El Markdown es un caché: **la cita de una
ficha apunta siempre al documento original**, porque es lo que una persona abre para
verificar.

**`scripts/portafolio.py`** es la aritmética — `init`, `config`, `index`, `compute`, `snapshot`,
`diff`, `selftest` —. De esos, `index` es el que decide el costo de una corrida: dos hashes
por documento, el de bytes para saber si vale extraer y el del texto para saber si vale
releer, más la verificación de que toda cita siga resolviendo.

**`scripts/informe.py`** arma el informe impreso a partir de lo que los otros dos ya
produjeron: **no vuelve a leer un documento ni vuelve a calcular nada.** Emite dos vistas
que **no se diferencian por detalle sino por autoridad** —`index.html` por campo con la
cadena de evidencia completa, `decisiones.html` por decisión para el patrocinador— y una
página por proyecto. Modo claro y `@media print` a propósito: **el PDF es el HTML
impreso**, porque una librería de PDF rompería la propiedad de que todo esto corre sin
instalar nada.

Y una cosa que hace este script y no hacen los otros: **traduce el esquema al castellano
de quien lee.** Un `plan.milestones[1].evidence` impreso tal cual no se ve mal, se ve
técnico, y quien lo lee supone que así se dice. En el informe sale *«la evidencia del hito
Motor de decisión certificado»*. Que ninguna ruta sobreviva sin traducir lo comprueba
`informe.py --selftest`, y que ninguna señal nueva salga en inglés lo comprueba
`tests/coherencia.py`.

**`scripts/servidor.py`** es **Rostrum**, cómo el informe llega a quien no abre una carpeta. Sirve
las páginas que `informe.py` ya escribió con **tres secciones** —informes de la PMO,
proyectos, productos—, y **no calcula nada**: abrir la página no
dispara ninguna lectura de documentos, y por eso dos personas ven lo mismo. Si
calculara al vuelo tendría que leer documentos, y el portafolio dejaría de ser uno
solo.

Lo único que escribe es la **cola de peticiones**, en una carpeta suya. Alguien deja
una pregunta y el agente la atiende al despertar. Esa cola es la única cosa que rompe
el silencio de `/criterio-portfolio:portfolio-wake` sin ser aritmética de fechas, porque una persona preguntó.
**El camino de escritura hacia la ficha no existe en ese archivo**, y el selftest lo
comprueba: escribe una petición y verifica que la ficha no cambió.

No autentica a nadie, a propósito. Un servidor de cien líneas sobre la librería
estándar no va a autenticar mejor que el proxy que el banco ya tiene, y prometerlo
sería lo que este plugin no hace. Escucha solo en el equipo salvo que se le diga lo
contrario, y cuando se le dice, lo advierte.

---

## A · Lo que hace, y hoy consume tiempo de alguien

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Convertir la documentación a texto legible | La carpeta como esté, en los formatos que haya | Markdown en caché, y la lista de lo que no se pudo leer con la razón | Construido · `texto.py` |
| Decidir qué hay que releer | El conjunto de archivos y `meta.documents_seen` con sus dos hashes | Qué cambió, qué se reguardó sin cambiar, qué se renombró o se borró, y qué citas dejaron de resolver | Construido · `/criterio-portfolio:document-index` |
| Consolidar el estado del portafolio | Documentos de cada proyecto | Una ficha por proyecto, con cita y fecha en cada campo, y el consolidado | Construido · `/criterio-portfolio:portfolio-scan`, `/criterio-portfolio:portfolio-report` |
| Armar el material de comité y el informe de dirección | Fichas, alertas, compromisos abiertos | Paquete de decisiones en borrador, con la consecuencia de no decidir | Construido · `/criterio-portfolio:steering-pack` |
| Contrastar la declaración de cada gerente contra la evidencia | `declared` de cada ficha y las alertas calculadas | `declared.unaccounted_signals`, `declared_vs_evidence`, `totals.green_contradicted` | Construido |
| Verificar que exista acta, línea base, doliente y autoridad | Documentos de gobierno y la ficha | `has_baseline`, `fields_missing`, `no_authority`, y la consecuencia de cada vacío | Construido · `/criterio-portfolio:project-charter` |
| Seguir los compromisos del comité | Minutas y transcripciones | Compromisos con doliente, fecha y fuente; vencidos, sin fecha, y reprogramados | Construido · `/criterio-portfolio:raid-log` |
| Las cuatro cifras del presupuesto | Aprobado, contratos, ejecución, proyección declarada | Disponible real, % ejecutado, % comprometido, sobrecosto de la proyección | Construido · `/criterio-portfolio:budget-tracking` |
| Cruzar entregables de proveedor contra evidencia y facturación | Contratos, actas de recibo, facturación, monto por entregable | Vencidos sin evidencia, aceptados sin documento, factura sin entrega, factura sobre lo aceptado | Construido · `/criterio-portfolio:vendor-tracking` |
| Detectar dependencias entre proyectos | Dependencias declaradas con el código del otro proyecto | El cruce con la fecha vigente del otro, y si fue confirmada o solo declarada | Construido |
| Reconciliar la replanificación contra lo autorizado | Línea base de solo agregar y cambios aprobados | Días que se movió, días autorizados, días que ningún documento autoriza | Construido · `/criterio-portfolio:change-control` |
| Mirar el portafolio por producto | `identity.product` de cada ficha | El estado del producto a través de sus proyectos, y los que no declaran producto | Construido · `/criterio-portfolio:product-view` |

## B · Lo que hace, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Detectar contradicciones entre documentos | Dos o más documentos que hablan del mismo campo | Campo en `ambiguous` con las dos fuentes y sus fechas; alerta sin umbral | Construido |
| Health check de un proyecto contra evidencia | Toda la documentación, sin ficha previa | Dictamen de tres estados, y lo que la carpeta no permite saber | Construido · `/criterio-portfolio:health-check` |
| Reconstruir el historial: qué pasó en catorce meses | Los documentos ordenados por fecha | Línea de tiempo, replanificaciones, atraso acumulado, y el punto de separación | Construido · `/criterio-portfolio:project-history` |
| Lecciones ancladas a hechos documentados | Criterio de éxito del acta y la historia documental | Lecciones que nombran hecho, fecha y efecto | Construido · `/criterio-portfolio:project-closure` |
| Borrador del paquete de decisión | Alertas escaladas y la autoridad declarada | La decisión formulada como pregunta cerrada, con opciones | Construido · `/criterio-portfolio:steering-pack` |
| Impacto de un cambio en el resto del portafolio | El cambio propuesto y las dependencias declaradas | Proyectos alcanzados —directos e indirectos, con su camino—, sus gerentes, quién no puede sostener su fecha y por cuántos días, y qué dependencia nunca se confirmó | **Construido** · `portafolio.py impact`, dentro de `/criterio-portfolio:change-control`. Quince comprobaciones, incluido el ciclo de dependencias |

**La calibración por gerente se descartó**, y conviene dejar escrito por qué para que no
vuelva como buena idea. Es el subproducto natural de guardar corridas: con el tiempo se sabe,
por persona, cuántas veces lo declarado se sostuvo. Su única aplicación natural es evaluar
personas, y el día que se use para eso nadie vuelve a declarar nada — y sin declaración no hay
contra qué contrastar la evidencia, que es todo el sistema. **No se construye.**

## C · Lo que el agente no hace

Lista de acciones que el agente no ejecuta. No es una evaluación de riesgo ni pretende ser
exhaustiva: **la responsabilidad de uso y ejecución es de la organización que lo despliega.**
Ver [Vera · y para qué no sirve](README.es.md#y-para-qué-no-sirve).

| Función | Requiere | Qué le entrega al agente |
|---|---|---|
| Priorizar y admitir la demanda | Autoridad | El portafolio aprobado y su orden: define qué fichas existen |
| Aprobar línea base, cambios y excepciones | Autoridad | La decisión fechada, que es la referencia de todo el cálculo |
| Decidir detener o matar un proyecto | Autoridad · información fuera de los documentos | El cierre, que dispara el registro de lecciones |
| Asignar recursos y capacidad | Juicio sobre personas · información que no está en la carpeta | Quién es el gerente de cada proyecto |
| Mediar conflictos entre áreas y escalar políticamente | Información fuera de los documentos | El acuerdo, cuando queda en acta |
| Evaluar el desempeño de un gerente de proyecto | Juicio sobre personas | Nada. Y si el sistema se usa para esto, deja de recibir declaraciones |
| Responder ante auditoría, riesgo operativo y el regulador | Autoridad | Los requerimientos del auditor, que entran como restricción o riesgo |
| Acompañar y formar gerentes de proyecto | Juicio sobre personas | Adopción: un gerente que entiende el método deja mejor rastro |

---

## Lo que sigue siendo de la PMO persona

El director de la PMO y sus analistas conservan la función completa. Y una distinción que no
es una función sino un límite: **el informe del agente es el insumo del comité, no el
comité.** El agente formula la decisión como pregunta cerrada con sus opciones; quién
decide, con qué criterio y asumiendo qué, es de la instancia que tiene la facultad.

Si una organización quitara al analista de PMO y dejara solo al agente, lo que se rompe
primero, en este orden:

1. **Nadie persigue lo que el informe pide.** El agente vuelve a reportar lo mismo, y se ignora.
2. **Nadie decide qué escala.** El agente sabe qué cruzó un umbral; no sabe qué vale la pena
   pelear esta semana.
3. **Nadie contesta en la sala.** La pregunta del patrocinador en el comité casi nunca es la
   que está en el informe.

---

## La estructura del portal, y por qué es esa

Tres secciones, y el orden importa: **cómo va todo, después el proyecto, después el
producto.** Es el orden en que alguien pregunta.

| Sección | Responde | Y no responde |
|---|---|---|
| **Informes PMO** | ¿Cómo va el portafolio? Lo que solo se ve mirando todo junto: los verdes que la evidencia no sostiene, lo que lleva semanas en silencio, quién patrocina más de una cosa | Cuál proyecto abrir. Para eso está el listado |
| **Proyectos** | ¿Cómo va este proyecto, y de dónde salió cada dato? | Para qué sirve lo que está construyendo. Para eso enlaza al producto |
| **Productos** | ¿Cómo va este producto, y quién lo está construyendo? | Adopción, ingreso, incidencias. Nada de eso está en la carpeta, y la página lo dice |

**El enlace entre proyecto y producto va en los dos sentidos**, y no es una comodidad
de navegación: es lo que produce el único hallazgo que no existe en ninguna otra
página. Cuando un producto lo construyen dos proyectos que reportan a comités
distintos, **cada comité ve su proyecto y ninguno ve el producto**. Nadie puede
detectarlo desde adentro de un proyecto, porque desde adentro de un proyecto no se ve
el otro.

De ahí salen las tres cosas que el informe de producto dice y el de proyecto no puede:
que más de un comité lo mira, que más de un patrocinador responde por él —y entonces
no hay una sola respuesta a quién se le escala—, y que **el proyecto sano no salva al
producto**: no llega hasta que llegan los dos, así que su estado es el del peor y no
el promedio.

Lo que el portal **no hace** es inventarle al producto una ficha propia. Todo lo que
dice sale de lo que los proyectos declararon en su acta, y se dice con esa salvedad.
Un proyecto que no declara producto no es un error suyo —hay proyectos que no
construyen un producto—, pero mientras no esté dicho su avance no se ve desde el lado
del producto, y eso se reporta.

## Cuando el proyecto tiene su propio agente

Un proyecto con **Samuel** instalada publica su ficha en la carpeta de gobierno, como
`ficha-pm.json`. Vera **la lee como lee cualquier otro documento** —no alcanza el
estado de Samuel y no hace falta— y sigue escribiendo la suya.

Son dos fichas y no se fusionan nunca: la séptima invariante. Lo que produce valor es
la diferencia entre las dos, porque los dos leyeron los mismos documentos. Cuando los
dos citan y no coinciden, alguien vio un documento que el otro no vio, y la señal dice
cuál y de qué fecha.

Del lado de Vera eso es una señal más —`pm_vs_pmo`, ocho campos contrastados— y por
lo tanto aritmética: **el código la calcula**, con las dos citas. El diseño completo,
incluidos los tres casos que **no** son hallazgo, vive en la hoja de Samuel, que es su
dueña: [Samuel · las dos fichas](../criterio-project/DISENO.es.md#las-dos-fichas).

Un proyecto sin Samuel no cambia en nada. La ficha de Vera sigue siendo la única, y
es el caso que hoy está construido y probado.

## Lo que falta

**`report.language`.** El informe sale hoy solo en castellano. Las piezas gráficas y
los dos README ya están en los dos idiomas; el informe no, y esa es la asimetría que
queda.

**`report.recipients`**, que el servidor deja a medias a propósito. Hoy el informe se
puede *consultar* por enlace, y eso resuelve al patrocinador que entra a mirar. No
resuelve que el informe *llegue* a un buzón sin que nadie lo reenvíe, y **eso no se va a
resolver dándole correo al plugin**: mandar correos en nombre de alguien es una facultad
que este agente no va a tener. Si tiene que llegar solo, lo manda un mecanismo de la
organización leyendo `/estado.json`, no Vera.

**Autenticación en el servidor**, que está decidido que no la trae y conviene releerlo
cada tanto por si la decisión deja de ser la correcta. Ver arriba.

**OCR para el PDF escaneado.** Hoy un escaneo sin capa de texto se declara ilegible, que es
la conducta correcta y no la útil. Cuando entre, entra marcado: con OCR el texto pasa a ser
una lectura probable y no el contenido.

### Lo que NO falta, aunque lo parezca

**Que la extracción esté calificada y que haya corridas sobre documentación real.** Eso no se
resuelve construyendo: se cubre con **pruebas progresivas** — corpus cada vez más parecidos a
una carpeta real, y el plugin corriendo como lo correría alguien de afuera. El grader ya tiene
el modo que las califica campo por campo contra la referencia. Es un programa de pruebas, no
un pendiente de construcción, y tratarlo como pendiente solo sirve para parecer incompleto.

## Decisiones abiertas propias de esta hoja

- **OCR para el PDF escaneado.** Hoy un escaneo sin capa de texto se declara ilegible, que es
  la conducta correcta y no la útil. Con OCR se vuelve legible y deja de ser determinístico:
  el texto pasa a ser una lectura probable, no el contenido. Si entra, entra marcado.
- **Quién ve la brecha.** Resuelto en discusión: la brecha aparece como **evento** cuando un
  documento cambia, con una pregunta asociada — no como contador permanente visible al
  patrocinador. Es la misma información, y la diferencia decide si el gerente la recibe como
  señal de trabajo o como calificación.

---

# El marco de la familia

Lo que sigue gobierna a los tres agentes y no solo a Vera. Vive en esta hoja porque es **diseño**: se discute aquí y se decide aquí, y lo que la organización que instala necesita saber está en el README, no en este apartado.

## La necesidad común: proyectos

Los tres agentes existen alrededor de un mismo objeto, y la elección carga todo el peso del
diseño: **un proyecto tiene plan, y sin plan no hay contra qué comparar.**

Toda la propuesta se sostiene en contrastar lo que alguien declara contra lo que sustentan los
documentos. Esa comparación necesita una referencia aprobada. En un proceso o en un área no
existe el *contra qué*; en un proyecto sí, y se llama línea base.

## Las tres clases

Cada función de cada rol cae en una de tres. **El alcance construido de Criterio es A y B.**

### A — Lo que el agente hace, y hoy consume tiempo de alguien

Trabajo que la organización ya ejecuta todas las semanas: leer, consolidar, cruzar, reportar.
El agente no lo acelera, lo sustituye. Se reconoce por una prueba simple: **si nadie lo hace,
alguien lo nota.**

### B — Lo que el agente hace y hoy no se hace

Trabajo que la organización no ejecuta, no por descuido sino porque costaría días por
proyecto: el forense de catorce meses, la contradicción entre cuarenta carpetas, el supuesto
que nadie verificó. Se reconoce por la prueba inversa: **si nadie lo hace, nadie lo nota.**

La distinción importa para entender el valor. La A ahorra tiempo en trabajo que ya se hace y la
agradece el equipo. La B produce lo que hoy no existe en ninguna PMO, y la compra un director.

### C — Lo que el agente no hace

Un conjunto de acciones que el agente **no ejecuta**. Nada más.

Esta lista no evalúa riesgos ni exposición de nadie: describe el límite del agente. Quien
instala Criterio acepta los [términos](../../TERMS.es.md) —la verificación es suya, §2; se
entrega sin garantía ni responsabilidad, §5— y el [descargo](../../DISCLAIMER.es.md). La
responsabilidad de uso y de ejecución es de la organización que lo despliega, y si en su
contexto la clase C es más grande que esta lista, delimitarla y documentarla le corresponde a
ella, con el descargo adicional que su gobierno interno exija.

Cada fila de C lleva dos datos, y ninguno es un riesgo:

- **Requiere** — por qué está fuera del alcance del agente: *autoridad* (compromete a la
  organización), *información fuera de los documentos*, o *juicio sobre personas*.
- **Qué le entrega al agente** — porque casi toda función de C produce el insumo de una función
  de A o de B. Es la parte que hace de esto un ciclo y no dos mundos separados.

## Cómo se llaman

**La capacidad se llama PMO, CFO o CLO. El agente lleva nombre de persona.** Son dos cosas
distintas y conviene no mezclarlas: la capacidad es la función de la organización, y el
agente es quien la extiende.

Que lleven nombre de persona no es un adorno: **son capacidades extendidas de personas
reales**, y el producto entero se sostiene en que la persona sigue ahí. Un nombre propio
dice eso sin tener que explicarlo.

| Pieza | Nombre | De dónde viene | La frase |
|---|---|---|---|
| Agente PMO | **Vera** | latín *verus*, lo verdadero | *Vera dice lo que los documentos dicen, no lo que se reporta* |
| Agente Project Manager | **Samuel** | «el que escuchó» | *Samuel oyó lo que se dijo en la reunión, y lo recuerda el viernes* |
| Agente Product Manager | **Alba** | el amanecer, antes de que haya luz | *Alba trabaja antes de que el proyecto exista* |
| El servidor | **Rostrum** | una tribuna | *Sostiene lo que ya está escrito, donde otros puedan leerlo* |

**La regla, que es lo que hace que esto escale y no la lista:** el nombre de un agente es
un nombre de persona **cuyo significado apunta al oficio que su familia extiende**, y tiene
que poder terminar la frase «X hace esto, y no opina». Si no la termina, está mal elegido.

Samuel es el que mejor lo muestra: la función central de ese agente es **el compromiso
dicho y no cumplido**, y el nombre significa literalmente «el que escuchó».

Las familias que vengan eligen con la misma regla y con las referencias de su propio
gremio — **CFO** con Mateo, patrono de contadores y banqueros, o Luca por Pacioli; **CLO**
con Ivo, patrono de los abogados. Quien pertenece al gremio reconoce la referencia sin que
nadie se la explique, y quien no la reconoce solo ve un nombre, que también está bien.

**El servidor es el único que no lleva nombre de persona, y es a propósito.** Los agentes
lo llevan porque toman decisiones sobre lo que leen; el servidor no toma ninguna. Es
infraestructura, y conserva nombre de objeto: una tribuna no mide, no corrige y no opina —
sostiene lo que ya está escrito a la altura de quien lo va a leer. Si algún día calculara
algo, el nombre dejaría de ser cierto, y eso es exactamente lo que se quiere que se note.

**Los nombres no se traducen** —son propios— y **no son identificadores**: el plugin se
sigue llamando `criterio-portfolio`, los comandos y los skills no cambian. El nombre le da
carácter a lo que la persona ve, no a lo que el código importa.

## Un dueño por cosa

No se duplica documentación. Una tabla copiada en tres documentos se desactualiza en el
primero que nadie mire, y eso ya pasó: la lista de señales de la página pública llegó a estar
cinco señales atrás y a prometer una que el código no emitía.

| Cosa | Dueño | Por qué ahí |
|---|---|---|
| Los valores de los umbrales | `DEFAULT_THRESHOLDS` en `scripts/portafolio.py` | Es lo que el código lee. Cualquier otra copia es una opinión |
| Qué significa cada señal y cuándo merece alarma | el skill `portfolio-health` | Es lo que el modelo carga en tiempo de ejecución, y tiene que sostenerse solo |
| El inventario de comandos y skills | el README del plugin | El plugin se distribuye por el market y su README viaja con él |
| La promesa pública y las cifras de terceros | el README del market | Es la primera página que alguien abre, y la única que decide una instalación |
| El diseño de cada agente | estas hojas | Clases, flujo, lo que es de las personas, lo que falta |
| El resultado de las corridas | `tests/<plugin>/EVIDENCIA.md` | La evidencia vive con el material que la produjo |

Lo verifican dos cosas, y ninguna es un humano acordándose: `scripts/validate_plugins.py`
exige que el README del plugin liste cada comando, y `tests/coherencia.py` exige que cada
señal que el código calcula esté documentada en su skill y que cada comando aparezca en la
página pública. **Si algo se agrega y no se documenta en su dueño, falla.**

## Decisiones de esquema, cerradas

Aquí vivían cinco, todas de esquema y todas por decidir **antes** de que un agente empezara a
llenar fichas: una ficha llena con el esquema equivocado es la migración que no queremos hacer.

**Las cinco se construyeron** —`source_kind`, `producto`, `autoridad`, el monto por entregable
y, la última, **`requerimiento` como registro**—, y por eso salen de la tabla en vez de quedarse
como historia. El registro de requerimiento es el contrato de datos de Alba, vive en
`criterio-product` con su propia aritmética, y es el que vuelve *«qué requerimientos faltan»* un
filtro en vez de una corrida de modelo sobre documentos cada vez. El esquema va en 0.2.

Lo que queda abierto de verdad está en cada hoja: **cómo bajan los estándares de la PMO a N
instalaciones** y **qué pasa cuando un gerente publica su ficha y no quiere** —las dos en la
hoja del Project Manager—, y **el análisis de canibalización**, que necesita las métricas de más
de un producto a la vista y hoy cada instalación mira el suyo.

Sobre la base de datos hay una trampa que conviene dejar escrita: **lo que trae un PPM son más
declaraciones, no evidencia.** El campo *"estado: verde"* de la herramienta corporativa es la
afirmación del gerente con otra interfaz. La evidencia sigue viviendo en actas y minutas.

---

# Criterios de aceptación

Escritos antes que el código, a propósito: un criterio escrito después describe lo que se
construyó, no lo que hacía falta.

Se verifican sobre la carpeta sintética de `tests/criterio-portfolio/` —seis proyectos y veintiséis
documentos, con las respuestas conocidas escritas a mano y un calificador encima—. El
resultado de la corrida, con lo que **no** cubre, está en
[`EVIDENCIA.md`](../../tests/criterio-portfolio/EVIDENCIA.md) y, generado desde la corrida misma, en
[`RESULTADOS.md`](../../tests/criterio-portfolio/RESULTADOS.md).

Las casillas que la aritmética puede decidir se marcan contra esa corrida. **Las que dependen
de cómo un modelo lee la carpeta siguen abiertas hasta que el plugin corra en una sesión**, y
esa distinción es la que impide que esta lista se marque sola.

## 1 · Cobertura

- [ ] Todo documento de la carpeta se lee, o queda listado como ilegible con la razón. Nada se
      salta en silencio.
- [ ] Documentos en formatos mezclados y en idiomas mezclados se manejan, o se declaran.
- [ ] Un proyecto que solo se menciona dentro de la minuta de otro proyecto igual aparece.

## 2 · Hallazgos que tienen que aparecer

- [x] Un proyecto cuyo estado reportado contradice sus propias fechas — PRY-001 y PRY-004.
- [ ] Un proyecto sin doliente identificable — el conjunto sintético tiene la autoridad
      ausente, no el doliente; falta agregar un proyecto sin él.
- [x] Un proyecto sin novedad en el último trimestre — PRY-004, 153 días.
- [x] Dos documentos que declaran fechas distintas para el mismo hito — PRY-006: el acta dice
      octubre, la minuta del comité dice enero, y nadie actualizó el plan.
- [x] Una dependencia nombrada en un plan y ausente del plan del que depende — PRY-001 la
      declara de PRY-002, sin confirmar.
- [x] Un proyecto que reporta verde con al menos una señal que el verde no explica, listada por
      señal y contada a nivel de portafolio — tres de seis.
- [x] Un entregable de proveedor vencido sin evidencia de entrega — PRY-003. El caso de la
      factura **no** se detecta: necesita monto por entregable. Ver el límite 1 de la evidencia.
- [x] Una replanificación que movió más días de los que autorizaron los cambios aprobados —
      PRY-001, 61 contra 60 autorizados.
- [x] Un impacto de cambio escrito en meses, reportado como ilegible en vez de convertido en un
      número — PRY-006.
- [x] A quién alcanza mover un proyecto, con quién no puede sostener su fecha y por cuántos
      días — mover PRY-002 sesenta días alcanza a PRY-001, que cierra 121 días antes.

## 3 · Trazabilidad

- [ ] Toda afirmación del informe de portafolio cita el documento y el lugar de donde salió.
- [ ] No se afirma ningún estado que ningún documento sostenga. *«No está dicho en ninguna
      parte»* es un hallazgo válido y esperado.

## 4 · Términos y aceptación

- [ ] Las mismas cuatro capas que todo plugin: puerta, pie, aviso y archivo de términos.

## 5 · El umbral

- [x] Todo hallazgo plantado se detecta — sin errores en la corrida.
- [x] **Un proyecto sano no produce ni una alerta** — PRY-005. Es el criterio que decide si el
      plugin es usable: un agente que alerta sobre un proyecto sano es un generador de ruido, y
      lo silencian en un mes.
- [ ] Cero proyectos, fechas o dolientes inventados, comprobado rastreando una muestra de
      afirmaciones hasta su fuente.
