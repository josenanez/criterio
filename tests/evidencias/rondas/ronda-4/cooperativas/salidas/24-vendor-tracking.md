# /criterio-portfolio:vendor-tracking PRY-200

## Proveedores — PRY-200 Crédito de libranza digital al 2026-10-15

**Sale de:**
- el contrato CT-451;
- dos actas de recibo (2026-03-07 y 2026-05-23);
- la factura FV-1451 del 2026-09-16;
- el informe de avance del 2026-09-23;
- el comité del 2026-10-05.

Las cifras derivadas vienen de `compute`. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-15), así que no los registré otra vez.

### Red Rural de Pagos S.A.S. — contrato CT-451
**Vigencia, preaviso y vencimiento:** sin dato. El contrato solo trae la fecha de firma (2025-06-24), los entregables y la condición de pago.

**Condición de pago:** cada entregable se factura contra acta de recibo firmada por el gerente del proyecto.

| Entregable | Comprometido | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del módulo | 2025-09-18 | pendiente (el contrato dice "en curso") | Ninguna |
| Bolsa de horas de desarrollo | 2025-12-05 | declarado entregado (el contrato dice "recibido") | **Ninguna** |
| Parametrización de líneas de crédito | 2026-02-21 | aceptado | Acta del 2026-03-07, firmada por Gustavo Neira |
| Mesa de ayuda del primer trimestre | 2026-05-10 | aceptado | Acta del 2026-05-23, firmada por Gustavo Neira |

Cada entregable vale 310.006.555 COP. El proveedor facturó 930.019.665 COP (FV-1451, radicada en cuentas por pagar). La factura no dice a qué entregables corresponde.

### Dónde no cuadra
- **Factura sin sustento completo:** 930.019.665 COP equivale a tres entregables, pero solo dos tienen acta. El script cuenta 3 de 4 como aceptados porque incluye la Bolsa de horas, que no tiene acta.
- **Bolsa de horas:** el contrato la marca "recibida", pero la carpeta no tiene acta, correo ni mención en minuta.
- **Licenciamiento:** sin entrega ni acta, con 392 días de atraso.
- **Salida a producción:** la ficha da el hito (2026-06-21) por cumplido, sin evidencia, con el licenciamiento sin entregar. No puedo decir si el módulo es requisito de la salida.

### Compromisos del proveedor vencidos
Ninguno. Ninguna reunión registra una promesa de Red Rural de Pagos. El único compromiso abierto es de Natalia Ospina ("Entregar el punto 31"), con fecha "por definir". Ella no figura entre los asistentes y nada indica que sea del proveedor.

### Sin dato
- Vigencia, renovación automática y preaviso del contrato. No puedo decir si hay un preaviso por vencer.
- A qué entregables corresponde la factura y si ya está pagada.
- El acta de la Bolsa de horas. Que no esté en la carpeta no prueba que no exista.

### Lo que sigue
- **Antes de aprobar el pago:** pedirle a Gustavo Neira el acta de la Bolsa de horas, o una factura desglosada sin ese entregable. Si quieres, lo llevo a comité como punto.
- **Licenciamiento:** hace falta una fecha nueva del proveedor y decidir si el atraso afecta la salida a producción.
- **Fuera del proveedor:** los 5 hitos del cronograma figuran cumplidos sin evidencia, y el avance declarado es 44% frente al 100% que sostendría el plan.

**Rigor:** leí el texto en caché de los PDF, no los PDF originales.

**Corrida registrada:**
- `2026-10-15-vendor-tracking-1`, caso PRY-200.
- El resumen automático cuenta señales de los 13 proyectos del portafolio, no solo de PRY-200. Para este caso son 9 señales.
- La salida completa está en `estado/corridas/salida-vendor-tracking.md`.