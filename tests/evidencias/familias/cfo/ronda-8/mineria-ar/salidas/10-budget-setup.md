# /criterio-budget:budget-setup finanzas/30709031143-minera-cordillera-de-cuyo

## Listo — Minera Cordillera de Cuyo · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** rige la v2 (2026-06-30), la más reciente de `10-aprobado/`.
- El acta 01 (2026-01-20) aprueba solo la v1. No hay acta que apruebe la v2.
- El acta 05 (2026-06-28) aprueba un traslado de 9.000.000 de Comercial · Publicidad a Comercial · Eventos.
- No fijé `approved_version`, porque nadie dijo que rija otra versión.

**Términos:** José Francisco Ñáñez los aceptó para esta prueba (versión 1.0.0, 2026-10-06). El comprobante está en `.criterio/terminos/`.

**Señales del motor (5):**
- `transfer_without_approval`: 2.
- `budget_version_mismatch`: 2.
- `forecast_stale`: 1.

Las trato en `/budget-scan`, no en este comando.

**Ejecución contra lo aprobado (corte 2026-09, v2):**

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 72.000.000,00 | 54.000.000,00 | 52.380.000,00 | 1.800.000,00 | 17.820.000,00 | -1.620.000,00 | -3,00 |
| Administración | Servicios públicos | 108.000.000,00 | 81.000.000,00 | 78.570.000,00 | 2.700.000,00 | 26.730.000,00 | -2.430.000,00 | -3,00 |
| Comercial | Eventos | 63.000.000,00 | 45.000.000,00 | 43.650.000,00 | 1.800.000,00 | 17.550.000,00 | -1.350.000,00 | -3,00 |
| Comercial | Publicidad | 135.000.000,00 | 103.500.000,00 | 100.395.000,00 | 3.150.000,00 | 31.455.000,00 | -3.105.000,00 | -3,00 |
| Operaciones | Transporte | 140.400.000,00 | 101.700.000,00 | 98.649.000,00 | 3.870.000,00 | 37.881.000,00 | -3.051.000,00 | -3,00 |
| Tecnología | Licencias | 165.600.000,00 | 127.800.000,00 | 123.966.000,00 | 3.780.000,00 | 37.854.000,00 | -3.834.000,00 | -3,00 |
| Tecnología | PRY-310 | 216.000.000,00 | 162.000.000,00 | 157.140.000,00 | 5.400.000,00 | 53.460.000,00 | -4.860.000,00 | -3,00 |
| Personal | Nómina | 720.000.000,00 | 540.000.000,00 | 540.000.000,00 | 18.000.000,00 | 162.000.000,00 | 0,00 | 0,00 |

**Respuestas que tomé por defecto (nadie contestó):**
- **Responsables de las áreas:** no figuran en los documentos, así que quedan como «no encontrado».
- **Umbrales:** desviación 10 %, comprometido 95 % y proyección vencida 45 días, los de `config.example.json`.
- **Fechas del comité:** no hay ninguna en los documentos, así que `committee_dates` queda vacío.
- **Fichas PMO:** las encontré en `estado-pmo/records`.
- **Marca de la raíz:** no escribí `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

**Compromiso abierto del acta 06:** Administración debe revisar el contrato de vigilancia antes del próximo comité.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

**Dónde quedó:**
- **Configuración:** `.criterio/presupuesto/30709031143/config.json`.
- **Ficha:** `estado-finanzas/30709031143-minera-cordillera-de-cuyo/presupuesto/2026/ficha.json`.
- **Reporte del motor:** `estado-finanzas/30709031143-minera-cordillera-de-cuyo/presupuesto/2026/reporte-variance-report.md`.
- **Corrida registrada:** `2026-10-06-budget-setup-1`, con su salida en `corridas/salida-budget-setup.md`.