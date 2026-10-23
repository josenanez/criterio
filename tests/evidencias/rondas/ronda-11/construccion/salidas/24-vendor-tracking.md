# /criterio-portfolio:vendor-tracking PRY-201

## Proveedores — PRY-201 Edificio de oficinas Torre Norte, al 2026-10-22

**Qué leí:** el contrato CT-521, la ficha, las actas de `20-seguimiento`, el informe de avance del 2026-10-21, los 6 comités y las notas del 2026-10-22. Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-22). No hizo falta registrarlos de nuevo.

### Interventorías Técnicas S.A.S. — contrato CT-521
No hay vigencia, fecha de terminación, renovación automática ni preaviso. El contrato solo trae la fecha de firma, 2026-04-14.

| Entregable (COP 77.546.392 c/u) | Comprometido | Estado | Evidencia | Facturado |
|---|---|---|---|---|
| Suministro de acero de refuerzo | 2026-06-28 | pendiente, 116 días de atraso | ninguna | sin dato |
| Bolsa de horas de ingeniería | 2026-09-01 | el contrato dice «en curso» y la ficha la recoge como pendiente; 51 días pasada la fecha | ninguna | sin dato |
| Alquiler de equipos de izaje | 2026-11-04 | pendiente, aún no vence | ninguna | sin dato |

El script da 3 entregables, 0 aceptados, 2 tardíos y 0 aceptados sin evidencia. No dio ninguna factura.

### Dónde no cuadra
- **Bolsa de horas:** el contrato la marca «en curso», pero la ficha la registra pendiente y no hay acta ni mención de avance.
- **Informe de avance en verde:** el informe del 2026-10-21 declara verde con dos entregables del proveedor vencidos y sin evidencia.
- **Facturación:** no hay facturas declaradas en los documentos, así que no se levantó la señal de factura sin entrega.

### Sin evidencia de recibo
- Ninguno de los tres entregables figura como entregado o aceptado.
- Las actas de recibo de la carpeta son de compromisos internos o de otros entregables: «matriz 6», «prueba 10» y «Diseños de detalle aprobados». No las usé como evidencia del proveedor.

### Compromisos del proveedor vencidos
- Ninguno. Óscar Ramírez tiene una «revisión con el proveedor» para el 2026-11-01, que aún no vence.
- Los 9 compromisos vencidos del proyecto son de personas internas y van en `/commitment-tracking`.

### Sin dato
- Vigencia y preaviso de CT-521. No puedo decir si el preaviso vence antes del cierre del proyecto (2026-12-15).
- Monto facturado.
- Evidencia de aceptación de los tres entregables.
- Las notas del 2026-10-22 dicen que «el proveedor podría no llegar con el equipo completo» y que nadie lo anotó como riesgo. No dicen de qué proveedor. Es un candidato a RAID, no un hallazgo de este informe.

### Después
El contrato factura cada entregable contra un acta de recibo firmada por el gerente del proyecto. Hoy no hay acta ni factura. Antes de aprobar cualquier factura hay que exigir el acta. Con el acero y la bolsa de horas en 116 y 51 días de atraso y el informe en verde, vale llevarlo a comité.

**Rigor:** las cifras salen de `portafolio.py compute`. Solo recalculé a mano los 13 días hasta el 2026-11-04. Lo hablado fuera de los documentos no lo sé.

La corrida quedó registrada como `2026-10-22-vendor-tracking-1`, con 28 segundos medidos. Esta salida está en `estado/corridas/salida-vendor-tracking.md`.