# /criterio-budget:budget-setup finanzas/20710000019-banco-ribera

## Listo — Banco Ribera (20710000019) · presupuesto 2026

**Lo que miré:** 2 versiones (v1 del 2026-01-15, v2 del 2026-06-30) · contabilidad de 2026-01 a 2026-09 · 3 actas.

**Versión aprobada:**
- El acta 01 (2026-01-20) aprueba la versión 1.
- El acta 05 (2026-06-28) aprueba trasladar 12,000.00 de Comercial · Publicidad a Comercial · Eventos.
- No fijé `approved_version`. Rige la más reciente de `10-aprobado/`, la 2.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.9.0-2026-10-06-3.md`. Mostré el `en_corto` y registré la aceptación por la instrucción de la prueba, no por un sí dado en la conversación.

**Señales del motor (4):**
- `declared_vs_evidence`: 1
- `transfer_without_approval`: 2
- `variance_over_threshold`: 1

El reporte detalla las dos que hay que atender. Los traslados sin acta se ven con `transfer-log`.

**Respuestas que tomé por la persona** (nadie podía contestar):
- **Datos de la entidad:** Banco Ribera, año 2026, corte 2026-09, aprueba Sofía León.
- **Umbrales:** los del ejemplo (10 %, 95 %, 45 días).
- **Cuentas de gasto:** prefijo 51, porque el mapeo solo usa cuentas 51xx.
- **Fichas PMO:** `estado-pmo/records`, donde existe `PRY-310.json`.
- **Estado:** `estado-finanzas/20710000019-banco-ribera`.
- **Fechas de comité:** ninguna, porque ningún documento trae una.
- **Marca `_CRITERIO_FINANZAS.txt`:** no la dejé, porque nadie autorizó escribir en los documentos.
- **Ficha:** la armé con las actas 01, 05 y 06 y el correo de Administración. El compromiso del acta 06, revisar el contrato de vigilancia, queda abierto.

La configuración nueva está en `.criterio/presupuesto/20710000019-banco-ribera/config.json`, porque no había una de presupuesto.

# Ejecución contra aprobado · Banco Ribera · presupuesto 2026, corte 2026-09

### Lo que hay que atender

1. `declared_vs_evidence`: Administración se reporta dentro del presupuesto (`presupuesto-2026/30-proyecciones/correo-administracion.md`) y 1 línea no lo sostiene: Servicios públicos · 16,200.00.
2. `variance_over_threshold`: Administración · Servicios públicos: ejecutado 124,200.00 contra 108,000.00 aprobado al corte (+15.0 %) · 16,200.00.

### El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos 2026-01 a 2026-09.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 144,000.00 | 108,000.00 | 124,200.00 | 3,600.00 | 16,200.00 | 16,200.00 | 15.00 |
| Administración | Mantenimiento | 96,000.00 | 72,000.00 | 69,840.00 | 2,400.00 | 23,760.00 | -2,160.00 | -3.00 |
| Comercial | Eventos | 84,000.00 | 60,000.00 | 58,200.00 | 2,400.00 | 23,400.00 | -1,800.00 | -3.00 |
| Comercial | Publicidad | 180,000.00 | 138,000.00 | 133,860.00 | 4,200.00 | 41,940.00 | -4,140.00 | -3.00 |
| Operaciones | Transporte | 187,200.00 | 135,600.00 | 131,532.00 | 5,160.00 | 50,508.00 | -4,068.00 | -3.00 |
| Tecnología | Licencias | 220,800.00 | 170,400.00 | 165,288.00 | 5,040.00 | 50,472.00 | -5,112.00 | -3.00 |
| Tecnología | PRY-310 | 288,000.00 | 216,000.00 | 209,520.00 | 7,200.00 | 71,280.00 | -6,480.00 | -3.00 |
| Personal | Nómina | 960,000.00 | 720,000.00 | 720,000.00 | 24,000.00 | 216,000.00 | 0.00 | 0.00 |

Todo lo que llegó se procesó. El reporte completo está en `estado-finanzas/20710000019-banco-ribera/presupuesto/2026/reporte-variance-report.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-3`, con lo que te mostré en `estado-finanzas/20710000019-banco-ribera/corridas/salida-budget-setup.md`.