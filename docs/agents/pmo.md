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
| **Evidencia** | [`tests/criterio-pmo/EVIDENCIA.md`](../../tests/criterio-pmo/EVIDENCIA.md) — corrida sintética, 69 comprobaciones |

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

## La subestructura: qué hace cada pieza

Cuatro capas. De abajo hacia arriba: dos scripts que no opinan, diez skills que son el
método, quince comandos que son la puerta, y diecisiete señales que son la salida.

### Los dos scripts

Librería estándar, sin dependencias, auditables antes de instalar.

| Script | Qué hace |
|---|---|
| `scripts/texto.py` | Convierte el documento a Markdown para que se pueda leer barato y para que el hash del texto sea estable. **No extrae campos.** `.docx`, `.xlsx` y `.pptx` se leen con la librería estándar porque son ZIP con XML adentro; `.eml` con el parser de correo; el PDF con `pdftotext` si está, y si no se declara |
| `scripts/pmo.py` | La aritmética. El modelo extrae, esto calcula: `init`, `config`, `index`, `compute`, `snapshot`, `diff`, `selftest` |

`pmo.py index` es el que decide el costo de una corrida: dos hashes por documento, el de
bytes para saber si vale extraer y el del texto para saber si vale releer, más la
verificación de que toda cita siga resolviendo.

### Los diez skills

Se cargan solos cuando el tema aparece. Son el conocimiento que los comandos comparten.

| Skill | Qué encapsula |
|---|---|
| `project-record` | La ficha: esquema, reglas de extracción, citación, estados de campo, y qué hacer cuando dos documentos se contradicen. Es la espina: ningún comando lee documentos crudos por su cuenta |
| `document-intake` | Qué documento hay que releer y cuál no, los cuatro estados de un documento, el renombrado, el borrado, y la cita que dejó de resolver |
| `baseline-variance` | Línea base de solo agregar, desviación contra la original y contra la vigente, la replanificación contra lo que autorizó el comité, y las cuatro cifras del presupuesto |
| `portfolio-health` | El semáforo declarado contra la evidencia calculada, los umbrales, las tres defensas contra el dato que dejó de ser cierto, y el orden del informe |
| `raid-taxonomy` | Las cuatro categorías y cómo distinguirlas, la valoración, el criterio de escalamiento, y los riesgos que se dijeron en una reunión y nadie registró |
| `commitment-tracking` | Compromisos dichos en reuniones: qué es un compromiso, los cuatro estados, qué cuenta como evidencia de cumplimiento, y el que se repite con fecha nueva cada vez |
| `governance-artifacts` | Acta, comité, control de cambios y cierre: qué contiene cada uno, quién decide qué, y qué falta cuando falta |
| `vendor-control` | Contrato contra evidencia de recibo contra facturación, con monto por entregable, y el preaviso que si vence renueva solo |
| `project-diagnosis` | El diagnóstico desde cero: en qué orden se lee, los tres dictámenes, y cuándo la respuesta correcta es que la carpeta no permite diagnosticar |
| `portfolio-history` | La historia de un proyecto desde sus documentos, y el punto donde la evidencia se separó de lo reportado |

### Los quince comandos

| Comando | Qué hace | Skills que aplica |
|---|---|---|
| `/pmo-setup` | Mira tus carpetas, hace cinco preguntas y produce un primer resultado sobre tres proyectos | todos, según lo que encuentre |
| `/document-index` | Qué documentos cambiaron de verdad, qué hay que releer, y qué citas dejaron de resolver | `document-intake`, `project-record` |
| `/portfolio-scan` | Lee la documentación y arma una ficha por proyecto, con cita y fecha en cada dato | `project-record`, `document-intake` |
| `/portfolio-report` | Qué cambió desde la corrida anterior, qué se contradice, qué está en silencio y qué no tiene sustento | `portfolio-health`, `project-record` |
| `/status-report` | Estado de un proyecto contra su plan, y las señales que su semáforo declarado no explica | `project-record`, `baseline-variance`, `raid-taxonomy`, `commitment-tracking` |
| `/health-check` | Diagnostica un proyecto desde cero, sin asumir nada de su informe de avance | `project-diagnosis`, `governance-artifacts`, `baseline-variance` |
| `/project-history` | Qué pasó en catorce meses, y desde cuándo lo declarado dejó de sostenerse | `portfolio-history`, `baseline-variance`, `commitment-tracking` |
| `/steering-pack` | El comité como paquete de decisiones, no como informe de avance | `governance-artifacts`, `portfolio-health` |
| `/raid-log` | Riesgos, supuestos, incidencias y dependencias, incluidos los que se dijeron y nadie registró | `raid-taxonomy`, `commitment-tracking` |
| `/change-control` | Evalúa un cambio en alcance, tiempo y costo, y crea línea base nueva sin borrar la anterior | `baseline-variance`, `governance-artifacts` |
| `/budget-tracking` | Aprobado, comprometido, ejecutado y proyección — las cuatro, no dos | `baseline-variance` |
| `/vendor-tracking` | Entregables contractuales contra evidencia de recibo y contra lo facturado | `vendor-control`, `commitment-tracking` |
| `/product-view` | El estado de un producto a través de todos los proyectos que lo construyen | `portfolio-health`, `baseline-variance` |
| `/project-charter` | Revisa el acta y dice qué falta y qué consecuencia tiene que falte | `governance-artifacts` |
| `/project-closure` | Cierra contra el criterio de éxito pactado, con lecciones ancladas a hechos | `governance-artifacts`, `portfolio-history` |

Los quince verifican la aceptación de los términos antes de producir nada, y cierran con el
pie que declara versión, fecha de la ficha y campos inciertos.

### Las diecisiete señales

Ocho umbrales las gobiernan, y todos son configuración.

| Señal | Habla cuando | Umbral |
|---|---|---|
| `milestone_overdue` | La fecha pasó y no hay evidencia de cumplimiento | — |
| `silent` | Días sin documento nuevo | `silent_days` 15 |
| `variance_time` | Desviación en tiempo contra la línea base original | `variance_time_pct` 10 |
| `variance_cost` | La proyección se pasa del aprobado | `variance_cost_pct` 10 |
| `budget_committed` | Lo comprometido se acerca a lo aprobado | `committed_pct` 90 |
| `commitment_overdue` | Pasó la fecha y no hay evidencia | — |
| `commitment_undated` | Un compromiso que nadie fechó | — |
| `commitment_rescheduled` | El mismo compromiso prometido de nuevo | `reschedules_to_flag` 3 |
| `contradiction` | Dos documentos dicen cosas distintas del mismo campo | — |
| `declared_vs_evidence` | Declara verde y hay una señal que ese verde no cubre | — |
| `declaration_stale` | La declaración es vieja | `declaration_stale_days` 30 |
| `rebaseline_unauthorized` | La línea base se movió más de lo autorizado | `rebaseline_tolerance_days` 0 |
| `change_without_baseline` | Un cambio aprobado movió fechas y no dejó línea base nueva | — |
| `vendor_deliverable_late` | Pasó la fecha, sin evidencia y sin declararse entregado | — |
| `vendor_accepted_without_evidence` | Declarado entregado y sin documento que lo pruebe | — |
| `vendor_invoiced_without_delivery` | Hay factura y ni un entregable aceptado | — |
| `vendor_invoiced_over_accepted` | La factura supera la suma de lo aceptado | — |

Un campo con más de `stale_field_months` 12 meses carga su antigüedad visible en el informe
sin levantar alerta. **El silencio cuando no pasó nada es la característica, no la falla.**

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
