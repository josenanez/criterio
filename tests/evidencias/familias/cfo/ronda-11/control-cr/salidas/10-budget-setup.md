# /criterio-budget:budget-setup finanzas/3101733015-comercial-control-de-costa-rica

## Listo: Comercial Control de Costa Rica, presupuesto 2026

El presupuesto 2026 quedó instalado y calculado al corte 2026-09, con todos los comandos corridos con `--today 2026-10-06`. Ningún valor de la ejecución se desvía de lo aprobado más del 3 %.

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2 (`presupuesto-2026-v2-2026-06-30.xlsx`), por ser la más reciente de `10-aprobado/`. No fijé `budget.approved_version`.
- **Acta 01, 2026-01-20:** aprueba la versión 1.
- **Acta 05, 2026-06-28:** aprueba trasladar 1.800.000,00 de Comercial · Publicidad a Comercial · Eventos.
- **Acta 06, 2026-09-10:** deja un compromiso abierto, que Administración revise el contrato de vigilancia antes del próximo comité.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.3, con fecha 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/`.

**Ejecución al corte 2026-09:**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 14.400.000,00 | 10.800.000,00 | 10.476.000,00 | 360.000,00 | 3.564.000,00 | -324.000,00 | -3,00 |
| Administración | Servicios públicos | 21.600.000,00 | 16.200.000,00 | 15.714.000,00 | 540.000,00 | 5.346.000,00 | -486.000,00 | -3,00 |
| Comercial | Eventos | 12.600.000,00 | 9.000.000,00 | 8.730.000,00 | 360.000,00 | 3.510.000,00 | -270.000,00 | -3,00 |
| Comercial | Publicidad | 27.000.000,00 | 20.700.000,00 | 20.079.000,00 | 630.000,00 | 6.291.000,00 | -621.000,00 | -3,00 |
| Operaciones | Transporte | 25.200.000,00 | 18.900.000,00 | 18.333.000,00 | 630.000,00 | 6.237.000,00 | -567.000,00 | -3,00 |
| Tecnología | Licencias | 36.000.000,00 | 27.000.000,00 | 26.190.000,00 | 900.000,00 | 8.910.000,00 | -810.000,00 | -3,00 |
| Tecnología | PRY-310 | 43.200.000,00 | 32.400.000,00 | 31.428.000,00 | 1.080.000,00 | 10.692.000,00 | -972.000,00 | -3,00 |
| Personal | Nómina | 144.000.000,00 | 108.000.000,00 | 108.000.000,00 | 3.600.000,00 | 32.400.000,00 | 0,00 | 0,00 |

El motor no levantó ninguna señal, y todo lo que llegó se procesó. El informe de ejecución, que salió sin fuentes citadas, quedó en `estado-finanzas/3101733015-comercial-control-de-costa-rica/presupuesto/2026/reporte-variance-report.md`.

**Decisiones que tomé por mi cuenta, porque nadie respondió:**
- **Umbrales:** usé los del ejemplo (desviación 10 %, comprometido 95 %, proyección vencida a 45 días).
- **Gastos:** `expense_prefixes` quedó en `["51"]`, porque el mapeo de cuentas solo trae cuentas 51xx.
- **Comité:** no encontré fechas en los documentos, así que `committee_dates` quedó vacío.
- **Fichas PMO:** apunté `pmo_records` a `estado-pmo/records`, donde existe `PRY-310.json`.
- **Marca de la carpeta:** no dejé `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.
- **Tiempo:** no medí los minutos hasta el primer resultado.

**Archivos:**
- **Configuración:** `.criterio/presupuesto/3101733015/config.json`
- **Ficha del presupuesto:** `estado-finanzas/3101733015-comercial-control-de-costa-rica/presupuesto/2026/ficha.json`
- **Salida de la corrida:** `estado-finanzas/3101733015-comercial-control-de-costa-rica/corridas/salida-budget-setup.md`; la corrida quedó registrada como `2026-10-06-budget-setup-1`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.