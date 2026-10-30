# /criterio-revenue:revenue-setup comercial/1790123456001-comercial-andina-del-pacifico

Valeria quedó instalada sobre Comercial Andina del Pacífico (1790123456001, Ecuador, USD), y el primer cruce de octubre de 2026 ya corrió. Encontró 3 ganadas sin contrato y 2 contratos vencidos sin factura. Las cinco señales están en el reporte; las cifras son las del motor.

- **Carpeta:** son 35 archivos nuevos y ninguno salió ilegible ni fuera de lugar.
- **CRM:** las tres exportaciones (2026-10-01, 2026-10-16 y 2026-11-03) son Dynamics 365, con 19 filas cada una y sin columnas faltantes.
- **Fichas:** Fidel está en `estado-legal/…/contratos` y Clara en `estado-finanzas/…`. Las comprobé con `find`, porque Glob no estaba disponible en esta sesión.
- **Términos:** José Francisco Ñáñez los aceptó el 2026-11-05 (versión 1.3). El comprobante en Markdown y PDF está en `.criterio/terminos/`.
- **Raíz sin marcar:** no dejé `_CRITERIO_COMERCIAL.txt`, porque la prueba no lo autorizó.
- **Respuestas por omisión:** tomé el periodo 2026-10, el plazo de facturación de 30 días y no publicar comisiones en Rostrum.

**Ganado sin contrato en las fichas de Fidel:**

| Oportunidad | Monto | Días |
|---|---|---|
| OPP-1708 | 75,000.00 | 31 |
| OPP-1730 | 60,000.00 | 29 |
| OPP-1729 | 45,000.00 | 30 |

**Firmado sin factura en las fichas de Clara (plazo vencido):**

| Contrato | Monto | Días |
|---|---|---|
| CTR-1731 | 60,000.00 | 27 |
| CTR-1730 | 45,000.00 | 28 |

OPP-1701 y OPP-1702 tienen contrato y factura. CTR-1703 sigue en plazo para facturar.

La corrida quedó registrada como `2026-11-05-revenue-setup-1`, con 5 hallazgos.

Archivos en `<espacio>/`:
- `.criterio/ingresos/1790123456001-comercial-andina-del-pacifico/config.json`
- `estado-comercial/1790123456001-comercial-andina-del-pacifico/ingresos/2026-10/reporte-won-to-invoice.md`
- `estado-comercial/1790123456001-comercial-andina-del-pacifico/corridas/salida-revenue-setup.md`