# /criterio-portfolio:vendor-tracking PRY-200

## Proveedores — PRY-200 Originación digital al 2026-10-16

Sale de la ficha PRY-200, del cálculo `portafolio.py compute` y de los 10 documentos de la carpeta del proyecto. Los términos ya estaban vigentes (v1.1, aceptados por José Francisco Ñáñez el 2026-10-16), así que no los registré de nuevo.

**Hallazgo principal:** los dos proveedores facturaron un monto contractual completo y ningún entregable de ninguno tiene acta de recibo. Datacore facturó 489.791.403 COP y Núcleo 707.420.229 COP. Ambos contratos condicionan el pago a un acta firmada por el gerente del proyecto, y esa acta no está en la carpeta. El script levanta `vendor_invoiced_without_delivery` para los dos.

### Datacore Colombia — CT-936
- **Firma:** 2025-12-03. El documento no trae fin, renovación ni preaviso.
- **Licenciamiento del motor:**
  - Comprometido para 2026-05-30, con 139 días de atraso.
  - Estado `pending`, sin evidencia de recibo.
- **Bolsa de horas de desarrollo:**
  - Comprometida para 2026-11-04.
  - Estado `pending` (el contrato dice "en curso"), sin evidencia de recibo.
- **Factura:** FV-1936, del 2026-09-27, por 489.791.403 COP. No dice qué entregable cubre.

### Núcleo Financiero S.A. — CT-107
- **Firma:** 2025-12-14. El documento no trae fin, renovación ni preaviso.

| Entregable | Comprometido | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del motor | 2026-03-28 (202 días de atraso) | `pending` | ninguna |
| Bolsa de horas de desarrollo | 2026-07-01 (107 días de atraso) | `pending` | ninguna |
| Parametrización del tarifario | 2026-10-04 (12 días de atraso) | `pending` | ninguna |
| Mesa de ayuda del primer trimestre | 2027-01-07 | `pending` | ninguna |

- **Factura:** FV-2107, del 2026-09-10, por 707.420.229 COP. No dice qué entregable cubre.
- **Estado en el contrato:** el contrato marca los cuatro entregables "en curso", aunque tres ya vencieron.

### Dónde no cuadra
- **Facturas sin acta:** ambas facturas están radicadas en cuentas por pagar sin el acta de recibo que exige el contrato. Entregables aceptados: 0.
- **Actas que existen:** las dos actas de la carpeta (2026-10-04, Diseño funcional aprobado; 2026-10-14, Ambiente de pruebas certificado) no corresponden a ningún entregable de estos contratos, así que no sustentan las facturas.
- **"Licenciamiento del motor":** aparece en ambos contratos, con fechas y montos distintos. Puede ser alcance duplicado; los documentos no lo aclaran.
- **Montos:** cada entregable de un contrato lleva el mismo monto que la factura completa. No se puede saber si la factura paga un entregable o todo el contrato.

### Compromisos del proveedor vencidos
Ninguno. El único compromiso del comité del 2026-10-16 es de Felipe Arango, patrocinador y no proveedor. Dice "Entregar el punto 4", para el 2026-10-25.

### Contexto del proyecto
El informe de avance del 2026-10-15 declara rojo y 49 %. No menciona proveedores, entregables vencidos ni las facturas. El script marca el avance 11,0 puntos por debajo de lo que sustenta el plan, y el hito "Integración con el core" como cumplido sin evidencia, con 38 días de vencido.

### Sin dato
- **Vigencia y preaviso:** ninguno de los dos contratos trae fecha de terminación, renovación automática ni preaviso. No pude evaluar si hay un preaviso por vencer.
- **Pagos:** las facturas solo dicen "radicada en cuentas por pagar". No hay documento que diga si ya se pagaron.
- **Cobertura de las facturas:** no hay documento que diga qué entregable cubre cada una.
- **Fuera de la carpeta:** pueden existir actas fuera de ella, y de eso no hay forma de saber.

### Después
Si las facturas no se han pagado, conviene frenarlas hasta que exista el acta o el gerente explique la excepción. Ofrezco llevarlo al comité del 2026-10-23 como decisión. Serían tres puntos:
- retener el pago;
- pedir las actas a Ricardo Salas;
- pedir a ambos proveedores la vigencia y el preaviso de los contratos.

**Pie de rigor:** las cifras salen de `compute` y de los documentos citados. Leí el texto convertido (caché), pero la cita apunta al original. Verifique contra los documentos antes de decidir. Criterio produce borradores de trabajo, no decisiones ni asesoría.

La corrida quedó registrada como `2026-10-16-vendor-tracking-1`, con la salida guardada en `estado/corridas/salida-vendor-tracking.md`.