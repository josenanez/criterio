# /criterio-portfolio:vendor-tracking PRY-201

## Proveedores — PRY-201 Programa de fidelización, al 2026-10-18

Los términos ya estaban vigentes (versión 1.1, aceptados por José Francisco Ñáñez el 2026-10-18), así que no hubo que registrarlos de nuevo. El informe sale de los dos contratos, el acta de recibo, las dos facturas, el informe de avance del 2026-10-17 y las cifras del script `compute`.

Hay un solo proveedor, Tecnología para Tiendas Ltda., con dos contratos. El informe de avance declara el proyecto en verde con 86 %.

**Lo que no cuadra**
- **CT-836:** se facturaron 419.283.282 COP (FV-2836, 2026-09-05) contra 311.826.194 aceptados según el contrato. Son 107.457.088 por encima.
- **Sin acta de recibo:** el contrato marca el licenciamiento de CT-836 como «recibido», pero no hay acta, y el contrato exige acta firmada para facturar. Con evidencia, lo aceptado es 0 y toda la factura queda sin sustento.
- **Monto de la factura:** 419.283.282 no coincide con ningún entregable ni con la suma de los dos (623.652.388), y el concepto no lo explica.
- **CT-144:** cuadra. Se facturaron 154.265.280, igual al licenciamiento con acta del 2026-06-09. Es una inferencia por el monto, porque la factura no desglosa.

**Entregables vencidos**
- **CT-144, bolsa de horas de desarrollo:** vencía el 2026-08-26 y lleva 53 días tarde, sin evidencia.
- **CT-836, bolsa de horas de desarrollo:** vencía el 2026-10-17 y lleva 1 día tarde.
- **CT-144, configuración del catálogo:** vence el 2026-11-12 y sigue pendiente.

**Contra el informe de avance:** el informe dice verde, pero el script ve tres hitos «cumplidos» sin evidencia, una proyección 22,6 % sobre el presupuesto (4.046.399.504 sobre 3.300.000.000) y los dos entregables vencidos.

**Lo que no pude saber**
- **Vigencia:** ningún contrato trae fecha de terminación, renovación ni preaviso. No puedo decir si hay un preaviso por vencer antes del cierre del proyecto (2027-01-01).
- **Reuniones:** la carpeta no tiene minutas, así que no sé qué prometió el proveedor en comité.
- **Facturas:** no sé si FV-2836 ya se pagó. Solo dice «radicada en cuentas por pagar».
- **Solapamiento:** hay dos contratos con los mismos nombres de entregable y ningún documento explica si se solapan. Lo dejo como pregunta.

**Para comité:** llevar FV-2836 (419.283.282 sin acta de recibo) y pedirle a Sandra Gil el acta del licenciamiento de CT-836. También pedir el estado de las dos bolsas de horas y los contratos completos.

Dejé el informe en `estado/corridas/salida-vendor-tracking.md` y registré la corrida `2026-10-18-vendor-tracking-1` para el caso PRY-201. Esa corrida del script recorrió los 13 proyectos en 39 segundos; el informe es solo de PRY-201.