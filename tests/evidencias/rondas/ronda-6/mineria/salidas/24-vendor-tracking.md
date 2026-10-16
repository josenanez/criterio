# /criterio-portfolio:vendor-tracking PRY-201

# Proveedores — PRY-201 Ampliación de la relavera, al 2026-10-16

**Salen de:** los contratos CT-600 y CT-563, la factura FV-2600, el acta de recibo del 2026-10-07, el informe de avance del 2026-10-15, el comité del 2026-10-08 y el cálculo de `portafolio.py compute`. Los términos ya estaban vigentes (v1.1, aceptados el 2026-10-16 por José Francisco Ñáñez), así que no registré nada nuevo.

**Hallazgo principal:** Montajes Industriales (CT-600) tiene radicada la factura FV-2600 por 371.934.503 COP (2026-09-23). Ninguno de sus 3 entregables está aceptado ni tiene acta de recibo. El contrato pide acta de recibo firmada por el gerente del proyecto para facturar cada entregable. Esa acta no está en la carpeta.

**Entregables vencidos y sin evidencia** (los dos proveedores comparten los mismos entregables y fechas):
- **Licenciamiento del software:** comprometido para el 2026-06-12, 126 días de atraso.
- **Bolsa de horas de ingeniería:** comprometida para el 2026-10-08, 8 días de atraso.
- **Calibración de sensores:** comprometida para el 2027-02-02, aún no vence.

| Proveedor | Contrato | Entregables aceptados | Facturado |
|---|---|---|---|
| Montajes Industriales Ltda. | CT-600 | 0 de 3 | 371.934.503 COP |
| Servicios Ambientales del Norte | CT-563 | 0 de 3 | sin dato (no hay factura) |

**Dónde no cuadra:**
- **Avance declarado:** el informe declara verde y 76% de avance. El plan sustenta entre 40% y 60% (2 de 5 hitos), una diferencia de 16,0 puntos. El hito "Ingeniería de detalle aprobada" figura cumplido sin acta, 73 días después de su fecha.
- **Acta del 2026-10-07:** recibe "Ingeniería básica aprobada", que es un hito del proyecto y no un entregable de ningún contrato. No sustenta la factura.
- **Alcance de los contratos:** los dos listan los mismos tres entregables con las mismas fechas. Puede ser una plantilla repetida o un solapamiento de alcance. Los documentos no lo aclaran.
- **Comprometido:** el informe reporta 1.599.687.700 COP y no pude reconciliarlo con los montos de los contratos.

**Compromisos del proveedor vencidos:** ninguno. El único abierto es de Carlos Peña ("Entregar el punto 36", para el 2026-10-28), y los documentos no dicen si es de alguno de los proveedores.

**Sin dato:**
- Vigencia, renovación y preaviso de ambos contratos (solo traen la fecha de firma). No puedo decir si algún preaviso vence antes del cierre del plan, 2027-04-18.
- Factura de CT-563.
- Qué entregables cubre FV-2600 (dice solo "Entregables del contrato CT-600").
- El estado real de los entregables: sin actas ni correos, por regla es `unknown`, no `delivered`.

**Recomendación:** llevar FV-2600 a comité antes de pagarla, y pedir a ambos proveedores el acta de recibo y el texto completo de los contratos.

Corrida registrada como `2026-10-16-vendor-tracking-1`, con 37 segundos medidos. La salida completa está en `estado/corridas/salida-vendor-tracking.md`.

Criterio produce borradores de trabajo, no decisiones ni asesoría. La verificación es suya.