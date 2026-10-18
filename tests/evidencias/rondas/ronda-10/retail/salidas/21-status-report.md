# /criterio-portfolio:status-report PRY-205

Terminé el informe de PRY-205 y dejé la corrida registrada. Esta es la salida completa:

---

Informe generado desde la ficha `estado/records/PRY-205.json` (actualizada el 2026-10-18) y el cálculo de `portafolio.py compute` con fecha de corte 2026-10-18. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no hizo falta registrarlos de nuevo.

## PRY-205 · Pago con QR en caja — estado al 2026-10-18

**Declara el gerente (Natalia Ospina):** rojo · 77% · al 2026-10-18 (`20-seguimiento/2026-10-18-informe-avance.pdf`)
**Sustento documental:** sin sustento en el avance. Ningún dato de la ficha viene de evidencia: 0 de evidencia, 3 de declaración. Los documentos no respaldan el 77%.
**Lo que el semáforo no explica:** `milestone_met_without_evidence`, `milestone_overdue`, `progress_vs_plan`. El gerente reporta rojo, pero esas tres señales siguen sin explicación.
**Último documento:** 2026-10-18 (0 días de silencio) · **Última reunión:** sin dato. La ficha no tiene ninguna reunión ni minuta de este proyecto.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2027-01-26 | 2027-01-26 | 0 días contra la original y 0 contra la vigente |
| Presupuesto | COP 2.400.000.000 aprobado | proyección COP 2.270.114.693 | -5,4% (la proyección queda por debajo de lo aprobado) |

Replanificaciones: 0. La ficha tiene una sola línea base (v1, 2026-04-18, acta de constitución) y ninguna solicitud de cambio.

Dinero (COP): comprometido 1.515.511.924 (63,1%) · ejecutado 383.723.374 (16,0%) · disponible real 884.488.076. Las cifras comprometida, ejecutada y de proyección salen del informe de avance, que es una declaración.

### Hitos
| Hito | Base | Vigente | Estado | Evidencia |
|---|---|---|---|---|
| Diseño de la experiencia aprobado | 2026-06-21 | 2026-06-21 | declarado cumplido | **ninguna**, 119 días desde la fecha |
| Ambiente de pruebas certificado | 2026-08-15 | 2026-08-15 | cumplido | acta de recibo del 2026-10-13 |
| Integración con el ERP | 2026-10-09 | 2026-10-09 | pendiente, **vencido hace 9 días** | ninguna |
| Piloto en tiendas | 2026-12-02 | 2026-12-02 | pendiente | — |
| Despliegue en la cadena | 2027-01-26 | 2027-01-26 | pendiente | — |

### Dónde no coincide
- **Avance.** El gerente declara 77% (informe del 2026-10-18). El plan sustenta entre 40% y 60%: hay 2 de 5 hitos cumplidos. La diferencia es de 17 puntos por encima del plan.
- **Hito sin evidencia.** «Diseño de la experiencia aprobado» figura como cumplido, pero no hay documento que lo respalde. El único hito con acta es el ambiente de pruebas, del 2026-10-13. Ese acta se firmó 59 días después de la fecha de línea base (2026-08-15) y la ficha no registra replanificación.
- **Hito vencido con fechas intactas.** La integración con el ERP venció el 2026-10-09 y las fechas vigentes siguen iguales a la línea base. Aun así el informe declara dos incidencias que restan tiempo: dos semanas perdidas por la rotación de un desarrollador clave, y una semana más en la validación con dos tiendas por el conteo de inventario. La ficha no tiene cambios ni replanificaciones que las reflejen, y la desviación calculada es 0 días.
- Semáforo en rojo con las tres señales anteriores sin explicar: el rojo declarado no dice a cuál de ellas responde.

### Abierto
**Riesgos e incidencias sin movimiento:**
- Riesgo: cambio en la regulación de datos personales que puede mover el alcance. No tiene probabilidad, impacto, responsable ni fecha, y su fuente es la declaración.
- Incidencia: pérdida de dos semanas por rotación de un desarrollador clave. Sin responsable; desde 2026-10-18, la fecha del informe.
- Incidencia: validación con dos tiendas extendida una semana por el conteo de inventario. Sin responsable; desde 2026-10-18.

Los días «sin movimiento» no se pueden medir: la ficha no registra fecha de último movimiento y las fechas «desde» son las del informe, no las de origen.
**Compromisos vencidos:** ninguno. La ficha no tiene compromisos registrados, lo que no equivale a que no existan, porque no hay minutas ni reuniones.
**Dependencias sin confirmar:** ninguna registrada.
**Proveedor Datos y Demanda S.A.S. (CT-600):** 1 de 2 entregables aceptado. «Licenciamiento de la plataforma» tiene acta de recibo (2026-08-19) y factura (2026-09-12) por COP 244.874.533, igual al monto aceptado. «Bolsa de horas de desarrollo» vence el 2026-11-14 y está pendiente. No hay facturación adelantada.

### Sin dato
- `identity.authority`: no encontrada, así que no se sabe quién tiene autoridad para decidir sobre las desviaciones de este proyecto.
- `identity.phase`: no encontrada.
- Última reunión, compromisos, responsables y probabilidad e impacto de los RAID: sin dato.
- El área de negocio figura como «Talento humano» en el acta de constitución, lo que no parece coincidir con un proyecto de pago con QR en caja. Conviene confirmarlo.

### Después
La desviación de plazo no supera el umbral (10%), pero hay un hito vencido, un avance declarado que el plan no sustenta, un hito sin evidencia y un riesgo regulatorio sin dueño. Puedo preparar el punto de comité (el próximo es el 2026-10-25). Si el atraso de las incidencias es real, también puedo preparar la solicitud de cambio, que hoy no existe.

---
criterio-portfolio 0.5.0 · ficha PRY-205 aplicada, actualizada el 2026-10-18 · campos inciertos: `identity.authority`, `identity.phase`, `identity.business_area` (posible incoherencia) · Términos v1.1 y nota legal: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.5.0

---

**Corrida registrada:** `2026-10-18-status-report-1`, con la salida guardada en `estado/corridas/salida-status-report.md`.

- **Tiempo:** 32 segundos, medidos por la corrida.
- **Casos:** la corrida cuenta 13 proyectos, que son todos los del portafolio, aunque el informe es solo de PRY-205.
- **Hallazgos:** PRY-205 tiene 3 señales abiertas. El portafolio completo suma 63, pero esas no se leyeron aquí.
- **No medido:** el número de documentos no se midió.