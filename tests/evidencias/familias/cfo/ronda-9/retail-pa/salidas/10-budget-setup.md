# /criterio-budget:budget-setup finanzas/155791002-2-2017-almacenes-del-canal

## Listo — Almacenes del Canal · presupuesto 2026

**Lo que miré:** 2 versiones (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 1, con el acta 01 del 2026-01-20. La vigente es la 2, que nace del traslado del acta 05 del 2026-06-28.

**Términos:** aceptados a nombre de José Francisco Ñáñez el 2026-10-06 para la versión 1.0.0, con términos 1.3. El comprobante está en `.criterio/terminos/`.

La carpeta de documentos no se tocó. No dejé el archivo `_CRITERIO_FINANZAS.txt`, porque en esta prueba nadie podía autorizarlo.

**Lo que hay que atender (variance-report, corte 2026-09):**
1. **Gasto sin línea presupuestal:** la cuenta 5135 con centro de costo ZZZ tiene 1,050.00 en 2026-08. Está en `2026-08/10-contabilidad/libro-mayor.xlsx`, fila 18.
2. **Comprometido cerca de lo aprobado:** en Administración · Mantenimiento, lo ejecutado más lo comprometido es el 96.0 % de lo aprobado del año. Quedan 1,425.00 disponibles.
3. **Proyección vencida (`forecast_stale`):** `compute` la cuenta como tercera señal, pero el reporte no la detalla. Se verá con `forecast`.

**Ejecución por línea:**
- Casi todas las líneas van 3.00 % por debajo de lo previsto al corte. Nómina va en 0.00.
- Los valores completos por área y línea están en `estado-finanzas/155791002-2-2017-almacenes-del-canal/corridas/salida-budget-setup.md`.

**Cómo se resolvieron las preguntas:**
- Nadie respondió en esta prueba. Tomé las respuestas de los documentos y quedaron anotadas en la ficha y en el reporte.
- No hay fecha del próximo comité en ningún documento: el acta 06 es del 2026-09-10 y no fija la siguiente. Por eso `committee_dates` quedó vacío.
- Las fichas PMO están en `estado-pmo/records` (PRY-310).
- No medí los minutos hasta el primer resultado.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La configuración quedó en `.criterio/presupuesto/155791002-2-2017/config.json` y la ficha en `estado-finanzas/155791002-2-2017-almacenes-del-canal/presupuesto/2026/ficha.json`. La corrida quedó registrada como `2026-10-06-budget-setup-1`.