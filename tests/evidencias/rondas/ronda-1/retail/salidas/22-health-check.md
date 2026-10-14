# /criterio-portfolio:health-check PRY-206

Corrida registrada. Este es el diagnóstico entero, tal como quedó en `estado-portafolio/corridas/salida-health-check.md`.

## Diagnóstico · PRY-206 Precios dinámicos · 2026-10-14

**Leí:** 6 documentos · del 2025-10-13 al 2026-10-07 · formatos: .docx (2), .md (3), .csv (1)
**No pude leer:** ninguno. Ningún documento de otro proyecto menciona PRY-206, "Precios dinámicos" ni CT-140.
**Términos:** TERMS.md v1.0, aceptados por José Francisco Ñáñez el 2026-10-14. Ya constaban en la configuración local.

### Dictamen
**Sostenido:** 3 afirmaciones · **Sin sustento:** 9 · **Contradicho:** 4

La carpeta sostiene tres cosas:
- El presupuesto aprobado es de 3.300.000.000 COP. El acta y el informe coinciden.
- La bolsa de horas del contrato CT-140 se recibió. Hay acta de recibo del 2026-08-02.
- La factura FV-1140 por 252.927.117 COP coincide con el monto de ese único entregable recibido.

Todo lo demás viene del informe del 2026-10-07, que escribe quien es evaluado. Ninguna cifra ni hito tiene un documento propio que la respalde.

Hay siete señales abiertas:
- 4 hitos declarados cumplidos sin evidencia.
- Avance declarado de 40%, frente a un plan que sostiene entre 80 y 100%.
- 1 entregable del proveedor vencido.
- El contraste entre el verde declarado y esas señales, que el informe no explica.

De este proyecto no se puede afirmar que esté en verde.

Base del conteo (16 afirmaciones):
- **Sostenidas (3):** presupuesto aprobado, bolsa de horas recibida, factura igual al monto recibido.
- **Contradichas (4):** estado verde, avance 40%, "se reprogramó el despliegue", piloto en tiendas cerrado.
- **Sin sustento (9):**
  - Hitos Diseño de la experiencia, Ambiente de pruebas e Integración con el ERP cumplidos.
  - Comprometido, ejecutado y proyección.
  - Hallazgo de seguridad.
  - Riesgo de congelamiento y riesgo de disponibilidad de jefes de tienda.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Paula Céspedes | Acta de constitución 2025-10-13 |
| Gerente | Carlos Peña | Acta 2025-10-13; informe 2026-10-07; acta de recibo 2026-08-02 |
| Autoridad declarada | No declarada en ningún documento. El acta no trae el campo. | Acta 2025-10-13 |
| Comité | Comité de Cadena de Abastecimiento, que aprobó el presupuesto el 2025-10-13 | Acta 2025-10-13 |

Sin autoridad declarada no hay desviación aprobada: las fechas son las que alguien escribió. El acta también tiene estas particularidades:
- El área dueña es Talento humano, para un proyecto de precios.
- El alcance son tres "Componente 1/2/3" sin contenido.
- "Fuera de alcance" dice "Lo que otro proyecto cubre".
- El producto asociado es "No aplica".
- Las dependencias dicen "Ninguna declarada".
- No hay constancia de firma.

### Contra el plan
- **Línea base original:** cronograma v1 del 2025-10-13, con cinco hitos. El último, Despliegue en la cadena, es el 2026-10-27.
- **Vigente:** idéntica a la original en los cinco hitos. Hay 0 replanificaciones, 0 días de atraso contra la original y 0 contra la vigente.
- **Choque con el informe:** el informe dice que "se reprogramó el despliegue por el congelamiento de temporada". El cronograma no se movió y no hay solicitud de cambio. O la reprogramación no está en la línea base, o no ocurrió; los documentos no dicen cuál.
- **Cierre:** el acta fija el cierre el 2026-12-03 y el cronograma termina el 2026-10-27. Ningún documento explica la diferencia.

### Hitos vencidos sin evidencia
Están marcados "cerrado" en el cronograma. Ningún documento de la carpeta lo prueba.

| Hito | Fecha | Días | Qué documento se esperaría |
|---|---|---|---|
| Diseño de la experiencia aprobado | 2026-01-04 | 283 | Acta de aprobación del diseño |
| Ambiente de pruebas certificado | 2026-03-19 | 209 | Acta o certificado del ambiente |
| Integración con el ERP | 2026-06-01 | 135 | Acta de pruebas o aceptación de la integración |
| Piloto en tiendas | 2026-08-14 | 61 | Informe o acta de cierre del piloto |

- **Avance:** declarado 40,0%. El plan sostiene entre 80 y 100% (4 de 5 hitos cumplidos). La brecha es de 40,0 puntos.
- **Proveedor:** Licenciamiento de la plataforma (CT-140) tenía fecha comprometida 2026-03-07 y sigue "pendiente", 221 días después.

### Dinero
Las cifras salen del informe del 2026-10-07, que es una declaración. Solo el monto aprobado y la factura tienen otro documento.

| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 3.300.000.000 | 2.184.854.645 | 1.454.327.865 | 3.117.880.048 | 1.115.145.355 |

- **Porcentajes:** ejecutado 44,1% del aprobado, comprometido 66,2%, proyección 5,5% por debajo del aprobado. Moneda COP.
- **Proveedor CT-140:** 1 de 2 entregables aceptados. Aceptado 252.927.117; facturado 252.927.117.
- **Factura:** dice "Entregables del contrato CT-140" en plural, por un valor igual al de un solo entregable. El documento no dice cuál cubre.

### Lo que se dijo y nadie registró
No hay minutas ni carpeta de reuniones en este proyecto, así que no hay compromisos que extraer. Lo que aparece está solo en el informe:
- **Hallazgo de seguridad en los medios de pago:** se levantó en el periodo, pero no está en "Riesgos abiertos". Tampoco hay registro RAID ni documento del hallazgo.
- **Dependencias no declaradas** (el acta dice "Ninguna"): el proveedor Logística del Valle, con el Licenciamiento pendiente, y la Integración con el ERP. Es inferencia mía a partir del contrato y del cronograma; ningún documento lo dice.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Estado verde | Informe 2026-10-07: "Verde" | Mismo informe y cronograma: 4 hitos sin evidencia, brecha de 40,0 puntos, entregable del proveedor 221 días vencido |
| Avance 40% | Informe: 40% | Cronograma: 4 de 5 hitos "cerrado" (el plan sostiene 80 a 100%) |
| Se reprogramó el despliegue | Informe: reprogramado | Cronograma: fecha base y vigente iguales (2026-10-27), 0 replanificaciones |
| Piloto en tiendas cerrado el 2026-08-14 | Cronograma: "cerrado" | Informe: sigue abierto el riesgo "Disponibilidad de los jefes de tienda para el piloto" |

### Sin sustento
- Diseño de la experiencia, Ambiente de pruebas e Integración con el ERP: cumplidos, sin documento.
- Comprometido, ejecutado y proyección: no hay presupuesto detallado, ejecución contable ni ficha de costos.
- Hallazgo de seguridad: ningún documento.
- Riesgos de congelamiento de temporada y de disponibilidad de jefes de tienda: solo el informe, sin minuta ni registro.
- Estado de la ficha: 0 datos con evidencia, 3 declarados y 10 sin marca de fuente. Diez campos de identidad y plan tienen 12 meses de antigüedad, todos de la misma acta.

### Lo que esta carpeta no permite saber
- **Si los cuatro hitos se cumplieron:** sin actas de aprobación o recibo, no se sabe si el proyecto va en 80% o en menos.
- **Si el despliegue del 2026-10-27 se mueve:** la reprogramación está en el informe y no en el plan. Sin solicitud de cambio ni autoridad declarada, no hay fecha vigente fiable.
- **Cuánto se ha gastado de verdad:** las tres cifras de dinero dependen de una sola fuente declarada.
- **Qué pasó con el hallazgo de seguridad en pagos:** sin documento no se sabe gravedad, dueño ni plazo.
- **Quién puede aprobar un cambio de fechas o de presupuesto:** la autoridad del gerente no está escrita.
- **Si hay seguimiento:** no hay actas de comité del proyecto, y el informe es el único documento de avance. Tiene 7 días, bajo el umbral de silencio de 15.
- **Qué cubre la factura FV-1140:** no dice cuál entregable. Tampoco hay registro de por qué el Licenciamiento sigue pendiente 221 días.

### Pie de rigor
Las cifras derivadas están copiadas de `portafolio.py compute` (corte 2026-10-14). Separé lo declarado (informe) de lo probado (actas, contrato, factura). Las dos inferencias marcadas arriba son mías. No recomiendo detener, continuar ni reestructurar: eso lo decide quien tiene la facultad.

### Siguiente paso posible
Puedo preparar las cuatro contradicciones como preguntas para Carlos Peña, una por una. También puedo preparar el punto de comité con la lista de documentos que faltan.

**Registro de la corrida:** `2026-10-14-health-check-1`, 86 segundos, caso PRY-206, 7 señales abiertas. El campo de documentos quedó sin medir porque el script no lo mide en esta corrida.