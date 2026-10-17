# /criterio-portfolio:vendor-tracking PRY-202

La bolsa de horas de desarrollo del contrato CT-267 está facturada por 428.583.833 COP (FV-1267, 2026-08-30) y marcada como aceptada, pero no hay acta de recibo. El propio contrato dice que cada entregable se factura contra un acta de recibo firmada por el gerente del proyecto. Las actas de la carpeta cubren otras cosas.

La corrida quedó registrada como `2026-10-17-vendor-tracking-1`. Usé los términos ya vigentes, aceptados por José Francisco Ñáñez el 2026-10-17 (versión 0.3.13), así que no hizo falta registrarlos otra vez. El informe completo está en `/home/claude/banco/ronda-8/bancos/espacio/estado/corridas/salida-vendor-tracking.md`.

PRY-202 tiene un solo proveedor, Datacore Colombia, con dos contratos (CT-267 y CT-243). Lo que encontré:

- **Aceptación sin evidencia:** además de la factura, la única mención de "recibido" está en la tabla del contrato, que se firmó el 2025-10-27. Esa tabla es una declaración, no un recibo. Como lo facturado coincide con lo declarado aceptado, el cálculo no levanta `vendor_invoiced_over_accepted`.
- **Vencidos sin entrega declarada:** el licenciamiento del motor de CT-267 lleva 196 días de atraso (comprometido para 2026-04-04) y el de CT-243 lleva 149 (2026-05-21).
- **Posible solape:** CT-267 y CT-243 comprometen los mismos dos entregables, con fechas y montos distintos. Ningún documento aclara si son alcances separados.
- **Compromisos del proveedor:** no hay ninguno vencido que se pueda atribuir a Datacore. Los seis vencidos del proyecto están a nombre de personas que ningún documento vincula con el proveedor.
- **Riesgo sin registrar:** en las notas del 2026-10-17 se comentó que el proveedor podría no llegar con el equipo completo para la siguiente fase, y nadie lo anotó como riesgo.

No pude evaluar el vencimiento de los contratos: ninguno trae vigencia, renovación ni preaviso. Tampoco consta la facturación de CT-243, ni qué entregable cubre FV-1267 (dice solo "Entregables del contrato CT-267").

Recomiendo llevar la factura al comité del 2026-10-20: pedir el acta de recibo de la bolsa de horas, o retener el pago hasta tenerla, y aclarar la relación entre CT-267 y CT-243. También habría que pedir a Compras los textos de vigencia y preaviso. No lo he llevado a ningún comité; eso lo decide usted.