# /criterio-budget:budget-setup finanzas/08010004578120-banco-de-occidente-sintetico

Tomás quedó instalado para Banco de Occidente Sintético, presupuesto 2026, con corte a septiembre. La configuración es válida, los términos están aceptados y la corrida está registrada.

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** rige la v2, que es la más reciente de `10-aprobado/`. No la fijé a mano.
- El acta 01 (2026-01-20) aprueba la v1.
- El acta 05 (2026-06-28) aprueba trasladar 150,000.00 de Publicidad a Eventos.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.1.0. El comprobante está en `.criterio/terminos/`.

**Lo que hay que atender, del reporte de variance:**
- **Servicios públicos (Administración):** el área dice en su correo del 2026-10-01 que va dentro del presupuesto, pero la línea va +15.0 % sobre el aprobado al corte. Ejecutó 1,552,500.00 contra 1,350,000.00, una diferencia de 202,500.00.
- **Resto de líneas:** Nómina está exacta y las demás van 3 % por debajo del aprobado al corte.

**Lo que el reporte no muestra:** `compute` levantó dos traslados sin acta entre la v1 y la v2. Operaciones · Transporte subió 240,000.00 y Tecnología · Licencias bajó 240,000.00. Ninguna acta lo aprueba. Lo agregué a mano al encabezado de la salida y está en `resultados.json`.

**Pendientes y decisiones que tomé por mi cuenta:**
- **Compromiso del comité:** el acta 06 pide que Administración revise el contrato de vigilancia antes del próximo comité. Quedó abierto y sin evidencia.
- **Fecha del comité:** ningún documento la trae, así que `committee_dates` quedó vacío.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque es lo único que se escribe dentro de los documentos y nadie pudo autorizarlo.
- **Umbrales:** usé los del ejemplo (desviación 10 %, comprometido 95 %, proyección vencida 45 días).
- **Fichas PMO:** apunté `pmo_records` a `estado-pmo/records`, donde existe `PRY-310.json`.

Los archivos están en:
- `.criterio/presupuesto/08010004578120/config.json` (configuración)
- `estado-finanzas/08010004578120-banco-de-occidente-sintetico/presupuesto/2026/reporte-variance-report.md` (reporte)
- `estado-finanzas/08010004578120-banco-de-occidente-sintetico/corridas/salida-budget-setup.md` (salida completa de la corrida)