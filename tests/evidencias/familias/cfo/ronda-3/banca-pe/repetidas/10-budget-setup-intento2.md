# /criterio-budget:budget-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera (20710000019) · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 1. El acta 01 del 2026-01-20 dice «Se aprueba el presupuesto 2026, versión 1». El acta 05 solo aprueba trasladar 12,000.00 de Comercial · Publicidad a Comercial · Eventos, de julio a diciembre. Ningún acta aprueba la v2, así que fijé la v1 como aprobada en la configuración. Una corrida anterior de hoy había calculado sobre la v2.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.9.0-2026-10-06-2.md`. Mostré el texto de `en_corto` y registré la aceptación por tu instrucción de la prueba, no por un sí de la persona.

**Señales del motor (14):**

| Señal | Cantidad |
|---|---|
| `declared_vs_evidence` | 1 |
| `transfer_without_approval` | 2 |
| `variance_over_threshold` | 1 |
| `forecast_over_approved` | 2 |
| `budget_version_mismatch` | 8 |

El reporte detalla las dos primeras. Los traslados, las proyecciones y las versiones se ven con `transfer-log`, `forecast` y `budget-scan`, que no corrí en esta sesión.

**Respuestas que tomé por la persona** (nadie podía contestar):
- **Entidad y año:** Banco Ribera, 2026, corte 2026-09, aprueba Sofía León.
- **Umbrales:** los del ejemplo: 10 % de desviación, 95 % comprometido y 45 días de proyección vencida.
- **Cuentas de gasto:** prefijo 51, porque el mapeo solo usa cuentas 51xx.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Estado:** `estado-finanzas/20710000019-banco-ribera`.
- **Fechas de comité:** ninguna, porque ningún documento trae una.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la dejé, porque nadie autorizó escribir en los documentos.
- **Ficha:** la armé con las actas 01, 05 y 06 y el correo de Administración. Quedó en `ficha.json`; así `compute` ya no devuelve documentos sin extraer.

La configuración quedó en `.criterio/presupuesto/20710000019/config.json`. Ya existía una de finanzas para esta entidad en otra ruta y no la toqué.

# Ejecución contra aprobado · Banco Ribera · presupuesto 2026, corte 2026-09

### Lo que hay que atender

| # | Señal | Qué | Monto |
|---|---|---|---|
| 1 | `declared_vs_evidence` | Administración se reporta dentro del presupuesto (`correo-administracion.md`) y 1 línea no lo sostiene: Servicios públicos | 16,200.00 |
| 2 | `variance_over_threshold` | Administración · Servicios públicos: ejecutado 124,200.00 contra 108,000.00 aprobado al corte (+15.0 %) | 16,200.00 |

### El resultado

Versión vigente: **1**. Periodos procesados: 2026-01 a 2026-09.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 144,000.00 | 108,000.00 | 124,200.00 | 3,600.00 | 16,200.00 | 16,200.00 | 15.00 |
| Tecnología | Licencias | 240,000.00 | 180,000.00 | 165,288.00 | 5,040.00 | 69,672.00 | -14,712.00 | -8.17 |
| Comercial | Eventos | 72,000.00 | 54,000.00 | 58,200.00 | 2,400.00 | 11,400.00 | 4,200.00 | 7.78 |
| Comercial | Publicidad | 192,000.00 | 144,000.00 | 133,860.00 | 4,200.00 | 53,940.00 | -10,140.00 | -7.04 |
| Operaciones | Transporte | 168,000.00 | 126,000.00 | 131,532.00 | 5,160.00 | 31,308.00 | 5,532.00 | 4.39 |
| Administración | Mantenimiento | 96,000.00 | 72,000.00 | 69,840.00 | 2,400.00 | 23,760.00 | -2,160.00 | -3.00 |
| Tecnología | PRY-310 | 288,000.00 | 216,000.00 | 209,520.00 | 7,200.00 | 71,280.00 | -6,480.00 | -3.00 |
| Personal | Nómina | 960,000.00 | 720,000.00 | 720,000.00 | 24,000.00 | 216,000.00 | 0.00 | 0.00 |

Todo lo que llegó se procesó. El reporte completo está en `estado-finanzas/20710000019-banco-ribera/presupuesto/2026/reporte-variance-report.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-2`, con la salida en `estado-finanzas/20710000019-banco-ribera/corridas/salida-budget-setup.md`.