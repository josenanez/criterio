# /criterio-portfolio:vendor-tracking PRY-211

**Proveedores de PRY-211:** hay dos facturas radicadas por pagar contra entregables sin acta de recibo, y el proyecto se declara en verde. El informe del 2026-10-14 no menciona a los proveedores.

**Datos y Demanda (CT-842)**
- Solo la bolsa de horas tiene acta de recibo, del 2026-08-20, por 775.475.640 COP.
- La factura FV-1842, del 2026-10-02, es por 1.197.938.594 COP. Eso deja 422.462.954 COP facturados sin acta que los respalde.
- Licenciamiento de la plataforma está vencido hace 99 días y Configuración del catálogo hace 18, ambos sin acta.

**Tecnología para Tiendas (CT-565)**
- No tiene ningún entregable aceptado.
- La factura FV-2565, del 2026-09-16, es por 723.840.453 COP, el monto exacto de un entregable. La emitió antes de que venciera la bolsa de horas, el 2026-10-12.
- Licenciamiento está vencido hace 72 días y la bolsa de horas hace 5.

**Lo que no puedo decir**
- **Contratos:** vigencia, renovación y preaviso de ambos, porque los contratos de la carpeta solo traen la tabla de entregables. No sé si hay un preaviso por vencer.
- **Facturas:** no traen desglose por entregable y no sé si ya se pagaron.
- **Compromisos:** ninguna minuta nombra a los proveedores, así que no hay compromisos de proveedor vencidos. Las notas del 2026-10-17 dicen que el proveedor podría no llegar con el equipo completo, sin decir cuál y sin que nadie lo registrara como riesgo.

Propongo llevar las dos facturas a comité antes de que se paguen, y pedir los contratos completos. Si quieres, preparo ese paquete con `/criterio-portfolio:steering-pack PRY-211`.

**Registro de la corrida**
- **Términos:** ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-17), así que no registré nada nuevo.
- **Corrida:** quedó registrada como `2026-10-17-vendor-tracking-1`, con 47 segundos medidos.
- **Salida:** `estado/corridas/salida-vendor-tracking.md` es el informe completo, con la sección de lo que no se sabe.
- **Señales:** el registro cuenta 61 señales abiertas de todo el portafolio. Las 26 de PRY-211 incluyen las dos de proveedores (`vendor_invoiced_over_accepted` y `vendor_invoiced_without_delivery`).