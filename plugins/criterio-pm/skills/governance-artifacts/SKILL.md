---
name: governance-artifacts
description: "Los artefactos de gobierno de un proyecto: acta de constitución, comité, control de cambios y cierre. Qué contiene cada uno, quién decide qué, y qué falta cuando falta. Úsalo al revisar o redactar un acta, al preparar material de comité, al evaluar una solicitud de cambio, al cerrar un proyecto, o cuando no esté claro quién aprueba algo. Project charter, steering committee, change control, closure."
---
<!-- COPIA · la fuente es plugins/criterio-pmo/skills/governance-artifacts/. La escribe scripts/sincronizar.py y no se edita aquí. -->

# Artefactos de gobierno

## El hilo común

Los cuatro artefactos responden la misma pregunta en momentos distintos: **quién decide qué, y con qué información.**

Un proyecto sin gobierno no es uno sin documentos: es uno donde nadie sabe quién autoriza gastar más, ampliar el alcance o darlo por terminado. Eso se detecta leyendo los documentos que existen y preguntando quién firmó.

## Acta de constitución

Lo que la hace útil, y casi nunca está completo:

- **Objetivo del negocio**, no la descripción de la solución. "Reducir el tiempo de originación de 5 días a 1" es objetivo; "implementar el motor de decisión" es solución.
- **Alcance, y exclusiones explícitas.** Lo que el proyecto declara que NO hace vale tanto como lo que hace, y es lo que evita la discusión del mes ocho.
- **Patrocinador con nombre.** Un área no patrocina; una persona sí.
- **Autoridad del gerente**: hasta qué monto y qué cambio de alcance puede decidir sin subir a comité. Este es el campo que falta en nueve de cada diez actas, y el que hace que todo termine en el comité.
- **Supuestos y restricciones** declarados de entrada.
- **Criterio de éxito medible**, y quién lo mide.

Cuando falte alguno, se reporta como vacío, no se redacta por el proyecto.

## Comité

El comité decide lo que excede la autoridad del gerente. Su material no es un informe de avance: es un **paquete de decisiones**.

Cada punto que sube lleva cuatro cosas: la decisión formulada como pregunta cerrada, las opciones con su implicación, lo que se recomienda y por qué, y qué pasa si no se decide hoy.

Un punto de comité sin decisión asociada es información, y la información va en el anexo, no en la agenda.

Lo que también sube, sin ser decisión: las contradicciones abiertas del portafolio, los riesgos escalados sin doliente, y las dependencias entre proyectos que ninguno de los dos gerentes puede resolver solo.

## Control de cambios

Un cambio se evalúa siempre en las tres dimensiones, aunque parezca tocar una sola:

- **Alcance** — qué entra, qué sale, qué se aplaza.
- **Tiempo** — efecto en hitos y en fecha de cierre.
- **Costo** — efecto en aprobado, comprometido y proyección.

Un cambio que declara impacto en una sola dimensión casi siempre está mal evaluado. Ampliar alcance sin mover fecha ni presupuesto significa que alguien va a absorberlo en calidad o en horas no pagadas.

Todo cambio aprobado que mueva fechas **crea una línea base nueva**, con su motivo. No sobrescribe la anterior. Ver `baseline-variance`.

Y todo cambio lleva quién decidió y con qué autoridad. Un cambio aprobado por quien no tenía la facultad es un hallazgo.

## Cierre

Un proyecto no se cierra porque se acabó el presupuesto o porque el equipo se fue. Se cierra cuando alguien declara que terminó, contra el criterio de éxito que se pactó al inicio.

El cierre responde: qué se entregó contra lo comprometido, qué quedó fuera y con acuerdo de quién, qué desviación final hubo contra la línea base original, qué riesgos se materializaron y cuáles no, y qué queda abierto y a cargo de quién.

**Lecciones aprendidas:** solo sirven las que se pueden sustentar en algo que pasó y quedó documentado. Una lección genérica —"mejorar la comunicación"— no es una lección, es un lugar común. Una lección útil nombra el hecho, la fecha y el efecto: *"el ambiente de pruebas se pidió en abril y estuvo en julio; los tres meses de espera están en el atraso del hito 4"*.

## Proyectos sin gobierno

El caso frecuente: no hay acta, no hay comité definido, nadie sabe quién aprueba.

Eso se reporta como el hallazgo que es, con su consecuencia concreta —"no hay a quién escalar el riesgo R-03"—, y no se resuelve inventando una estructura. Proponerla sí: es una de las cosas que la PMO puede ofrecer con el diagnóstico en la mano.
