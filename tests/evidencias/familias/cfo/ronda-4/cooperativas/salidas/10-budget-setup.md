# /criterio-budget:budget-setup finanzas/1790012345001-cooperativa-sierra-alta

## Listo — Cooperativa Sierra Alta · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, que es la más reciente de `10-aprobado/`. Nace del traslado del acta 05 (2026-06-28) sobre la versión 1, que aprueba el acta 01 (2026-01-20). El traslado de 3,000.00 de Publicidad a Eventos coincide con los cambios de julio a diciembre en la v2.

**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 0.10.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.10.0-2026-10-06.md` y `.pdf`.

**Lo que no hice, y por qué:**
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt` porque nadie autorizó escribir dentro de los documentos.
- **Responsable por área:** ningún documento lo dice, así que quedó sin asignar.
- **Fechas de comité:** `committee_dates` quedó vacío porque ningún documento trae la próxima fecha.

**Lo que hay que atender:**
- Tecnología · Licencias: lo ejecutado más lo comprometido llega al 96.0 % de lo aprobado en el año, con 2,390.00 disponibles.
- El cálculo trae otras 3 señales fuera de este reporte: `budget_version_mismatch` (2) y `forecast_stale` (1). Su detalle sale con `forecast`, `transfer-log` y `budget-scan`.
- Compromiso abierto del acta 06: Administración revisa el contrato de vigilancia antes del próximo comité.

**Ejecución al corte 2026-09, en USD:**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 24,000.00 | 18,000.00 | 17,460.00 | 600.00 | 5,940.00 | -540.00 | -3.00 |
| Administración | Servicios públicos | 36,000.00 | 27,000.00 | 26,190.00 | 900.00 | 8,910.00 | -810.00 | -3.00 |
| Comercial | Eventos | 21,000.00 | 15,000.00 | 14,550.00 | 600.00 | 5,850.00 | -450.00 | -3.00 |
| Comercial | Publicidad | 45,000.00 | 34,500.00 | 33,465.00 | 1,050.00 | 10,485.00 | -1,035.00 | -3.00 |
| Operaciones | Transporte | 42,000.00 | 31,500.00 | 30,555.00 | 1,050.00 | 10,395.00 | -945.00 | -3.00 |
| Tecnología | Licencias | 60,000.00 | 45,000.00 | 43,650.00 | 13,960.00 | 2,390.00 | -1,350.00 | -3.00 |
| Tecnología | PRY-310 | 72,000.00 | 54,000.00 | 52,380.00 | 1,800.00 | 17,820.00 | -1,620.00 | -3.00 |
| Personal | Nómina | 240,000.00 | 180,000.00 | 180,000.00 | 6,000.00 | 54,000.00 | 0.00 | 0.00 |

Todo lo que llegó se procesó. El reporte completo está en `estado-finanzas/1790012345001-cooperativa-sierra-alta/presupuesto/2026/reporte-variance-report.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La configuración quedó en `.criterio/presupuesto/1790012345001-cooperativa-sierra-alta/config.json` y la corrida quedó registrada como `2026-10-06-budget-setup-1`.