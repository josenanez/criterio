---
name: audit-methodology
description: "La metodología de auditoría de la organización en la configuración de los tres agentes: los ciclos de rotación por nivel de riesgo, desde qué calificación un riesgo es alto, la escala de prioridad con su impacto y su probabilidad, la fecha de la última evaluación de riesgos y de la última evaluación externa de calidad, y cuántas reprogramaciones se permiten. Úsalo en el setup de cada agente y cuando un valor de la metodología cambie. Audit methodology, cycles, priority scale."
---

# La metodología de auditoría

**Los ciclos, los plazos y la escala los fija la organización.** Salen de su estatuto y de su metodología de auditoría, en `00-referencia/`, y van a la configuración (`methodology`) con su cita. Si la metodología no trae un valor, **no se inventa**: se le pregunta a la persona y se registra su respuesta con la fecha.

| Valor | En la configuración | Lo usa |
|---|---|---|
| Los meses del ciclo de rotación de cada nivel de riesgo del universo | `methodology.cycles_months`, por ejemplo `{"Alto": 12, "Medio": 24, "Bajo": 36}` | Prudencia |
| Desde qué calificación de la matriz un riesgo es alto | `methodology.high_ratings`, por ejemplo `["Alto", "Crítico"]` | Prudencia |
| La fecha de la última evaluación de riesgos que sostiene el plan, y dónde consta | `methodology.risk_assessment_date`, `methodology.risk_assessment_source` | Prudencia |
| La fecha de la última evaluación externa de calidad, y dónde consta | `methodology.external_assessment_date`, `methodology.external_assessment_source` | Prudencia |
| Quién aprueba el plan y sus cambios según el estatuto | `methodology.plan_approver` | Prudencia |
| La escala de prioridad: cada nivel con el puntaje mínimo de impacto por probabilidad | `methodology.priority.levels`, por ejemplo `[["Alta", 15], ["Media", 8], ["Baja", 1]]` | Justo |
| Cuántas veces se puede correr la fecha de un plan de acción | `methodology.max_reschedules` | Remedios |

## Lo que viene de fuera

Lo que fijan las Normas Globales de Auditoría Interna (F-01) no se configura: la evaluación de riesgos, al menos una vez al año (9.4); la evaluación externa de calidad, al menos una vez cada cinco años (8.4); lo que el plan tiene que considerar —el gobierno de TI, el riesgo de fraude y los programas de cumplimiento y ética— (9.4); los doce meses de la objetividad (2.2). Los requisitos temáticos y el día desde el que rige cada uno (F-02) están en el motor.

Lo que dice la regulación del país sobre quién aprueba el plan: en Colombia, el comité de auditoría aprueba el plan y sus cambios (F-10); en Brasil, el consejo de administración y el comité de auditoría (F-12). Lo del Perú (F-11) está **por verificar** y no se usa. La metodología de la organización sigue mandando: el país dice quién aprueba, no el ciclo ni la escala.
