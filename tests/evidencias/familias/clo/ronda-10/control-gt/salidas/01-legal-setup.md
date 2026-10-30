# /criterio-legal:legal-setup legal/61077291-comercial-control-de-guatemala

Fidel quedó instalado sobre Comercial Control de Guatemala. Las fichas de los 6 contratos están escritas y el motor no devolvió ningún `record_issues`.

- **Configuración:** `.criterio/legal/61077291/config.json`, y el motor la validó sin problemas. Tomé la entidad, el país (GT) y la moneda (GTQ) de los contratos. Los umbrales son los de `config.example.json`: aviso de vencimiento a 60 días, de preaviso a 30, y certificado de la contraparte de hasta 30 días. La entidad quedó como no pública. El estado queda en `estado-legal/61077291-comercial-control-de-guatemala`.
- **Términos:** mostré la versión 1.3 y la registré como aceptada por José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/`.
- **Calendario:** en la ventana de 30 días atrás a 90 adelante no hay nada abierto. Salen cinco filas. La única con evidencia es el reporte de operaciones al oficial de cumplimiento de CTR-3501, que vencía el 2026-09-30 y está entregado. CTR-3505 termina el 2026-11-20 y CTR-3503 el 2026-12-31. Cada uno tiene su informe final y acta de liquidación pendiente, sin evidencia todavía.
- **Corrida:** quedó registrada como `2026-10-06-legal-setup-1`, con 0 hallazgos. Lo que te mostré está en `corridas/salida-legal-setup.md`, y el reporte del motor en `contratos/reporte-obligations-calendar.md`, ambos dentro de la carpeta de estado.

- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` dentro de tus documentos, porque es lo único que se escribe ahí y nadie podía autorizarlo.
- **Festivos:** quedaron los del ejemplo (solo 2026-10-12) y no los verifiqué para Guatemala. Si hay otros, el cálculo de plazos puede cambiar.
- **Sin chequear:** no corrí el cruce de facultades, el de pagos ni el de garantías. Este comando solo arma las fichas y el calendario.