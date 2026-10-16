# /criterio-portfolio:vendor-tracking PRY-200

## Proveedores — PRY-200 Crédito de libranza digital al 2026-10-16

**Sale de:**
- la ficha `estado/records/PRY-200.json`;
- la salida de `portafolio.py compute`, con corte al 2026-10-16;
- los contratos CT-802 y CT-395;
- el acta de recibo de CT-802 (2025-12-01);
- el informe de avance del 2026-09-26.

Los dos PDF de factura no tienen texto extraíble. Sus montos salen de la ficha y no los pude contrastar con el documento.

Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

CT-802 cuadra. CT-395 tiene 207.643.011 COP facturados con 0 de 4 entregables aceptados. El informe declara verde y 25 %, pero el plan marca los 5 hitos como cumplidos y ninguno tiene evidencia.

### Talento Solidario Ltda. — CT-802
Vigencia, preaviso y vencimiento: el contrato no los dice. Solo trae fecha de firma (2025-06-10).

| Entregable | Comprometido | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del módulo | 2025-11-13 | aceptado | Acta de recibo del 2025-12-01, firmada por Ricardo Salas |
| Bolsa de horas de desarrollo | 2026-04-04 | pendiente, 195 días de atraso | ninguna |

Se facturaron 148.158.298 COP (factura del 2026-09-03). Es igual al monto aceptado con acta, así que cuadra.

### Soluciones Solidarias S.A.S. — CT-395
Vigencia, preaviso y vencimiento: el contrato no los dice. Solo trae fecha de firma (2025-06-13).

| Entregable | Comprometido | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del módulo | 2025-09-18 | pendiente, 393 días | ninguna |
| Bolsa de horas de desarrollo | 2025-12-12 | pendiente, 308 días | ninguna |
| Parametrización de líneas de crédito | 2026-03-07 | pendiente, 223 días | ninguna |
| Mesa de ayuda del primer trimestre | 2026-05-31 | pendiente, 138 días | ninguna |

Se facturaron 207.643.011 COP (factura del 2026-09-06). El monto aceptado con acta es 0.

### Dónde no cuadra
- **CT-395 facturado sin entrega.** Su condición de pago exige un acta de recibo firmada por el gerente del proyecto. No hay ninguna acta de recibo de CT-395.
- **Hitos del plan contra proveedores.** El cronograma marca como cumplidos "Integración con el core cooperativo", "Piloto con asociados" y "Salida a producción". Con el licenciamiento, la parametrización y la mesa de ayuda de CT-395 sin recibir, esos hitos no tienen sustento en las entregas.
- **Estado declarado.** El informe dice verde y 25 %. El plan da 100 %, una brecha de 75,0 puntos, y hay 5 señales abiertas: silencio, avance, hitos sin evidencia, entregables tarde y factura sin entrega.

### Sin evidencia de recibo
- Los 4 entregables de CT-395 y la bolsa de horas de CT-802.
- Los 5 hitos del plan marcados como cumplidos, con 401, 324, 247, 169 y 92 días desde su fecha.

Ningún entregable está aceptado sin evidencia. El problema es el contrario: entregables sin recibir que ya se facturaron.

### Compromisos del proveedor vencidos
La ficha no tiene compromisos y la carpeta no trae minutas. El informe menciona un riesgo, "el proveedor no ha confirmado la fecha de la última entrega", pero sin dueño ni fecha. Sin dato.

### Sin dato
- La vigencia, la renovación automática y el preaviso de ambos contratos. No puedo decir si algún preaviso vence antes del cierre.
- El contenido de las facturas PDF.
- Contra qué entregable se facturó en CT-395, porque hay un solo total por contrato.
- El proyecto lleva 20 días en silencio, con el último documento del 2026-09-26.

### Después
No hay un preaviso por vencer que pueda afirmar, porque ningún contrato trae vigencia. El hallazgo para comité es CT-395: 207.643.011 COP facturados sin un solo entregable aceptado. Puedo preparar ese punto para el comité del 2026-10-23 si lo pides.

*Pie de rigor: es un borrador de trabajo, no una decisión ni asesoría. Los días, sumas y conteos están copiados de `compute`. Cada dato remite al documento citado y la verificación es suya. No sé lo que se haya hablado fuera de esos documentos.*

La salida completa quedó en `estado/corridas/salida-vendor-tracking.md`. La corrida quedó registrada como `2026-10-16-vendor-tracking-1`.