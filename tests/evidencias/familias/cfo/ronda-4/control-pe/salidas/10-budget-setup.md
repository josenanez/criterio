# /criterio-budget:budget-setup finanzas/20790000014-comercial-control-sur

## Listo: Comercial Control Sur · presupuesto 2026

Esta fue una sesión sin interfaz, así que tomé yo las respuestas sugeridas a partir de los documentos.

**Lo que miré:** 2 versiones (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la vigente es la 2, la más reciente de `10-aprobado/`. La versión 1 la aprueba el acta 01 del 2026-01-20. La versión 2 nace del traslado del acta 05 del 2026-06-28, que mueve 9,000.00 de Comercial · Publicidad a Comercial · Eventos. No fijé `approved_version`.

**Términos:** José Francisco Ñáñez los aceptó para la versión 0.10.0 (fecha 2026-10-06). Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.

**Lo que no encontré:**
- No hay responsables por área en los documentos, así que no registré ninguno.
- Tampoco hay fecha del próximo comité; `committee_dates` quedó vacío.
- No dejé la marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos. Es lo único que se escribe ahí; si la quieres, la creo.

**Qué hay en la ficha:**
- **Administración:** un correo del 2026-10-01 dice que va dentro del presupuesto. El motor no levantó ninguna señal contra esa afirmación.
- **Comité:** el acta 06 deja un compromiso abierto, que Administración revise el contrato de vigilancia antes del próximo comité.

**Ejecución al corte 2026-09** (PEN, cifras del motor; la versión vigente es la 2):

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 72,000.00 | 54,000.00 | 52,380.00 | 1,800.00 | 17,820.00 | -1,620.00 | -3.00 |
| Administración | Servicios públicos | 108,000.00 | 81,000.00 | 78,570.00 | 2,700.00 | 26,730.00 | -2,430.00 | -3.00 |
| Comercial | Eventos | 63,000.00 | 45,000.00 | 43,650.00 | 1,800.00 | 17,550.00 | -1,350.00 | -3.00 |
| Comercial | Publicidad | 135,000.00 | 103,500.00 | 100,395.00 | 3,150.00 | 31,455.00 | -3,105.00 | -3.00 |
| Operaciones | Transporte | 126,000.00 | 94,500.00 | 91,665.00 | 3,150.00 | 31,185.00 | -2,835.00 | -3.00 |
| Tecnología | Licencias | 180,000.00 | 135,000.00 | 130,950.00 | 4,500.00 | 44,550.00 | -4,050.00 | -3.00 |
| Tecnología | PRY-310 | 216,000.00 | 162,000.00 | 157,140.00 | 5,400.00 | 53,460.00 | -4,860.00 | -3.00 |
| Personal | Nómina | 720,000.00 | 540,000.00 | 540,000.00 | 18,000.00 | 162,000.00 | 0.00 | 0.00 |

Todo lo que llegó se procesó. Nada queda abierto en lo que procesa este comando, y `record_issues` salió vacío.

Los informes y la salida de la corrida quedaron en `estado-finanzas/20790000014-comercial-control-sur/`. El reporte completo, con las preguntas y respuestas, está en `presupuesto/2026/reporte-variance-report.md`. La salida de esta conversación está en `corridas/salida-budget-setup.md`. La configuración está en `.criterio/presupuesto/20790000014/config.json`.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.