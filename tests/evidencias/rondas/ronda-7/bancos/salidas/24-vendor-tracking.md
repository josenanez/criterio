# /criterio-portfolio:vendor-tracking PRY-209

## Proveedores — PRY-209 Nómina electrónica al 2026-10-17

**Sale de:** el contrato CT-258, el acta de recibo del 2026-07-21, la factura FV-1258, el informe de avance del 2026-10-15, la minuta del comité del 2026-10-12 y la salida de `compute`.

**Términos:** ya estaban vigentes, con la aceptación de José Francisco Ñáñez del 2026-10-17. No los registré otra vez.

**Hallazgo principal:** Integra Sistemas Ltda. facturó 1.115.928.705 COP (FV-1258, 2026-10-01) y solo hay un acta de recibo, la del licenciamiento del motor por 750.219.723 COP. Quedan **365.708.982 COP facturados sin acta**.
- El contrato dice que cada entregable se factura contra acta firmada por el gerente.
- La factura dice solo "Entregables del contrato CT-258". No dice cuáles cubre, y el monto no es múltiplo de 750.219.723.
- Está radicada en cuentas por pagar. Ningún documento dice si ya se pagó.

| Entregable | Fecha | Estado | Evidencia |
|---|---|---|---|
| Licenciamiento del motor | 2026-07-09 | aceptado | Acta de recibo del 2026-07-21, firmada por Gustavo Neira |
| Bolsa de horas de desarrollo | 2026-10-20 | pendiente | Ninguna (vence en 3 días) |
| Parametrización del tarifario | 2027-01-30 | pendiente | Ninguna |
| Mesa de ayuda del primer trimestre | 2027-05-13 | pendiente | Ninguna |

- **Atrasos y aceptaciones sin evidencia:** `compute` no encontró ninguno.
- **Contrato:** la tabla de estados trae un "recibido" de julio dentro de un contrato firmado el 2026-03-23. Se actualizó después de la firma y no hay versión fechada.
- **Compromisos:** ninguno del proveedor está vencido. El único compromiso de la reunión es de Javier Hoyos ("punto 19", fecha "por definir"). Nada dice que Hoyos sea del proveedor.

**Sin dato:**
- **Vigencia del contrato:** el contrato no trae fecha de fin, renovación automática ni preaviso, así que no pude evaluar si hay uno por vencer.
- **Desglose de la factura:** falta saber qué entregables cubre.
- **Estado de pago:** no consta si la factura se pagó.

**Siguiente paso:** llevar los 365.708.982 COP al comité del 2026-10-24. Pedir a Integra el desglose de FV-1258 y retener el pago del excedente hasta que haya acta firmada por el gerente.

La corrida quedó registrada como `2026-10-17-vendor-tracking-1`, con el texto completo en `estado/corridas/salida-vendor-tracking.md`. Las cifras derivadas salen de `compute`. La lectura de los documentos es mía y puede fallar, así que conviene verificarla contra las citas.