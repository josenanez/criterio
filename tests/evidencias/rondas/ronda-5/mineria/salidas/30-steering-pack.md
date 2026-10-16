# /criterio-portfolio:steering-pack 

Términos ya vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no registré ninguno nuevo. La configuración existe y los scripts corrieron por su ruta absoluta, uno por llamada.

Sale de 13 fichas (`estado/records`, PRY-199 a PRY-211, selladas el 2026-10-16; informes de avance entre 2026-10-07 y 2026-10-15) y de `portafolio.py compute` al 2026-10-16. Reutilizo lo ya producido hoy por change-control (PRY-207) y raid-log.

# Comité de proyectos — 2026-10-16
6 decisiones · 7 escalamientos sin decisión asociada · 11 proyectos con hallazgos (58 señales; PRY-199 y PRY-209 sin señales)

**Lo primero:** ninguna de las 13 fichas declara quién tiene autoridad para aprobar un cambio (`identity.authority`: no encontrado en las 13). Cada ficha nombra un comité, pero son cinco distintos y ninguno tiene umbral escrito. Por eso la decisión 1 es quién decide; las demás dirigen cada punto al comité que nombra el acta, **por defecto** y a la espera de la decisión 1.

## Decisiones del comité anterior
No hay comité anterior registrado: ninguna corrida previa de `steering-pack` y ninguna ficha con decisión de comité fechada. Lo único que existe son dos aprobaciones sin acta:

| Decisión | Fecha | Qué pasó | Estado |
|---|---|---|---|
| PRY-204 CC-01 «autorizada por el comité» (+61 días, 122.000.000 COP) | no consta (solicitud del 2026-10-09) | Línea base v2 registrada el 2026-10-13; no nombra qué comité ni la fecha | Sin acta (decisión 5) |
| PRY-208 CC-01 «autorizada por el comité» (+110 días, 220.000.000 COP) | no consta (solicitud del 2026-10-07) | Línea base v2 registrada el 2026-10-07; no nombra qué comité ni la fecha | Sin acta (decisión 5) |

## Decisiones de hoy

### [1] ¿Quién aprueba los cambios de fecha, alcance y presupuesto de cada proyecto, y con qué umbral?
**Proyecto:** los 13 · **Quién decide:** no determinable; se propone a este comité por ser quien se reúne sobre los 13 · **Si no se decide hoy:** las decisiones 2 a 6 se toman sin que esté escrito que ese comité sea el competente, y los cambios siguen entrando sin umbral.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Cada proyecto aprueba en el comité que nombra su acta (5 comités: Inversiones, Operaciones, Tecnología, Seguridad, Ambiental) | Sin cambio | Sin cambio | Sin cambio |
| B. A, más un umbral escrito: lo que pase de cierto número de días o de cierta suma sube a este comité | Exige fijar el umbral | Sin cambio | Sin cambio |
| C. No definirlo hoy | Sin cambio | Sin cambio | Sin cambio |

**Recomendación:** B. Sin umbral, los tres cambios pendientes (203, 210, 211) ya movieron su línea base antes de ser aprobados. Qué umbral es decisión del comité: los documentos no traen ninguno y no propongo cifras.

### [2] ¿Se aprueba el CC-01 de PRY-203: ampliación de alcance, +66 días y 132.000.000 COP?
**Proyecto:** PRY-203 Despacho automático de flota (gerente Beatriz Cuéllar, declarado rojo) · **Quién decide:** Comité de Seguridad, por defecto (acta del 2026-03-09) · **Si no se decide hoy:** la línea base v2 (cierre 2027-03-15) sigue en uso sin autorización: 66 días movidos, 0 autorizados.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar | Ampliación (componentes 1, 2 y 3 más lo pedido) | +66 días; cierre 2027-03-15 | 132.000.000 COP adicionales sobre 800.000.000 aprobados |
| B. Rechazar y volver a la v1 | Sin ampliación | Cierre 2027-01-08 | Sin adicional; la proyección ya es 966.342.753 (+20,8 %) |
| C. Devolver con motivo y costo total | Sin cambio hasta responder | Se mantiene v1 como vigente | Sin cambio |

**Recomendación:** C. La v2 no trae motivo (`not_found`), la proyección de 966.342.753 ya supera lo aprobado en 20,8 % con o sin el cambio, y el hito «Ingeniería básica aprobada» figura cumplido sin evidencia. Falta el costo total que justifique decidir.

### [3] ¿Se aprueba el CC-01 de PRY-211: ampliación de alcance, +70 días y 140.000.000 COP?
**Proyecto:** PRY-211 Control de polvo en vías (gerente Elena Duarte, declarado verde) · **Quién decide:** Comité de Operaciones, por defecto · **Si no se decide hoy:** la v2 (cierre 2026-12-11, antes 2026-10-02) sigue en uso sin autorización: 70 días movidos, 0 autorizados.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar | Ampliación | +70 días; cierre 2026-12-11 | 140.000.000 COP sobre 800.000.000 aprobados |
| B. Rechazar y volver a la v1 | Sin ampliación | Cierre 2026-10-02 | Sin adicional; proyección 835.519.093 (+4,4 %) |
| C. Devolver y corregir el estado declarado | Sin cambio hasta responder | v1 vigente | Sin cambio |

**Recomendación:** C. Declara verde con 48 % de avance mientras el plan sostiene entre 75 y 100 %, 3 hitos cumplidos sin evidencia y 70 días de línea base movidos sin autorización. Un verde no sostenido no es base para aprobar.

### [4] ¿Se aprueba el CC-01 de PRY-210: ampliación de alcance, +33 días y 66.000.000 COP?
**Proyecto:** PRY-210 Programa de relacionamiento comunitario (gerente Laura Vélez, declarado verde) · **Quién decide:** Comité Ambiental, por defecto · **Si no se decide hoy:** la v2 (cierre 2027-08-21, antes 2027-07-19) sigue sin autorización: 33 días movidos, 0 autorizados.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar | Ampliación | +33 días; cierre 2027-08-21 | 66.000.000 COP sobre 3.300.000.000 aprobados |
| B. Rechazar y volver a la v1 | Sin ampliación | Cierre 2027-07-19 | Sin adicional; proyección 3.118.748.068 (−5,5 %) |
| C. Devolver con motivo | Sin cambio hasta responder | v1 vigente | Sin cambio |

**Recomendación:** C. La solicitud es de hoy y la v2 no tiene motivo. Declara 72 % con un plan que sostiene entre 20 y 40 %: el avance no cuadra con el plan y hay que explicarlo antes de ampliar nada.

### [5] ¿Se ratifica con acta el CC-01 de PRY-204 (+61 días, 122.000.000 COP) y el de PRY-208 (+110 días, 220.000.000 COP), que solo constan como «autorizada por el comité»?
**Proyecto:** PRY-204 Monitoreo de taludes (rojo) y PRY-208 Trazabilidad del mineral (verde) · **Quién decide:** Comité de Inversiones (ambas actas) · **Si no se decide hoy:** las dos líneas base v2 quedan como vigentes sin un documento que muestre quién aprobó.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Ratificar con acta fechada | Ampliaciones se mantienen | PRY-204 cierre 2026-02-19; PRY-208 cierre 2027-05-20 | 122.000.000 y 220.000.000 COP adicionales |
| B. Exigir el acta y, mientras no aparezca, tratarlas como no autorizadas | Ampliaciones en suspenso | Vuelven a v1: PRY-204 2025-12-20; PRY-208 2027-01-30 | Sin adicional hasta ratificar |

**Recomendación:** B. Hoy la aprobación es una frase en la propia solicitud; el comité que sesiona es quien puede decir si la dio. Si la dio, A se resuelve con un acta de una línea.

### [6] ¿Cómo se trata el sobrecosto de PRY-206: proyección 7.517.983.731 COP contra 6.800.000.000 aprobados (+10,6 %)?
**Proyecto:** PRY-206 Red privada LTE en mina (gerente Liliana Torres, declarado verde, 80 %) · **Quién decide:** Comité de Inversiones, por defecto · **Si no se decide hoy:** el proyecto sigue en verde con +10,6 % sobre un umbral de 10 %, sin línea base y con fecha de cierre 2026-10-07 ya pasada.
| Opción | Alcance | Tiempo | Costo |
|---|---|---|---|
| A. Aprobar un aumento de presupuesto | Sin cambio declarado | Sin cambio | Hasta cubrir la proyección; no hay solicitud con la cifra |
| B. Exigir plan de contención y solicitud formal con línea base | Sin cambio hasta responder | Se fija fecha de cierre real | Se mantiene 6.800.000.000 mientras tanto |

**Recomendación:** B. No existe solicitud de cambio, ni línea base (`has_baseline`: falso), y la ficha no dice cuándo cierra el proyecto desde hoy. Con esos datos no hay cifra que aprobar.

## Escalamientos sin decisión asociada
| Proyecto | Qué | Desde cuándo | Qué se necesita |
|---|---|---|---|
| PRY-207 | Solicitud de mover 30 días la salida a producción, sin solicitante ni motivo (llegó por change-control, sin documento). Cierre 2027-04-26 (cronograma) o 2027-06-16 (acta) | Hoy | Que alguien la formule con solicitante, motivo, costo y fecha de referencia; hoy no es una decisión. Va al Comité de Inversiones |
| PRY-207 | Hito «Licencia y permisos obtenidos» vencido 8 días; bolsa de horas de CT-858 vencida 33 días (pendiente) | Licencia 2026-10-08; bolsa 2026-09-13 | Fecha comprometida del gerente y del proveedor |
| PRY-200 | Cierre del cronograma 2026-08-08 y del acta 2026-09-30: dos fechas, ambas ya pasadas; declara amarillo, 54 %, sin replanificación | 2026-08-08 | Que el gerente diga cuál es la fecha vigente y la formalice |
| PRY-202 | Cierre 2026-08-29 ya pasado; declara verde, 35 %, sin replanificación | 2026-08-29 | Replanificación o motivo por el que sigue en verde |
| PRY-204 | Cierre vigente 2026-02-19 ya pasado; declara rojo, 77 % | 2026-02-19 | Nueva fecha de cierre sustentada; depende de la decisión 5 |
| PRY-200 | 6 compromisos vencidos, 2 sin fecha y 4 reprogramados (el de Elena Duarte, 6 veces) | Compromisos desde 2026-09-12 | Doliente que desbloquee o cierre cada uno; los 4 reprogramados alcanzan el umbral de 3 |
| PRY-200, PRY-202, PRY-210 | PRY-200-R2 (proveedor sin equipo completo) dicho en reunión y sin registrar; la «parada de planta» figura como riesgo y como incidencia ya ocurrida en 202 y 210 | 2026-10-16 | Cada gerente formaliza con doliente y fecha, o lo cierra. Los 40 ítems RAID no tienen doliente ni fecha |

## Para conocimiento
- PRY-199: sin señales; verde, 20 %.
- PRY-200: amarillo, 54 %; 18 señales (ver escalamientos).
- PRY-201: amarillo, 58 %; 1 hito cumplido sin evidencia.
- PRY-202: verde, 35 %; verde contradicho por 2 hitos sin evidencia y avance rezagado.
- PRY-203: rojo, 82 %; decisión 2.
- PRY-204: rojo, 77 %; decisión 5 y escalamiento.
- PRY-205: verde, 73 %; verde contradicho por 2 hitos sin evidencia.
- PRY-206: verde, 80 %; decisión 6.
- PRY-207: amarillo, 75 %; 4 señales, escalamientos.
- PRY-208: verde, 48 %; verde contradicho: +110 días, avance rezagado, 2 hitos sin evidencia; decisión 5.
- PRY-209: amarillo, 54 %; sin señales, pero sin línea base ni dependencias.
- PRY-210: verde, 72 %; decisión 4.
- PRY-211: verde, 48 %; decisión 3.

## Anexo
**Estado del portafolio (`compute`):** 13 proyectos, 11 con alertas, 58 señales, 6 con verde contradicho por la evidencia (202, 205, 206, 208, 210, 211), 2 sin línea base (206, 209), 13 sin autoridad declarada.

**Contradicciones abiertas**
- Verde contra evidencia: PRY-202, 205, 206, 208, 210, 211.
- PRY-200: fecha de cierre del cronograma (2026-08-08) frente al acta (2026-09-30).
- PRY-207: fecha de cierre del cronograma (2027-04-26) frente al acta (2027-06-16).

**Vacíos de información**
- Autoridad de aprobación: ausente en las 13 fichas.
- Dependencias entre proyectos: ninguna ficha tiene. El acta de 203, 207 y otros excluye «lo que otro proyecto cubre» sin nombrar el proyecto. No puedo decir si un cambio afecta a otro proyecto: no está declarado.
- Línea base v2 sin motivo en PRY-203, 210 y 211.
- RAID: 40 ítems, ninguno con doliente, fecha, probabilidad ni impacto. Doce frases se repiten entre proyectos y pueden ser de plantilla.
- Ningún campo de las fichas está marcado como evidencia independiente del estado declarado.

**Lo que no sé**
- Qué se decidió en comités anteriores, fuera de las dos frases «autorizada por el comité».
- El costo total de cada cambio pendiente: cada solicitud trae solo el adicional.
- Si alguno de los umbrales de aprobación existe fuera de estos documentos.

**Después:** cuando el comité sesione, registro las decisiones en las fichas (aprobación, quién, fecha y documento), que es lo que cierra el ciclo y alimenta el comité siguiente. Línea base nueva solo con aprobación documentada.

---
Pie: Criterio Portfolio 0.3.11 · términos v1.1 · 13 fichas aplicadas (corte 2026-10-16) · campos inciertos: autoridad (13), línea base (206, 209), motivo de v2 (203, 210, 211), RAID (40 ítems) · borrador de trabajo, no decisión ni asesoría; la verificación es suya · https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.3.11

La corrida quedó registrada como `2026-10-16-steering-pack-1`. Tardó 126 segundos y cubrió 13 proyectos y 58 señales. Su salida está en `estado/corridas/salida-steering-pack.md`.