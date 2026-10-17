# /criterio-portfolio:health-check PRY-200

## Diagnóstico · PRY-200 Crédito de libranza digital · 2026-10-17

**Leí:** 16 documentos de la carpeta del proyecto, de 2025-12-13 a 2026-10-17. Son 13 .md, 1 .txt, 1 .json y 1 .xlsx.
**No pude leer:** nada de la carpeta del proyecto quedó sin leer. En las otras carpetas busqué «PRY-200» y «libranza digital» solo en texto plano (.md, .txt, .json) y no hay menciones. Los .docx, .xlsx y .pdf de otros proyectos no se pueden buscar así y no los abrí.

Los términos ya estaban vigentes (versión 1.1, aceptada por José Francisco Ñáñez el 2026-10-17), así que no pedí una aceptación nueva.

`00-gobierno/ficha-pm.json` es la ficha del gerente. La leí como declaración suya, no como evidencia. Las cifras derivadas salen de `portafolio.py compute` con corte 2026-10-17. Donde el script no da una cifra, no la escribí.

### Dictamen
**Sostenido:** 6 afirmaciones · **Sin sustento:** 14 · **Contradicho:** 4

El informe del 2026-10-07 declara **verde** y **48 %**. La carpeta no sostiene ninguna de las dos cosas.
- El informe se contradice con su propio texto: la prueba de carga falló y la salida se reprogramó.
- El cronograma marca los cinco hitos como cerrados, lo que daría 100 %, no 48 %. De esos cinco solo uno tiene acta de recibo, del 2026-10-07.
- El cierre comprometido, 2026-10-01, venció hace 16 días sin evidencia de salida a producción y sin ningún cambio registrado.
- Los tres entregables del contrato CT-410 están vencidos y ninguno tiene acta de recibo.
- Del dinero, solo el presupuesto aprobado tiene sustento. Comprometido, ejecutado y proyección son cifras del informe sin documento detrás.

Lo que sí se puede afirmar con documentos:
- Quién patrocina y quién gerencia.
- El presupuesto aprobado.
- La integración con el core, recibida el 2026-10-07.
- Tres compromisos de comité cerrados con acta.

No hay autoridad del gerente declarada, así que ninguna fecha movida cuenta como desviación aprobada.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Carlos Peña | `00-gobierno/2025-12-18-acta-constitucion.md` |
| Gerente | Jorge Medina | ídem |
| Autoridad declarada | No está | ídem |
| Comité | Consejo de Administración | ídem; `30-reuniones/` |

- El alcance del acta es «Componente 1, 2, 3» y el fuera de alcance es «Lo que otro proyecto cubre». No se puede medir contra un alcance que no está escrito.
- Dependencias declaradas: «Ninguna». La integración con el core cooperativo es una dependencia y no está declarada.
- El contrato CT-410 se firmó el 2025-12-13, cinco días antes de que se aprobaran el acta y el presupuesto (2025-12-18).
- Las minutas del comité solo listan compromisos. Ninguna registra una decisión.
- El criterio de éxito es «en producción y medido». Nada en la carpeta muestra ninguna de las dos cosas.

### Contra el plan
- **Línea base original:** v1, aprobada el 2025-12-18, inicio 2025-12-28, cierre 2026-10-01.
- **Línea base vigente:** igual a la original. No hay cronograma v2, solicitud de cambio ni replanificación. El script da 0 días de atraso, pero eso es ausencia de registro, no ausencia de atraso. El informe dice «Se reprogramó la salida» y ningún documento lo aprueba.
- **Cronograma:** el archivo se llama «v1» y tiene fecha 2025-12-18, pero marca como «cerrado» hitos de febrero a octubre de 2026. O se editó después sin versionarse, o la fecha del nombre no es la del contenido. Lo uso solo como línea base de fechas, no como prueba de cumplimiento.

### Hitos vencidos sin evidencia
| Hito | Fecha | Días | Qué documento se esperaría |
|---|---|---|---|
| Diseño funcional aprobado | 2026-02-21 | 238 | Acta de aprobación |
| Ambiente de pruebas certificado | 2026-04-17 | 183 | Certificado o acta de recibo |
| Piloto con asociados | 2026-08-06 | 72 | Informe o acta de cierre del piloto |
| Salida a producción | 2026-10-01 | 16 | Acta de puesta en producción |

«Integración con el core cooperativo» sí tiene acta (2026-10-07), contra una fecha de línea base de 2026-06-12. El acta no dice qué criterio se verificó. El script no calcula los días de ese atraso, así que no escribo la cifra.

### Dinero
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 4.200.000.000 COP | 3.390.376.801 COP (80,7 %) | 1.405.474.333 COP (33,5 %) | 4.010.066.854 COP (4,5 % por debajo) | 809.623.199 COP |

- Comprometido, ejecutado y proyección vienen solo del informe. No hay ejecución presupuestal, facturas ni órdenes de compra.
- Comprometido está en 80,7 %, por debajo del umbral de 90 % de la configuración.
- El contrato fija tres entregables de 194.058.672 COP cada uno, y condiciona la factura a un acta de recibo. No consta cuánto se facturó o pagó.
- Laura Vélez enviará «el ajuste del presupuesto la otra semana». No hay solicitud de cambio ni cifra.

### Lo que se dijo y nadie registró
- **Riesgo:** el proveedor podría no llegar con el equipo completo para la siguiente fase. La nota dice que nadie lo anotó, y no tiene responsable. Ese proveedor ya tiene tres entregables vencidos.
- **Incidencias del informe:** la prueba de carga fallida y las dos semanas perdidas por rotación no tienen registro ni responsable. No hay registro RAID en la carpeta.
- **Riesgo del informe:** la concentración del conocimiento en una sola persona tampoco tiene responsable.
- **Compromisos nuevos del 2026-10-17:**
  - Óscar Ramírez: revisión con el proveedor, 2026-10-27.
  - Laura Vélez: ajuste del presupuesto, sin fecha.
  - Felipe Arango: «enviar el documento 1», 2026-11-24.
- **Compromisos reprogramados:**
  - Felipe Arango, «Enviar el documento 1»: 6 veces. Original 2026-09-12, hoy 2026-11-24.
  - Óscar Ramírez, «Cerrar la prueba 2»: 5 veces. Original 2026-09-26, hoy 2026-12-01.
  - Elena Duarte, «Revisar el anexo 3»: 4 veces. Original 2026-09-28, hoy 2026-11-17.
- **Compromisos vencidos sin evidencia:** 5 en total.
  - Elena Duarte, «Enviar el documento 9»: 22 días.
  - Felipe Arango, «Cerrar la prueba 10»: 13 días.
  - Rubén Cárdenas, «Cerrar la prueba 18»: 6 días.
  - Gustavo Neira, «Actualizar la matriz 14»: 3 días.
  - Óscar Ramírez, «Confirmar la fecha 23»: 2 días.
- **Compromisos sin fecha:** Sandra Gil («Aprobar el diseño 5»), Gustavo Neira («Validar el ambiente 12») y Laura Vélez (el ajuste del presupuesto).
- **Dichos como entregados sin acta:** 5 compromisos. Después de decirlo salieron de las tablas sin que se presentara acta. Son los de Sandra Gil, Elena Duarte, Gustavo Neira, Felipe Arango y Rubén Cárdenas.
- **Cadencia:** las notas dicen «próxima reunión en dos semanas», y las seis minutas anteriores son semanales. Entre tanto vencen compromisos del 2026-10-20 al 2026-10-28.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Estado **verde** | Informe de avance 2026-10-07, «Verde» | El mismo informe (prueba de carga fallida, salida reprogramada) y el contrato CT-410 (3 entregables vencidos sin acta) |
| Avance **48 %** | Informe de avance | Cronograma: 5 de 5 hitos «cerrado», brecha de 52,0 puntos según el script |
| «Salida a producción» **cerrada** | Cronograma (estado «cerrado», 2026-10-01) | Informe: «la prueba de carga … se repite», «Se reprogramó la salida» |
| Plan vigente = línea base, 0 cambios | Cronograma v1 y acta de constitución | Informe: se reprogramó la salida |

### Sin sustento
Son 14 afirmaciones que nada contradice y nada respalda:
1. Comprometido 3.390.376.801 COP.
2. Ejecutado 1.405.474.333 COP.
3. Proyección 4.010.066.854 COP.
4. «Diseño funcional aprobado» cumplido.
5. «Ambiente de pruebas certificado» cumplido.
6. «Piloto con asociados» cumplido.
7. La prueba de carga no alcanzó el umbral (no hay resultado de la prueba ni el umbral pactado).
8. Dos semanas perdidas por rotación.
9. Riesgo de concentración del conocimiento.
10. a 14. Los cinco compromisos dichos como entregados sin acta.

Las 6 **sostenidas**:
- Presupuesto aprobado.
- Fechas comprometidas de inicio y cierre.
- Integración con el core recibida.
- «Validar el ambiente 4», con acta del 2026-09-12.
- «Entregar el punto 8», con acta del 2026-09-26.
- «Aprobar el diseño 13», con acta del 2026-10-10.

### Lo que esta carpeta no permite saber
- **El estado real (verde, amarillo o rojo).** Faltan las actas de tres hitos y la de producción. El comité no tiene base para aceptar el verde.
- **Qué puede decidir el gerente.** Sin autoridad declarada, cada fecha movida es una fecha que alguien escribió.
- **Qué incluye el alcance.** No se puede saber qué falta por entregar.
- **Cuánto se facturó o pagó al proveedor.** Tampoco se puede saber qué parte de los 1.405.474.333 COP ejecutados corresponde al CT-410.
- **Cómo evolucionó el estado.** Hay un solo informe de avance, así que no se ve cuándo empezó la brecha.
- **Qué decidió el comité.** Las minutas solo listan compromisos.
- **Qué dependencias tiene el proyecto.** El acta declara ninguna y la integración con el core sugiere una.

---
**Pie de rigor.** La base son 16 documentos de la carpeta de PRY-200, leídos el 2026-10-17, con la ficha del gerente tratada como declaración. Las cifras derivadas salen de `portafolio.py compute`. No verifiqué nada fuera de los documentos: lo hablado fuera de ellos no consta. No recomiendo detener, continuar ni reestructurar; eso lo decide quien tiene la facultad. Cada dato lleva su fuente para que usted la verifique.

La salida está en `estado/corridas/salida-health-check.md` y la corrida quedó registrada como `2026-10-17-health-check-1`. Puedo llevar las 4 contradicciones al gerente como preguntas, una por una, si quiere.