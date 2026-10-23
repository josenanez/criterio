# /criterio-portfolio:status-report PRY-207

## PRY-207 · Onboarding PyME — estado al 2026-10-23

Ficha: `estado/records/PRY-207.json`, actualizada el 2026-10-23. Las cifras salen de `portafolio.py compute`. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no hubo que registrar nada.

**El gerente declara** (Javier Hoyos): amarillo, 22%, al 2026-10-03.

**Sustento documental:** sin sustento. Ningún dato viene de evidencia, y las cifras de presupuesto son declaración del gerente.

**Lo que el semáforo no explica:**
- **Silencio:** 20 días sin documentos, con umbral de 15.
- **Avance contra plan:** el gerente declara 22%, y el plan, con 3 de 4 hitos marcados como cumplidos, sostiene entre 75% y 100%. La diferencia es de 53 puntos y va en sentido contrario a lo habitual: lo declarado está por debajo del plan.
- **Hitos sin evidencia:** 3 hitos aparecen como cumplidos sin evidencia de cumplimiento.

**Último documento:** 2026-10-03. **Última reunión:** sin dato, porque no hay actas.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2027-01-13 | 2027-01-13 | 0 días |
| Presupuesto aprobado (COP) | 6.800.000.000 | 6.883.597.700 (proyección) | +1,2% |

No hay replanificaciones. Del presupuesto, el gerente declara 5.550.704.544 comprometidos (81,6%) y 1.525.989.422 ejecutados (22,4%). Quedan 1.249.295.456 disponibles.

### Hitos
| Hito | Fecha | Estado según el cronograma | Evidencia |
|---|---|---|---|
| Diseño funcional aprobado | 2025-12-17 | cumplido | ninguna (310 días desde la fecha) |
| Ambiente de pruebas certificado | 2026-04-27 | cumplido | ninguna (179 días) |
| Integración con el core | 2026-09-05 | cumplido | ninguna (48 días) |
| Piloto con usuarios internos | 2027-01-13 | pendiente | no aplica |

El «cumplido» viene del cronograma v1, fechado el 2025-07-30. Ese documento es anterior a los tres hitos, así que no puede acreditar que se cumplieron.

### Dónde no coincide
- El informe dice 22%, y el cronograma sostiene entre 75% y 100%. Ninguno de los dos lleva evidencia, y no sé cuál es el correcto.
- El informe cuenta que la prueba de carga falló y se repite, y que se perdieron dos semanas. Aun así, la fecha de cierre no se movió y no hay replanificación ni solicitud de cambio. Además, esa prueba de carga fallida choca con el hito «Ambiente de pruebas certificado», que figura como cumplido desde abril.

### Abierto
- **Riesgo:** dependencia del calendario de liberaciones del core.
- **Incidencias:**
  - Se perdieron dos semanas por la rotación de un desarrollador clave.
  - La prueba de carga no alcanzó el umbral y se repite.
- **Sin dueño ni fecha de inicio:** ninguno de los tres tiene dueño ni fecha de inicio, así que no se pueden calcular los días sin movimiento.
- **Compromisos vencidos:** ninguno registrado, pero tampoco hay actas.
- **Dependencias:** ninguna declarada, aunque el riesgo del core apunta a una.

### Sin dato
- Autoridad del proyecto.
- Fase.
- Dueño de cada elemento RAID.
- Fecha de inicio de las incidencias.
- Última reunión.
- Evidencia de los hitos.
- Antigüedad de los datos de identidad, plan y presupuesto aprobado: 15 meses, por encima del umbral de 12.

### Después
Las desviaciones de plazo y de costo están bajo el umbral del 10%, pero hay tres señales sin explicar y ningún riesgo tiene dueño. Puedo preparar el punto de comité para el 2026-10-30. No hay un cambio no formalizado que justifique una solicitud de cambio.

---
*criterio-portfolio 0.8.0 · ficha PRY-207 del 2026-10-23 · campos inciertos: autoridad, fase, dueños RAID, evidencia de hitos · términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.8.0*

La salida completa quedó en `estado/corridas/salida-status-report.md`. Registré la corrida como `2026-10-23-status-report-1`. El registro cuenta los 13 proyectos de la ficha en su resumen general, pero el caso asociado es solo PRY-207.