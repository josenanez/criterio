# /criterio-revenue:revenue-setup comercial/20210047035-comercial-control-del-peru

Valeria quedó instalada sobre Comercial Control del Perú (20210047035). El primer cruce de ganado, contrato y factura salió sin hallazgos.

Nadie contestó preguntas en esta prueba, así que tomé la respuesta sugerida por los documentos en cada una:
- **CRM:** los tres archivos de `10-crm/` (cortes 2026-10-01, 2026-10-16 y 2026-11-03) son Zoho, con 7 filas cada uno y sin columnas faltantes. Registré «Last Activity Time» como la última actividad.
- **Cuentas:** las 7 cuentas de `00-referencia/cuentas.csv` traen identificación.
- **Fichas:** las de Fidel están en `estado-legal/…/contratos` y las de Clara en `estado-finanzas/…`. Ambas rutas existen en el espacio.
- **Facturación:** el plazo para facturar un contrato firmado quedó en 30 días, el valor por omisión.
- **Rostrum:** las comisiones no se publican en Rostrum, también por omisión.
- **Marca de la carpeta:** no dejé `_CRITERIO_COMERCIAL.txt`, igual que en la instalación de Augusto.
- **Términos:** José Francisco Ñáñez aceptó la versión 1.3 el 2026-11-05. Mostré su `en_corto` completo y el comprobante quedó en `.criterio/terminos/aceptacion-criterio-revenue-0.2.0-2026-11-05.md` y `.pdf`.

**Lo ganado contra lo firmado y lo facturado, periodo 2026-10, corte 2026-10-31:**

| Oportunidad | Monto | Contrato | Factura |
|---|---|---|---|
| OPP-2201 | 300,000.00 | CTR-2201 | FE-2201 |
| OPP-2202 | 450,000.00 | CTR-2202 | FE-2202 |

CTR-2203 está firmado el 2026-10-20 y sin factura, pero sigue en plazo hasta el 2026-11-19.

La configuración quedó en `.criterio/ingresos/20210047035-comercial-control-del-peru/config.json` y el reporte en `<estado>/ingresos/2026-10/reporte-won-to-invoice.md`. Lo mostrado quedó guardado en `estado-comercial/…/corridas/salida-revenue-setup.md`, y la corrida se registró como `2026-11-05-revenue-setup-1`.