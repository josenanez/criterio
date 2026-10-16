# /criterio-portfolio:status-report PRY-206

El informe de PRY-206 está listo y la corrida quedó registrada. Esto es lo que contiene, igual que en `estado/corridas/salida-status-report.md`.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15 para la 0.3.10), así que no los registré de nuevo.

## PRY-206 Pagos con QR: estado al 2026-10-15

Sale de la ficha `estado/records/PRY-206.json` (actualizada el 2026-10-15) y del cálculo de `compute` con corte 2026-10-15.

**Declara el gerente (Elena Duarte):** verde · 64% · al 2026-09-23 (hace 22 días).
**Sustento documental:** sin sustento. Los dos documentos del proyecto son el acta de constitución y el informe de avance, y ese informe es una declaración. No hay ninguna fuente de evidencia.
**Lo que el semáforo no explica:** `silent`. Lleva 22 días sin documentos nuevos y el umbral es 15.
**Último documento:** 2026-09-23. **Última reunión:** sin dato, porque ningún documento registra una reunión.

El script levantó dos alertas: `silent` y `declared_vs_evidence`.

### Contra el plan
| | Línea base original | Vigente | Desviación |
|---|---|---|---|
| Fecha de cierre | 2027-02-11 | 2027-02-11 | 0 días |
| Presupuesto aprobado | COP 2.400.000.000 | COP 2.400.000.000 | sin cambio |

No hay replanificaciones. Existe una sola línea base, la del acta de 2025-10-30.

Las cifras de presupuesto son las que declaró el gerente el 2026-09-23. Ninguna otra fuente las confirma.
- **Comprometido:** COP 1.708.940.032 (71.2%).
- **Ejecutado:** COP 534.840.876 (22.3%).
- **Proyección al cierre:** COP 2.216.045.578 (-7.7% frente a lo aprobado).
- **Disponible real:** COP 691.059.968.

El avance declarado (64%) y lo ejecutado (22.3%) no coinciden, y el informe no explica la diferencia. El plan no tiene hitos con los que contrastarla.

### Hitos
Sin dato. La ficha no tiene ningún hito, así que no se puede decir si el 64% tiene respaldo en el plan.

### Dónde no coincide
- **Declarado:** verde y 64% (informe del 2026-09-23).
- **Documentos:** el mismo informe dice que el equipo perdió dos semanas por la rotación de un desarrollador clave. La fecha de cierre no se movió y no hay solicitud de cambio ni replanificación. Un atraso reconocido que no llegó al plan es lo que el verde no explica. Además, no ha entrado ningún documento nuevo desde esa fecha.

### Abierto
**Riesgos e incidencias sin movimiento** (la única fuente de ambos es el informe del 2026-09-23, hace 22 días):
- **Riesgo:** aprobación del reglamento por el Consejo de Administración. No tiene responsable.
- **Incidencia:** dos semanas perdidas por la rotación de un desarrollador clave. No tiene responsable y la fecha de inicio no está declarada.

**Compromisos vencidos:** ninguno registrado. La ficha no tiene compromisos y no hay minutas que los sustenten.
**Dependencias sin confirmar:** ninguna registrada.

### Sin dato
- `identity.authority` (quién aprueba) y `identity.phase` (fase del proyecto) no se encontraron.
- No hay hitos, reuniones ni compromisos.
- Varios campos vienen del acta de 2025-10-30 y llevan 12 meses sin reconfirmarse: código, nombre, área, producto, patrocinador, gerente, comité, fechas, alcance y exclusiones. No digo que estén mal, solo que nadie los ha reconfirmado.

### Después
La fecha no pasa el umbral de desviación. Aun así, hay un verde con 22 días de silencio y una incidencia de dos semanas que no llegó al plan. Puedo preparar el punto de comité (el próximo es el 2026-10-22) o una solicitud de cambio si el atraso es real y no está formalizado.

---
*Criterio · criterio-portfolio 0.3.10 · Ficha de PRY-206 del 2026-10-15; declaración del gerente al 2026-09-23 · Campos inciertos: authority, phase, hitos, reuniones · Es un borrador de trabajo y la verificación es suya. Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal*

**Corrida registrada:** `2026-10-15-status-report-1`, caso PRY-206, 27 segundos medidos. El número de documentos leídos no quedó medido. Los 64 hallazgos y las señales por caso que muestra el registro son de los 13 proyectos del portafolio, no solo de este.