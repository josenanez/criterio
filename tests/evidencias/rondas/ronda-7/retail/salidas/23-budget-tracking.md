# /criterio-portfolio:budget-tracking PRY-205

## Presupuesto — PRY-205 Pago con QR en caja al 2026-10-17
**Fuentes:** la ficha de PRY-205 y el cálculo del script con corte al 2026-10-17. Las cifras de comprometido, ejecutado y proyección salen del informe de avance del 2026-10-14. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no hubo que registrarlos de nuevo. Todo está en COP; no hay otra moneda ni conversiones.

| | Monto (COP) | % del aprobado | Fuente | Fecha |
|---|---|---|---|---|
| Aprobado | 3.300.000.000 | 100 | Acta de constitución | 2025-12-17 |
| Comprometido | 3.152.315.214 | 95,5 | Informe de avance (declaración) | 2026-10-14 |
| Ejecutado | 1.792.674.413 | 54,3 | Informe de avance (declaración) | 2026-10-14 |
| Proyección al cierre | 3.379.087.994 | 102,4 | Informe de avance (declaración) | 2026-10-14 |

**Disponible real** (aprobado menos comprometido): 147.684.786 COP.

- **Línea base:** el presupuesto aprobado no ha cambiado y hay 0 replanificaciones de presupuesto. CC-01 pide +150.000.000 COP, pero su decisión está pendiente y no se suma al aprobado.
- **Ejecución frente a avance:** ejecutado 54,3 % y hitos cumplidos 2 de 4, con avance declarado de 50 %. Van parejos en magnitud. Pero uno de esos dos hitos ("Ambiente de pruebas certificado", vencido el 2026-07-24) no tiene evidencia de recibo; con evidencia solo hay 1 de 4.

### Alertas
- **Comprometido en 95,5 %, sobre el umbral de 90 %.** Solo se ha ejecutado el 54,3 %, pero el presupuesto está casi agotado y quedan 147.684.786 COP libres.
- **La proyección excede el aprobado en 2,4 %.** No hay margen sin una decisión de presupuesto.
- **El cronograma v2 ya asume CC-01, que sigue sin decidir.** Mueve el cierre 75 días (de 2027-02-19 a 2027-05-05) sin autorización. La desviación de tiempo contra la línea base original es de 17,9 %, sobre el umbral de 10 %.
- **El informe de avance declara "verde"** y no reconoce ninguna de estas señales.

### Sin dato
- Faltan la autoridad que aprueba el presupuesto y la fase del proyecto.
- Comprometido, ejecutado y proyección son solo declaración del gerente. Ningún contrato, factura ni extracto contable los respalda.
- No se dice en ningún documento si la proyección ya incluye los 150 M de CC-01.
- No hay proveedores en la ficha, así que no se puede abrir el detalle por proveedor.

**Siguiente paso:** puedo preparar la solicitud de cambio de presupuesto, porque la proyección excede el aprobado y CC-01 está pendiente de presentación al comité. El detalle por proveedor requiere los contratos.

*Pie de rigor: borrador de trabajo, no decisión ni asesoría. Cada cifra sale del script o de la ficha, y la verificación contra los documentos es suya.*

La salida quedó en `estado/corridas/salida-budget-tracking.md`. La corrida quedó registrada como `2026-10-17-budget-tracking-1` (13 proyectos leídos, 23 segundos).