# /criterio-portfolio:health-check PRY-204

## Diagnóstico · PRY-204 Débito contactless · 2026-10-16

**Leí:** 7 documentos de la carpeta de PRY-204, del 2025-08-31 al 2026-10-12. Los formatos son docx, csv, xlsx y md. También busqué el código y el nombre del proyecto en las carpetas de los otros 12 proyectos y en las decisiones de producto, y ningún otro documento habla de PRY-204.
**No pude leer:** nada quedó sin leer. El docx y el xlsx los leí por su conversión a texto (caché), y las citas apuntan al original.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

### Dictamen
**Sostenido:** 4 afirmaciones · **Sin sustento:** 11 · **Contradicho:** 3 (18 revisadas)

Desde esta carpeta se puede afirmar:
- quién gobierna el proyecto;
- cuál fue el plan original;
- que hubo una replanificación de +31 días, 13,8 % sobre la línea base original y por encima del umbral de 10 %;
- que el 2026-10-10 se recibió el ambiente de pruebas.

No se puede afirmar:
- que el proyecto esté en verde;
- que lleve 71 % de avance;
- que tres de sus cuatro hitos se cumplieron;
- cuánto se ejecutó realmente;
- que alguien haya autorizado el cambio CC-01.

Entre 2025-08-31 y 2026-10-05 la carpeta no tiene ningún documento. Los cinco restantes son de octubre de 2026, y casi todos los firma o recibe la propia gerente.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Natalia Ospina | 00-gobierno/2025-08-31-acta-constitucion.docx |
| Gerente | María Restrepo | 00-gobierno/2025-08-31-acta-constitucion.docx |
| Autoridad declarada | Ningún documento la declara. Sin autoridad declarada no hay desviación aprobada: hay fechas que alguien escribió. | (ausente) |
| Comité | Comité de Medios de Pago. Única minuta: 2026-10-12, con María Restrepo y Natalia Ospina. Temas «Avance» y «Compromisos», sin decisiones registradas. | 30-reuniones/2026-10-12-comite-semanal.md |

### Contra el plan
- **Línea base original** (cronograma v1, 2025-08-31):
  - Diseño funcional: 2025-11-05.
  - Ambiente de pruebas: 2025-12-31.
  - Integración con el core: 2026-02-25.
  - Piloto: 2026-04-22.
  - El acta fija el cierre en 2026-05-20 y el criterio de éxito «en producción y medido».
- **Vigente** (cronograma v2, 2026-10-07): solo el Piloto se mueve, a 2026-05-23. La base original se conserva en la columna `fecha_linea_base`. La desviación es de 31 días (13,8 %) contra la original y 0 contra la vigente. Hay 1 replanificación.
- **Motivo de la replanificación:** CC-01 dice «Ampliación de alcance» sin decir qué alcance. El acta lista «Componente 1, 2, 3», así que no se puede comprobar qué se amplió. El informe atribuye los problemas del periodo a la prueba de carga y a la rotación, no a ese alcance.
- **Autorización:** CC-01 (2026-10-05) dice «Autorizada por el comité», sin fecha ni aprobador con nombre. La única minuta del comité (2026-10-12) no la menciona. El cronograma v2 se fechó el 2026-10-07.
- **El plan no cubre el cierre:** el cierre del acta (2026-05-20) y la última fecha del cronograma (2026-05-23) ya vencieron. El plan no tiene ningún hito de producción ni de medición.

### Hitos vencidos sin evidencia
Ningún hito aparece como vencido y abierto: los cuatro están «cerrado» en el cronograma. Pero tres de ellos no tienen documento que lo pruebe:

| Hito | Fecha vigente | Días desde la fecha | Qué documento se esperaría |
|---|---|---|---|
| Diseño funcional aprobado | 2025-11-05 | 345 | Acta de recibo o aprobación del diseño |
| Integración con el core | 2026-02-25 | 233 | Acta de recibo o informe de pruebas de integración |
| Piloto con usuarios internos | 2026-05-23 | 146 | Informe de resultados del piloto y acta de recibo |

«Ambiente de pruebas certificado» figura cerrado con fecha 2025-12-31 en ambos cronogramas. Su única acta de recibo es del 2026-10-10 (ver Contradicho).

### Dinero
Todo viene del informe del 2026-10-07 (declarado). Solo el aprobado tiene respaldo documental.

| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 9.500.000.000 COP | 4.993.617.766 COP (52,6 %) | 2.541.292.498 COP (26,8 %) | 9.687.255.229 COP (2,0 % sobre lo aprobado) | 4.506.382.234 COP |

El aprobado del informe no incluye los 62.000.000 COP adicionales de CC-01. El ejecutado es 26,8 % del aprobado, mientras el informe declara 71 % de avance y el cronograma muestra 4 de 4 hitos cerrados.

### Lo que se dijo y nadie registró
La carpeta no tiene registro de riesgos, supuestos, incidencias ni dependencias. El acta dice «Ninguna declarada» en dependencias.
- **Incidencia:** la prueba de carga no alcanzó el umbral pactado y se repite (informe). No hay umbral, responsable ni fecha de la repetición.
- **Incidencia materializada:** dos semanas perdidas por la rotación de un desarrollador clave (informe). Sin registro.
- **Dependencia:** una aprobación regulatoria «pendiente desde el trimestre anterior», ya recibida según el informe. El acta no la declaraba y no hay documento de la aprobación.
- **Riesgo:** disponibilidad del equipo de seguridad para la revisión final (informe). Es el único riesgo escrito, y no tiene responsable, probabilidad ni fecha.
- **Compromiso vencido:** Rubén Cárdenas, «Entregar el punto 18», para 2026-10-03; lleva 13 días vencido al 2026-10-16. La minuta del 2026-10-12 lo recoge después de su fecha y no dice qué es el «punto 18». Rubén Cárdenas no asistió y el acta de PRY-204 no lo menciona. Con ese nombre aparece como gerente de PRY-207.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Estado verde | Informe 2026-10-07: «Verde» | Desviación de 13,8 % contra la original (umbral 10 %), compromiso vencido 13 días y 3 hitos cerrados sin evidencia (cronogramas v1 y v2, minuta 2026-10-12) |
| Avance 71 % | Informe 2026-10-07: 71 % | Cronograma v2: 4 de 4 hitos cerrados (el plan sostiene 100 %; diferencia de 29 puntos) |
| Ambiente de pruebas cerrado el 2025-12-31 | Cronogramas v1 y v2: vigente 2025-12-31, «cerrado» | Acta de recibo: fecha de recibo 2026-10-10, recibido por la gerente |

### Sin sustento
- Hitos cerrados: Diseño funcional, Integración con el core y Piloto, sin acta de recibo.
- Comprometido, ejecutado y proyección: no hay extracto contable ni contratos.
- CC-01: la autorización «por el comité» y los 62.000.000 COP adicionales.
- Aprobación regulatoria recibida, dos semanas perdidas por rotación, prueba de carga fallida y repetida.
- Que el recibo del ambiente de pruebas sea una aceptación independiente. Lo recibe la misma gerente, sin firma del patrocinador ni criterios de aceptación.

Es el bloque más largo: 11 de 18.

### Lo que esta carpeta no permite saber
- **Si los tres hitos sin acta se cumplieron.** Sin eso no se pueden usar ni el 71 % ni el 100 % del plan, y el verde queda sin base.
- **Quién autorizó CC-01 y cuándo.** Sin eso, los 31 días y los 62.000.000 COP no son una desviación aprobada.
- **Qué alcance se amplió.** El acta no detalla el alcance.
- **Qué falta para el cierre.** El plan termina en el piloto. El criterio de éxito (producción y medición) no tiene hito ni fecha, y ambas fechas de cierre ya pasaron.
- **La ejecución financiera real.** Sin libro mayor ni contratos, el disponible real sale de cifras declaradas.
- **Qué pasó entre 2025-09 y 2026-09.** No hay documentos de ese periodo. No se sabe si el proyecto no produjo papel o si la carpeta está incompleta.
- **Qué es el «punto 18»** y quién es Rubén Cárdenas respecto de este proyecto.
- **La autoridad de la gerente** para cambiar fechas o presupuesto.

### Después
No recomiendo detener, continuar ni reestructurar: esa decisión es de quien tiene la facultad. Puedo preparar el punto de comité con la lista de lo que falta, o llevar las tres contradicciones a la gerente como preguntas, una por una.

---
*Pie de rigor:* borrador de trabajo, no decisión ni asesoría. Cada dato sale de los documentos citados. Las cifras derivadas (días, porcentajes, disponible real) son las de `portafolio.py compute` del 2026-10-16. Lo declarado y lo probado van separados, y la verificación contra el original es suya.

---
La corrida quedó registrada como `2026-10-16-health-check-1` (141 segundos, caso PRY-204). El texto de arriba está en `estado/corridas/salida-health-check.md`.

El registro cuenta 50 hallazgos en los 13 proyectos, porque `compute` corre sobre todo el portafolio. Este diagnóstico cubre solo PRY-204, que tiene 7 de esas señales.