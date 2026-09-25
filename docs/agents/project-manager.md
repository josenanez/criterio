# Agente Project Manager

Extiende al **gerente de proyecto**: la persona que responde por un proyecto.

Marco general, definición de las clases y de las columnas: [README](README.md).

| | |
|---|---|
| **Instancia** | Una por proyecto |
| **Alcance** | Un proyecto. Profundidad, cadencia diaria o por reunión |
| **Escribe** | La ficha del proyecto — **excepto el estado declarado** |
| **Lee** | Su propia ficha y el estándar que publica la PMO |
| **Estado** | En construcción. El método existe; la superficie de comandos, no |

---

## El flujo

El agente no asiste a la reunión. Trabaja sobre el rastro que la reunión deja, **y produce el
rastro que necesita**: el que arma la agenda antes recibe la minuta después.

```
GERENTE DE PROYECTO  (clase C)                 AGENTE PM  (clases A y B)
──────────────────────────────────────────────────────────────────────────────────
                                          ┌──  lee lo que cambió en la carpeta
                                          │    mantiene el plan contra la evidencia
                                          │    calcula desviación y alertas
   ◄──── agenda de la reunión ◄───────────┘     ordena por lo que necesita a alguien

dirige la reunión
negocia, desbloquea, decide
   └─► transcripción o notas ────────────────►  redacta el acta
                                               extrae compromisos: quién, qué, cuándo
                                               marca los vencidos sin evidencia
                                               levanta los riesgos dichos al pasar

   ◄──── informe semanal ◄────────────────────  todo salvo una línea
declara el estado del proyecto
   └─► `declared` ───────────────────────────►  la mitad de la comparación

acepta o rechaza lo entregado
   └─► evidencia de aceptación ──────────────►  se cruza contra la facturación

compromete una fecha
   └─► línea base o compromiso ──────────────►  referencia del cálculo siguiente
```

---

## La restricción que define este agente

**El agente PM no escribe `declared`.** Es la sexta invariante del diseño, no una
recomendación: la persona declara, el agente le muestra contra qué. Si el agente declara, la
comparación compara al sistema consigo mismo.

---

## A · Lo que hace, y hoy consume tiempo de alguien

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Mantener el plan actualizado contra la evidencia | Documentos del proyecto y el plan vigente | La ficha al día; desviación contra la línea base original y la vigente | Construido |
| Llevar el RAID al día | Registro existente y las minutas | Riesgos, supuestos, incidencias y dependencias con doliente y fecha; los dichos y no registrados, marcados | Construido |
| Consolidar las cifras del proyecto | Aprobado, contratos y órdenes, ejecución, proyección | Las cuatro cifras y el disponible real | Construido |
| Preparar la solicitud de cambio | Lo que se quiere cambiar, la línea base vigente, la autoridad declarada | Borrador con impacto en alcance, tiempo y costo, y quién debe decidir | Construido |
| Mantener el expediente ordenado y trazable | La carpeta como esté | Cada dato con su ruta y su fecha; lo que no está, declarado | Construido |
| Seguir los entregables del proveedor | Contrato, actas de recibo, facturación declarada | Vencidos sin evidencia, aceptados sin documento, factura sin entrega | Construido |
| Ver si la replanificación se pasó de lo autorizado | Línea base de solo agregar y cambios aprobados | Días que se movió, días autorizados, días que nadie autorizó | Construido |
| **Extraer y seguir los compromisos de cada reunión** | Minuta o transcripción | Compromisos con doliente, fecha y fuente; vencidos sin evidencia; sus reprogramaciones | **Falta el comando.** El skill está completo; hoy solo se llega por `/raid-log` o por un barrido de portafolio, que es cadencia de PMO |
| **Armar el informe de avance semanal** | Ficha, alertas y lo que cambió desde la corrida anterior | El informe completo salvo el estado declarado | **Parcial** — `/status-report` existe con forma y cadencia de comité |
| **Armar la estructura de la reunión** | Alertas abiertas, compromisos vencidos, decisiones pendientes | Agenda con los puntos que necesitan a alguien, en orden | **Falta** |
| **Redactar el acta de la reunión** | Transcripción o notas | Acta con acuerdos, compromisos y decisiones, cada uno atribuido | **Falta** |

## B · Lo que hace, y hoy no se hace

| Función | Entra | Produce o mantiene | Estado |
|---|---|---|---|
| Revisar el acta de constitución y decir qué falta | El acta | Los campos ausentes con su consecuencia; sobre todo la autoridad del gerente | Construido |
| Borrador del cierre y de las lecciones | Criterio de éxito pactado y la historia documental | Entregado contra comprometido, desviación final, lecciones con hecho y fecha | Construido |
| Evaluar el efecto real de un cambio en el cronograma y en otros proyectos | El cambio y las dependencias declaradas | Hitos alcanzados, proyectos afectados y sus gerentes | **Parcial** |
| Preparar el escalamiento con la decisión formulada | El ítem que excede su autoridad | La decisión como pregunta cerrada, con opciones y consecuencia de no decidir | **Parcial** |
| **Detectar el compromiso reprogramado tres veces** | Historial de compromisos del mismo doliente sobre lo mismo | Un compromiso con su historial de reprogramaciones, señalado como bloqueo | **Falta en código.** El skill lo describe; `compute` solo marca vencidos |
| **Primer borrador del plan y de la WBS** | El acta y proyectos análogos del portafolio | Borrador de WBS y cronograma, con los supuestos declarados | **Falta** |

Tres veces reprogramado **no es un problema de seguimiento: es un bloqueo que nadie ha
nombrado.** Es información distinta de tres compromisos vencidos, y es la que le sirve al
gerente.

## C · Lo que el agente no hace

Lista de acciones que el agente no ejecuta. No es una evaluación de riesgo ni pretende ser
exhaustiva: **la responsabilidad de uso y ejecución es de la organización que lo despliega.**
Ver [README](README.md#c--lo-que-el-agente-no-hace).

| Función | Requiere | Qué le entrega al agente |
|---|---|---|
| Declarar el estado del proyecto | Que sea de una persona, por diseño — sexta invariante | La declaración: la mitad de la comparación. Sin ella el sistema no tiene señal |
| Dirigir la reunión | Información fuera de los documentos · autoridad | La minuta, que es el insumo principal de este agente |
| Negociar con proveedores y con otras áreas | Autoridad | El acuerdo, cuando queda escrito |
| Aceptar o rechazar un entregable | Autoridad | La evidencia de aceptación, que el agente cruza contra la facturación |
| Gestionar a las personas del equipo | Juicio sobre personas | El desbloqueo, que es lo que cierra un compromiso vencido |
| Leer la política del patrocinador y decidir qué se pelea | Información fuera de los documentos | La prioridad real, que decide qué se escala |
| Comprometer al proyecto en una fecha | Autoridad | La fecha, que se vuelve línea base o compromiso |
| Decidir la prioridad cuando dos cosas chocan | Autoridad · información fuera de los documentos | La decisión fechada |

---

## Lo que sigue siendo del gerente persona

Todas las semanas el gerente va a la reunión, la dirige, hace y recibe seguimiento, negocia,
acepta o rechaza lo entregado, sostiene a su equipo, lee la política de su patrocinador y
**declara el estado de su proyecto.**

Lo que cambia es que llega con la semana preparada: la agenda armada, los compromisos vencidos
con nombre y fecha, el plan al día contra la evidencia, el informe listo salvo el estado, y la
lista de lo que la evidencia no sostiene.

Si una organización quitara al gerente y dejara solo al agente, lo que se rompe primero:

1. **Nadie dirige la reunión**, y la reunión es donde se desbloquea lo que está trabado.
2. **Nadie declara**, y sin declaración no hay contra qué contrastar la evidencia: el hallazgo
   de más valor desaparece.
3. **La ficha se seca.** Su fuente principal es lo que la reunión produce, así que el agente se
   queda ciego exactamente en la función que lo justifica.

El tercero conviene tenerlo claro al hablar con un director: **este agente no es viable sin su
persona.** No por prudencia — por arquitectura.

---

## Lo que falta por construir, en orden

1. **El comando de compromisos.** Es la función central del agente y la única sin puerta propia.
2. **La estructura de la reunión.** Cierra el ciclo y es la de más apalancamiento.
3. **El informe semanal**, con cadencia y forma de proyecto, no de comité.
4. **El acta de la reunión.**
5. **En código:** el compromiso reprogramado.

## Decisiones abiertas propias de esta hoja

- **Un plugin con dos roles, o dos plugins.** Hoy el repo asume lo primero —
  `ROLES = ("pmo", "pm")` está en `check_config`— y no lo construye. Instalar como `pm` entrega
  once comandos de portafolio, y la mayoría no aplica a un proyecto.
- **Cómo bajan los estándares de la PMO.** `paths.standard` está declarado en la configuración y
  no lo lee ninguna línea de código. Con N instancias de agente PM, la versión del esquema y los
  umbrales se vuelven un problema de consistencia distribuida: barato si la carpeta del estándar
  es de solo lectura y versionada, caro si cada PM puede cambiar sus umbrales.
- **Dónde vive el registro de preguntas.** Una pregunta al gerente es el mismo objeto que un
  compromiso —quién, qué, cuándo— y necesita estado y vencimiento. Con una regla que decide si
  esto sobrevive a setenta proyectos: **la misma pregunta no se hace dos veces.** Si nadie
  contestó, la corrida siguiente reporta *"preguntada el 12, sin respuesta"*, que es un hallazgo,
  en vez de volver a preguntar.
