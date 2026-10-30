# /criterio-revenue:revenue-setup comercial/SPM140708QJ2-servicios-profesionales-mexicanos

Valeria quedó instalada sobre Servicios Profesionales Mexicanos (SPM140708QJ2), con el primer cruce de octubre calculado y la corrida registrada. La marca de la raíz no quedó.

**Qué hice**
- **Preguntas:** nadie respondió, así que tomé la respuesta sugerida de los documentos en cada una.
- **Configuración:** la escribí en `.criterio/ingresos/SPM140708QJ2-servicios-profesionales-mexicanos/config.json`, y el motor la validó sin problemas.
- **Exportaciones del CRM:** las tres (`oportunidades-2026-10-01.xlsx`, `…-10-16.xlsx` y `…-11-03.xlsx`) tienen formato genérico, 22 filas cada una y ninguna columna faltante. Reusé el mapeo de columnas de la configuración de ventas que ya existía.
- **Fichas de contratos y facturas:** las rutas son las que encontré con `find`. Los contratos de Fidel están en `estado-legal/SPM140708QJ2-servicios-profesionales-mexicanos/contratos` y las facturas de Clara en `estado-finanzas/SPM140708QJ2-servicios-profesionales-mexicanos`.
- **Plazo y comisiones:** el plazo de facturación es de 30 días y las comisiones no se publican en Rostrum.
- **Términos:** la aceptación quedó registrada a nombre de José Francisco Ñáñez, fecha 2026-11-05. El comprobante (Markdown y PDF) está en `.criterio/terminos/`.

**Qué encontró el cruce de octubre**
- **Ganado sin contrato:** hay cuatro oportunidades sin contrato firmado en las fichas de Fidel. Son OPP-1508 (450,000.00), OPP-1533 (450,000.00), OPP-1532 (360,000.00) y OPP-1531 (270,000.00).
- **Firmado sin factura:** CTR-1530 (270,000.00) se firmó el 2026-09-08 y el plazo de facturación venció el 2026-10-08 sin factura en las fichas de Clara.
- **Facturados:** CTR-1501 y CTR-1502 tienen su factura (FE-1501 y FE-1502).
- **En plazo:** CTR-1503 todavía está dentro del plazo de facturación.
- **Comisión:** hay una señal `commission_differs_from_plan`, que no entra en este reporte. Se revisa con `commission-check`.

**Lo que no salió**
- **`marcar-raiz`:** falló con un error del motor, `KeyError: 'cso'`, porque no conoce esa familia. No toqué el código. La carpeta se queda sin `_CRITERIO_COMERCIAL.txt`, que es opcional.

**Archivos**
- **Reporte:** `estado-comercial/SPM140708QJ2-servicios-profesionales-mexicanos/ingresos/2026-10/reporte-won-to-invoice.md`
- **Salida de la corrida:** `estado-comercial/SPM140708QJ2-servicios-profesionales-mexicanos/corridas/salida-revenue-setup.md`

La corrida quedó como `2026-11-05-revenue-setup-1`, con seis hallazgos.