# /criterio-portfolio:raid-log portafolio

La corrida quedó registrada como `2026-10-15-raid-log-1`. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a registrar. No modifiqué ninguna ficha. Este es el registro, igual que en `estado/corridas/salida-raid-log.md`.

---

**Sale de:** las 13 fichas de `estado/records/` (PRY-199 a PRY-211, cortes entre 2026-09-23 y 2026-10-15), las notas de reunión de PRY-203 del 2026-10-15 (`2026-10-15-notas-reunion.txt`) y los contratos y cronogramas que las fichas ya citan. Busqué frases de riesgo en todos los `.md` y `.txt` de la carpeta. Los `.docx`, `.pdf` y `.xlsx` no los releí: uso lo que la ficha ya extrajo. Escala de valoración: la organización no definió una y las fichas no traen probabilidad ni impacto. No inventé ninguna; van como «sin valorar».

## RAID — portafolio al 2026-10-15
7 riesgos · 0 supuestos · 19 incidencias · 13 dependencias (ya reclasificados, ver abajo)
38 de 38 ítems registrados sin doliente · 38 de 38 sin fecha · 5 no registrados formalmente (1 dicho en una reunión, 4 salen de contratos) · sin movimiento: no se puede medir

Los ids (`199-D1`, `203-N1`…) son etiquetas de trabajo de este documento: el registro no trae ids. D = dependencia, R = riesgo, I = incidencia, N = no registrado.

**Lo que más pesa:** ninguna ficha tiene un solo supuesto, ninguna dependencia lleva el código del proyecto del que depende, y ningún ítem tiene doliente. El cruce de dependencias entre proyectos no se puede hacer con lo registrado. Abajo va lo que se puede inferir, marcado como inferencia.

### Necesitan decisión ahora
| Id | Tipo | Qué | Doliente | Desde | Por qué sube |
|---|---|---|---|---|---|
| 201-D1, 203-D1, 204-D1, 209-D1 | Dependencia | «Dependencia del proveedor del core cooperativo», declarada por cuatro proyectos | Sin doliente | Informes del 10-03 al 10-15; fecha de origen no declarada | Afecta a varios proyectos a la vez. PRY-202 *Core cooperativo* es el candidato obvio, pero ninguna ficha lo dice (inferencia). Su hito «Integración con el core cooperativo» vencía el 2026-10-12 y sigue pendiente sin evidencia (3 días) |
| 199-D2, 205-D1, 206-D1, 208-D1, 210-D1 y las incidencias 202-I1, 204-I2, 205-I2, 207-I1 | Dependencia / Incidencia | «Aprobación del reglamento por el Consejo de Administración» y «el Consejo pidió ajustar el reglamento antes del piloto» | Sin doliente (el decisor es externo a los proyectos) | Informes del 09-23 al 10-14 | El doliente está fuera de los proyectos y no hay respuesta registrada. Si es el mismo reglamento, una sola decisión destraba nueve ítems; las fichas no lo confirman. Pilotos cercanos: PRY-210 el 2026-11-05 (21 días) y PRY-208 el 2026-11-24 (40 días) |
| 211-R1, 211-I1, 211-N1 | Riesgo / Incidencia / No registrado | Proyecto en rojo. La concentración de conocimiento en una persona ya tuvo efecto: el equipo perdió dos semanas por la rotación de un desarrollador clave. CT-884 tiene sus 4 entregables en `pending`; 3 ya vencidos (247, 128 y 8 días) | Sin doliente | Informe del 2026-10-15 | Es el único rojo con incidencia abierta y contrato sin ninguna entrega registrada. Hay una factura del 2026-09-26 en la carpeta; su contenido no lo leí |
| 200-N1, 207-N1, 210-N1 | No registrado | Entregables de proveedor vencidos sin entrega: CT-451 *Licenciamiento* 392 días (PRY-200); CT-315 *Parametrización* 216 días (PRY-207); CT-220 *Licenciamiento* 228 y *Parametrización* 39 días, CT-252 *Licenciamiento* 204 días (PRY-210) | Sin doliente | Fechas contractuales 2025-09-18 a 2026-09-06 | Mitigación o seguimiento inexistente sobre un atraso de más de 6 meses; los tres proyectos tienen factura de proveedor en la carpeta y el hito de salida o integración figura cumplido sin evidencia |
| 203-I1, 200-I1, 204-I3, 205-I3, 209-I1 | Incidencia | «Hallazgo de seguridad levantado en la revisión de arquitectura», con la misma redacción en cinco proyectos | Sin doliente | Sin fecha en ninguno | Si es un solo hallazgo, afecta a cinco proyectos y nadie lo tiene. Si son cinco, ninguno tiene responsable. Las fichas no permiten distinguir |
| 199-I1, 203-I2, 206-I1, 210-I1, 211-I1 | Incidencia | «El equipo perdió dos semanas por rotación de un desarrollador clave», en cinco proyectos | Sin doliente | Sin fecha | Misma lectura: puede ser una persona o equipo compartido entre proyectos. Hay que confirmarlo |
| 210-I2 | Incidencia | El patrocinador y el gerente de PRY-210 son la misma persona (Liliana Torres); la minuta del 2026-10-02 lista un solo asistente | Liliana Torres | Minuta del 2026-10-02 | Con CC-01 pendiente (2026-10-04, +84 días, 168.000.000 COP) nadie distinto del gerente puede decidir. Excede la autoridad del gerente |

### Detectados en reuniones, no registrados
| Qué | Tipo | Dicho en | Fecha |
|---|---|---|---|
| 203-N1: «el proveedor podría no llegar con el equipo completo para la siguiente fase, nadie lo anotó como riesgo». Las notas no dicen qué proveedor; la ficha de PRY-203 no tiene proveedores cargados | Riesgo | PRY-203, `2026-10-15-notas-reunion.txt` | 2026-10-15 |

En las demás minutas y notas en texto (`.md`, `.txt`) la búsqueda de frases de riesgo no encontró otro caso. No reviso a mano las minutas `.docx` de PRY-208 y PRY-211: me quedo con lo que la ficha extrajo. Que no aparezca algo aquí no prueba que no se dijera. Hay un punto de contacto: Óscar Ramírez tiene «Revisión con el proveedor» para el 2026-10-25; es el sitio natural para confirmar este riesgo.

**Derivados de contratos, no de reuniones.** Estos cuatro no se dijeron en ninguna reunión: salen de las fechas de entregables de las fichas. Van marcados como no registrados porque ningún informe de avance los lista y tampoco ninguna minuta los menciona.
| Id | Proyecto | Contrato | Entregables vencidos en `pending` al 2026-10-15 |
|---|---|---|---|
| 200-N1 | PRY-200 | CT-451, Red Rural de Pagos | Licenciamiento (2025-09-18), 392 días |
| 207-N1 | PRY-207 | CT-315, Red Rural de Pagos | Parametrización de líneas de crédito (2026-03-13), 216 días |
| 210-N1 | PRY-210 | CT-220, Soluciones Solidarias; CT-252, Datos para Cooperativas | CT-220 Licenciamiento (2026-03-01) 228 días y Parametrización (2026-09-06) 39 días; CT-252 Licenciamiento (2026-03-25) 204 días |
| 211-N1 | PRY-211 | CT-884, Red Rural de Pagos | Licenciamiento (2026-02-10) 247 días; Bolsa de horas (2026-06-09) 128 días; Parametrización (2026-10-07) 8 días |

Que no haya acta de recibo en la carpeta no prueba que el entregable no se haya recibido; puede estar en otro sitio.

### Sin doliente o sin fecha
Los 38 ítems registrados carecen de doliente. Las 19 incidencias tienen «desde cuándo» como no declarado, y los 19 riesgos y dependencias registrados no traen fecha ninguna (ni de revisión ni de mitigación). No relleno ninguno.

| Proyecto | Ítems registrados | Sin doliente | Sin fecha |
|---|---|---|---|
| PRY-199 | 4 | 4 | 4 |
| PRY-200 | 2 | 2 | 2 |
| PRY-201 | 2 | 2 | 2 |
| PRY-202 | 4 | 4 | 4 |
| PRY-203 | 3 | 3 | 3 |
| PRY-204 | 4 | 4 | 4 |
| PRY-205 | 5 | 5 | 5 |
| PRY-206 | 2 | 2 | 2 |
| PRY-207 | 3 | 3 | 3 |
| PRY-208 | 2 | 2 | 2 |
| PRY-209 | 2 | 2 | 2 |
| PRY-210 | 3 | 3 | 3 |
| PRY-211 | 2 | 2 | 2 |

Sin movimiento en dos períodos: no lo puedo decir. Solo hay un corte (`estado/snapshots/2026-10-15.json`) y las incidencias no declaran desde cuándo existen. Lo reporto como sin dato, no como cero.

Antigüedad: los últimos informes de PRY-200 y PRY-206 son del 2026-09-23 (22 días, por encima del umbral de 15). Su RAID tiene al menos esa edad.

Proyectos con fecha de fin ya pasada y RAID abierto: PRY-207 (fin 2026-04-28), PRY-209 (2026-05-11) y PRY-200 (2026-06-21). Todos sus hitos figuran cumplidos y el RAID sigue abierto, con 3, 2 y 2 ítems. O el proyecto no ha cerrado, o esos ítems están muertos.

### Dependencias en riesgo
Ninguna dependencia está confirmada por la contraparte; todas son declaradas, no acordadas. Ninguna trae código de proyecto. Las vinculaciones que siguen se infieren del texto.

| Id | Depende de | Confirmada | Qué pasó |
|---|---|---|---|
| 201-D1, 203-D1, 204-D1, 209-D1 | Proveedor del core cooperativo. PRY-202 es candidato, sin confirmar | No | El hito «Integración con el core cooperativo» de PRY-202 (2026-10-12) sigue pendiente sin evidencia. PRY-202 declara una reprogramación de salida «por el cierre contable» que su cronograma v1 no refleja. En PRY-203 la integración con el core ya se movió de 2027-03-13 a 2027-07-06 (+115 días) y CC-01 sigue sin decidir. PRY-209 figura con el hito de integración cumplido sin evidencia |
| 199-D1, 201-D2, 202-D1, 207-D1 | Un proveedor sin nombrar: «no ha confirmado la fecha de la última entrega» | No, por su propia redacción | PRY-199: el primer entregable de CT-199 vence el 2026-11-14 (30 días). PRY-207: la Parametrización de CT-315 ya lleva 216 días vencida. PRY-201 y PRY-202: la carpeta no trae contrato |
| 199-D2, 205-D1, 206-D1, 208-D1, 210-D1 | Consejo de Administración (un órgano, no un proyecto) | No | En PRY-205 la aprobación ya vino con objeciones: el Consejo pidió ajustar el reglamento antes del piloto (205-I2). Lo mismo consta en 202, 204 y 207 |

### Registro completo
Prob. e impacto: sin valorar en todos (no hay escala ni valor en las fichas). Fecha: sin fecha en todos. Último movimiento: lo único que hay es la fecha del documento donde el ítem aparece; no es una fecha de movimiento.

| Id | Tipo | Qué | Prob. | Impacto | Doliente | Fecha | Último movimiento |
|---|---|---|---|---|---|---|---|
| 199-D1 | Dependencia (antes riesgo) | El proveedor no ha confirmado la fecha de la última entrega | s/v | s/v | — | — | visto 2026-10-13 |
| 199-D2 | Dependencia (antes riesgo) | Aprobación del reglamento por el Consejo de Administración | s/v | s/v | — | — | visto 2026-10-13 |
| 199-I1 | Incidencia | El equipo perdió dos semanas por rotación de un desarrollador clave | — | — | — | — | visto 2026-10-13 |
| 199-I2 | Incidencia | Se reprogramó la salida por el cierre contable de fin de mes; el cronograma v1 no refleja ningún cambio | — | — | — | — | visto 2026-10-13 |
| 200-R1 | Riesgo | Concentración del conocimiento en una sola persona | s/v | s/v | — | — | visto 2026-09-23 |
| 200-I1 | Incidencia | Hallazgo de seguridad levantado en la revisión de arquitectura | — | — | — | — | visto 2026-09-23 |
| 200-N1 | No registrado | CT-451 Licenciamiento vencido 392 días (ver arriba) | — | — | — | — | contrato, 2025-09-18 |
| 201-D1 | Dependencia (antes riesgo) | Dependencia del proveedor del core cooperativo | s/v | s/v | — | — | visto 2026-10-12 |
| 201-D2 | Dependencia (antes riesgo) | El proveedor no ha confirmado la fecha de la última entrega | s/v | s/v | — | — | visto 2026-10-12 |
| 202-R1 | Riesgo | Cambio normativo del supervisor que puede mover el alcance | s/v | s/v | — | — | visto 2026-10-06 |
| 202-D1 | Dependencia (antes riesgo) | El proveedor no ha confirmado la fecha de la última entrega | s/v | s/v | — | — | visto 2026-10-06 |
| 202-I1 | Incidencia | El Consejo de Administración pidió ajustar el reglamento antes del piloto | — | — | — | — | visto 2026-10-06 |
| 202-I2 | Incidencia | Se reprogramó la salida por el cierre contable de fin de mes; el cronograma v1 no refleja ningún cambio | — | — | — | — | visto 2026-10-06 |
| 203-D1 | Dependencia (antes riesgo) | Dependencia del proveedor del core cooperativo | s/v | s/v | — | — | visto 2026-10-12 |
| 203-N1 | Riesgo, no registrado | El proveedor podría no llegar con el equipo completo para la siguiente fase | s/v | s/v | — | — | dicho 2026-10-15 |
| 203-I1 | Incidencia | Hallazgo de seguridad en la revisión de arquitectura | — | — | — | — | visto 2026-10-12 |
| 203-I2 | Incidencia | Rotación de un desarrollador clave: el equipo perdió dos semanas | — | — | — | — | visto 2026-10-12 |
| 204-D1 | Dependencia (antes riesgo) | Dependencia del proveedor del core cooperativo | s/v | s/v | — | — | visto 2026-10-03 |
| 204-R1 | Riesgo | Concentración del conocimiento en una sola persona | s/v | s/v | — | — | visto 2026-10-03 |
| 204-I1 | Incidencia | Hallazgo de seguridad levantado en la revisión de arquitectura | — | — | — | — | visto 2026-10-03 |
| 204-I2 | Incidencia | El Consejo de Administración pidió ajustar el reglamento antes del piloto | — | — | — | — | visto 2026-10-03 |
| 205-D1 | Dependencia (antes riesgo) | Aprobación del reglamento por el Consejo de Administración | s/v | s/v | — | — | visto 2026-10-03 |
| 205-R1 | Riesgo | Concentración del conocimiento en una sola persona | s/v | s/v | — | — | visto 2026-10-03 |
| 205-I1 | Incidencia | La prueba de carga no alcanzó el umbral pactado y se repite | — | — | — | — | visto 2026-10-03 |
| 205-I2 | Incidencia | El Consejo de Administración pidió ajustar el reglamento antes del piloto | — | — | — | — | visto 2026-10-03 |
| 205-I3 | Incidencia | Hallazgo de seguridad levantado en la revisión de arquitectura | — | — | — | — | visto 2026-10-03 |
| 206-D1 | Dependencia (antes riesgo) | Aprobación del reglamento por el Consejo de Administración | s/v | s/v | — | — | visto 2026-09-23 |
| 206-I1 | Incidencia | El equipo perdió dos semanas por rotación de un desarrollador clave | — | — | — | — | visto 2026-09-23 |
| 207-R1 | Riesgo | Concentración del conocimiento en una sola persona | s/v | s/v | — | — | visto 2026-10-14 |
| 207-D1 | Dependencia (antes riesgo) | El proveedor no ha confirmado la fecha de la última entrega | s/v | s/v | — | — | visto 2026-10-14 |
| 207-I1 | Incidencia | El Consejo de Administración pidió ajustar el reglamento antes del piloto | — | — | — | — | visto 2026-10-14 |
| 207-N1 | No registrado | CT-315 Parametrización vencida 216 días (ver arriba) | — | — | — | — | contrato, 2026-03-13 |
| 208-D1 | Dependencia (antes riesgo) | Aprobación del reglamento por el Consejo de Administración | s/v | s/v | — | — | visto 2026-10-13 |
| 208-I1 | Incidencia | La prueba de carga no alcanzó el umbral pactado y se repite | — | — | — | — | visto 2026-10-13 |
| 209-D1 | Dependencia (antes riesgo) | Dependencia del proveedor del core cooperativo | s/v | s/v | — | — | visto 2026-10-15 |
| 209-I1 | Incidencia | Hallazgo de seguridad levantado en la revisión de arquitectura | — | — | — | — | visto 2026-10-15 |
| 210-D1 | Dependencia (antes riesgo) | Aprobación del reglamento por el Consejo de Administración | s/v | s/v | — | — | visto 2026-10-03 |
| 210-I1 | Incidencia | El equipo perdió dos semanas por rotación de un desarrollador clave | — | — | — | — | visto 2026-10-03 |
| 210-I2 | Incidencia | Patrocinador y gerente son la misma persona (Liliana Torres) | — | — | Liliana Torres | — | minuta 2026-10-02 |
| 210-N1 | No registrado | CT-220 y CT-252: tres entregables vencidos (ver arriba) | — | — | — | — | contratos, 2026-03-01 a 2026-09-06 |
| 211-R1 | Riesgo | Concentración del conocimiento en una sola persona | s/v | s/v | — | — | visto 2026-10-15 |
| 211-I1 | Incidencia | El equipo perdió dos semanas por rotación de un desarrollador clave | — | — | — | — | visto 2026-10-15 |
| 211-N1 | No registrado | CT-884: tres entregables vencidos, cuatro en `pending` (ver arriba) | — | — | — | — | contrato, 2026-02-10 |

### Reclasificados, y por qué
Apliqué la prueba rápida del criterio (pasó → incidencia; depende de alguien fuera del proyecto → dependencia; se asume sin verificar → supuesto; lo demás, riesgo). Es una propuesta para este documento: no modifiqué ninguna ficha.
- **13 «riesgos» pasan a dependencia.** «Dependencia del proveedor del core» (×4), «el proveedor no ha confirmado la fecha de la última entrega» (×4) y «aprobación del reglamento por el Consejo» (×5) dependen de un tercero o de un órgano que el proyecto no controla. Se coordinan y se confirman; no se mitigan. Dejarlos como riesgo les asigna un plan de mitigación a algo que solo se resuelve con una respuesta ajena.
- **Quedan como riesgo 6:** concentración de conocimiento (200, 204, 205, 207, 211) y cambio normativo del supervisor (202). En PRY-211 el riesgo de concentración ya produjo la incidencia de rotación (211-I1), así que se leen juntos.
- **Incidencias que dependen de otra cosa:** 210-I2 (patrocinador y gerente iguales) es una condición de gobierno, no un hecho con fecha. La dejo como incidencia porque ya está ocurriendo, pero conviene decidir si es otra cosa.
- **Supuestos: ninguno registrado.** No levanté ninguno: nadie dijo un supuesto en lo que leí y no los invento. Los candidatos típicos (que el proveedor entregue, que el Consejo apruebe sin cambios) hoy figuran como riesgos; con la reclasificación pasan a dependencia, no a supuesto.

## Qué no sé
- Qué proveedor es «el proveedor» en 203-N1, 199-D1, 201-D2, 202-D1 y 207-D1, y si «el core» es PRY-202.
- Si el hallazgo de seguridad, la rotación del desarrollador y el reglamento del Consejo son un solo hecho repetido en varias fichas o hechos distintos.
- Desde cuándo existe cada incidencia y cuánto lleva sin movimiento: el registro no lo trae y hay un solo corte.
- Si hay mitigaciones acordadas: ninguna ficha registra una, así que no puedo decir que alguna haya vencido sin evidencia.
- Probabilidad e impacto de todo.
- Lo que se dijo en reuniones que no están en la carpeta, o que están en `.docx` y `.pdf` que no releí.

## Después
Puedo subir a comité los que cumplen el criterio de escalamiento: las cuatro dependencias del core (afectan a varios proyectos), las del Consejo (doliente externo, sin respuesta), PRY-211 (rojo con incidencia y contrato sin entregas) y el choque de gobierno de PRY-210 (excede la autoridad del gerente). Cada uno iría con la decisión formulada.
Para los ítems sin doliente puedo proponer uno por ítem; propongo, no asigno. Candidatos razonables: el gerente del proyecto para las incidencias propias, el patrocinador para lo que depende del Consejo, y quien lleve CT-884, CT-451, CT-315, CT-220 y CT-252 para los entregables vencidos. Dime si quieres que lo prepare.

*Rigor: los conteos salen de las fichas (`estado/records/PRY-199.json` a `PRY-211.json`) con un script de lectura propio; los días de atraso, de `datetime` con corte 2026-10-15. La búsqueda en reuniones fue por palabras clave sobre `.md` y `.txt`, no una lectura completa de cada minuta. Las reclasificaciones y las inferencias (PRY-202 como el core, hallazgos o rotaciones compartidos) son mías y están marcadas como tales. No modifiqué ninguna ficha ni el registro.*

---

La corrida tardó 156 segundos. `portafolio.py` marcó `vendor_invoiced_without_delivery` en PRY-211 y `vendor_invoiced_over_accepted` en PRY-210. Lo escribí en la tabla de decisiones como «hay factura en la carpeta», sin juzgar el monto. Esas dos señales merecen su propio punto de comité.