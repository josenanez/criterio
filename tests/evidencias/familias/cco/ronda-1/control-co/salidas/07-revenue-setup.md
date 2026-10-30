# /criterio-revenue:revenue-setup comercial/900000002-comercial-control-andina

La instalación de Valeria quedó lista para Comercial Control Andina (900000002). El primer cruce de 2026-10 no deja ninguna señal abierta.

- **Carpeta y CRM:** el inventario encontró 21 archivos nuevos y ninguno fuera de lugar. Las tres exportaciones de `10-crm/` quedaron reconocidas como formato genérico, con 7 filas cada una y sin columnas faltantes. Para eso mapeé monto, cierre y última actividad a "Valor estimado", "Fecha estimada de cierre" y "Última gestión".
- **Fichas de Fidel y Clara:** usé `estado-legal/900000002-comercial-control-andina/contratos` y `estado-finanzas/900000002-comercial-control-andina`. Comprobé que ambas existen.
- **Valores por omisión:** facturación a 30 días y comisiones sin publicar en Rostrum.
- **Términos:** la versión 1.3 quedó aceptada a nombre de José Francisco Ñáñez el 2026-11-05. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_COMERCIAL.txt`, porque nadie podía autorizarlo en esta prueba.
- **Ganado contra firmado y facturado:**

| Oportunidad | Monto | Contrato | Factura |
|---|---|---|---|
| OPP-1301 | 72.000.000 | CTR-1301 | FE-1301 |
| OPP-1302 | 108.000.000 | CTR-1302 | FE-1302 |

- **Contrato sin factura:** CTR-1303 (cliente 830013004, firmado el 2026-10-20) no tiene factura todavía, pero está en plazo hasta el 2026-11-19.

La configuración quedó en `.criterio/ingresos/900000002-comercial-control-andina/config.json`, y el reporte lo escribió el motor en `estado-comercial/900000002-comercial-control-andina/ingresos/2026-10/reporte-won-to-invoice.md`. Lo que te mostré, entero, está en `corridas/salida-revenue-setup.md`, y la corrida quedó registrada como `2026-11-05-revenue-setup-1`.