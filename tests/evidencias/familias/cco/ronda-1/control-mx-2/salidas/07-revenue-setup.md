# /criterio-revenue:revenue-setup comercial/CCM101010AB3-comercial-control-de-mexico

La instalación quedó lista, pero no pude marcar la carpeta con `_CRITERIO_COMERCIAL.txt`. El comando `marcar-raiz` falló con `KeyError: 'cso'` en `raiz.py`, porque no reconoce la familia comercial. La carpeta quedó sin marcar y el resto del flujo no depende de eso.

Soy Valeria. Pongo cada venta al lado de su política, su contrato y su factura; no apruebo descuentos ni liquido comisiones.

**Qué hice (nadie contestó, así que tomé las respuestas de los documentos)**
- **Carpeta raíz:** la del argumento, con 22 documentos, ninguno fuera de lugar ni ilegible.
- **CRM:** las 3 exportaciones de `10-crm/` son HubSpot, con 7 filas cada una y sin columnas faltantes.
- **Cuentas:** las 7 cuentas de `00-referencia/cuentas.csv` traen identificación.
- **Fichas:** las de Fidel están en `estado-legal/CCM101010AB3-comercial-control-de-mexico/contratos` y las de Clara en `estado-finanzas/CCM101010AB3-comercial-control-de-mexico`.
- **Opciones por omisión:** plazo de facturación de 30 días y comisiones sin publicar en Rostrum.
- **Configuración:** quedó en `.criterio/ingresos/CCM101010AB3/config.json` y el motor la validó sin problemas.
- **Términos:** José Francisco Ñáñez aceptó la versión 1.3 el 2026-11-05. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-revenue-0.1.0-2026-11-05.md` y `.pdf`.

**Primer cruce, periodo 2026-10**
No hay nada abierto que atender.

| Oportunidad ganada | Monto | Contrato | Factura |
|---|---|---|---|
| OPP-1601 | 840,000.00 | CTR-1601 | FE-1601 |
| OPP-1602 | 1,260,000.00 | CTR-1602 | FE-1602 |

Además, CTR-1603 (Cliente Control Pacífico, firmado el 2026-10-20) está en plazo para facturar hasta el 2026-11-19 y todavía no tiene factura.

El reporte completo está en `estado-comercial/CCM101010AB3-comercial-control-de-mexico/ingresos/2026-10/reporte-won-to-invoice.md`. Lo que te mostré quedó guardado en `corridas/salida-revenue-setup.md`, y la corrida quedó registrada como `2026-11-05-revenue-setup-1`.