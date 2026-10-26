# /criterio-budget:budget-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera (20710000019) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. El acta 01 (2026-01-20) aprueba la v1. La v2 nace del traslado del acta 05 (2026-06-28): 12,000.00 de Comercial · Publicidad a Comercial · Eventos, de julio a diciembre.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2), el 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/`.

**Lo que hay que atender (corte 2026-09):**
- **Administración · Servicios públicos** ejecutó 124,200.00 contra 108,000.00 aprobado al corte. La desviación es de 16,200.00 (+15.0 %) y supera el umbral del 10 %.
- **El correo de Administración del 2026-10-01** dice que el área va «dentro del presupuesto». Esa misma línea no lo sostiene.
- **El motor también cuenta 2 señales `transfer_without_approval`.** El reporte de ejecución no las detalla. Las trae `/transfer-log`.
- **Las demás líneas** están entre 0 % y −3 % de desviación.

**Respuestas que tomé sin preguntar** (la sesión no tiene interfaz):
- **Gasto:** las cuentas con prefijo 51, según el mapeo.
- **Umbrales:** los del ejemplo (10 % de desviación, 95 % comprometido, 45 días de proyección vencida). Son configuración, no norma.
- **Comité:** ninguna fecha, porque los documentos no traen ninguna.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`. Nadie lo autorizó y es lo único que se escribiría en los documentos.

**Dónde quedó todo:**
- **Configuración:** `.criterio/presupuesto/20710000019/config.json`
- **Ficha:** `estado-finanzas/20710000019-banco-ribera/presupuesto/2026/ficha.json`
- **Reporte completo, con la tabla por área y línea:** `estado-finanzas/20710000019-banco-ribera/presupuesto/2026/reporte-variance-report.md`
- **Salida y corrida:** `estado-finanzas/20710000019-banco-ribera/corridas/salida-budget-setup.md`, registrada como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.