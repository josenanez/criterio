# /criterio-portfolio:health-check PRY-206

## Diagnóstico · PRY-206 Precios dinámicos · 2026-10-18

**Leí:** 21 documentos de la carpeta del proyecto · del 2026-04-05 al 2026-10-18 · formatos: .md (12), .docx (2), .pdf (3), .csv (2), .json (1), .txt (1). Además busqué menciones de PRY-206 en los otros 62 documentos del portafolio.
**No pude leer:** ninguno. Leí el texto convertido en el caché; las citas apuntan al original, y las rutas de abajo son relativas a la carpeta `PRY-206-precios-dinámicos/`.
**Términos:** ya estaban vigentes (versión 0.5.0, aceptados por José Francisco Ñáñez el 2026-10-18), así que no pedí aceptación nueva.
**Aviso de método:** `00-gobierno/ficha-pm.json` es la ficha que lleva el propio gerente. La traté como declaración, no como evidencia. Los hitos, importes y compromisos los verifiqué contra los documentos fuente.

### Dictamen
**Sostenido:** 7 afirmaciones · **Sin sustento:** 15 · **Contradicho:** 5

Esos números son mi clasificación de las 27 afirmaciones que listo abajo, no una salida del script. Desde esta carpeta se puede afirmar que el proyecto existe y tiene patrocinador, gerente, comité y presupuesto aprobado, y que está en rojo por declaración propia. También se puede afirmar que la desviación de plazo contra la línea base original es de 53 días (25.0%), por encima del umbral de 10%. Hay 6 compromisos vencidos, 2 reprogramados 3 o más veces y 3 sin fecha. Un proveedor facturó sin ninguna entrega recibida.

No se puede afirmar casi nada de lo que sostiene el verde del plan. Tres de los cuatro hitos «cerrados» no tienen acta. Ninguna cifra de dinero de más arriba del importe aprobado tiene documento contable detrás. La autorización del cambio CC-01 no deja rastro más que la propia solicitud. Según el script, en esta ficha hay 0 datos marcados como evidencia y 9 como declaración.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Paula Céspedes. También figura como *gerente de proyecto* de PRY-203 (acta del 2026-06-20) y es dueña de compromisos aquí. | `00-gobierno/2026-04-05-acta-constitucion.docx`; PRY-203 `00-gobierno/2026-06-20-acta-constitucion.md` |
| Gerente | Andrés Lozano. También es gerente de PRY-199 (acta del 2026-06-10). | `00-gobierno/2026-04-05-acta-constitucion.docx`; PRY-199 `00-gobierno/2026-06-10-acta-constitucion.md` |
| Autoridad declarada | **Ninguna.** El acta no dice qué puede aprobar el gerente ni hasta qué umbral de tiempo o costo. | `00-gobierno/2026-04-05-acta-constitucion.docx` (campo ausente) |
| Comité | Comité de Expansión. Aprobó el presupuesto el 2026-04-05. Hay 6 minutas semanales, del 2026-09-06 al 2026-10-11. **No hay minutas entre abril y el 2026-09-06.** | acta; `30-reuniones/` |

El acta tiene alcance de relleno («Componente 1, 2, 3»), una exclusión sin contenido («Lo que otro proyecto cubre») y un criterio de éxito sin métrica («en producción y medido»). Declara «Ninguna» como dependencia.

### Contra el plan
- **Línea base original:** inicio 2026-04-15, cierre 2026-11-13 (`00-gobierno/2026-04-05-acta-constitucion.docx`).
- **Vigente:** cierre 2027-01-05 (`10-plan/2026-10-15-cronograma-v2.csv`).
- **Replanificaciones:** 1. Motivo declarado: CC-01, «ampliación de alcance», +53 días y 106.000.000 COP adicionales (`20-seguimiento/2026-10-17-solicitud-cambio-cc-01.md`). El documento no dice qué se amplía ni por qué.
- **Desviación de plazo:** 53 días contra la original (25.0%) y 0 días contra la vigente. El umbral es 10%. El script marca CC-01 como aprobado sin línea base nueva: el cronograma v2 conserva la columna `fecha_linea_base` original y solo mueve `fecha_vigente`.
- **Autorización:** la solicitud dice «Autorizada por el comité». No dice cuál comité, qué fecha ni quién firmó, y ninguna minuta lo recoge. La última minuta es del 2026-10-11, seis días antes de la solicitud. Las notas del 2026-10-18 no lo mencionan.
- **Cronología:** el cronograma v2 lleva fecha 2026-10-15 y ya muestra 2027-01-05, dos días *antes* de que se pidiera y autorizara el cambio.
- **Línea base original no verificable:** el `cronograma-v1.csv` lleva fecha 2026-04-05 pero su columna `estado` ya marca «cerrado» hitos de hasta el 2026-10-02. Se editó después. Solo el cierre 2026-11-13 está respaldado por otro documento (el acta). Las fechas de los hitos intermedios no tienen respaldo independiente.
- **Costo:** la proyección declarada supera lo aprobado en 2.5%, debajo del umbral de 10%. Ningún documento dice si esa proyección incluye los 106.000.000 COP de CC-01, ni hay presupuesto aprobado nuevo.

### Hitos vencidos sin evidencia
Los hitos figuran «cerrado» en el cronograma v2, pero no hay documento que lo pruebe.

| Hito | Fecha | Días | Qué documento se esperaría |
|---|---|---|---|
| Diseño de la experiencia aprobado | 2026-05-27 | 144 | Acta de recibo o aprobación firmada por el gerente (como la del ambiente de pruebas) |
| Integración con el ERP | 2026-08-20 | 59 | Acta de recibo o de pruebas de integración |
| Piloto en tiendas | 2026-10-02 | 16 | Acta de recibo del piloto con sus resultados |

«Ambiente de pruebas certificado» sí tiene acta (`20-seguimiento/2026-10-15-acta-recibo-ambiente-de-pruebas-certificado.pdf`), pero es del 2026-10-15 y la fecha vigente del hito es 2026-07-09. El cronograma no refleja ese atraso. Es posible que el atraso real sea mayor que los 53 días.

### Dinero
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 9.500.000.000 (acta) | 3.611.179.640 (declarado) | 2.375.369.823 (declarado) | 9.737.352.769 (declarado) | 5.888.820.360 (script) |

El script da 25.0% ejecutado y 38.0% comprometido. Las tres cifras declaradas salen solo del informe del 2026-10-15 (`20-seguimiento/2026-10-15-informe-avance.pdf`). Ningún documento contable las respalda. Los importes contractuales visibles son seis, uno por entregable: 410.335.213 cuatro veces en CT-847 y 599.677.238 dos veces en CT-980. No los sumé porque el script no entrega esa suma, así que **no pude conciliar el comprometido declarado contra los contratos**. Falta el consolidado de compromisos.

**Proveedores**
- **Tecnología para Tiendas Ltda. (CT-980):** 0 de 2 entregables recibidos. Facturó 599.677.238 COP el 2026-09-09 (FV-1980, «radicada en cuentas por pagar»). La condición de pago del contrato exige acta de recibo firmada por el gerente y no existe ninguna. Licenciamiento vencido hace 108 días (2026-07-02) y bolsa de horas hace 30 (2026-09-18).
- **Sistemas Comerciales del Norte (CT-847):** facturó 410.335.213 COP el 2026-09-06 (FV-2847, concepto genérico «Entregables del contrato»). El contrato dice «recibido» para el licenciamiento, pero no hay acta. La bolsa de horas (2026-07-17) lleva 93 días vencida y la configuración del catálogo (2026-09-02), 46. El soporte del primer trimestre vence el 2026-10-19.

### Lo que se dijo y nadie registró
No existe ningún registro RAID en la carpeta.

- **Riesgo (10-18):** «el proveedor podría no llegar con el equipo completo para la siguiente fase»; la nota dice que «nadie lo anotó como riesgo». No nombra proveedor, fase, dueño, probabilidad ni impacto. Las dos «bolsas de horas» ya vencidas sin recibir pueden ser ya una incidencia y no un riesgo.
- **Incidencia:** «el equipo perdió dos semanas por rotación de un desarrollador clave». Está en el informe, sin dueño, fecha ni efecto en el cronograma.
- **Riesgos solo en el informe, sin dueño, probabilidad ni impacto:** concentración del conocimiento en una persona, y cambio de regulación de datos personales que puede mover el alcance. CC-01 amplía alcance sin decir por qué, así que no se sabe si están relacionados.
- **Dependencias sin registrar:** los dos proveedores, el concepto de Jurídica, y el hito «Integración con el ERP» (existe PRY-209 «Migración del ERP» en el portafolio; ningún documento dice que haya relación).
- **Compromisos vencidos (6):**
  - Javier Hoyos, «Validar el ambiente 4» (2026-10-09, 9 días).
  - Jorge Medina, «Confirmar la fecha 7» (2026-10-06, 12 días).
  - Ricardo Salas, «Aprobar el diseño 13» (2026-10-15, 3 días).
  - Liliana Torres, «Actualizar la matriz 14» (2026-10-11, 7 días).
  - Javier Hoyos, «Entregar el punto 16» (2026-10-09, 9 días).
  - Sandra Gil, «Entregar el punto 24» (2026-10-17, 1 día).
- **Reprogramados:**
  - Liliana Torres, «Enviar el documento 1»: 6 veces. Era para 2026-09-13 y hoy está en 2026-12-03. La nota escribe «03/12/2026», que se puede leer como 3 de diciembre o 12 de marzo; lo leí como 3 de diciembre por la secuencia anterior.
  - Paula Céspedes (patrocinadora), «Cerrar la prueba 2»: 5 veces. Era para 2026-09-14 y hoy está en 2026-11-25.
- **Sin fecha (3):** Paula Céspedes «Validar el ambiente 20», Beatriz Cuéllar «Confirmar la fecha 23», Laura Vélez «ajuste del presupuesto» («la otra semana»).
- **Dichos entregados sin acta, y retirados de la lista:**
  - Carlos Peña, «Actualizar la matriz 6» (minuta del 2026-09-27).
  - Liliana Torres, «Actualizar la matriz 14» (2026-10-04).
  - Jorge Medina, «Cerrar la prueba 18» (2026-10-11).
- **Cadencia:** las notas del 2026-10-18 dicen «próxima reunión en dos semanas». El comité venía reuniéndose cada semana y ningún documento decide el cambio.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Avance 47% | `20-seguimiento/2026-10-15-informe-avance.pdf`: 47% | `10-plan/2026-10-15-cronograma-v2.csv`: 4 de 5 hitos «cerrado». El script dice que el plan sostiene entre 80% y 100%, y que el avance declarado va 33.0 puntos por debajo. |
| «Ambiente de pruebas certificado» se cerró en su fecha vigente (2026-07-09) | `10-plan/2026-10-15-cronograma-v2.csv` | `20-seguimiento/2026-10-15-acta-recibo-ambiente-de-pruebas-certificado.pdf`: recibido el 2026-10-15 |
| `cronograma-v1` es la línea base original del 2026-04-05 | Nombre y fecha del archivo | Su propia columna `estado`, con hitos «cerrado» hasta el 2026-10-02 |
| El contrato CT-847 es del 2026-04-13 | `00-gobierno/2026-04-13-contrato-ct-847.docx`: fecha de firma | Su columna de estado, con «recibido» y «en curso», imposibles en esa fecha |
| El cronograma v2 (2027-01-05) deriva de CC-01 | `10-plan/2026-10-15-cronograma-v2.csv`: 2026-10-15 | `20-seguimiento/2026-10-17-solicitud-cambio-cc-01.md`: solicitada y autorizada el 2026-10-17 |

### Sin sustento
Lo que nada contradice y nada respalda:
- **Dinero (3):** comprometido, ejecutado y proyección. Solo salen del informe.
- **Informe del 2026-10-15 (2):** el concepto de Jurídica sobre los términos de uso, y las dos semanas perdidas por la rotación.
- **Riesgos (2):** concentración del conocimiento, y cambio regulatorio de datos personales.
- **Hitos «cerrado» sin acta (3):** diseño de la experiencia, integración con el ERP y piloto en tiendas.
- **Contrato (1):** el licenciamiento de CT-847 como «recibido».
- **Cambio (1):** que CC-01 fue «autorizada por el comité».
- **Entregas dichas en reunión sin acta (3):** matriz 6 (Carlos Peña), matriz 14 (Liliana Torres) y prueba 18 (Jorge Medina).

**Sostenido (7):** estado rojo (coherente con las señales abiertas); presupuesto aprobado de 9.500.000.000 COP; patrocinador y gerente; «Ambiente de pruebas certificado» recibido (acta del 2026-10-15); y los compromisos cerrados con acta: «Aprobar el diseño 5» (Jorge Medina, 2026-09-20), «Revisar el anexo 11» (Camilo Beltrán, 2026-10-04) y «Revisar el anexo 3» (María Restrepo, 2026-10-11).

### Lo que esta carpeta no permite saber
- **Autoridad del gerente.** No se puede saber si +53 días y +106.000.000 COP estaban dentro de lo que podía pedir o decidir, ni qué instancia debía aprobar CC-01.
- **Quién autorizó CC-01.** Sin fecha, comité ni firma, no se puede decir que la línea base vigente (2027-01-05) esté aprobada.
- **Qué amplía CC-01 y por qué.** No se puede saber si 53 días alcanzan, ni si el cambio tiene que ver con el riesgo regulatorio.
- **El gasto real.** Sin libro de compromisos ni ejecución, ni lo ejecutado, ni lo comprometido, ni la proyección se pueden comprobar. El «disponible real» de 5.888.820.360 COP descansa en una cifra declarada.
- **Qué entregable paga cada factura.** FV-1980 no tiene entrega recibida detrás. FV-2847 tiene un entregable «recibido» que solo el contrato afirma.
- **Si el verde del plan es cierto.** Tres hitos no tienen acta, y el atraso real de los hitos con acta no está reflejado en el cronograma.
- **Qué pasó entre abril y septiembre.** No hay minutas de comité de ese período, que es cuando se cerraron tres de los cuatro hitos.
- **Qué entrega el proyecto.** El alcance es de relleno y el criterio de éxito no tiene métrica, así que no se puede comparar lo entregado con lo aprobado.
- **Quién es la persona clave, y cuál es el proveedor y la fase del riesgo del 2026-10-18.** Ningún documento los nombra.

### Después
Este diagnóstico no recomienda detener, continuar ni reestructurar; eso lo decide quien tiene la facultad. La carpeta permite diagnosticar el estado de la *evidencia*, no el avance real del proyecto. Puedo preparar el punto de comité del 2026-10-25 con la lista de lo que falta: las actas de los tres hitos, el acta o minuta de autorización de CC-01, el consolidado de compromisos y gasto, y las actas de recibo contra FV-1980 y FV-2847. Si quieres, llevo las 5 contradicciones al gerente como preguntas, una por una.

---
criterio-portfolio 0.5.0 · diagnóstico desde 21 documentos de PRY-206, 2026-04-05 a 2026-10-18 · cifras derivadas del script `compute` al 2026-10-18; el conteo 7/15/5 es clasificación propia · campos inciertos: `identity.authority`, `identity.product`, `identity.phase` · Términos v1.1 y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.5.0

---

**Corrida registrada:** `2026-10-18-health-check-1`, con la salida guardada en `estado/corridas/salida-health-check.md`. El registro dice 182 segundos y `documentos: null`, porque no pudo medir cuántos documentos se leyeron. Cuenta 63 hallazgos y 13 proyectos, porque `compute` recorre el portafolio entero y no solo PRY-206. El diagnóstico es de PRY-206 y está anotado con ese caso.

**Dos desvíos del procedimiento:** leí los documentos con `cat` desde Bash, porque Glob no estaba disponible en esta sesión. Y el `cd` de una llamada se arrastró a la siguiente; no afectó los resultados.