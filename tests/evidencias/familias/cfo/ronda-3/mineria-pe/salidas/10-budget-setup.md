# /criterio-budget:budget-setup finanzas/20730000015-minera-puna-alta

## Listo — Minera Puna Alta · presupuesto 2026

**Lo que miré:** 2 versiones del presupuesto, contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** el acta 01 del 2026-01-20 aprueba la versión 1. El motor calcula contra la versión 2 (`presupuesto-2026-v2-2026-06-30.xlsx`), que no tiene acta de aprobación propia. El acta 05 (2026-06-28) solo aprueba un traslado de 18,000.00 de Comercial · Publicidad a Comercial · Eventos. Conviene confirmar con Sofía León si la versión 2 fue aprobada.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.9.0 (términos 1.2). El comprobante está en `.criterio/terminos/aceptacion-criterio-budget-0.9.0-2026-10-06.md`.

## Ejecución contra aprobado · corte 2026-09

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 144,000.00 | 108,000.00 | 104,760.00 | 33,540.00 | 5,700.00 | -3,240.00 | -3.00 |
| Administración | Servicios públicos | 216,000.00 | 162,000.00 | 157,140.00 | 5,400.00 | 53,460.00 | -4,860.00 | -3.00 |
| Comercial | Eventos | 126,000.00 | 90,000.00 | 87,300.00 | 3,600.00 | 35,100.00 | -2,700.00 | -3.00 |
| Comercial | Publicidad | 270,000.00 | 207,000.00 | 200,790.00 | 6,300.00 | 62,910.00 | -6,210.00 | -3.00 |
| Operaciones | Transporte | 252,000.00 | 189,000.00 | 183,330.00 | 6,300.00 | 62,370.00 | -5,670.00 | -3.00 |
| Tecnología | Licencias | 360,000.00 | 270,000.00 | 261,900.00 | 9,000.00 | 89,100.00 | -8,100.00 | -3.00 |
| Tecnología | PRY-310 | 432,000.00 | 324,000.00 | 314,280.00 | 10,800.00 | 106,920.00 | -9,720.00 | -3.00 |
| Personal | Nómina | 1,440,000.00 | 1,080,000.00 | 1,080,000.00 | 36,000.00 | 324,000.00 | 0.00 | 0.00 |

**Lo que hay que atender (según la tabla del reporte):**
- Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año. Le quedan 5,700.00 disponibles.

**Señales que el motor levantó y la tabla del reporte no muestra** (están en `resultados.json`):
- Dos casos de `budget_version_mismatch`: `proyeccion-comercial-2026-09-30.csv` usa la versión 1 en Comercial · Publicidad (fila 2) y en Comercial · Eventos (fila 3). La vigente es la 2.
- Un caso de `forecast_stale`: la proyección de Operaciones · Transporte es del 2026-07-15, hace 83 días.

**Sin respuesta (sesión sin interfaz):**
- Las fechas del comité de presupuesto quedaron vacías.
- No aparecen los responsables de cada área en los documentos.
- No escribí `_CRITERIO_FINANZAS.txt` en la carpeta raíz.
- El acta 06 deja abierto un compromiso: Administración revisa el contrato de vigilancia.

**Dónde quedó todo:**
- Configuración: `.criterio/presupuesto/20730000015/config.json`
- Ficha: `estado-finanzas/20730000015-minera-puna-alta/presupuesto/2026/ficha.json`
- Reporte: `estado-finanzas/20730000015-minera-puna-alta/presupuesto/2026/reporte-variance-report.md`
- Salida de esta corrida: `estado-finanzas/20730000015-minera-puna-alta/corridas/salida-budget-setup.md` (corrida `2026-10-06-budget-setup-1`, 4 hallazgos)

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.