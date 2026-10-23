# /criterio-portfolio:vendor-tracking PRY-200

## Proveedores — PRY-200 Mantenimiento predictivo de camiones, al 2026-10-23

**Fuentes:** la ficha, el cálculo del script, el contrato CT-326, tres actas de recibo, la factura FV-1326, el informe de avance del 2026-10-18 y el comité del 2026-10-19. Los términos ya estaban vigentes (v1.2, a nombre de José Francisco Ñáñez).

**Equipos Pesados Andinos, contrato CT-326.** Se firmó el 2025-09-04. El contrato no declara fin de vigencia, renovación ni preaviso. No sé si hay un preaviso por vencer.

| Entregable | Comprometido | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del software | 2025-11-05 | pendiente, 352 días de atraso | ninguna |
| Bolsa de horas de ingeniería | 2025-12-18 | aceptado | acta de recibo del 2026-01-07 |
| Calibración de sensores | 2026-01-30 | aceptado | **ninguna** |
| Soporte del primer trimestre | 2026-03-14 | pendiente, 223 días de atraso | ninguna |

Cada entregable vale 275.896.256 COP.

**Dónde no cuadra**
- **Calibración de sensores:** solo figura como "recibido" en la columna de estado del propio contrato. No hay acta, correo ni minuta que lo pruebe.
- **Factura FV-1326:** es de 551.792.512 COP, radicada el 2026-09-02, con el concepto "Entregables del contrato CT-326". El contrato exige facturar cada entregable contra un acta firmada. Solo hay un acta de recibo de CT-326, la de la bolsa de horas. El monto de un entregable (275.896.256) queda sin acta.
- **Desglose:** la factura no dice qué entregables cubre. Supongo que son los dos aceptados, pero ella no lo dice.
- **Alerta del script:** no levantó `vendor_invoiced_without_delivery`, porque cuenta Calibración como aceptada. Esa aceptación es una declaración, no evidencia.

**Compromisos del proveedor vencidos:** ninguno. Del comité del 2026-10-19 quedan dos compromisos abiertos, de Liliana Torres (para 2026-10-23) y de Beatriz Cuéllar (sin fecha). Ninguno está ligado al proveedor, así que no los atribuyo a Equipos Pesados Andinos. El informe de avance sí menciona un riesgo: el proveedor no ha confirmado la fecha de la última entrega.

**Sin dato**
- Vigencia, renovación y preaviso de CT-326.
- Qué entregables cubre la factura.
- Las actas de "Montaje e instalación" (2026-10-21) y "Pruebas en operación" (2026-10-11) no corresponden a ningún entregable de CT-326. Son hitos del proyecto y no los crucé contra el proveedor.
- Tres hitos del cronograma figuran cerrados sin acta: Ingeniería básica, Ingeniería de detalle y Licencia y permisos. Es un hallazgo del proyecto, no del proveedor.

**Para comité (próximo: 2026-10-29):** hay una factura radicada con un entregable sin acta y dos sin entregar. Antes de pagar conviene pedir el acta de Calibración de sensores o el desglose de la factura. Si quieres, lo llevo a comité.

*Rigor: es un borrador de trabajo, no una decisión ni asesoría. Cada dato sale de los documentos citados y la verificación es tuya. Lo que se habló fuera de ellos no está aquí.*

La corrida quedó registrada como `2026-10-23-vendor-tracking-1`, con el texto completo en `estado/corridas/salida-vendor-tracking.md`.