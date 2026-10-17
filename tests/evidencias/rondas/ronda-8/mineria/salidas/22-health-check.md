# /criterio-portfolio:health-check PRY-204

## Diagnóstico · PRY-204 Monitoreo de taludes · 2026-10-17

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no pedí un registro nuevo.

**Leí:** 5 documentos de la carpeta del proyecto, de 2025-08-19 a 2026-10-17: un .docx, dos .csv y dos .md. También leí los 5 documentos del producto PRD-301 «Alerta de taludes», porque el acta asocia ese producto al proyecto. Busqué el código y el nombre en el texto de las demás carpetas (.md, .txt, .csv).
**No pude leer:** no quedó sin leer nada de lo que existe. La búsqueda cruzada no abrió el contenido de los .docx de otros proyectos, así que una mención de PRY-204 dentro de uno de ellos no habría aparecido. Abrí la ficha previa del proyecto para orientarme, pero cada dato de abajo sale de los documentos.

### Dictamen
**Sostenido:** 3 afirmaciones · **Sin sustento:** 7 · **Contradicho:** 3

La carpeta permite afirmar quién gobierna el proyecto, cuánto se aprobó y que hay una solicitud de cambio pendiente. No permite afirmar el estado verde ni el 45 %. El informe de avance es la única fuente de ambos, y el cronograma y la solicitud de cambio lo contradicen. Ninguno de los tres hitos cerrados tiene un documento que lo respalde. Se puede dictaminar que el verde no se sostiene, pero no cuál es el estado real.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Jorge Medina | Acta de constitución 2025-08-19 |
| Gerente | Beatriz Cuéllar | Acta 2025-08-19; informe de avance 2026-10-17 |
| Autoridad declarada | **No declarada.** El acta no dice qué puede aprobar el gerente ni quién aprueba replanificaciones | Acta 2025-08-19 |
| Comité | Comité de Seguridad, que aprobó el presupuesto el 2025-08-19 | Acta 2025-08-19 |

Sin autoridad declarada no hay desviación aprobada: las fechas nuevas son fechas que alguien escribió. La carpeta no tiene actas ni minutas del comité (no existe `30-reuniones`).

### Contra el plan
- **Línea base original (v1, 2025-08-19):** cierre 2026-03-31. El inicio, 2025-08-29, sale del acta; el csv no lo trae.
- **Vigente (v2, archivo del 2026-10-17):** el hito «Licencia y permisos obtenidos» pasa de 2026-03-31 a 2026-05-10, y con él el cierre. **Ningún documento da el motivo de la replanificación.** El csv no trae aprobación ni aprobador, y la fecha de aprobación que figura es la del archivo.
- **Desviación en tiempo:** +40 días contra la original, 18.7 %, sobre el umbral de 10 %. Contra la vigente es 0 días. Hay 1 replanificación.
- **Autorizados: 0 de 40 días.** La solicitud CC-01 (2026-10-06, Beatriz Cuéllar) pide +40 días «sobre la línea base vigente» y +80.000.000 COP. Dice «Pendiente de presentación al comité», pero el cronograma ya refleja los 40 días. Los documentos no dicen si los 40 días de CC-01 son los mismos que ya están en v2 o se suman a ellos.
- **El cierre vigente (2026-05-10) pasó hace 160 días** y el proyecto sigue abierto. El cronograma tiene tres hitos, los tres «cerrado». No tiene ninguno para los componentes 1, 2 y 3 ni para el criterio de éxito del acta («monitoreo de taludes en producción y medido»). Ningún documento dice cuándo se espera terminar.

### Hitos vencidos sin evidencia
Los tres figuran como «cerrado» y ninguno tiene documento que lo respalde. Los días van desde la fecha vigente hasta el corte.

| Hito | Fecha | Días | Qué documento se esperaría |
|---|---|---|---|
| Ingeniería básica aprobada | 2025-11-08 | 343 | Acta o carta de aprobación de la ingeniería básica |
| Ingeniería de detalle aprobada | 2026-01-18 | 272 | Acta o carta de aprobación de la ingeniería de detalle |
| Licencia y permisos obtenidos | 2026-05-10 (original 2026-03-31) | 160 | Resolución o licencia de la autoridad que otorga el permiso |

### Dinero
Moneda: COP. Las cifras de ejecución y proyección vienen solo del informe de avance, sin soporte contable en la carpeta.

| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 800.000.000 | 434.957.088 (54.4 %) | 361.778.067 (45.2 %) | 765.155.217 (−4.4 % vs aprobado) | 365.042.912 |

- El 45.2 % ejecutado coincide con el 45 % de avance declarado. El informe no dice con qué se mide ese avance.
- La proyección no dice si incluye los 80.000.000 COP de CC-01, que sigue pendiente.
- Lo comprometido está lejos del umbral de 90 %, así que no hay alerta de dinero.

### Lo que se dijo y nadie registró
No hay minutas en la carpeta. Lo que el informe de avance menciona y ningún registro recoge:
- **Dependencia no declarada:** el acta dice «Ninguna declarada», pero el informe habla de un proveedor que no ha confirmado la fecha de la última entrega. No hay contrato, entregables ni facturas del proveedor. El riesgo no tiene dueño.
- **Dos incidencias sin dueño ni fecha:**
  - Un hallazgo de la auditoría de seguridad, sin informe de auditoría ni descripción.
  - El primer ensayo de disponibilidad de los equipos «no alcanzó lo pactado y se repite», sin lo pactado, sin resultado y sin fecha del nuevo ensayo.
- **Compromisos:** ninguno registrado.
- **Producto:** el acta asocia el producto «alerta de taludes», que es el nombre de PRD-301, pero no cita su código. PRD-301 dice «Proyectos que lo construyen: ninguno declarado». Sus 14 requerimientos del comité del 2026-10-15 tienen «—» en «Proyecto que lo ejecuta». Beatriz Cuéllar es doliente de dos (REQ-4100 y REQ-4111). Ningún requerimiento está ligado a PRY-204.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Estado verde | Informe de avance 2026-10-17: «Verde» | Cronograma v1 → v2: +40 días (18.7 %) sin aprobación; CC-01 pendiente; el propio informe reporta un hallazgo de auditoría y un ensayo que no alcanzó lo pactado |
| Avance 45 % | Informe de avance: 45 % | Cronograma v2: 3 de 3 hitos cerrados, que sostendrían 100 %. O el avance está mal o el cronograma está incompleto; los documentos no dicen cuál |
| El cronograma v2 es el vigente | Cronograma v2, archivo del 2026-10-17, con cierre 2026-05-10 | CC-01 (2026-10-06): el cambio de tiempo está «pendiente de presentación al comité» |

### Sin sustento
Nada en la carpeta lo contradice y nada lo respalda:
1. Hito «Ingeniería básica aprobada» cerrado.
2. Hito «Ingeniería de detalle aprobada» cerrado.
3. Hito «Licencia y permisos obtenidos» cerrado.
4. Comprometido 434.957.088, ejecutado 361.778.067 y proyección 765.155.217. No hay ejecución presupuestal, facturas ni contratos.
5. Hallazgo levantado en la auditoría de seguridad.
6. Primer ensayo de disponibilidad que no alcanzó lo pactado.
7. El proveedor no ha confirmado la fecha de la última entrega.

### Lo que esta carpeta no permite saber
- **Quién aprueba replanificaciones:** sin eso no se puede decir si los 40 días son una desviación aprobada o una fecha sin aprobación. Lo responde el patrocinador o el comité.
- **Si los tres hitos se cumplieron:** sin esa evidencia no se puede medir el avance real ni confirmar el 100 % que sugiere el plan.
- **Qué hay en los componentes 1, 2 y 3:** el acta no los describe, así que el avance no se puede medir contra el alcance.
- **Cuándo termina el proyecto:** la fecha vigente pasó hace 160 días y no hay otra, así que no se puede calcular un atraso futuro.
- **Qué pactó el proveedor y qué se le pagó:** sin contrato ni entregables no se puede cruzar lo entregado con lo ejecutado.
- **Qué se pactó para el ensayo de disponibilidad y qué midió:** sin eso no se sabe qué tan grave es la incidencia.
- **Qué dijo el comité:** sin minutas no se sabe si CC-01 se presentó ni qué se decidió.
- **Fase actual del proyecto:** ningún documento la declara.
- **Si la proyección incluye CC-01:** sin eso no se sabe si el cierre previsto queda dentro o por encima de los 800.000.000 aprobados.
- **Antigüedad del dato:** gobierno, alcance y presupuesto aprobado vienen del acta de 2025-08-19, con 14 meses, por encima del umbral de 12.

### Cierre
Esto es un borrador de trabajo, con la cita al documento de cada dato. La verificación es de quien lo recibe. No recomiendo detener, continuar ni reestructurar: eso lo decide quien tiene la facultad. Puedo llevar las tres contradicciones al gerente como preguntas, una por una, o preparar el punto de comité con la lista de lo que falta.

La corrida quedó registrada como `2026-10-17-health-check-1`, con la salida en `estado/corridas/salida-health-check.md`. Tardó 84 segundos. El script no pudo medir el número de documentos leídos (`documentos: null`).