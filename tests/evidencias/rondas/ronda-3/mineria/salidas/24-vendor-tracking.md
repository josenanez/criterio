# /criterio-portfolio:vendor-tracking PRY-203

## Proveedores — PRY-203 Despacho automático de flota al 2026-10-15

Revisé el contrato CT-683 de Montajes Industriales Ltda. contra sus actas de recibo y su factura. La bolsa de horas está recibida y facturada. El licenciamiento del software lleva 210 días vencido, sin entrega ni factura.

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré de nuevo.

**Entregables de CT-683:**

| Entregable | Comprometido | Estado | Facturado |
|---|---|---|---|
| Licenciamiento del software (1.025.448.522 COP) | 2026-03-19 | Pendiente, vencido hace 210 días, sin acta de recibo | No |
| Bolsa de horas de ingeniería (1.025.448.522 COP) | 2026-09-04 | Recibido: acta del 2026-09-05, firmada por el gerente Camilo Beltrán | Sí: FV-1683 del 2026-09-08 por 1.025.448.522 COP |

- **Cruce:** la factura coincide en monto y en fecha con la bolsa de horas, que ya tenía acta. El script no levanta la señal de facturado sin entrega, y no hay entregables aceptados sin evidencia.
- **Concepto de la factura:** FV-1683 dice «Entregables del contrato CT-683», en plural y sin nombrar cuál. El monto solo cuadra con la bolsa de horas.
- **Acta de licencia:** el acta del 2026-10-06 «Licencia y permisos obtenidos» es un hito del proyecto. No sustenta el licenciamiento del proveedor.
- **Compromisos vencidos:** los 4 compromisos vencidos del proyecto son de personas del equipo, no del proveedor. Hay una «revisión con el proveedor» a cargo de Óscar Ramírez para el 2026-10-25, que aún no vence.
- **Riesgo sin registrar:** en las notas del 2026-10-15 se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase. Nadie lo registró como riesgo.

**Sin dato:**
- La vigencia, la renovación automática, el preaviso y el vencimiento de CT-683 no están en el contrato de la carpeta. No puedo decir si el preaviso vence antes del cierre del proyecto.
- No sé cuál es «la última entrega» que el proveedor no ha confirmado, según el informe de avance del 2026-10-13.
- Ningún documento vincula el hito vencido «Montaje e instalación» (10 días de atraso) con este contrato.
- Los dos documentos del proyecto fijan el fin en fechas distintas: 2027-01-05 (cronograma) y 2027-02-21 (acta de constitución).

**Para el comité:** no hay facturas sin evidencia que llevar. Sí vale llevar el licenciamiento vencido y sin explicación escrita, y el riesgo del equipo incompleto sin registrar. Conviene pedir el texto completo de CT-683 con su vigencia.

La salida completa quedó en `estado/corridas/salida-vendor-tracking.md`. La corrida `2026-10-15-vendor-tracking-1` quedó registrada con caso PRY-203 y tardó 37 segundos. Este informe es un borrador de trabajo: la verificación contra los documentos es suya. Al leer los PDF solo tuve el texto, así que no pude comprobar la firma del acta.