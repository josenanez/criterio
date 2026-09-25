# Agente PMO

Extiende a la **oficina de proyectos**: la función que responde por el conjunto de los
proyectos, no por uno.

Marco general, clases y códigos de riesgo: [README](README.md).

| | |
|---|---|
| **Instancia** | Una por organización |
| **Alcance** | Todos los proyectos. Barrido amplio, cadencia de comité |
| **Escribe** | Hallazgos. Estándar: umbrales, versión del esquema, convenciones |
| **No escribe** | La declaración de ningún gerente |
| **Lee** | Todas las fichas |
| **Estado** | Disponible. Clase A cerrada; la B a medias |

---

## A · Lo que hace, y hoy consume tiempo de alguien

| Función | Mecanismo | Estado |
|---|---|---|
| Consolidar el estado del portafolio | `/portfolio-scan`, `/portfolio-report` | Construido |
| Armar el material de comité y el informe de dirección | `/steering-pack` | Construido |
| Contrastar la declaración de cada gerente contra la evidencia | `declared_vs_evidence`, `totals.green_contradicted` | Construido |
| Verificar que exista acta, línea base y doliente | `/project-charter`, `has_baseline`, `fields_missing` | Construido |
| Seguir los compromisos del comité | `commitment-tracking`, `commitments_overdue` | Construido |
| Las cuatro cifras del presupuesto, por proyecto y consolidadas | `/budget-tracking` | Construido |
| Cruzar entregables de proveedor contra evidencia y contra facturación | `/vendor-tracking`, `vendors` | Construido |
| Detectar dependencias declaradas y si la contraparte se movió | `dependencies` en `compute` | Construido |
| Reconciliar la replanificación contra lo que autorizó el comité | `rebaseline_unauthorized` | Construido |
| Control documental y trazabilidad de cada dato a su fuente | `project-record` | **Parcial** — el hash solo existe en markdown, y nada verifica que una cita siga resolviendo |
| Verificar la autoridad declarada del gerente | `governance-artifacts` | **Parcial** — es prosa, no campo |

## B · Lo que hace porque hoy no se hace

| Función | Mecanismo | Estado |
|---|---|---|
| Detectar contradicciones entre documentos | `ambiguous` + alerta sin umbral | Construido |
| Borrador del paquete de decisión: opciones y consecuencias | `/steering-pack` | Construido |
| Lecciones aprendidas ancladas a hechos documentados | `/project-closure` | Construido |
| Análisis de impacto de un cambio en el resto del portafolio | `/change-control` paso 3 | **Parcial** — en prosa |
| Health check de un proyecto contra evidencia | — | **Falta.** `/status-report` es estado de rutina, no auditoría |
| Reconstruir el historial de un proyecto: qué pasó en catorce meses | — | **Falta.** Nada recorre la línea de tiempo documental |
| Calibrar la declaración de cada gerente a lo largo del tiempo | — | **Falta**, y no puede ir primero: necesita historia de corridas |

Las tres filas que faltan son el argumento comercial de la capacidad. Ninguna PMO las hace
hoy, y no por descuido: cada una cuesta días de trabajo por proyecto.

**La calibración por gerente hay que tratarla con cuidado.** Es técnicamente el subproducto
natural de guardar corridas —declaración contra evidencia, repetido en el tiempo, da un
patrón por persona— y en manos equivocadas es una herramienta de evaluación de desempeño. Eso
la pondría en C por **PER**, y el efecto sería que nadie vuelve a declarar nada. Se construye
como insumo de conversación con el gerente, o no se construye.

## C · Lo que no hace

| Función | Riesgo | Por qué |
|---|---|---|
| Priorizar y admitir la demanda | **AUT** | Es asignación de capital y de política interna |
| Aprobar línea base, cambios y excepciones | **AUT** | La autoridad no se delega a algo que no puede responder |
| Decidir detener o matar un proyecto | **AUT** + **INF** | |
| Asignar recursos y capacidad | **PER** + **INF** | Las horas reales no están en la carpeta |
| Mediar conflictos entre áreas y escalar políticamente | **INF** | La mitad de eso se negocia fuera de todo documento |
| Evaluar el desempeño de un gerente de proyecto | **PER** | Y si se usa así, nadie vuelve a declarar nada |
| Responder ante auditoría, riesgo operativo y el regulador | **AUT** | Consecuencia legal |
| Acompañar y formar gerentes de proyecto | **PER** | |

---

## Lo que sigue siendo de la PMO persona

El director de la PMO y sus analistas conservan la función completa: **la admisión y
priorización de la demanda, la autoridad de aprobación, la asignación de capacidad, la
mediación entre áreas, la relación con auditoría y con el regulador, y el desarrollo de los
gerentes de proyecto.**

Y algo que no aparece en la tabla de C porque no es una función sino una distinción:
**el informe del agente es el insumo del comité, no el comité.** El agente formula la
decisión como pregunta cerrada con sus opciones; quién decide, con qué criterio y asumiendo
qué, es de la instancia que tiene la facultad.

Si una organización quitara al analista de PMO y dejara solo al agente, lo que se rompe
primero, en este orden:

1. **Nadie persigue lo que el informe pide.** El agente vuelve a reportar lo mismo la semana
   siguiente, y en un mes se ignora.
2. **Nadie decide qué escala.** El agente sabe qué cruzó un umbral; no sabe qué vale la pena
   pelear esta semana.
3. **Nadie contesta en la sala.** La pregunta del patrocinador en el comité casi nunca es la
   que está en el informe.

---

## Lo que falta por construir, en orden

1. **El hash del lado del código.** Es la regla que controla el costo de todo el sistema y hoy
   vive en dos archivos markdown. Con dos etapas: hash de bytes para decidir si vale extraer,
   hash del texto extraído para decidir si vale releer.
2. **Verificación de citas.** Comparar el conjunto completo de archivos contra
   `meta.documents_seen` para detectar borrados y renombrados. Una cita que dejó de resolver
   es un hallazgo — `source_missing` —, no un hueco silencioso.
3. **El health check**, como comando propio y distinto del estado de rutina.
4. **El forense de un proyecto.**
5. **La calibración por gerente**, si se decide construirla, y al final: se gana con el tiempo.

## Decisiones abiertas propias de esta hoja

- **`autoridad` como campo** en vez de prosa, para que el control de cambios sepa si algo
  excede la facultad sin releer el acta.
- **Si la calibración por gerente se construye**, y con qué visibilidad.
- **Quién ve la brecha.** Resuelto en discusión, pendiente de escribir: la brecha aparece
  como **evento** cuando un documento cambia, con una pregunta asociada — no como contador
  permanente visible al patrocinador. Es la misma información, y la diferencia decide si el
  gerente la recibe como señal de trabajo o como calificación.
