# /criterio-portfolio:budget-tracking PRY-207

## Presupuesto — PRY-207 Onboarding PyME al 2026-10-14

**Fuentes:** la ficha `estado/records/PRY-207.json` y el cálculo de `portafolio.py compute` con corte 2026-10-14. Las cuatro cifras salen de un solo documento, el informe de avance del gerente del 2026-10-14. Los términos están aceptados (José Francisco Ñáñez, v1.0, 2026-10-14). La moneda es COP, la única que aparece.

| | Monto (COP) | % del aprobado |
|---|---|---|
| Aprobado | 3.300.000.000 | 100% |
| Comprometido | 2.194.692.657 | 66.5% |
| Ejecutado | 1.916.164.829 | 58.1% |
| Proyección al cierre | 4.055.804.996 | 22.9% por encima del aprobado |

El disponible real (aprobado menos comprometido) es 1.105.307.343 COP. Las cuatro cifras son declaraciones del gerente. Ningún documento contable o contractual las respalda.

**Alertas**
- **La proyección excede el aprobado en 22.9%.** El umbral es 10%.
- **El estado declarado es verde pese a esa señal.** El informe reporta él mismo la proyección que lo contradice.
- **CC-01 está aprobado sin línea base nueva.** Suma 25 días y 50.000.000 COP, y dice "autorizada por el comité" sin acta que lo registre. La línea base de fechas sigue en 2026-01-14, anterior al corte, y no hay replanificación registrada.
- **El comprometido (66.5%) está bajo el umbral de 90%.** No genera alerta.

**Contra el avance:** no se puede cruzar contra hitos porque el plan no tiene ninguno cargado. El 72% de avance declarado supera el 58.1% ejecutado. Sin hitos no se puede decir si eso es eficiencia o avance sobrestimado.

**Sin dato**
- El presupuesto original no está declarado en ningún documento, así que la desviación contra la línea base original no se puede calcular.
- No se sabe si los 3.300.000.000 incluyen los 50.000.000 de CC-01.
- No hay hitos.
- No hay proveedores ni contratos en la ficha. El informe menciona un componente entregado y pendiente de aceptación.
- Faltan la autoridad de aprobación y la fase del proyecto.

La proyección excede el aprobado, así que ofrezco preparar la solicitud de cambio de presupuesto con `/criterio-portfolio:change-control`. No la preparé porque en esta sesión nadie puede confirmar el alcance.

La corrida quedó registrada como `2026-10-14-budget-tracking-1`, con la salida completa en `estado/corridas/salida-budget-tracking.md`.