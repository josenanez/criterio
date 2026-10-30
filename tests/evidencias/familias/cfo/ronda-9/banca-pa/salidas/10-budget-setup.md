# /criterio-budget:budget-setup finanzas/155731001-2-2016-banco-istmeno

## Listo — Banco Istmeño · presupuesto 2026

Administración dice estar dentro del presupuesto, pero Servicios públicos va +15.0 % sobre lo aprobado al corte. Además, `compute` levantó dos traslados entre la versión 1 y la 2 sin acta que los apruebe: Operaciones · Transporte (9,600.00) y Tecnología · Licencias (-9,600.00). Esos dos no salen en el reporte de ejecución; se revisan con `transfer-log`.

**Lo que miré:** 2 versiones, contabilidad de 2026-01 a 2026-09 y 3 actas.
**Versión aprobada:** la 2, la más reciente de `10-aprobado/`. La aprobación de la versión 1 está en `acta-01-aprobacion.docx` (2026-01-20) y el traslado de Comercial en `acta-05-traslado.docx` (2026-06-28). No fijé `approved_version`.
**Términos:** aceptados por José Francisco Ñáñez para la versión 1.0.0. El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-1.0.0-2026-10-06.md` y `.pdf`.

### Ejecución contra aprobado (corte 2026-09)

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 72,000.00 | 54,000.00 | 62,100.00 | 1,800.00 | 8,100.00 | 8,100.00 | 15.00 |
| Administración | Mantenimiento | 48,000.00 | 36,000.00 | 34,920.00 | 1,200.00 | 11,880.00 | -1,080.00 | -3.00 |
| Comercial | Eventos | 42,000.00 | 30,000.00 | 29,100.00 | 1,200.00 | 11,700.00 | -900.00 | -3.00 |
| Comercial | Publicidad | 90,000.00 | 69,000.00 | 66,930.00 | 2,100.00 | 20,970.00 | -2,070.00 | -3.00 |
| Operaciones | Transporte | 93,600.00 | 67,800.00 | 65,766.00 | 2,580.00 | 25,254.00 | -2,034.00 | -3.00 |
| Tecnología | Licencias | 110,400.00 | 85,200.00 | 82,644.00 | 2,520.00 | 25,236.00 | -2,556.00 | -3.00 |
| Tecnología | PRY-310 | 144,000.00 | 108,000.00 | 104,760.00 | 3,600.00 | 35,640.00 | -3,240.00 | -3.00 |
| Personal | Nómina | 480,000.00 | 360,000.00 | 360,000.00 | 12,000.00 | 108,000.00 | 0.00 | 0.00 |

**Lo que hay que atender:**
1. `declared_vs_evidence`: Administración se reporta dentro del presupuesto (correo del 2026-10-01) y Servicios públicos no lo sostiene (8,100.00).
2. `variance_over_threshold`: Servicios públicos, ejecutado 62,100.00 contra 54,000.00 aprobado al corte (+15.0 %).

Todo lo que llegó se procesó. El reporte completo, con sus fuentes, está en `estado-finanzas/155731001-2-2016-banco-istmeno/presupuesto/2026/reporte-variance-report.md`.

**Respuestas que tomé yo, porque nadie contestaba:**
- Cuentas de gasto: prefijo 51, según `mapeo-presupuesto.csv`.
- Umbrales: los del ejemplo (10 % de desviación, 95 % comprometido, 45 días para una proyección vencida).
- Fichas PMO: `estado-pmo/records`, donde está `PRY-310.json`.
- Estado: `estado-finanzas/155731001-2-2016-banco-istmeno`, fuera de la carpeta de documentos.
- Fechas del comité: no aparecen en los documentos, así que quedó vacío.
- No marqué la carpeta con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

La configuración quedó en `.criterio/presupuesto/155731001-2-2016/config.json`. La corrida quedó registrada como `2026-10-06-budget-setup-1`, y el texto de esta salida está en `estado-finanzas/155731001-2-2016-banco-istmeno/corridas/salida-budget-setup.md`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.