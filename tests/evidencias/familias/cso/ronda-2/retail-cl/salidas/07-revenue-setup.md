# /criterio-revenue:revenue-setup comercial/76543210-3-tiendas-del-maipo

Valeria quedó instalada sobre Tiendas del Maipo (76543210-3, Chile, CLP) y el primer cruce de 2026-10 dejó 6 señales por atender. Nadie respondió preguntas en esta sesión, así que en cada punto tomé la respuesta sugerida por los documentos.

- **Carpeta raíz:** usé la del argumento. No la marqué con `_CRITERIO_COMERCIAL.txt`, porque nadie lo autorizó.
- **Exportaciones del CRM:** las tres son Zoho, traen todas las columnas y tienen 19 filas cada una. Son las de 2026-10-01, 2026-10-16 y 2026-11-03.
- **Periodo y plazo:** el periodo es 2026-10 y el plazo para facturar un contrato firmado es de 30 días. Los tomé de la instalación comercial y de la configuración de ejemplo.
- **Fichas de los otros agentes:** encontré las de Fidel en `estado-legal/76543210-3-tiendas-del-maipo/contratos` y las de Clara en `estado-finanzas/76543210-3-tiendas-del-maipo`.
- **Comisiones:** no se publican en Rostrum, que es la opción por omisión.
- **Términos:** José Francisco Ñáñez los aceptó con fecha 2026-11-05. El comprobante está en `.criterio/terminos/aceptacion-criterio-revenue-0.2.0-2026-11-05.md` y `.pdf`.
- **Configuración:** la escribí en `.criterio/ingresos/76543210-3-tiendas-del-maipo/config.json` y el motor la validó sin problemas.
- **Corrida:** quedó registrada como `2026-11-05-revenue-setup-1`, con la salida en `estado-comercial/76543210-3-tiendas-del-maipo/corridas/salida-revenue-setup.md`.

**Lo que hay que atender (todas las cifras vienen del motor):**
- **Ganadas sin contrato firmado en las fichas de Fidel:**
  - OPP-2308 por 60.000.000, ganada el 2026-10-05.
  - OPP-2330 por 48.000.000, ganada el 2026-10-07.
  - OPP-2329 por 36.000.000, ganada el 2026-10-06.
- **Contratos firmados sin factura en las fichas de Clara, con el plazo vencido:**
  - CTR-2332 por 60.000.000, firmado el 2026-09-10.
  - CTR-2331 por 48.000.000, firmado el 2026-09-09.
  - CTR-2330 por 36.000.000, firmado el 2026-09-08.

Facturados sí están los contratos CTR-2301 (FE-2301) y CTR-2302 (FE-2302), y CTR-2303 sigue dentro del plazo. Todo lo que llegó se procesó.

El reporte completo, con las tablas de resultado y las fuentes, está en `estado-comercial/76543210-3-tiendas-del-maipo/ingresos/2026-10/reporte-won-to-invoice.md`. El archivo de salida de la corrida lo trae completo, junto con el resumen de arriba.