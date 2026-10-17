# /criterio-portfolio:project-history PRY-201

## Historia · PRY-201 Programa de fidelización · 2025-09-25 a 2026-10-14

**Leí:** 9 documentos entre 2025-09-25 y 2026-10-14. Los términos ya estaban vigentes para esta versión (0.3.13, aceptados por José Francisco Ñáñez el 2026-10-17), así que no registré uno nuevo.

**Trimestres sin documentos:** 2025-T4 y 2026-T1, T2 y T3, es decir 12 meses. Un documento es de 2025-T3 y ocho son de 2026-T4.

**En una línea:** el proyecto se constituyó el 2025-09-25 y no deja un solo documento hasta octubre de 2026. Ese mes aparece todo junto:
- dos actas de recibo de hitos con línea base de mayo y agosto;
- un informe en verde;
- un cronograma v2 que mueve el cierre al 2027-04-27;
- una solicitud de cambio de +33 días que dice estar autorizada por el comité.

| Replanificaciones | Atraso vs. original | Meses declarando sin sustento | Cambios de gobierno |
|---|---|---|---|
| 1 | 33 días (6,2 %) | No calculable | 0 documentados |

"Meses declarando sin sustento" no se puede calcular porque solo hay una declaración de estado (2026-10-09), no una serie.

**Lo que muestran los documentos:**
- **Replanificación anterior a su autorización:** el cronograma v2 es del 2026-10-09 y la solicitud de cambio CC-01 que la sustenta es del 2026-10-14. El script marca `change_without_baseline`: CC-01 aprobada sin una línea base nueva registrada.
- **Autorización sin rastro:** CC-01 dice "Autorizada por el comité", pero el acta del comité de ese mismo día no la menciona.
- **Actas tardías:**
  - Integración con el ERP: acta del 2026-10-08, línea base 2026-08-22.
  - Ambiente de pruebas certificado: acta del 2026-10-11, línea base 2026-05-07.
- **Hito sin soporte:** "Diseño de la experiencia aprobado" (2026-01-20) figura cumplido sin ningún documento de respaldo (270 días, según el script).
- **Avance declarado:** 36 %, frente a 60-80 % que sostiene el plan. Está por debajo del plan, no por encima; no lo interpreto.
- **Informe en verde:** reconoce que la prueba de carga no alcanzó el umbral y que el proveedor no confirmó la última entrega.
- **Dinero:** ejecutado 59,7 %, comprometido 65,7 %, proyección -1,9 % frente al aprobado. No puedo afirmar si la proyección incluye los 66.000.000 COP de CC-01.
- **Compromisos:** solo uno, de Paula Céspedes, "Entregar el punto 29", para 2026-11-14. No se repitió ni venció.

**Lo que no sé:**
- Qué pasó entre 2025-10 y 2026-09, porque no hay documentos de ese período.
- Si el comité realmente autorizó CC-01 y dónde quedó registrado.
- Desde cuándo lo declarado dejó de sostenerse: no puedo fechar el punto de separación con una sola declaración.

Esto no atribuye intención: son brechas entre fechas y documentos, y qué las explica es una conversación para tener con el gerente y el patrocinador. Puedo llevar la historia al cierre del proyecto o al comité del 2026-10-22, por ejemplo para registrar la línea base nueva de CC-01.

**Pie de rigor:** es un borrador de trabajo basado en 9 documentos. Cada cifra derivada sale de `portafolio.py compute` del 2026-10-17. Verifique contra los originales antes de usarlo.

La corrida quedó registrada como `2026-10-17-project-history-1`, con la salida completa en `estado/corridas/salida-project-history.md`.