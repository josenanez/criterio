# /criterio-portfolio:health-check PRY-211

## Diagnóstico · PRY-211 Pronóstico de demanda · 2026-10-17

**Términos:** ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos otra vez.

**Leí:** 20 archivos del proyecto, de 2026-05-21 a 2026-10-17. Los formatos son 14 `.md`, 2 `.pdf`, 1 `.docx`, 1 `.xlsx`, 1 `.txt` y 1 `.json`. Busqué menciones del proyecto, de sus contratos y de sus proveedores en las carpetas de los otros proyectos y no hay ninguna.
**No pude leer:** nada. La `ficha-pm.json` la leí, pero no la cuento como evidencia: es el resumen que el gerente publicó de estos mismos documentos.

### Dictamen
**Sostenido:** 8 · **Sin sustento:** 12 · **Contradicho:** 4

- **Sostenidas (8):**
  - Patrocinador, gerente y comité, según el acta.
  - Presupuesto aprobado de 6.800.000.000 COP.
  - Fechas comprometidas del 2026-05-31 al 2026-11-30.
  - El recibo de la Bolsa de horas de CT-842 (acta del 2026-08-20).
  - Los cuatro compromisos cerrados con acta (diseño 5, matriz 6, ambiente 4, ambiente 12).
- **Contradichas (4):**
  - El estado «verde».
  - La «reprogramación del despliegue».
  - La factura FV-1842 contra lo recibido en CT-842.
  - La factura FV-2565 contra la falta de acta en CT-565.
- **Sin sustento (12):**
  - El avance de 49%, el comprometido, el ejecutado y la proyección.
  - Los tres hitos «cerrados».
  - La extensión de la validación con dos tiendas.
  - Las cuatro entregas «ya hechas» dichas en comité sin acta (diseño 13, matriz 14, punto 16, ambiente 20).

El único documento que respalda el verde es el informe del gerente. Ese mismo informe proyecta **26,9% sobre lo aprobado**. No se puede saber quién autorizaría una desviación, porque el acta no declara la autoridad del gerente. Tampoco se sabe cuánto se pagó de verdad, porque no hay registro de cuentas por pagar.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Jorge Medina. Asistió a los comités del 09-12, 09-19 y 09-26. No figura en los del 10-03 y 10-10 ni en las notas del 10-17. | acta de constitución; `30-reuniones/*` |
| Gerente | Andrés Lozano, que firma las actas de recibo. | acta; `20-seguimiento/*` |
| Autoridad declarada | **No está.** | acta (sin sección) |
| Comité | Comité Comercial. Las minutas listan compromisos y ninguna registra una decisión. | acta; `30-reuniones/*` |

El acta tampoco describe el alcance («Componente 1, 2, 3»), no nombra el proyecto de la exclusión y declara «Dependencias: ninguna» con dos contratos de proveedores en marcha.

### Contra el plan
- **Línea base:** hay una sola (v1, 2026-05-21), del 2026-05-31 al 2026-11-30. La vigente es igual. Hay 0 replanificaciones, 0 días de atraso y 0 cambios aprobados.
- **Cronograma:** el informe dice que se reprogramó el despliegue, pero el cronograma sigue con 2026-11-30 en la fecha base y en la vigente. O el cambio no se registró, o el cronograma está desactualizado. El archivo lleva 2026-05-21 en el nombre y declara cerrados hitos de julio a septiembre.
- **Avance:** declarado 49%. Si los tres hitos fueran ciertos, el plan sostiene entre 60% y 80%, es decir 11,0 puntos más. Los hitos no tienen evidencia.

### Hitos vencidos sin evidencia
| Hito | Fecha | Días | Qué documento se esperaría |
|---|---|---|---|
| Diseño de la experiencia aprobado | 2026-07-06 | 103 | Acta de aprobación del diseño |
| Ambiente de pruebas certificado | 2026-08-12 | 66 | Certificado o acta de pruebas |
| Integración con el ERP | 2026-09-18 | 29 | Acta de pruebas de integración |

Entregables de proveedor vencidos y sin acta:
- CT-842 Licenciamiento: 99 días.
- CT-842 Configuración del catálogo: 18 días.
- CT-565 Licenciamiento: 72 días.
- CT-565 Bolsa de horas: 5 días.

### Dinero
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 6.800.000.000 | 2.114.474.257 | 1.539.004.991 | 8.631.313.230 | 4.685.525.743 |

Está ejecutado el 22,6% y comprometido el 31,1%. Solo el aprobado viene de un documento de gobierno. Las otras tres cifras son declaración del informe, sin libro ni método de cálculo.

- **CT-842:** se facturaron 1.197.938.594 y solo hay acta por 775.475.640. Se facturó 422.462.954 por encima de lo recibido.
- **CT-565:** se facturaron 723.840.453 con 0 de 2 entregables recibidos. La factura (2026-09-16) es anterior a la fecha de la Bolsa de horas (2026-10-12).
- **No pude conciliar** el comprometido y el ejecutado con las facturas. El script no da esa suma y no la escribí a mano.

### Lo que se dijo y nadie registró
- **Riesgo:** «el proveedor podría no llegar con el equipo completo» (notas del 10-17). Nadie lo registró ni dijo de cuál proveedor.
- **Ajuste de presupuesto:** Laura Vélez lo manda «la otra semana». No hay solicitud de cambio en la carpeta.
- **Entregas sin acta:** cuatro «ya entregué» (diseño 13, matriz 14, punto 16, ambiente 20). Laura Vélez y Felipe Arango no figuran entre los asistentes de las reuniones donde se les atribuyó la afirmación.
- **Compromisos vencidos (7):**

  | Compromiso | Responsable | Venció | Días |
  |---|---|---|---|
  | Confirmar la fecha 7 | Paula Céspedes | 2026-09-26 | 21 |
  | Cerrar la prueba 10 | Rubén Cárdenas | 2026-10-10 | 7 |
  | Validar el ambiente 20 | Óscar Ramírez | 2026-10-10 | 7 |
  | Cerrar la prueba 18 | Ricardo Salas | 2026-10-12 | 5 |
  | Actualizar la matriz 14 | Beatriz Cuéllar | 2026-10-16 | 1 |
  | Confirmar la fecha 15 | Ricardo Salas | 2026-10-16 | 1 |
  | Entregar el punto 16 | Felipe Arango | 2026-10-16 | 1 |

- **Compromisos reprogramados (5):**
  - Javier Hoyos, Cerrar la prueba 2: 6 veces, hasta 2026-12-03, posterior al cierre del proyecto.
  - Liliana Torres, Enviar el documento 1: 4 veces.
  - Beatriz Cuéllar, Revisar el anexo 3: 4 veces.
  - María Restrepo, Enviar el documento 9: 3 veces.
  - Óscar Ramírez, Revisar el anexo 11: 3 veces.
- **Sin fecha (2):** Aprobar el diseño 13 y Mandar el ajuste del presupuesto, ambos de Laura Vélez.
- **Cadencia:** seis comités semanales seguidos. Las notas del 10-17 dicen «próxima reunión en dos semanas».

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| El proyecto está en verde | Informe del 10-14: «Verde» | El mismo informe proyecta 8.631.313.230 contra 6.800.000.000 aprobados (+26,9%). Hay además 3 hitos sin evidencia, 7 compromisos vencidos y 4 entregables de proveedor vencidos. |
| Se reprogramó el despliegue | Informe del 10-14 | Cronograma: 2026-11-30 en la fecha base y en la vigente, y 0 cambios aprobados |
| FV-1842 cubre «Entregables del contrato» | Factura por 1.197.938.594 | Contrato (pago contra acta) y acta del 08-20: recibido 775.475.640 |
| FV-2565 cubre «Entregables del contrato» | Factura por 723.840.453 | Contrato (pago contra acta): ninguna acta de recibo |

### Sin sustento
- **Avance de 49%:** no hay método ni medición.
- **Comprometido, ejecutado y proyección:** aparecen solo en el informe.
- **Tres hitos «cerrados»:** sin documento de cierre.
- **Validación con dos tiendas:** nada la menciona, y el Piloto sigue en 2026-10-24.
- **Cuatro entregas «ya hechas»:** dichas en comité, sin acta.

Observaciones que no entran en el conteo: tres entregables de proveedor figuran «en curso» sin acta, el riesgo del congelamiento de temporada solo lo cita el informe, y los dos contratos repiten nombres de entregables con proveedores distintos.

### Lo que esta carpeta no permite saber
- **Quién autoriza una desviación:** no se puede decir que la proyección, un atraso o un ajuste de presupuesto estén aprobados.
- **Qué pasó entre 2026-05-31 y 2026-09-05:** casi no hay documentos. No se puede reconstruir cómo se cerraron los tres hitos ni dar una tendencia.
- **Cuánto se pagó y cuándo:** el ejecutado declarado no se concilia con las dos facturas radicadas.
- **Si el cronograma está vigente:** la reprogramación del despliegue no se puede confirmar ni descartar.
- **Qué contienen los «Componente 1, 2 y 3»:** sin alcance descrito no hay contra qué medir un entregable como terminado.
- **De cuál proveedor es el riesgo del equipo incompleto.**

---
**Pie de rigor.** Las cifras derivadas salen del `compute` de esta corrida. Verifiqué fechas y montos contra los documentos originales y no calculé ninguna suma a mano. Es un borrador de trabajo, no una decisión ni asesoría, y la verificación es suya. No recomiendo detener, continuar ni reestructurar. Eso lo decide quien tiene la facultad, y hoy el acta no dice quién es.

**Siguiente paso posible:** llevar las 4 contradicciones al gerente como preguntas, una por una, o preparar el punto de comité con la lista de lo que falta.

**Corrida registrada:** `2026-10-17-health-check-1`, 155 segundos medidos por la corrida. La salida completa quedó en `estado/corridas/salida-health-check.md`.