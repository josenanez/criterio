# /criterio-portfolio:vendor-tracking PRY-208

**Sale de:** el contrato CT-751, el acta de recibo de la bolsa de horas, la factura FV-1751, el informe de avance del 2026-10-14, el comité del 2026-10-14, la ficha de PRY-208 y la salida de `compute` al 2026-10-23. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-23), así que no hubo que registrarlos de nuevo.

## Proveedores — PRY-208 Reducción de quema de gas

**Integridad y Corrosión S.A.S. (CT-751).** El contrato no trae vigencia, renovación ni preaviso, solo la firma del 2025-06-26. No se puede decir si algún preaviso vence antes del cierre del proyecto (2026-11-23).

| Entregable | Comprometido | Estado | Evidencia | Facturado |
|---|---|---|---|---|
| Alquiler del taladro (50.106.103 COP) | 2026-01-05 | Pendiente, 291 días vencido | Ninguna | No |
| Bolsa de horas de ingeniería (50.106.103 COP) | 2026-07-10 | Aceptada | Acta firmada por Liliana Torres, 2026-07-18 | Sí, FV-1751 del 2026-09-23 por 50.106.103 COP |

**Dónde no cuadra:**
- **Factura contra lo aceptado:** lo facturado (50.106.103) es igual a lo aceptado (50.106.103), y el script no levantó `vendor_invoiced_without_delivery`.
- **Concepto de la factura:** dice «Entregables del contrato CT-751» sin nombrar cuál. Los dos entregables valen lo mismo, y solo el acta permite atribuirla a la bolsa de horas.
- **Informe contra contrato:** el informe declara que se reprogramó la movilización del taladro y marca el proyecto en verde. No hay solicitud de cambio ni nueva fecha contractual.

**Sin evidencia de recibo:** ningún entregable de CT-751 está marcado como entregado sin acta.

**Compromisos del proveedor vencidos:** ninguno atribuible. El único compromiso abierto es de Ricardo Salas, «Entregar el punto 12», vencido hace 4 días. Ningún documento dice que sea del proveedor, así que no lo conté aquí.

**Sin dato:**
- Vigencia, renovación y preaviso del contrato.
- Total contractual (solo constan los dos montos).
- Si el taladro tiene una nueva fecha acordada.
- Otros proveedores (la ficha solo trae uno).

**Para decidir:** el taladro sigue vencido sin cambio aprobado y la fecha de fin del proyecto no se ha movido. Decide si se lleva a comité. No hay facturas sin evidencia que escalar.

Fuera de lo que mide este comando, el informe declara verde con cuatro señales sin explicar: el compromiso vencido, tres hitos «cumplidos» sin evidencia, un avance de 51% frente a 80–100% que sostiene el plan, y el taladro tardío.

La salida completa quedó en `estado/corridas/salida-vendor-tracking.md` y la corrida se registró como `2026-10-23-vendor-tracking-1` (caso PRY-208). Las cifras de la corrida abarcan los 13 proyectos del portafolio, no solo PRY-208. Criterio produce borradores de trabajo, no decisiones ni asesoría; la verificación contra los documentos citados es de quien lo lea.