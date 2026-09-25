# Agente PMO

Extiende a la **oficina de proyectos**: la función que responde por el conjunto de los
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

Y dos scripts, que son lo único que no opina:

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
| Calibrar la declaración de cada gerente en el tiempo | Los snapshots de varias corridas | El patrón de la brecha por persona | **Falta**, y no puede ir primero: necesita historia |

**La calibración por gerente hay que tratarla con cuidado.** Es el subproducto natural de
guardar corridas, y en manos equivocadas es una herramienta de evaluación de desempeño. El
efecto de usarla así es predecible: nadie vuelve a declarar nada, y con eso desaparece la
mitad de la comparación. Se construye como insumo de conversación con el gerente, o no se
construye.

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

## Lo que falta

De las clases A y B queda **una fila**: la calibración por gerente, que necesita historia de
corridas y está tan pendiente de decidirse como de construirse.

Fuera de las clases, lo que sigue abierto no es método sino **mecanismo**: las siete claves
de configuración de cadencia y notificaciones —`paths.standard`, `cycle.committee_next`,
`cycle.report_lead_days`, `cycle.daily_sweep`, `report.language`, `report.recipients`,
`confirmation.fields_per_run`— siguen declaradas y sin leer. Ahí vive la promesa de que el
agente corre solo: el disparador ya existe, `/document-index` es el mecanismo, y lo que falta
es quién lo invoca sin que alguien abra una sesión.

Y un límite que no se cierra con código: **un cambio aprobado cuyo impacto de tiempo está
escrito en meses** no suma a los días autorizados ni aparece como cambio sin línea base. Solo
sale en la lista de ilegibles. Cada paso es correcto y el cambio real queda fuera del
control; la mitigación es preguntar, no convertir.

## Decisiones abiertas propias de esta hoja

- **Si la calibración por gerente se construye**, y con qué visibilidad.
- **OCR para el PDF escaneado.** Hoy un escaneo sin capa de texto se declara ilegible, que es
  la conducta correcta y no la útil. Con OCR se vuelve legible y deja de ser determinístico:
  el texto pasa a ser una lectura probable, no el contenido. Si entra, entra marcado.
- **Quién ve la brecha.** Resuelto en discusión: la brecha aparece como **evento** cuando un
  documento cambia, con una pregunta asociada — no como contador permanente visible al
  patrocinador. Es la misma información, y la diferencia decide si el gerente la recibe como
  señal de trabajo o como calificación.
