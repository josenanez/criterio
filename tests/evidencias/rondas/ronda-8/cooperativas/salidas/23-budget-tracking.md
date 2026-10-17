# /criterio-portfolio:budget-tracking PRY-206

## Presupuesto — PRY-206 Pagos con QR, al 2026-10-17

Salió de la ficha de PRY-206, del acta de constitución (2026-04-15) y del informe de avance (2026-10-10). Las cifras derivadas vienen de `portafolio.py compute`. Los términos ya estaban vigentes (aceptados por José Francisco Ñáñez, v1.1, 2026-10-17), así que no hubo que volver a registrarlos.

**Moneda:** COP. Es la única; no hay conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 3.300.000.000 | 100% | acta de constitución | 2026-04-15 |
| Comprometido | 2.970.911.597 | 90.0% | informe de avance | 2026-10-10 |
| Ejecutado | 1.806.185.462 | 54.7% | informe de avance | 2026-10-10 |
| Proyección al cierre | 3.444.173.074 | 4.4% por encima del aprobado | informe de avance | 2026-10-10 |

**Disponible real** (aprobado menos comprometido): COP 329.088.403.

**Contra la línea base:** solo existe la línea base original (v1, 2026-04-15). No hay cambios de presupuesto registrados, así que el aprobado vigente es el original. Replanificaciones de presupuesto: 0.

**Ejecución frente a avance:**
- Ejecutado 54.7%, y 1 de 4 hitos cumplidos.
- El avance declarado es 83%, pero el plan solo respalda entre 25% y 50% (brecha de 33 puntos).
- El hito "Diseño funcional aprobado" figura como cumplido sin evidencia.
- "Ambiente de pruebas certificado" lleva 11 días vencido.

**Alertas:**
- **Comprometido:** está en el umbral del 90%. La holgura aparente del 45.3% sin ejecutar no es real, porque solo quedan COP 329.088.403 sin comprometer.
- **Proyección:** excede el aprobado en 4.4%. Es una declaración del informe del 2026-10-10, no un dato duro.
- **Avance declarado:** el 83% no está sustentado por el plan.
- **Compromiso vencido:** Jorge Medina, "Entregar el punto 14", vencido desde 2026-10-10 (7 días).

**Sin dato:**
- No hay una línea base de presupuesto vigente distinta de la original; se asume que no hubo cambios porque no hay ninguno registrado.
- Autoridad y fase del proyecto no están declaradas.
- La ficha no registra proveedores para PRY-206.

**Siguiente paso:** como la proyección excede el aprobado, puedo preparar la solicitud de cambio de presupuesto. El detalle por proveedor no se puede hacer: no hay proveedores registrados.

Las cuatro cifras son declaraciones en documentos (acta e informe), no datos de un sistema contable. La verificación es suya.

**Corrida registrada:** `2026-10-17-budget-tracking-1`. La salida completa quedó en `estado/corridas/salida-budget-tracking.md`. El registro de la corrida cuenta 13 proyectos y 69 hallazgos porque `compute` barre todo el portafolio; el informe es solo de PRY-206.