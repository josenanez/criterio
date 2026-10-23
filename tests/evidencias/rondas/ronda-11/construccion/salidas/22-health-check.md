# /criterio-portfolio:health-check PRY-205

## Diagnóstico · PRY-205 Ampliación del aeropuerto regional · 2026-10-22

Los términos v1.2 ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-22, así que no los registré de nuevo.

**Leí:** 4 documentos del proyecto, de 2025-06-21 a 2026-10-20. Son 2 docx, 1 xlsx y 1 pdf, y los leí desde su texto convertido, no desde los originales. La ficha no guarda huella del texto del PDF del informe. Ningún otro proyecto ni el caché menciona PRY-205 o el aeropuerto.

### Dictamen
**Sostenido:** 3 afirmaciones · **Sin sustento:** 7 · **Contradicho:** 2

De la carpeta se pueden afirmar los nombres de gobierno y el presupuesto aprobado (18.000.000.000 COP). No se puede afirmar el estado:
- **Informe:** declara Verde y 34 % de avance.
- **Cronograma:** da por cerrados los 4 hitos, de modo que el plan sostiene 100 %.
- **Hitos:** ninguno de los 4 tiene un documento de recibo.
- **Obra:** el mismo informe cuenta un ensayo de concreto fallido y un vaciado reprogramado.

### Gobierno
- **Patrocinador:** Natalia Ospina.
- **Gerente:** Andrés Lozano.
- **Comité:** Comité Técnico, que aprobó el presupuesto el 2025-06-21 y sesionó el 2026-10-20.
- **Autoridad del gerente:** no está declarada en el acta. Sin ella, ninguna desviación queda aprobada.
- **Acta:** el alcance («Componente 1, 2, 3»), las exclusiones y el criterio de éxito son genéricos. Los datos de gobierno tienen 16 meses de antigüedad.

### Contra el plan
- **Línea base:** hay una sola (versión 1, cierre 2026-09-01), sin replanificaciones ni solicitudes de cambio.
- **Desviación:** el cálculo da 0 días, pero solo porque nadie registró una replanificación. El cierre comprometido pasó hace 51 días y el informe del 2026-10-18 reporta obra en curso.
- **Fecha del cronograma:** el archivo está fechado 2025-06-21 y aun así marca como cerrados hitos de 2026. No se sabe cuándo se marcó cada cierre.

### Hitos vencidos sin evidencia
| Hito | Fecha | Días |
|---|---|---|
| Diseños de detalle aprobados | 2025-10-15 | 372 |
| Licencias y permisos obtenidos | 2026-01-30 | 265 |
| Cimentación terminada | 2026-05-17 | 158 |
| Estructura terminada | 2026-09-01 | 51 |

Se esperaría un acta de recibo por cada uno. Otros proyectos del portafolio las tienen en `20-seguimiento`; este no tiene ninguna.

### Dinero (COP)
| Aprobado | Comprometido | Ejecutado | Proyección | Disponible real |
|---|---|---|---|---|
| 18.000.000.000 | 5.584.385.585 (31.0 %) | 4.482.743.262 (24.9 %) | 16.597.564.697 (−7.8 % vs aprobado) | 12.415.614.415 |

Comprometido, ejecutado y proyección salen solo del informe. No hay factura ni contrato que los respalde.

### Lo que se dijo y nadie registró
- **Incidencias sin responsable:** el ensayo de concreto que no alcanzó el valor pactado y el vaciado reprogramado por la llegada tardía del acero.
- **Dependencia no declarada:** el acero depende de un proveedor del que no hay contrato, y el acta dice «Ninguna declarada».
- **Riesgo sin dueño:** concentración del conocimiento en una sola persona.
- **Compromiso abierto:** Camilo Beltrán debe «Entregar el punto 32» para el 2026-11-12. No está vencido. Camilo no figura entre los asistentes y ningún documento define el «punto 32».
- **Minuta del 2026-10-20:** lista «Avance» como tema pero no registra qué se dijo.

### Contradicho
| Afirmación | Documento A | Documento B |
|---|---|---|
| Avance | Informe: 34 % | Cronograma: 4 de 4 hitos cerrados |
| Estructura terminada, cerrado el 2026-09-01 | Cronograma | Informe: el ensayo de concreto se repite y el vaciado se reprogramó |

### Sin sustento
- El estado Verde.
- Los hitos de diseños, licencias y cimentación.
- Las cifras de comprometido, ejecutado y proyección.

### Lo que esta carpeta no permite saber
- **Si el proyecto está en verde:** el estado descansa en hitos sin recibo y en un avance que el plan no respalda.
- **Cuánto atraso real hay:** sin replanificación ni fecha nueva de cierre, la desviación no se puede calcular.
- **Quién aprueba un cambio de fecha o de dinero:** el acta no declara la autoridad del gerente.
- **Qué pasó entre 2025-06-21 y 2026-10-18:** no hay ningún documento en ese tramo, que es donde caen los 4 hitos. El silencio es de la carpeta entera, no solo de quien reporta.
- **El impacto del ensayo de concreto fallido** sobre costo y fecha.
- **Si el gasto declarado es real:** no hay factura, contrato ni conciliación.

**Pie de rigor.** Las cifras derivadas vienen de `portafolio.py compute` del 2026-10-22. Los conteos del dictamen (3, 7 y 2) son criterio de esta lectura. Lo que se habló fuera de los documentos no se sabe. No recomiendo detener, continuar ni reestructurar: eso lo decide quien tiene la facultad.

Puedo llevar cada contradicción y cada hito sin recibo al gerente como pregunta, una por una, o preparar el punto de comité con la lista de lo que falta.

La corrida quedó registrada como `2026-10-22-health-check-1`. La salida completa está en `estado/corridas/salida-health-check.md`.