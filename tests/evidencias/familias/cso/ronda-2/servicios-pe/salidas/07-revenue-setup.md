# /criterio-revenue:revenue-setup comercial/20210046021-consultores-asociados-de-lima

Valeria quedó instalada para Consultores Asociados de Lima (20210046021). El primer cruce de 2026-10 dio 5 señales en el reporte de lo ganado a la factura, y una sexta de comisiones que ese reporte no incluye.

- **Raíz y exportaciones:** usé la carpeta que venía en el argumento. Las tres exportaciones del CRM (2026-10-01, 2026-10-16 y 2026-11-03) son Dynamics 365 Sales, con 20 filas cada una y sin columnas faltantes.
- **Fichas cruzadas:** las de Fidel están en `estado-legal/.../contratos` (7 contratos) y las de Clara en `estado-finanzas/...` (cierres 2026-09 y 2026-10).
- **Configuración:** quedó en `.criterio/ingresos/20210046021/config.json` y el motor la validó sin problemas. Usa un plazo de 30 días para facturar y no publica comisiones en Rostrum.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez el 2026-11-05. Los comprobantes están en `.criterio/terminos/`.
- **Raíz sin marcar:** no dejé `_CRITERIO_COMERCIAL.txt` en la carpeta, porque nadie autorizó crear ese archivo en esta prueba.

**Lo ganado contra lo firmado (Fidel):**
- OPP-2131 (90,000.00) y OPP-2132 (120,000.00) están ganadas y no tienen contrato firmado.
- Las otras dos ganadas, OPP-2101 y OPP-2102, sí tienen su contrato (CTR-2101 y CTR-2102).

**Lo firmado contra lo facturado (Clara):**
- CTR-2105 (240,000.00), CTR-2131 (120,000.00) y CTR-2130 (90,000.00) pasaron el plazo de facturación sin factura.
- CTR-2103 sigue dentro del plazo.
- CTR-2101 y CTR-2102 ya están facturados (FE-2101 y FE-2102).

**Comisión:** el motor marcó una comisión liquidada que difiere de la que da el plan. El detalle sale con `/commission-check`.

Todo lo que llegó se procesó y la corrida se registró con 6 hallazgos. Las fichas de Clara no traen facturas de septiembre para estos clientes, así que el reporte dice "no hay factura emitida" y no distingue si falta emitirla o falta cargarla en su ficha.

Archivos principales en `estado-comercial/20210046021-consultores-asociados-de-lima/`:
- `ingresos/2026-10/reporte-won-to-invoice.md`
- `corridas/salida-revenue-setup.md`