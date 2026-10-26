# /criterio-budget:budget-setup finanzas/900765432-almacenes-caribe

## Listo — Almacenes Caribe · presupuesto 2026

**Lo que miré:** 2 versiones (v1 del 2026-01-15, v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** rige la v2, la más reciente de `10-aprobado/`. El acta 01 del 2026-01-20 aprueba la v1. El acta 05 del 2026-06-28 aprueba el traslado de 2.400.000 de Comercial · Publicidad a Comercial · Eventos. No fijé `approved_version`.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (términos 1.2), con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.10.0-2026-10-06.md` y `.pdf`.

**Primera ejecución contra lo aprobado:**
- **Gasto sin línea:** hay 560.000,00 en la cuenta 5135, centro ZZZ, en 2026-08, sin línea presupuestal. Está en la fila 18 de `2026-08/10-contabilidad/libro-mayor.xlsx`.
- **Proyección:** `compute` marcó una proyección de área por encima de lo aprobado. El reporte no la detalla; está en `resultados.json`.
- **Mayor desviación:** Administración · Mantenimiento, con 1.120.000,00 sobre lo previsto al corte (7,78 %), por debajo del umbral del 10 %.
- **Compromiso abierto:** el acta 06 pide que Administración revise el contrato de vigilancia antes del próximo comité. No hay evidencia de que se haya hecho.
- **Resto de líneas:** están entre 0 % y −3,00 % de desviación. El reporte completo, con las ocho líneas, está en `estado-finanzas/900765432-almacenes-caribe/presupuesto/2026/reporte-variance-report.md`.

**Decisiones por defecto (nadie respondió):**
- **Umbrales:** usé los de `config.example.json`: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días.
- **Fechas del comité:** quedan vacías, porque el acta 06 no fija la próxima.
- **Fichas PMO:** apunté a `estado-pmo/records`, donde existe `PRY-310.json`.
- **Marca de la raíz:** no escribí `_CRITERIO_FINANZAS.txt` en la carpeta de documentos.

La configuración está en `.criterio/presupuesto/900765432-almacenes-caribe/config.json`. La salida de esta corrida está en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-budget-setup.md` y la corrida quedó registrada como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.