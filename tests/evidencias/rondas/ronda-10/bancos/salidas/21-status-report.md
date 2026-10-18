# /criterio-portfolio:status-report PRY-200

El informe de PRY-200 está listo y la corrida quedó registrada. Esto es lo que dice, al 2026-10-18, a partir de la ficha del mismo día. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-18.

## PRY-200 Originación digital — estado al 2026-10-18

- **Lo que declara el gerente:** verde, 75%, al 2026-09-29 (Laura Vélez, informe de avance, 19 días de antigüedad).
- **Sustento documental:** sin sustento. Ningún dato de la ficha está marcado como evidencia (0 de evidencia, 6 de declaración, 13 sin marcar).
- **Lo que el semáforo no explica:**
  - un hito cumplido sin evidencia;
  - un hito vencido;
  - 19 días de silencio.
  - El script marca `declared_vs_evidence`: reporta verde y hay evidencia que ese verde no cubre.
- **Último documento:** 2026-09-29. **Última reunión:** sin dato, porque la carpeta no tiene actas ni transcripciones.

**Contra el plan**
- **Fecha de cierre:** 2027-02-14 en la línea base original y en la vigente, con 0 días de desviación.
- **Presupuesto:** aprobado 4.200.000.000 COP, proyección 4.383.262.818 COP, es decir +4,4% (el umbral es 10%).
- **Ejecutado y comprometido:** ejecutado 25,7% y comprometido 37,3%. Esas cifras son declaradas en el informe, no contrastadas con ningún documento financiero.
- **Replanificaciones:** 0 registradas. Sin embargo, el informe dice «Se reprogramó la salida por ventana de cambio», y no hay fecha movida ni solicitud de cambio. Los documentos no permiten saber si hubo un cambio no formalizado o si el cronograma está desactualizado.

**Hitos**

| Hito | Base y vigente | Estado | Evidencia |
|---|---|---|---|
| Diseño funcional aprobado | 2026-02-10 | cumplido (declarado) | ninguna, 250 días |
| Ambiente de pruebas certificado | 2026-06-13 | cumplido (declarado) | ninguna, 127 días |
| Integración con el core | 2026-10-14 | pendiente, vencido hace 4 días | — |
| Piloto con usuarios internos | 2027-02-14 | pendiente | — |

El avance declarado es 75% y el plan sustenta entre 50% y 75%. La brecha es 0 puntos, pero solo si se aceptan como ciertos los dos hitos sin evidencia.

**Dónde no coincide**
- El verde del 09-29 frente al hito del 10-14 que sigue pendiente. No hay documento posterior que explique qué pasó.
- El verde frente a 19 días sin documentos nuevos (el umbral es 15).
- Los dos hitos cumplidos frente a una carpeta sin acta ni certificado que los respalde.
- La reprogramación declarada frente a un plan que no se movió.

**Abierto**
- **Riesgo:** «Concentración del conocimiento en una sola persona», sin responsable ni mitigación en los documentos.
- **Compromisos vencidos:** ninguno registrado. Es porque no hay actas de las que extraerlos, no porque estén al día.
- **Dependencias:** ninguna registrada. La ventana de cambio de Operaciones es una dependencia implícita que nadie registró.

**Sin dato**
- Autoridad del gerente, fase y última reunión.
- Proveedores.
- Casi toda la identidad y el plan (fechas, alcance, moneda, aprobado), que vienen del acta y el cronograma de 2025-09-30, con 13 meses de antigüedad (el umbral es 12).

**Siguiente paso:** el hito vencido y la alerta `declared_vs_evidence` justifican llevar el caso al comité del 2026-10-25. Si la reprogramación movió fechas, corresponde una solicitud de cambio. Puedo preparar cualquiera de las dos si lo pides.

---
Criterio Portfolio 0.5.0 · Ficha de PRY-200 del 2026-10-18, declaración del 2026-09-29 · Campos inciertos: autoridad, fase, última reunión, y fechas y presupuesto con 13 meses · Términos: https://www.josenanez.com/es/agents/criterio-pmo/legal#v0.5.0

El informe completo está en `/home/claude/banco/ronda-10/bancos/espacio/estado/corridas/salida-status-report.md`. La corrida quedó como `2026-10-18-status-report-1`, con caso PRY-200 y 32 segundos medidos. Sus cifras (13 proyectos, 67 hallazgos) son del portafolio entero porque `compute` lo recalcula todo. Las de PRY-200 son 5 señales: `declared_vs_evidence`, `milestone_overdue`, `silent` y dos `milestone_met_without_evidence`.