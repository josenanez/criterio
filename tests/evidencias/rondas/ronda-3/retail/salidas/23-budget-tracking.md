# /criterio-portfolio:budget-tracking PRY-208

**Fuentes:** la ficha de PRY-208, armada con el acta de constitución (2025-05-23), el cronograma v1 (2025-05-23) y el informe de avance (2026-10-11). Las cifras salen de `portafolio.py compute`, recalculado al 2026-10-15.

Los términos ya estaban vigentes (v0.3.9, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los volví a mostrar ni los registré otra vez.

## Presupuesto — PRY-208 Domicilios en dos horas, al 2026-10-15
**Moneda:** COP. Es la única moneda y no convertí nada.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 6.800.000.000 | 100% | acta de constitución | 2025-05-23 |
| Comprometido | 2.667.124.370 | 39.2% | informe de avance (declaración) | 2026-10-11 |
| Ejecutado | 2.364.534.774 | 34.8% | informe de avance (declaración) | 2026-10-11 |
| Proyección al cierre | 8.103.742.416 | 19.2% por encima del aprobado | informe de avance (declaración) | 2026-10-11 |

**Disponible real** (aprobado menos comprometido): 4.132.875.630 COP.

### Contra la línea base
- El aprobado original y el vigente son iguales: 6.800.000.000 COP, con desviación 0.
- No hay replanificaciones de presupuesto ni solicitudes de cambio registradas.
- La proyección supera el aprobado en 19.2% y no hay un cambio aprobado que la respalde.

### Ejecución frente a avance
Ejecutado 34.8% · Hitos cumplidos 4 de 4 (declarados) · Avance declarado 81%.

- **Lectura:** la ejecución está muy por debajo del avance declarado. Podría ser trabajo hecho y no facturado que aparezca de golpe, pero no puedo afirmarlo. Los 4 hitos figuran como cumplidos sin evidencia en ningún documento.
- **Plan:** el cronograma terminaba el 2026-01-28, hace 260 días, y respalda 100%. El informe declara 81%, una brecha de 19.0 puntos hacia atrás.

### Alertas
- **Proyección sobre el aprobado:** +19.2%, con umbral de 10%. Es una declaración del informe del 2026-10-11, no un dato duro. Como no hay movimientos de presupuesto, no es más vieja que el último.
- **Estado verde con tres señales abiertas:** el informe lo declara verde, pero siguen abiertos hitos cumplidos sin evidencia, avance contra plan y desviación de costo. El informe no las explica.
- **Hitos cumplidos sin evidencia (4):**
  - Diseño de la experiencia aprobado
  - Ambiente de pruebas certificado
  - Integración con el ERP
  - Piloto en tiendas
- **Dato viejo:** el monto aprobado viene de un acta de hace 17 meses, con umbral de 12.
- El comprometido está en 39.2%, por debajo del umbral de 90%, así que no hay alerta por ahí.

### Sin dato
- Autoridad de aprobación del presupuesto y fase del proyecto: no están en ningún documento.
- Por qué la proyección (8.103.742.416) está tan lejos de lo comprometido (2.667.124.370): ningún documento lo explica.
- Monto en pesos del exceso sobre el aprobado: el script solo da el porcentaje y no lo calculé a mano.
- Proveedores y contratos: la ficha no registra ninguno, así que no hay detalle por proveedor.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. No la preparé.

La corrida quedó registrada como `2026-10-15-budget-tracking-1`, con la salida guardada en `estado/corridas/salida-budget-tracking.md`.

**Pie de rigor:** esto es un borrador de trabajo, no una decisión. Todas las cifras de dinero son declaraciones del informe del 2026-10-11, salvo el aprobado, que viene del acta. Ninguna tiene evidencia independiente, así que la verificación contra los documentos es suya.