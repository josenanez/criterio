# Agente PMO

Extiende a la **oficina de proyectos**: la función que responde por el conjunto de los
proyectos, no por uno.

Marco general, definición de las clases y de las columnas: [README](README.md).

| | |
|---|---|
| **Instancia** | Una por organización |
| **Alcance** | Todos los proyectos. Barrido amplio, cadencia de comité |
| **Escribe** | Hallazgos. Estándar: umbrales, versión del esquema, convenciones |
| **No escribe** | La declaración de ningún gerente |
| **Lee** | Todas las fichas |
| **Estado** | Disponible. Clase A cerrada; la B a medias |
| **Evidencia** | [`tests/criterio-pmo/EVIDENCIA.md`](../../tests/criterio-pmo/EVIDENCIA.md) — corrida sintética, 49 comprobaciones |

---

## El flujo

```
DIRECTOR / ANALISTA DE PMO  (clase C)          AGENTE PMO  (clases A y B)
──────────────────────────────────────────────────────────────────────────────────
prioriza y admite la demanda
   └─► portafolio aprobado ──────────────────► define qué fichas existen
                                          ┌──  barre los documentos de cada proyecto
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
                                               y de la reconciliación de replanes

responde ante comité, auditoría
y regulador
   └─► requerimientos del auditor ───────────► entran como restricción o riesgo
```

El ciclo se cierra por la izquierda: **si nadie persigue lo que el informe pide, el informe
siguiente dice lo mismo**, y en un mes se ignora.

---

## A · Lo que hace, y hoy consume tiempo de alguien

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Consolidar el estado del portafolio | Documentos de cada proyecto: actas, cronogramas, minutas, hojas de cálculo | Una ficha por proyecto, con cita y fecha en cada campo, y el consolidado | Construido |
| Armar el material de comité y el informe de dirección | Fichas, alertas, compromisos abiertos | Paquete de decisiones en borrador, con la consecuencia de no decidir | Construido |
| Contrastar la declaración de cada gerente contra la evidencia | `declared` de cada ficha y las alertas ya calculadas | `declared.unaccounted_signals`, alerta `declared_vs_evidence`, `totals.green_contradicted` | Construido |
| Verificar que exista acta, línea base y doliente | Documentos de gobierno y la ficha | `has_baseline`, `fields_missing`, y la consecuencia concreta de cada vacío | Construido |
| Seguir los compromisos del comité | Minutas y transcripciones de comité | Compromisos con doliente, fecha y fuente; los vencidos sin evidencia | Construido |
| Las cuatro cifras del presupuesto | Aprobado, contratos y órdenes, ejecución, proyección declarada | Disponible real, % ejecutado, % comprometido, sobrecosto de la proyección | Construido |
| Cruzar entregables de proveedor contra evidencia y facturación | Contratos, actas de recibo, facturación declarada | Entregables vencidos sin evidencia, aceptados sin documento, factura sin ningún entregable aceptado | **Construido con un límite probado** — la factura contra un entregable que no empezó no se detecta: haría falta monto por entregable. Ver evidencia, límite 1 |
| Detectar dependencias entre proyectos | Dependencias declaradas con el código del otro proyecto, y las fechas de cierre de todos | El cruce con la fecha vigente del otro proyecto y si fue confirmada o solo declarada | Construido |
| Reconciliar la replanificación contra lo autorizado | Línea base de solo agregar y cambios aprobados con impacto en tiempo | Días que se movió, días autorizados, días que ningún documento autoriza | Construido |
| Control documental y trazabilidad | El conjunto de archivos y `meta.documents_seen` con su hash | Qué releer, qué se conserva, y las citas que dejaron de resolver | **Parcial** — el hash solo existe en markdown; nada verifica que una cita siga resolviendo |
| Verificar la autoridad declarada del gerente | El acta de constitución | El hallazgo cuando falta, con su consecuencia | **Parcial** — es prosa, no campo |

## B · Lo que hace, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Detectar contradicciones entre documentos | Dos o más documentos que hablan del mismo campo | Campo en `ambiguous` con las dos fuentes y sus fechas; alerta sin umbral | Construido |
| Lecciones ancladas a hechos documentados | Criterio de éxito del acta y la historia documental del proyecto | Lecciones que nombran hecho, fecha y efecto | Construido |
| Impacto de un cambio en el resto del portafolio | El cambio propuesto y las dependencias declaradas | Proyectos alcanzados y sus gerentes | **Parcial** — en prosa |
| Health check de un proyecto contra evidencia | Toda la documentación del proyecto, sin ficha previa | Dictamen: qué se sostiene, qué no, qué no está dicho en ninguna parte | **Falta** — `/status-report` es estado de rutina, no auditoría |
| Reconstruir el historial: qué pasó en catorce meses | Los documentos ordenados por fecha | Línea de tiempo de decisiones, replanificaciones y desviación acumulada | **Falta** |
| Calibrar la declaración de cada gerente en el tiempo | Los snapshots de varias corridas | El patrón de la brecha por persona a lo largo del tiempo | **Falta**, y no puede ir primero: necesita historia |

Las tres filas que faltan son el argumento comercial de la capacidad.

**La calibración por gerente hay que tratarla con cuidado.** Es el subproducto natural de
guardar corridas, y en manos equivocadas es una herramienta de evaluación de desempeño. El
efecto de usarla así es predecible: nadie vuelve a declarar nada, y con eso desaparece la mitad
de la comparación. Se construye como insumo de conversación con el gerente, o no se construye.

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

El director de la PMO y sus analistas conservan la función completa. Y una distinción que no es
una función sino un límite: **el informe del agente es el insumo del comité, no el comité.** El
agente formula la decisión como pregunta cerrada con sus opciones; quién decide, con qué
criterio y asumiendo qué, es de la instancia que tiene la facultad.

Si una organización quitara al analista de PMO y dejara solo al agente, lo que se rompe primero,
en este orden:

1. **Nadie persigue lo que el informe pide.** El agente vuelve a reportar lo mismo, y se ignora.
2. **Nadie decide qué escala.** El agente sabe qué cruzó un umbral; no sabe qué vale la pena
   pelear esta semana.
3. **Nadie contesta en la sala.** La pregunta del patrocinador en el comité casi nunca es la que
   está en el informe.

---

## Lo que falta por construir, en orden

1. **El hash del lado del código.** Es la regla que controla el costo de todo el sistema y hoy
   vive en dos archivos markdown. Con dos etapas: hash de bytes para decidir si vale extraer,
   hash del texto extraído para decidir si vale releer.
2. **Verificación de citas.** Comparar el conjunto completo de archivos contra
   `meta.documents_seen` para detectar borrados y renombrados. Una cita que dejó de resolver es
   un hallazgo —`source_missing`—, no un hueco silencioso.
3. **El health check**, como comando propio y distinto del estado de rutina.
4. **El forense de un proyecto.**
5. **La calibración por gerente**, si se decide construirla, y al final.

## Decisiones abiertas propias de esta hoja

- **`autoridad` como campo** en vez de prosa.
- **Monto por entregable de proveedor.** Salió de la corrida sintética, no de una
  conversación: sin él, una factura contra un entregable que nunca empezó pasa
  desapercibida mientras haya otros aceptados.
- **Si la calibración por gerente se construye**, y con qué visibilidad.
- **Quién ve la brecha.** Resuelto en discusión: la brecha aparece como **evento** cuando un
  documento cambia, con una pregunta asociada — no como contador permanente visible al
  patrocinador. Es la misma información, y la diferencia decide si el gerente la recibe como
  señal de trabajo o como calificación.
