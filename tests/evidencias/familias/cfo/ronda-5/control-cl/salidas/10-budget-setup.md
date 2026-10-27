# /criterio-budget:budget-setup finanzas/76097001-8-comercial-control-andes

## Listo — Comercial Control Andes · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 (9 periodos), 3 actas, compromisos al 2026-09-30 y 5 proyecciones de área.

**Versión aprobada:** la 2, la más reciente de `10-aprobado/`. Nace del traslado que aprueba el acta 05 del 2026-06-28: 900.000 de Comercial · Publicidad a Comercial · Eventos. Antes rigió la v1, que aprobó el acta 01 del 2026-01-20. No fijé `budget.approved_version`.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.10.0-2026-10-06.md` y `.pdf`.

**Respuestas por defecto:** como no había nadie que contestara, tomé la respuesta sugerida desde los documentos en cada pregunta. Están en la ficha y en el reporte.

**Lo que no hice:**
- No dejé `_CRITERIO_FINANZAS.txt` en la carpeta de documentos, porque nadie lo autorizó.
- `committee_dates` queda vacío: ningún documento trae una fecha de comité.

**Ejecución contra lo aprobado, corte 2026-09** (el motor no levantó ninguna señal ni ningún problema de ficha):

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 7.200.000,00 | 5.400.000,00 | 5.238.000,00 | 180.000,00 | 1.782.000,00 | -162.000,00 | -3,00 |
| Administración | Servicios públicos | 10.800.000,00 | 8.100.000,00 | 7.857.000,00 | 270.000,00 | 2.673.000,00 | -243.000,00 | -3,00 |
| Comercial | Eventos | 6.300.000,00 | 4.500.000,00 | 4.365.000,00 | 180.000,00 | 1.755.000,00 | -135.000,00 | -3,00 |
| Comercial | Publicidad | 13.500.000,00 | 10.350.000,00 | 10.039.500,00 | 315.000,00 | 3.145.500,00 | -310.500,00 | -3,00 |
| Operaciones | Transporte | 12.600.000,00 | 9.450.000,00 | 9.166.500,00 | 315.000,00 | 3.118.500,00 | -283.500,00 | -3,00 |
| Tecnología | Licencias | 18.000.000,00 | 13.500.000,00 | 13.095.000,00 | 450.000,00 | 4.455.000,00 | -405.000,00 | -3,00 |
| Tecnología | PRY-310 | 21.600.000,00 | 16.200.000,00 | 15.714.000,00 | 540.000,00 | 5.346.000,00 | -486.000,00 | -3,00 |
| Personal | Nómina | 72.000.000,00 | 54.000.000,00 | 54.000.000,00 | 1.800.000,00 | 16.200.000,00 | 0,00 | 0,00 |

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

**Dónde quedó todo:**
- Configuración: `.criterio/presupuesto/76097001-8/config.json`.
- Ficha: `estado-finanzas/76097001-8-comercial-control-andes/presupuesto/2026/ficha.json`.
- Reporte: `estado-finanzas/76097001-8-comercial-control-andes/presupuesto/2026/reporte-variance-report.md`.
- Salida de la corrida: `estado-finanzas/76097001-8-comercial-control-andes/corridas/salida-budget-setup.md`. La corrida quedó registrada como `2026-10-06-budget-setup-1`.