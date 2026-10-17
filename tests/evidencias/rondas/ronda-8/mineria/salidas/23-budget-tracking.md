# /criterio-portfolio:budget-tracking PRY-200

## Presupuesto — PRY-200 (Mantenimiento predictivo de camiones) al 2026-10-17

Las cifras salen de `portafolio.py compute` y de la ficha `estado/records/PRY-200.json`, construida con 6 documentos del proyecto. El más reciente es la solicitud de cambio CC-01, del 2026-10-12. Los términos ya estaban vigentes, aceptados por José Francisco Ñáñez (versión 0.3.13, 2026-10-17), así que no los registré de nuevo.

**Moneda:** COP. Es la única, sin conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 800.000.000 | 100 % | acta de constitución | 2025-12-27 |
| Comprometido | 624.011.195 | 78.0 % | informe de avance | 2026-10-09 |
| Ejecutado | 163.775.869 | 20.5 % | informe de avance | 2026-10-09 |
| Proyección al cierre | 883.635.954 | excede el aprobado en 10.5 % | informe de avance | 2026-10-09 |

**Disponible real** (aprobado menos comprometido): 175.988.805 COP.

Comprometido, ejecutado y proyección son declaraciones de un informe de avance. Ningún documento de evidencia (contrato, factura, extracto) las respalda.

### Contra la línea base
- **Presupuesto:** no hay ninguna replanificación aprobada. El original y el vigente son 800.000.000 COP.
- **CC-01 (2026-10-12):** ampliación de alcance, 208.000.000 COP adicionales y +104 días. Está pendiente, sin decisión ni decisor.
- **Cronograma:** el fin pasó de 2027-04-11 a 2027-07-24, 104 días (22.6 %). Ningún cambio aprobado lo autoriza y el motivo figura como `not_found`.

### Ejecución frente a avance
- **Cifras:** ejecutado 20.5 %, hitos cumplidos 2 de 4, avance declarado 36 %. El plan sustenta entre 50 y 75 %, o sea 14.0 puntos de atraso.
- **Lectura:** la ejecución va por debajo del avance, no por encima. Eso puede ser trabajo hecho y no facturado, o trabajo no hecho, y los datos no permiten saber cuál.
- **Hitos:** los dos que figuran cumplidos no tienen evidencia de aceptación: Ingeniería básica (vencía el 2026-05-01) e Ingeniería de detalle (vencía el 2026-08-24).

### Alertas
- **Proyección sobre el aprobado:** supera el umbral de 10 % por poco, con 10.5 %.
- **Proyección anterior a CC-01:** la proyección es del 2026-10-09 y CC-01 del 2026-10-12. El informe no dice si ya la incluye. Si no la incluye, la proyección está vieja frente al último movimiento de presupuesto.
- **Comprometido:** 78.0 %, por debajo del umbral de 90 %. Sin alerta.
- **Estado declarado:** rojo, pero el informe no explica 5 de las señales abiertas: tiempo, costo, avance contra plan, hitos sin evidencia y replanificación no autorizada.

### Sin dato
- **Autoridad que aprueba:** `identity.authority` es `not_found`, así que no se sabe quién decide CC-01.
- **Fase del proyecto:** `not_found`.
- **Motivo de la replanificación v2:** `not_found`.
- **Corte contable:** la fecha exacta del comprometido y del ejecutado. Solo se conoce la del documento.
- **Proveedores:** no hay ninguno ni contrato en la ficha, así que no hay detalle por proveedor.

**Siguiente paso:** evaluar CC-01 con `/criterio-portfolio:change-control`. No ofrezco preparar una solicitud nueva porque CC-01 ya está presentada.

La corrida quedó registrada como `2026-10-17-budget-tracking-1`. El informe completo está en `estado/corridas/salida-budget-tracking.md`.

*Pie de rigor: borrador de trabajo, no decisión ni asesoría. Cada dato lleva la cita de su documento y la verificación es suya. No sé lo que se habló fuera de los documentos.*