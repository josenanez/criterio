# /criterio-portfolio:raid-log portafolio

**Leí:** las 13 fichas del portafolio (PRY-199 a PRY-211) y sus 13 informes de avance (2026-10-01 a 2026-10-18). También leí 13 minutas de comité (PRY-199, 201 ×6, 202, 206, 207, 208, 209, 210), las notas de la reunión de PRY-201 del 2026-10-18 y la solicitud de cambio CC-01 de PRY-210. Los PDF y el .docx los leí por su texto en el caché de estado, no desde el original.
**No pude leer:** nada quedó sin leer. No revisé actas de constitución, contratos ni facturas más allá de lo que ya está en las fichas. Este registro sale de lo que los informes y las reuniones dicen de riesgos.

Términos vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-18). Ya estaban registrados, así que no hubo que aceptarlos otra vez.

## RAID — portafolio al 2026-10-18
12 riesgos · 0 supuestos · 13 incidencias · 10 dependencias (después de reclasificar). Como llegaron a las fichas eran 22 riesgos, 13 incidencias y 0 dependencias.
35 de 35 sin doliente · 35 de 35 sin fecha · 22 riesgos originales sin probabilidad ni impacto · 1 sin movimiento (PRY-206) · 1 no registrado formalmente

Tres cosas antes de la tabla:

- **Ningún ítem tiene id, doliente ni fecha en el documento de origen.** Los ids de abajo (`PRY-200/R1`) son provisionales: los puse yo para poder referirme a cada ítem y no están en las fichas. Doliente, fecha, probabilidad e impacto aparecen como `n/d` (no declarado). No los relleno.
- **Reclasifiqué 10 riesgos como dependencias**, por la prueba rápida (dependen de alguien fuera del proyecto). Es una propuesta y no modifiqué las fichas. Más abajo explico cada caso.
- **«Sin movimiento» no se puede medir bien.** Cada ítem aparece una sola vez, con la fecha del informe que lo menciona. No hay un informe anterior para ver si se movió, así que solo puedo decir la antigüedad de esa última mención.

### Necesitan decisión ahora
| Id | Tipo | Qué | Doliente | Desde | Por qué sube |
|---|---|---|---|---|---|
| PRY-200/D1, PRY-201/D2, PRY-202/D1, PRY-207/D1, PRY-209/D1 | Dependencia (estaba como riesgo) | Dependencia del «proveedor del core cooperativo» | n/d | 2026-10-06 (PRY-207) | Afecta a 5 proyectos a la vez, y ninguno nombra de qué proyecto o contrato depende. PRY-202 (Core cooperativo) es el candidato evidente, pero ningún documento lo dice. Su fin en línea base es 2026-08-10, hoy lleva 69 días vencido con 67%, y la línea base nunca se movió (0 cambios). La decisión: quién es la contraparte y qué fecha confirma. |
| PRY-201/D1, PRY-201/D2, PRY-201/R1 | Dependencia · dependencia · riesgo | El proveedor no confirmó la fecha de la última entrega; depende del core; podría no llegar con el equipo completo a la siguiente fase | n/d | 2026-10-17 | PRY-201 se declara en verde (91%), pero su fin de línea base (2026-10-04) ya pasó. El hito «Integración con el core cooperativo» (2026-10-04) sigue pendiente, 14 días después. Los tres ítems hablan del mismo proveedor y ninguno tiene doliente. La revisión con el proveedor quedó para el 2026-10-28 (Óscar Ramírez, notas del 2026-10-18). |
| PRY-199/D1, PRY-208/D1, PRY-210/D1 (y las incidencias PRY-202/I2, PRY-203/I2, PRY-211/I2) | Dependencia · incidencia | Aprobación o ajuste del reglamento por el Consejo de Administración | n/d | 2026-10-11 (PRY-203, PRY-211) | Toca a 6 proyectos con el mismo texto, y en 3 ya es incidencia («pidió ajustar el reglamento antes del piloto»). Un séptimo, PRY-201, lo menciona en su informe del 2026-10-17 y no lo registró. Los informes no dicen que sea el mismo reglamento, así que hay que confirmarlo. Se decide en un solo lugar, no en seis fichas. |

### Detectados en reuniones, no registrados
| Qué | Tipo | Dicho en | Fecha |
|---|---|---|---|
| «Se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, nadie lo anotó como riesgo» | Riesgo (PRY-201/R1) | PRY-201, notas de reunión | 2026-10-18 |

De las 13 minutas y las notas leídas, esta es la única mención de un riesgo. Las 13 minutas solo traen listas de compromisos. No encontré en ellas riesgos, supuestos ni dependencias dichos al pasar, y no inventé ninguno. Las notas no dicen quién lo comentó. Está en la ficha de PRY-201 con la marca de origen, pero sin doliente.

Fuera de reuniones: el informe de PRY-201 del 2026-10-17 dice en «Lo que pasó» que el Consejo de Administración pidió ajustar el reglamento antes del piloto. La ficha no lo tiene como incidencia (en PRY-202, 203 y 211 sí). Es el mismo hecho, sin registrar.

### Sin doliente o sin fecha
| Id | Tipo | Qué | Qué falta |
|---|---|---|---|
| Los 35 ítems de «Registro completo» | R, I, D | Todos | Doliente y fecha en los 35 |
| Los 22 riesgos y dependencias | R, D | Todos | Probabilidad e impacto (no hay escala definida en la configuración; si se valoran, alta/media/baja) |
| PRY-203/I1, PRY-207/I1, PRY-208/I1, PRY-209/I1, PRY-211/I1 | I | «Se reprogramó la salida por el cierre contable de fin de mes» | La nueva fecha: ninguno de los cinco informes la da |

Observación: las mismas frases aparecen en varios proyectos con gerentes distintos.
- «Concentración del conocimiento en una sola persona» está en 6.
- «Cambio normativo del supervisor» está en 5.
- «Dependencia del proveedor del core» está en 5.
- El reglamento del Consejo está en 6.
- El cierre contable está en 5.

Ninguna lleva un detalle propio del proyecto (a quién, desde cuándo, con qué efecto). No sé si son riesgos reales con redacción común o texto de plantilla. El gerente de cada proyecto puede decirlo.

### Dependencias en riesgo
| Id | Depende de | Confirmada | Qué pasó |
|---|---|---|---|
| PRY-200/D1, PRY-201/D2, PRY-202/D1, PRY-207/D1, PRY-209/D1 | «Proveedor del core cooperativo»; proyecto de código no nombrado (candidato: PRY-202) | No (declarada, no acordada) | Si es PRY-202: su fin vigente es 2026-08-10, sin replanificación registrada, 67% y amarillo, con una prueba de carga que no alcanzó el umbral y se repite (informe 2026-10-14). Es una inferencia mía: ningún documento une las dos cosas. |
| PRY-201/D1, PRY-204/D1 | «El proveedor» de la última entrega; sin nombre en el informe | No | PRY-201: hito de integración pendiente y vencido 14 días (ver arriba). PRY-204: el informe dice que el proveedor no confirmó fecha, y no hay más en esa mención. |
| PRY-199/D1, PRY-208/D1, PRY-210/D1 | Consejo de Administración (órgano de gobierno, no proyecto) | No | En PRY-202, 203 y 211 ya pidió ajustes al reglamento. |

El cruce que pide el método (una dependencia que apunta a un proyecto que movió su fecha) no se puede hacer limpio. Ninguna dependencia lleva código de proyecto, y ningún proyecto tiene replanificaciones registradas: hay 0 cambios en las 13 fichas, salvo CC-01 de PRY-210, que está pendiente de presentarse al comité y no es una dependencia. Falta pedirle el código a cada gerente.

### Registro completo
Tipo: R riesgo · I incidencia · D dependencia (propuesta). `n/d` = no declarado en el documento. «Último movimiento» es la fecha del informe o de las notas que lo mencionan, o la fecha de «desde» en las incidencias. Fuente: documento en la carpeta del proyecto.

| Id | Tipo | Qué | Prob. · Impacto | Doliente | Fecha | Último movimiento | Fuente |
|---|---|---|---|---|---|---|---|
| PRY-199/D1 | D ← registrado como riesgo | Aprobación del reglamento por el Consejo de Administración | n/d · n/d | n/d | n/d | 2026-10-16 | 2026-10-16-informe-avance |
| PRY-200/R1 | R | Concentración del conocimiento en una sola persona | n/d · n/d | n/d | n/d | 2026-10-13 | 2026-10-13-informe-avance |
| PRY-200/D1 | D ← registrado como riesgo | Dependencia del proveedor del core cooperativo | n/d · n/d | n/d | n/d | 2026-10-13 | 2026-10-13-informe-avance |
| PRY-201/D1 | D ← registrado como riesgo | El proveedor no ha confirmado la fecha de la última entrega | n/d · n/d | n/d | n/d | 2026-10-17 | 2026-10-17-informe-avance |
| PRY-201/D2 | D ← registrado como riesgo | Dependencia del proveedor del core cooperativo | n/d · n/d | n/d | n/d | 2026-10-17 | 2026-10-17-informe-avance |
| PRY-201/R1 | R (no registrado formalmente) | El proveedor podría no llegar con el equipo completo para la siguiente fase | n/d · n/d | n/d | n/d | 2026-10-18 | 2026-10-18-notas-reunion |
| PRY-202/D1 | D ← registrado como riesgo | Dependencia del proveedor del core cooperativo | n/d · n/d | n/d | n/d | 2026-10-14 | 2026-10-14-informe-avance |
| PRY-202/R1 | R | Cambio normativo del supervisor que puede mover el alcance | n/d · n/d | n/d | n/d | 2026-10-14 | 2026-10-14-informe-avance |
| PRY-202/I1 | I | La prueba de carga no alcanzó el umbral pactado y se repite | no aplica | n/d | n/d | 2026-10-14 | 2026-10-14-informe-avance |
| PRY-202/I2 | I | El Consejo de Administración pidió ajustar el reglamento antes del piloto | no aplica | n/d | n/d | 2026-10-14 | 2026-10-14-informe-avance |
| PRY-203/R1 | R | Cambio normativo del supervisor que puede mover el alcance | n/d · n/d | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-203/I1 | I | Se reprogramó la salida por el cierre contable de fin de mes (el informe no da la nueva fecha) | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-203/I2 | I | El Consejo de Administración pidió ajustar el reglamento antes del piloto | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-204/D1 | D ← registrado como riesgo | El proveedor no ha confirmado la fecha de la última entrega | n/d · n/d | n/d | n/d | 2026-10-13 | 2026-10-13-informe-avance |
| PRY-204/R1 | R | Concentración del conocimiento en una sola persona | n/d · n/d | n/d | n/d | 2026-10-13 | 2026-10-13-informe-avance |
| PRY-205/R1 | R | Cambio normativo del supervisor que puede mover el alcance | n/d · n/d | n/d | n/d | 2026-10-06 | 2026-10-06-informe-avance |
| PRY-205/R2 | R | Concentración del conocimiento en una sola persona | n/d · n/d | n/d | n/d | 2026-10-06 | 2026-10-06-informe-avance |
| PRY-206/R1 | R | Cambio normativo del supervisor que puede mover el alcance | n/d · n/d | n/d | n/d | 2026-10-01 (17 días: pasa el umbral de 15) | 2026-10-01-informe-avance |
| PRY-207/D1 | D ← registrado como riesgo | Dependencia del proveedor del core cooperativo | n/d · n/d | n/d | n/d | 2026-10-06 | 2026-10-06-informe-avance |
| PRY-207/I1 | I | Se reprogramó la salida por el cierre contable de fin de mes (el informe no da la nueva fecha) | no aplica | n/d | n/d | 2026-10-06 | 2026-10-06-informe-avance |
| PRY-207/I2 | I | El equipo perdió dos semanas por rotación de un desarrollador clave | no aplica | n/d | n/d | 2026-10-06 | 2026-10-06-informe-avance |
| PRY-208/D1 | D ← registrado como riesgo | Aprobación del reglamento por el Consejo de Administración | n/d · n/d | n/d | n/d | 2026-10-18 | 2026-10-18-informe-avance |
| PRY-208/R1 | R | Concentración del conocimiento en una sola persona | n/d · n/d | n/d | n/d | 2026-10-18 | 2026-10-18-informe-avance |
| PRY-208/I1 | I | Se reprogramó la salida por el cierre contable de fin de mes (el informe no da fecha nueva) | no aplica | n/d | n/d | 2026-10-18 | 2026-10-18-informe-avance |
| PRY-209/R1 | R | Concentración del conocimiento en una sola persona | n/d · n/d | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-209/D1 | D ← registrado como riesgo | Dependencia del proveedor del core cooperativo | n/d · n/d | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-209/I1 | I | Se reprogramó la salida por el cierre contable de fin de mes (el informe no da la nueva fecha) | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-209/I2 | I | La prueba de carga no alcanzó el umbral pactado y se repite | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-210/D1 | D ← registrado como riesgo | Aprobación del reglamento por el Consejo de Administración | n/d · n/d | n/d | n/d | 2026-10-17 | 2026-10-17-informe-avance |
| PRY-210/R1 | R | Cambio normativo del supervisor que puede mover el alcance | n/d · n/d | n/d | n/d | 2026-10-17 | 2026-10-17-informe-avance |
| PRY-210/I1 | I | Se levantó un hallazgo de seguridad en la revisión de arquitectura | no aplica | n/d | n/d | 2026-10-17 | 2026-10-17-informe-avance |
| PRY-211/R1 | R | Concentración del conocimiento en una sola persona | n/d · n/d | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-211/I1 | I | Se reprogramó la salida por el cierre contable de fin de mes (el informe no da la nueva fecha) | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-211/I2 | I | El Consejo de Administración pidió ajustar el reglamento antes del piloto | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |
| PRY-211/I3 | I | La prueba de carga no alcanzó el umbral pactado y se repite | no aplica | n/d | n/d | 2026-10-11 | 2026-10-11-informe-avance |

**Por qué reclasifiqué.**
- «Dependencia del proveedor del core» y «El proveedor no ha confirmado la fecha» dependen de un tercero que el proyecto no controla.
- «Aprobación del reglamento por el Consejo» depende de un órgano fuera del proyecto.
- Esas tres se gestionan distinto que un riesgo: se coordinan y se confirman con la contraparte, no se mitigan.
- Dejé como incidencias lo que ya ocurrió (prueba de carga, reprogramación, rotación, hallazgo de seguridad, ajuste del reglamento) y como riesgos lo que aún puede ocurrir.
- No encontré supuestos declarados en ningún documento y no infiero ninguno.

**Lo que no sé.**
- Si los riesgos repetidos entre proyectos son reales.
- Quién es la contraparte del core.
- Si el reglamento del Consejo es uno solo.
- Si siguen abiertos los riesgos de los informes más viejos (PRY-206, 2026-10-01; PRY-205 y PRY-207, 2026-10-06), porque no hay un informe posterior.

## Después
Los tres bloques de «Necesitan decisión ahora» cumplen el criterio de escalamiento: afectan a otros proyectos del portafolio. El comité de la configuración es el 2026-10-25. Pueden subir con la decisión ya formulada:
- Confirmar contraparte y fecha del core.
- Fijar la fecha de decisión del Consejo sobre el reglamento.
- Aclarar el estado real de PRY-201 con el proveedor.

Propuesta de doliente (no asignada): para riesgos e incidencias internas de cada proyecto, quien firma su informe.
- PRY-199 y 203: Andrés Lozano
- PRY-200: Gustavo Neira
- PRY-201: Natalia Ospina
- PRY-202: Diana Molina
- PRY-204 y 205: Javier Hoyos
- PRY-206: Elena Duarte
- PRY-207: Beatriz Cuéllar
- PRY-208: Felipe Arango
- PRY-209 y 210: Liliana Torres
- PRY-211: Camilo Beltrán

Las dependencias del core y del reglamento no son de un solo gerente. Quién las lleva lo decide el comité. Nadie respondió preguntas en esta sesión, así que tomé la respuesta sugerida: proponer, no asignar, y no modificar las fichas.

---
La salida completa quedó en `estado/corridas/salida-raid-log.md`. La corrida quedó registrada como `2026-10-18-raid-log-1`, con 141 segundos medidos sobre 13 proyectos.