# /criterio-budget:budget-setup finanzas/08010006129040-almacenes-del-valle-de-sula

Ya quedó instalado Tomás sobre Almacenes del Valle de Sula y corrió la primera ejecución contra lo aprobado, con corte a 2026-09.

**Lo que miré:** 2 versiones del presupuesto, contabilidad de enero a septiembre y 3 actas.

**Versión vigente:** la 2, del 2026-06-30. Nace del traslado del acta 05 (2026-06-28): 120,000.00 de Comercial · Publicidad a Comercial · Eventos. El acta 01 (2026-01-20) aprueba la v1.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.1.0. El comprobante está en `.criterio/terminos/`.

**Señales:**
1. **Gasto sin línea presupuestal:** 28,000.00 en la cuenta 5135, centro ZZZ, en 2026-08. Está en `2026-08/10-contabilidad/libro-mayor.csv`, fila 18.
2. **Comprometido cerca de lo aprobado:** Administración · Mantenimiento tiene ejecutado más comprometido en 96.0 % de lo aprobado. Le quedan 38,000.00 disponibles.
3. **Proyección vencida (`forecast_stale`):** el reporte no la detalla. La proyección de Operaciones es del 2026-07-15.

**Desviación:** todas las líneas están en -3.00 %, salvo Nómina en 0.00 %.

**Compromiso del comité:** Administración debe revisar el contrato de vigilancia antes del próximo comité. Queda abierto, sin evidencia.

**Respuestas que tomé sin preguntar:**
- **Umbrales:** los de `config.example.json`: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- **Prefijos de gasto:** 51, tomados del mapeo de cuentas.
- **Fichas PMO:** `estado-pmo/records`, que existe y trae PRY-310.
- **Fechas del comité:** no están en los documentos, así que quedaron vacías.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la dejé en la carpeta porque nadie lo autorizó.

**Archivos:**
- Configuración: `.criterio/presupuesto/08010006129040/config.json`
- Reporte: `estado-finanzas/08010006129040-almacenes-del-valle-de-sula/presupuesto/2026/reporte-variance-report.md`
- Salida de la corrida: `estado-finanzas/08010006129040-almacenes-del-valle-de-sula/corridas/salida-budget-setup.md`, ya registrada como `2026-10-06-budget-setup-1`.

Tomás vuelve cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.