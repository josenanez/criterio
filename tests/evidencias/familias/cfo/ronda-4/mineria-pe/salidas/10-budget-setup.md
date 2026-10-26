# /criterio-budget:budget-setup finanzas/20730000015-minera-puna-alta

## Listo: Minera Puna Alta (20730000015) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. Nace del traslado del acta 05, que mueve 18,000.00 de Comercial · Publicidad a Comercial · Eventos (`presupuesto-2026/40-actas/acta-05-traslado.docx`). La v1 la aprueba el acta 01, del 2026-01-20 (`presupuesto-2026/40-actas/acta-01-aprobacion.md`).

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0. Los comprobantes quedaron en `.criterio/terminos/`.

### Lo que hay que atender (reporte de ejecución)

- **Administración · Mantenimiento:** ejecutado más comprometido es el 96.0 % de lo aprobado. Quedan 5,700.00 disponibles.
- **Resto del cuadro:** todas las demás líneas están 3.00 % por debajo de lo previsto al corte. Nómina está en 0.00 %.
- La tabla completa por área y línea está en `estado-finanzas/20730000015-minera-puna-alta/presupuesto/2026/reporte-variance-report.md`.

### Otras señales que el reporte no lista

Están en `resultados.json`:
- **Versión equivocada:** la proyección comercial del 2026-09-30 usa la versión 1 en Eventos y Publicidad, y la vigente es la 2 (filas 2 y 3).
- **Proyección vencida:** la de Operaciones · Transporte es del 2026-07-15, hace 83 días.
- **Compromiso abierto del acta 06:** Administración debe revisar el contrato de vigilancia, y todavía no hay evidencia de que lo haya hecho.

### Decisiones tomadas sin preguntar

Como nadie podía contestar, tomé la respuesta sugerida en cada punto:
- Umbrales del ejemplo: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días.
- Sin fechas de comité, porque ningún documento las trae.
- Fichas PMO en `estado-pmo/records`, donde existe `PRY-310.json`.
- Estado en `estado-finanzas/20730000015-minera-puna-alta`.
- No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta raíz, porque nadie autorizó escribir ahí.

La configuración quedó en `.criterio/presupuesto/20730000015/config.json`. La salida completa y la corrida registrada están en `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-budget-setup.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.