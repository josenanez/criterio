# Agente Project Manager

Extiende al **gerente de proyecto**: la persona que responde por un proyecto.

Marco general, clases y códigos de riesgo: [README](README.md).

| | |
|---|---|
| **Instancia** | Una por proyecto |
| **Alcance** | Un proyecto. Profundidad, cadencia diaria o por reunión |
| **Escribe** | La ficha del proyecto — **excepto el estado declarado** |
| **Lee** | Su propia ficha y el estándar que publica la PMO |
| **Estado** | En construcción. El método existe; la superficie de comandos, no |

---

## La restricción que define este agente

**El agente PM no escribe `declared`.**

No es una recomendación de la documentación: es una restricción del camino de escritura. Si el
agente declara el estado, la comparación entre declaración y evidencia compara al sistema
consigo mismo, y todo el diseño se vuelve un generador de informes bonitos.

**La persona declara; el agente le muestra contra qué.**

Es la única fila marcada **SEÑ** en las tres hojas.

---

## El ciclo

El agente no asiste a la reunión. Trabaja sobre el rastro que la reunión deja — y produce el
rastro que necesita:

```
agenda ──► reunión (persona) ──► minuta ──► ficha ──► alertas ──► informe ──► agenda
```

El agente que arma la estructura de la reunión antes, recibe la minuta que necesita después.
**Fabrica su propio insumo**, y eso convierte la dependencia que parecía bloqueante —*si no
hay minuta, el agente queda ciego en su función central*— en una función del propio agente.

---

## A · Lo que hace, y hoy consume tiempo de alguien

| Función | Mecanismo | Estado |
|---|---|---|
| Mantener el plan actualizado contra la evidencia | `project-record`, `baseline-variance` | Construido |
| Llevar el RAID al día, incluidos los riesgos dichos al pasar | `/raid-log` | Construido |
| Consolidar las cuatro cifras del proyecto | `/budget-tracking` | Construido |
| Preparar la solicitud de cambio con sus tres impactos | `/change-control` | Construido |
| Mantener el expediente ordenado y trazable | `project-record` | Construido |
| Seguir los entregables del proveedor contra evidencia de recibo | `/vendor-tracking` | Construido |
| Ver si la replanificación se pasó de lo autorizado | `rebaseline_unauthorized` | Construido |
| **Extraer y seguir los compromisos de cada reunión** | `commitment-tracking` | **Falta el comando.** El skill está completo; hoy solo se llega por `/raid-log` o por un barrido de portafolio, que es cadencia de PMO |
| **Armar el informe de avance semanal del proyecto** | `/status-report` | **Parcial** — existe con forma y cadencia de comité |
| **Armar la estructura de la reunión** | — | **Falta** |
| **Redactar el acta de la reunión** | — | **Falta** |

## B · Lo que hace porque hoy no se hace

| Función | Mecanismo | Estado |
|---|---|---|
| Revisar el acta de constitución y decir qué falta | `/project-charter` | Construido |
| Borrador del cierre y de las lecciones contra el criterio pactado | `/project-closure` | Construido |
| Evaluar el efecto real de un cambio en el cronograma y en otros proyectos | `/change-control` paso 3 | **Parcial** |
| Preparar el escalamiento con la decisión formulada | `raid-taxonomy`, `/steering-pack` | **Parcial** |
| **Detectar el compromiso reprogramado tres veces** | — | **Falta en código.** El skill lo describe; `compute` solo marca vencidos |
| **Primer borrador del plan y de la WBS desde proyectos análogos** | — | **Falta** |

El compromiso reprogramado merece su nota: tres veces reprogramado **no es un problema de
seguimiento, es un bloqueo que nadie ha nombrado.** Es información distinta de tres
compromisos vencidos, y es la que le sirve al gerente.

## C · Lo que no hace

| Función | Riesgo | Por qué |
|---|---|---|
| **Declarar el estado del proyecto** | **SEÑ** | Si el agente declara, el sistema pierde su única señal |
| Dirigir la reunión | **INF** + **AUT** | |
| Negociar con proveedores y con otras áreas | **AUT** | |
| Aceptar un entregable | **AUT** | El agente lee que se entregó; no sabe si sirve |
| Gestionar a las personas del equipo: asignar, desbloquear, sostener | **PER** | |
| Leer la política del patrocinador y decidir qué se pelea | **INF** | |
| Comprometer al proyecto en una fecha | **AUT** | |
| Decidir la prioridad cuando dos cosas chocan | **AUT** + **INF** | |

---

## Lo que sigue siendo del gerente persona

Todas las semanas el gerente **va a la reunión, la dirige, hace y recibe seguimiento,
negocia, acepta o rechaza lo entregado, sostiene a su equipo, lee la política de su
patrocinador y declara el estado de su proyecto.**

Lo que cambia es que llega con la semana preparada: la agenda armada, los compromisos
vencidos con nombre y fecha, el plan al día contra la evidencia, el informe listo salvo el
estado, y la lista de lo que la evidencia no sostiene.

Si una organización quitara al gerente y dejara solo al agente, lo que se rompe primero:

1. **Nadie dirige la reunión**, y la reunión es donde se desbloquea lo que está trabado.
2. **Nadie declara**, y sin declaración no hay nada contra qué contrastar la evidencia: el
   hallazgo de más valor del sistema desaparece.
3. **La ficha se seca.** Su fuente principal es lo que la reunión produce. El agente se queda
   ciego exactamente en la función que lo justifica.

El tercero es el que conviene tener claro al hablar con un director: **este agente no es
viable sin su persona.** No por prudencia — por arquitectura.

---

## Lo que falta por construir, en orden

1. **El comando de compromisos.** Es la función central del agente y es la única que hoy no
   tiene puerta propia.
2. **La estructura de la reunión.** Cierra el ciclo y es la de más apalancamiento.
3. **El informe semanal del proyecto**, con cadencia y forma de proyecto, no de comité.
4. **El acta de la reunión**, a partir de la transcripción o de las notas.
5. **En código:** el compromiso reprogramado.

## Decisiones abiertas propias de esta hoja

- **Un plugin con dos roles, o dos plugins.** Hoy el repo asume lo primero —
  `ROLES = ("pmo", "pm")` está en `check_config` — y no lo construye. Instalar como `pm`
  entrega once comandos de portafolio, y la mayoría no aplica a un proyecto.
- **Cómo bajan los estándares de la PMO.** `paths.standard` está declarado en la
  configuración y no lo lee ninguna línea de código. Con N instancias de agente PM, la
  versión del esquema y los umbrales se vuelven un problema de consistencia distribuida:
  barato si la carpeta del estándar es de solo lectura y versionada, caro si cada PM puede
  cambiar sus umbrales.
- **Dónde vive el registro de preguntas.** Una pregunta al gerente es el mismo objeto que un
  compromiso — quién, qué, cuándo — y necesita estado y vencimiento. Con una regla que decide
  si esto sobrevive a setenta proyectos: **la misma pregunta no se hace dos veces.** Si nadie
  contestó, la corrida siguiente reporta *"preguntada el 12, sin respuesta"*, que es un
  hallazgo, en vez de volver a preguntar.
