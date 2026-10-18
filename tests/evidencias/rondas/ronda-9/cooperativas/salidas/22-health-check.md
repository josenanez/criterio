# /criterio-portfolio:health-check PRY-208

Términos vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17); no hizo falta registrar una aceptación nueva.

## Diagnóstico · PRY-208 Motor de crédito · 2026-10-17

**Leí:** 6 documentos (3 Markdown, 1 CSV, 2 PDF), fechados entre 2025-12-09 y 2026-10-15. También busqué el código y el nombre del proyecto en el resto de `documentos/`, y ningún otro documento los menciona.
**No pude leer:** nada quedó sin leer. En la carpeta faltan actas de recibo, registro de riesgos, solicitudes de cambio y soportes contables.

### Dictamen
**Sostenido:** 5 afirmaciones · **Sin sustento:** 8 · **Contradicho:** 4

**Esta carpeta no permite diagnosticar el avance real.**

- **Lo que sí se puede afirmar:** quién gobierna el proyecto, cuánto se aprobó, qué se pactó con el proveedor y que se radicó una factura.
- **Lo que no:** que algún hito esté cumplido, que el avance sea 31 % ni que el estado sea verde.
- **Contradicción central:** el cronograma marca los cinco hitos como «cerrado», pero el informe del 2026-09-28 dice 31 % y que el piloto aún no ocurrió.
- **Silencio:** no hay ningún documento fechado entre 2025-12-12 y 2026-09-18, que es justo cuando vencieron los cinco hitos.

### Gobierno
| | Qué dice el documento | Fuente |
|---|---|---|
| Patrocinador | Carlos Peña | acta de constitución |
| Gerente | Andrés Lozano | acta; informe de avance |
| Autoridad declarada | No está | acta |
| Comité | Consejo de Administración. El 2026-10-15 constan solo dos asistentes: Lozano y Peña. | acta; minuta |

El acta no declara autoridad del gerente. Sin ella no hay desviación aprobada: solo hay fechas y cifras escritas. El acta tampoco nombra el alcance (Componentes 1, 2 y 3), el proyecto que cubre lo excluido ni dependencias («Ninguna declarada»).

### Contra el plan
- **Línea base v1:** aprobada el 2025-12-12 por el Consejo. Inicio 2025-12-22, cierre 2026-08-05.
- **Vigente:** igual a la original, con 0 replanificaciones, 0 solicitudes de cambio y 0 días de desviación. Ese 0 solo prueba que nadie escribió una fecha nueva.
- **Cronograma sin fecha propia:** el archivo está fechado 2025-12-12 y marca como cerrados hitos de hasta 2026-08-05. O se editó después sin dejar versión, o el estado se anotó por anticipado. La carpeta no permite saber cuál.
- **Avance contra plan:** declarado 31 %. Con 5 de 5 hitos cerrados el plan sostiene 100 %, así que la brecha es de 69 puntos.

### Hitos vencidos sin evidencia
Los cinco figuran «cerrado» y ninguno tiene documento que lo respalde.

| Hito | Fecha | Días | Qué documento se esperaría |
|---|---|---|---|
| Diseño funcional aprobado | 2026-02-05 | 254 | Aprobación firmada del diseño |
| Ambiente de pruebas certificado | 2026-03-22 | 209 | Acta o certificado del ambiente |
| Integración con el core cooperativo | 2026-05-06 | 164 | Acta o informe de pruebas de integración |
| Piloto con asociados | 2026-06-21 | 118 | Informe de resultados del piloto; el informe del 2026-09-28 sugiere que no ocurrió |
| Salida a producción | 2026-08-05 | 73 | Acta de paso a producción |

El entregable «Bolsa de horas de desarrollo» (CT-314) venció el 2026-06-06, hace 133 días. El contrato lo marca «en curso».

### Dinero
Cifras en COP. Solo el aprobado viene del acta. Comprometido, ejecutado y proyección son declarados en el informe, sin soporte contable en la carpeta.

| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 9.500.000.000 | 5.624.497.293 (59,2 %) | 2.042.116.829 (21,5 %) | 9.766.333.561 (2,8 % sobre lo aprobado) | 3.875.502.707 |

- **Proyección:** supera lo aprobado en 2,8 %, por debajo del umbral de 10 %, pero sin solicitud de cambio en la carpeta.
- **Proveedor (CT-314):** se facturaron 909.461.374 COP (FV-1314, radicada el 2026-09-18). Ese monto coincide con un solo entregable, pero la factura dice «Entregables» en plural y no nombra cuál. El contrato condiciona el pago a un acta de recibo firmada, y esa acta no está.

### Lo que se dijo y nadie registró
- **Incidencia, no riesgo:** «El proveedor no ha confirmado la fecha de la última entrega». El informe la lista como riesgo, pero la bolsa de horas ya está vencida. No tiene responsable ni fecha.
- **Incidencia:** el Consejo pidió ajustar el reglamento antes del piloto. Sin responsable ni fecha, y es una dependencia que el acta no declaró.
- **Dependencia:** el acuerdo con arquitectura sobre requisitos no funcionales. No hay acta, persona ni fecha.
- **Compromisos del 2026-10-15:**
  - María Restrepo, «Entregar el punto 13», para 2026-11-07: abierto.
  - Ricardo Salas, «Entregar el punto 32», para 2026-10-15: **vencido hace 2 días, sin evidencia**.
  - Ninguno de los dos asistió a la sesión, y ningún documento define esos puntos.
- **Minuta:** enuncia «Avance» y «Compromisos» sin contenido. No dice nada del estado, del piloto ni del reglamento.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Estado Verde | Informe 2026-09-28: «Verde» | Contrato: bolsa de horas «en curso» y vencida; el mismo informe lista la entrega sin confirmar; la minuta tiene un compromiso vencido |
| Avance 31 % | Informe: 31 % | Cronograma: 5 de 5 hitos cerrados (plan 100 %) |
| Piloto cerrado (2026-06-21) | Cronograma: «cerrado» | Informe: ajustar el reglamento «antes del piloto» |
| Salida a producción cerrada (2026-08-05) | Cronograma: «cerrado» | Informe: sin piloto no hay salida; el criterio de éxito es «en producción y medido» y el avance es 31 % |

### Sin sustento
1. Comprometido, ejecutado y proyección: solo existen en el informe.
2. «Diseño funcional aprobado» cerrado.
3. «Ambiente de pruebas certificado» cerrado.
4. «Integración con el core cooperativo» cerrado.
5. «Licenciamiento del módulo» recibido. El contrato lo marca «recibido», pero está firmado el 2025-12-09, tres meses antes de la fecha de entrega, y no hay acta de recibo.
6. Que la factura FV-1314 corresponda al licenciamiento y se haya emitido contra acta de recibo.
7. El acuerdo con arquitectura.
8. Que el Consejo pidió ajustar el reglamento: solo lo dice el informe y la minuta no lo menciona.

**Sostenido:** patrocinador, gerente y comité; presupuesto aprobado de 9.500.000.000 COP; fechas de inicio y cierre del plan; términos del contrato CT-314; radicación de la factura por 909.461.374 COP.

### Lo que esta carpeta no permite saber
- **Si algún hito se cumplió:** sin actas ni certificados, el avance real es indeterminado.
- **Si el piloto ocurrió:** los dos documentos que lo mencionan se contradicen.
- **Cuándo se escribió el estado del cronograma:** no tiene fecha ni versión propia.
- **Qué se pagó y contra qué:** sin acta de recibo no se sabe si la factura cumple la condición de pago.
- **Cuánto se gastó de verdad:** el disponible real depende de un comprometido que solo declara el gerente.
- **Qué puede decidir el gerente:** no hay autoridad declarada.
- **Qué pasó entre 2025-12-12 y 2026-09-18:** no hay documentos en ese periodo.
- **Si hay dependencias con otros proyectos:** el portafolio tiene «Core cooperativo» (PRY-202). No leí sus documentos para esto y no afirmo relación alguna.

### Después
No recomiendo detener, continuar ni reestructurar: eso lo decide quien tiene la facultad. Puedo preparar el punto de comité con lo que falta: actas de hitos, acta de recibo del licenciamiento, soporte contable, autoridad del gerente y aclaración del piloto. También puedo llevar las cuatro contradicciones a Andrés Lozano como preguntas, una por una.

**Rigor:** todo sale de los 6 documentos citados y de la salida de `portafolio.py compute` del 2026-10-17. En la carpeta no hay ninguna fuente marcada como evidencia, solo declaraciones y documentos sin marcar. La verificación es de quien lee.

El «pie de rigor» no está definido en ningún archivo del plugin, así que usé el pie anterior, que es mío.

La salida quedó guardada en `estado/corridas/salida-health-check.md`. La corrida quedó registrada como `2026-10-17-health-check-1`, con PRY-208 como caso. El script tardó 101 segundos y no pudo medir el número de documentos.