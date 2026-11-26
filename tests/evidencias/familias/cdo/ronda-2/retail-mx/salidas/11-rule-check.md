# /criterio-data-quality:rule-check 

Las reglas de calidad de Retail Central Sintético (RCM190305AB1) del periodo 2026-11, con corte 2026-11-25. Los términos v1.6 ya estaban aceptados por José Francisco Ñáñez el 2026-11-25. El periodo salió de la configuración.

**Reglas bajo su umbral**
- RQ-02 sobre Movimiento.valor, dato crítico: dio 96.1 y su umbral es 98.
- RQ-12 sobre Cliente.correo: dio 91 y su umbral es 95.

**Reglas sin corrida en el periodo**
- RQ-03 (Crédito.fecha_desembolso, crítico) y RQ-22 (Cuenta.saldo, crítico) no tienen resultado.
- RQ-04 (Proveedor.correo) tampoco tiene, pero el dato no es crítico y el reporte no lo marca como señal.

**Datos críticos que ninguna regla mide**
- Cliente.ingresos y Crédito.calificación.

La única regla que pasa es RQ-01 (Cliente.documento), con 99.6 frente a un umbral de 99.

El reporte completo, con las citas por fila, está en `calidad/2026-11/reporte-rule-check.md`.

La salida está en `estado-datos/rcm190305ab1-retail-central-sintetico/corridas/salida-rule-check.md`. La corrida quedó registrada como `2026-11-25-rule-check-1`, con 14 hallazgos.

Nadie respondió preguntas en esta corrida y no hizo falta ninguna.