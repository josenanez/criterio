# /criterio-portfolio:budget-tracking PRY-206

**Fuentes:** el acta de constitución del 2025-06-16 y el informe de avance con corte al 2026-10-14. Las cifras derivadas salen del script `compute`, al 2026-10-23. Los términos ya estaban vigentes (v0.8.0, aceptados por José Francisco Ñáñez el 2026-10-23), así que no los registré otra vez.

## Presupuesto — PRY-206 Precios dinámicos al 2026-10-23
**Moneda:** COP. Es la única, y no hubo conversión.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 6.800.000.000 | 100% | Acta de constitución | 2025-06-16 |
| Comprometido | 4.549.637.864 | 66.9% | Informe de avance (declaración del gerente) | 2026-10-14 |
| Ejecutado | 2.471.333.613 | 36.3% | Informe de avance (declaración del gerente) | 2026-10-14 |
| Proyección al cierre | 7.989.396.294 | 117.5% | Informe de avance (declaración del gerente) | 2026-10-14 |

**Disponible real** (aprobado menos comprometido): COP 2.250.362.136. La proyección dice que ni eso alcanza.

**Contra la línea base:**
- El aprobado original y el vigente son iguales: 6.800.000.000. Hay 0 replanificaciones de presupuesto.
- La proyección queda 17.5% por encima del aprobado. El umbral de la configuración es 10%.

**Ejecución frente a avance:**
- El ejecutado es 36.3% y el avance declarado es 60%.
- La ficha no tiene hitos, así que no puedo cruzarlo con hitos cumplidos.
- Los documentos no permiten saber si el avance está sobrestimado o si hay trabajo hecho que aún no se ha causado.

**Alertas:**
- **Proyección sobre el aprobado.** Excede en 17.5% y el informe no lo explica. Lo declara en amarillo.
- **Fecha de fin vencida.** El plan terminaba el 2026-06-09, no hay replanificación y el script no da un atraso en días.
- **Declaración sin evidencia.** Comprometido, ejecutado y proyección son declaración del gerente; ninguno tiene evidencia.
- **Aprobado envejecido.** El acta tiene 16 meses; el umbral de dato envejecido es 12.
- **Comprometido.** Está en 66.9%, por debajo del umbral de 90%, y no genera alerta.

**Sin dato:**
- Hitos del plan.
- Detalle por proveedor o contrato.
- Cambios de presupuesto.
- Evidencia que respalde las cifras declaradas.

Como la proyección excede el aprobado, puedo preparar la solicitud de cambio con `/criterio-portfolio:change-control`. No la preparé.

*Pie de rigor:* esto es un borrador de trabajo, no una decisión ni asesoría. Cada cifra viene del documento citado y del cálculo del script, y la verificación es de quien lo lee. No sé nada de lo que se habló fuera de esos dos documentos.

La corrida quedó registrada como `2026-10-23-budget-tracking-1` (47 segundos). El informe completo está en `estado/corridas/salida-budget-tracking.md`.