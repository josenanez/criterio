# /criterio-portfolio:budget-tracking PRY-206

## Presupuesto — PRY-206 Pagos con QR, al 2026-10-15

**Moneda:** COP. Es la única que aparece en los documentos, así que no hubo conversión.

Los términos ya estaban vigentes a nombre de José Francisco Ñáñez (2026-10-15). No tuve que registrarlos de nuevo.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 2.400.000.000 | — | Acta de constitución | 2026-06-10 |
| Comprometido | 720.144.603 | 30,0 % | Informe de avance (declaración) | 2026-10-12 |
| Ejecutado | 821.233.249 | 34,2 % | Informe de avance (declaración) | 2026-10-12 |
| Proyección al cierre | 3.033.676.286 | 26,4 % por encima del aprobado | Informe de avance (declaración) | 2026-10-12 |

**Disponible real** (aprobado menos comprometido): 1.679.855.397 COP. Puede estar sobrestimado, por la segunda alerta.

**Contra la línea base:**
- **Presupuesto:** el original es 2.400.000.000. No hay presupuesto vigente registrado en ningún documento, así que la desviación no se puede calcular.
- **Replanificaciones de presupuesto:** 0. La única replanificación (v2, 2026-10-12) es de cronograma: +20 días, 5,9 % sobre la fecha original, sin motivo declarado.

**Ejecución frente a avance:** el ejecutado es 34,2 %, el avance declarado es 50 % y hay 1 de 4 hitos cumplidos. El gasto no va por delante del avance. Pero el único hito cumplido, «Diseño funcional aprobado», no tiene evidencia, así que ese 50 % es una declaración.

**Alertas:**
1. **La proyección excede el aprobado en 26,4 %.** El umbral es 10 % y el informe no explica el exceso.
2. **El comprometido (720.144.603) es menor que el ejecutado (821.233.249).** Lo normal es que lo comprometido incluya lo ejecutado. Si el informe reporta solo lo pendiente por causar, el comprometido real es mayor y el disponible real menor. No lo corregí; lo dejé señalado.
3. **CC-01 se aprobó sin línea base de costo nueva.** Agrega 40.000.000 COP y +20 días, y el documento dice que decidió «el comité», sin nombrar a nadie.
4. **La proyección es más vieja que CC-01.** La proyección es del 2026-10-12 y CC-01 es del 2026-10-15. No está declarado si la proyección ya incluye esos 40.000.000.
5. **El comprometido está en 30,0 %,** lejos del umbral de 90 %.

**Sin dato:**
- El presupuesto vigente después de CC-01.
- El motivo de la replanificación v2.
- Si el comprometido incluye lo ejecutado.
- Si la proyección incluye CC-01.
- La evidencia del hito cumplido.
- No hay proveedores en la ficha, así que no hay detalle por proveedor.

Comprometido, ejecutado y proyección vienen de un informe de avance en PDF, sin contraste con registros contables.

**Siguiente paso:** puedo preparar la solicitud de cambio de presupuesto. CC-01 cubre 40.000.000 de una brecha de 633.676.286 que ya muestra la proyección.

Es un borrador de trabajo, no asesoría. Las cifras salen de la ficha y de `portafolio.py compute`, y la verificación contra los documentos es de quien lo use.

La corrida quedó registrada como `2026-10-15-budget-tracking-1` (28 segundos). El texto completo está en `estado/corridas/salida-budget-tracking.md`.