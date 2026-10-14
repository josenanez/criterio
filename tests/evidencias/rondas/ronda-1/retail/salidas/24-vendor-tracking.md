# /criterio-portfolio:vendor-tracking PRY-206

## Proveedores — PRY-206 Precios dinámicos, al 2026-10-14

**Fuentes:** la ficha PRY-206, el contrato CT-140, el acta de recibo del 2026-08-02, la factura FV-1140, el informe de avance del 2026-10-07 y el cronograma v1. Las cifras vienen de `portafolio.py compute`. Los términos están aceptados (v1.0, 2026-10-14, José Francisco Ñáñez).

### Logística del Valle Ltda. — contrato CT-140
**Vigencia:** firmado el 2025-10-21. El contrato no trae fecha de terminación, renovación automática ni preaviso, así que no puedo decir si algún preaviso está por vencer.

| Entregable | Comprometido | Estado | Evidencia | Facturado |
|---|---|---|---|---|
| Licenciamiento de la plataforma (252.927.117 COP) | 2026-03-07 | Pendiente, atrasado 221 días | Ninguna | No consta; la factura no lo nombra |
| Bolsa de horas de desarrollo (252.927.117 COP) | 2026-07-20 | Aceptado | Acta de recibo del 2026-08-02, firmada por Carlos Peña | La FV-1140 cubre un entregable por 252.927.117 COP, sin decir cuál |

El script cuenta 2 entregables, 1 aceptado, 1 atrasado y 0 aceptados sin evidencia. Lo facturado y lo aceptado suman lo mismo: 252.927.117.

### Dónde no cuadra
- **La factura no dice qué cobra.** El contrato exige facturar cada entregable contra acta firmada. La FV-1140 (2026-09-10) usa el concepto genérico «Entregables del contrato CT-140». Su monto coincide con la Bolsa de horas, que sí tiene acta. Pero los dos entregables valen lo mismo, así que el monto no descarta que se haya facturado el licenciamiento.
- **La Bolsa de horas llegó tarde.** Estaba comprometida para el 2026-07-20 y se recibió el 2026-08-02.
- **No salta la señal de factura sin entrega** (`vendor_invoiced_without_delivery`), porque hay un entregable aceptado con acta.

### Sin evidencia de recibo
Ningún entregable está marcado como entregado sin acta. El licenciamiento sigue pendiente y vencido desde el 2026-03-07.

### Compromisos del proveedor vencidos
Ninguno. La ficha no tiene compromisos registrados y no hay minutas de comité con el proveedor en la carpeta.

### Contexto del proyecto
- **Estado frente a evidencia:** el informe declara verde y 40 %, pero el plan sostiene entre 80 y 100 %. Tampoco menciona el licenciamiento atrasado.
- **Hitos sin evidencia:** hay 4 hitos marcados como cumplidos sin evidencia: Diseño, Ambiente de pruebas, Integración con el ERP y Piloto en tiendas.
- **Despliegue y seguridad:** el despliegue del 2026-10-27 se reprogramó sin fecha nueva. Hay un hallazgo de seguridad en medios de pago sin dueño.

### Sin dato
- Vigencia, renovación y preaviso de CT-140.
- Qué entregable cubre la FV-1140.
- Compromisos del proveedor en comités, porque no hay minutas.

### Después
Ofrezco llevar a comité dos puntos:
1. Pedir a Logística del Valle que la FV-1140 nombre el entregable, y confirmar que el licenciamiento no se pagó.
2. El estado verde frente a la evidencia.

La corrida quedó registrada como `2026-10-14-vendor-tracking-1`, con la salida en `estado-portafolio/corridas/salida-vendor-tracking.md`. En la corrida, `por_caso` lista para PRY-206 siete señales abiertas, entre ellas `vendor_deliverable_late`.

**Pie de rigor:** cada dato de documento va citado y las cifras salen del script. No se infirió ninguna entrega sin acta.