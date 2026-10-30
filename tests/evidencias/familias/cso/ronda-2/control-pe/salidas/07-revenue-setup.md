# /criterio-revenue:revenue-setup comercial/20210047035-comercial-control-del-peru

Valeria quedó instalada sobre Comercial Control del Perú (20210047035). El primer cruce de 2026-10 no deja nada abierto: las dos oportunidades ganadas tienen contrato y factura.

- **Lo ganado contra lo firmado (Fidel):**
  - OPP-2201 (300,000.00) tiene el contrato CTR-2201.
  - OPP-2202 (450,000.00) tiene el contrato CTR-2202.
- **Lo firmado contra lo facturado (Clara):**
  - CTR-2201 tiene la factura FE-2201.
  - CTR-2202 tiene la factura FE-2202.
  - CTR-2203, firmado el 2026-10-20, aún no tiene factura. Está en plazo hasta el 2026-11-19.
- **Exportaciones del CRM:** las tres son Zoho, con 7 filas cada una y sin columnas faltantes.
- **Cuentas:** las 7 cuentas de la tabla traen su identificación.
- **Rutas:**
  - Las fichas de Fidel están en `estado-legal/20210047035-comercial-control-del-peru/contratos`.
  - Las de Clara están en `estado-finanzas/20210047035-comercial-control-del-peru`.
  - Lo que encuentro se guarda en `estado-comercial/20210047035-comercial-control-del-peru`.
- **Términos:** acepté los términos a nombre de José Francisco Ñáñez, con fecha 2026-11-05. Los comprobantes quedaron en `.criterio/terminos/`.

Nadie contestó las preguntas, así que tomé la respuesta sugerida por los documentos en cada una:
- periodo 2026-10;
- 30 días para facturar;
- comisiones sin publicar en Rostrum.

Tampoco dejé la marca `_CRITERIO_COMERCIAL.txt` en la raíz, porque nadie la autorizó.

La configuración está en `.criterio/ingresos/20210047035/config.json` y el comando `config` la validó sin problemas. El reporte quedó en `estado-comercial/20210047035-comercial-control-del-peru/ingresos/2026-10/reporte-won-to-invoice.md`. La salida y la corrida quedaron registradas en `estado-comercial/20210047035-comercial-control-del-peru/corridas/salida-revenue-setup.md`.