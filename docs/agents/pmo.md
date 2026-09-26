# Plomada · el agente PMO

Cuelga quieta y dice si algo está derecho. Extiende a la **oficina de proyectos**: la función que responde por el conjunto de los
proyectos, no por uno.

Esta hoja es la referencia completa de la capacidad: el flujo, las piezas que la componen y
qué hace cada una, las tres clases de función, y lo que falta. Marco general y definiciones:
[README](README.md).

| | |
|---|---|
| **Instancia** | Una por organización |
| **Alcance** | Todos los proyectos. Barrido amplio, cadencia de comité |
| **Escribe** | Hallazgos. Estándar: umbrales, versión del esquema, convenciones |
| **No escribe** | La declaración de ningún gerente — sexta invariante |
| **Lee** | Todas las fichas, y la carpeta de documentación |
| **Estado** | Disponible. Clase A cerrada; de la B queda una fila |
| **Evidencia** | [`tests/criterio-pmo/EVIDENCIA.md`](../../tests/criterio-pmo/EVIDENCIA.md) |

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
| **Los valores** | Los ocho umbrales por defecto | `DEFAULT_THRESHOLDS` en [`scripts/pmo.py`](../../plugins/criterio-pmo/scripts/pmo.py) |
| **El método** | Qué significa cada una de las 18 señales y cuándo merece alarma | el skill [`portfolio-health`](../../plugins/criterio-pmo/skills/portfolio-health/SKILL.md) |
| **El inventario** | Los 15 comandos y los 10 skills, con lo que hace cada uno | el [README del plugin](../../plugins/criterio-pmo/README.md), porque el plugin se distribuye solo y su README tiene que sostenerse solo |
| **El diseño** | El flujo, las tres clases, qué es de las personas, qué falta | esta hoja |

Y cuatro scripts, que son lo único que no opina:

**`scripts/texto.py`** convierte el documento a Markdown para que se pueda leer barato y para
que el hash del texto sea estable. **No extrae campos.** `.docx`, `.xlsx` y `.pptx` se leen
con la librería estándar porque son ZIP con XML adentro; `.eml` con el parser de correo; el
PDF con `pdftotext` si está, y si no se declara. El Markdown es un caché: **la cita de una
ficha apunta siempre al documento original**, porque es lo que una persona abre para
verificar.

**`scripts/pmo.py`** es la aritmética — `init`, `config`, `index`, `compute`, `snapshot`,
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

**`scripts/servidor.py`** es **Atril**, cómo el informe llega a quien no abre una carpeta. Sirve
las páginas que `informe.py` ya escribió con **tres secciones** —informes de la PMO,
proyectos, productos—, y **no calcula nada**: abrir la página no
dispara ninguna lectura de documentos, y por eso dos personas ven lo mismo. Si
calculara al vuelo tendría que leer documentos, y el portafolio dejaría de ser uno
solo.

Lo único que escribe es la **cola de peticiones**, en una carpeta suya. Alguien deja
una pregunta y el agente la atiende al despertar. Esa cola es la única cosa que rompe
el silencio de `/pmo-wake` sin ser aritmética de fechas, porque una persona preguntó.
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
| Decidir qué hay que releer | El conjunto de archivos y `meta.documents_seen` con sus dos hashes | Qué cambió, qué se reguardó sin cambiar, qué se renombró o se borró, y qué citas dejaron de resolver | Construido · `/document-index` |
| Consolidar el estado del portafolio | Documentos de cada proyecto | Una ficha por proyecto, con cita y fecha en cada campo, y el consolidado | Construido · `/portfolio-scan`, `/portfolio-report` |
| Armar el material de comité y el informe de dirección | Fichas, alertas, compromisos abiertos | Paquete de decisiones en borrador, con la consecuencia de no decidir | Construido · `/steering-pack` |
| Contrastar la declaración de cada gerente contra la evidencia | `declared` de cada ficha y las alertas calculadas | `declared.unaccounted_signals`, `declared_vs_evidence`, `totals.green_contradicted` | Construido |
| Verificar que exista acta, línea base, doliente y autoridad | Documentos de gobierno y la ficha | `has_baseline`, `fields_missing`, `no_authority`, y la consecuencia de cada vacío | Construido · `/project-charter` |
| Seguir los compromisos del comité | Minutas y transcripciones | Compromisos con doliente, fecha y fuente; vencidos, sin fecha, y reprogramados | Construido · `/raid-log` |
| Las cuatro cifras del presupuesto | Aprobado, contratos, ejecución, proyección declarada | Disponible real, % ejecutado, % comprometido, sobrecosto de la proyección | Construido · `/budget-tracking` |
| Cruzar entregables de proveedor contra evidencia y facturación | Contratos, actas de recibo, facturación, monto por entregable | Vencidos sin evidencia, aceptados sin documento, factura sin entrega, factura sobre lo aceptado | Construido · `/vendor-tracking` |
| Detectar dependencias entre proyectos | Dependencias declaradas con el código del otro proyecto | El cruce con la fecha vigente del otro, y si fue confirmada o solo declarada | Construido |
| Reconciliar la replanificación contra lo autorizado | Línea base de solo agregar y cambios aprobados | Días que se movió, días autorizados, días que ningún documento autoriza | Construido · `/change-control` |
| Mirar el portafolio por producto | `identity.product` de cada ficha | El estado del producto a través de sus proyectos, y los que no declaran producto | Construido · `/product-view` |

## B · Lo que hace, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Detectar contradicciones entre documentos | Dos o más documentos que hablan del mismo campo | Campo en `ambiguous` con las dos fuentes y sus fechas; alerta sin umbral | Construido |
| Health check de un proyecto contra evidencia | Toda la documentación, sin ficha previa | Dictamen de tres estados, y lo que la carpeta no permite saber | Construido · `/health-check` |
| Reconstruir el historial: qué pasó en catorce meses | Los documentos ordenados por fecha | Línea de tiempo, replanificaciones, atraso acumulado, y el punto de separación | Construido · `/project-history` |
| Lecciones ancladas a hechos documentados | Criterio de éxito del acta y la historia documental | Lecciones que nombran hecho, fecha y efecto | Construido · `/project-closure` |
| Borrador del paquete de decisión | Alertas escaladas y la autoridad declarada | La decisión formulada como pregunta cerrada, con opciones | Construido · `/steering-pack` |
| Impacto de un cambio en el resto del portafolio | El cambio propuesto y las dependencias declaradas | Proyectos alcanzados y sus gerentes | **Parcial** — en prosa |

**La calibración por gerente se descartó**, y conviene dejar escrito por qué para que no
vuelva como buena idea. Es el subproducto natural de guardar corridas: con el tiempo se sabe,
por persona, cuántas veces lo declarado se sostuvo. Su única aplicación natural es evaluar
personas, y el día que se use para eso nadie vuelve a declarar nada — y sin declaración no hay
contra qué contrastar la evidencia, que es todo el sistema. **No se construye.**

## C · Lo que el agente no hace

Lista de acciones que el agente no ejecuta. No es una evaluación de riesgo ni pretende ser
exhaustiva: **la responsabilidad de uso y ejecución es de la organización que lo despliega.**
Ver [README](README.md#c--lo-que-el-agente-no-hace).

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

## Lo que falta

**`report.language`.** El informe sale hoy solo en castellano. Las piezas gráficas y
los dos README ya están en los dos idiomas; el informe no, y esa es la asimetría que
queda.

**`report.recipients`**, que el servidor deja a medias a propósito. Hoy el informe se
puede *consultar* por enlace, y eso resuelve al patrocinador que entra a mirar. No
resuelve que el informe *llegue* a un buzón sin que nadie lo reenvíe, y **eso no se va a
resolver dándole correo al plugin**: mandar correos en nombre de alguien es una facultad
que este agente no va a tener. Si tiene que llegar solo, lo manda un mecanismo de la
organización leyendo `/estado.json`, no Plomada.

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
