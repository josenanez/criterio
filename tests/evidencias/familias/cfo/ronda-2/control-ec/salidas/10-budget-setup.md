# /criterio-budget:budget-setup finanzas/1790000001001-comercial-control

## Listo — Comercial Control (1790000001001) · presupuesto 2026

**Lo que miré:** 2 versiones aprobadas, contabilidad de enero a septiembre de 2026 (9 periodos), 3 actas, 1 archivo de compromisos, 5 proyecciones de área y 1 correo de Administración.

**Versión aprobada:** el acta 01 (2026-01-20) aprueba la versión 1. El traslado del acta 05 (2026-06-28) está aplicado en la versión 2 (2026-06-30), que es la que usó el cálculo.

**Términos:** aceptados por José Francisco Ñáñez para la versión 0.8.0 (términos 1.2), con fecha 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/aceptacion-criterio-budget-0.8.0-2026-10-06.*`.

**Respuestas por defecto:** nadie contestó, así que tomé estas de los documentos:
- **Año y corte:** presupuesto 2026, con corte en 2026-09.
- **Umbrales:** los de `config.example.json`, que son configuración y no norma. Desviación 10 %, comprometido 95 % y proyección vencida a los 45 días.
- **Fichas del PMO:** `estado-pmo/records`, donde está `PRY-310.json`.
- **Estado:** `estado-finanzas/1790000001001-comercial-control`.
- **Sin dato:** ningún documento trae las fechas del comité ni los responsables por área, así que quedaron vacíos.
- **Marca de la raíz:** no dejé `_CRITERIO_FINANZAS.txt`. La ruta vino en el argumento y no había quién autorizara escribir en los documentos.

### Ejecución contra aprobado (corte 2026-09)

El motor no dio ninguna señal abierta. Siete de las ocho líneas van un 3.00 % por debajo de lo previsto al corte; Nómina va en 0.00 %.

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 36,000.00 | 27,000.00 | 26,190.00 | 900.00 | 8,910.00 | -810.00 | -3.00 |
| Administración | Servicios públicos | 54,000.00 | 40,500.00 | 39,285.00 | 1,350.00 | 13,365.00 | -1,215.00 | -3.00 |
| Comercial | Eventos | 31,500.00 | 22,500.00 | 21,825.00 | 900.00 | 8,775.00 | -675.00 | -3.00 |
| Comercial | Publicidad | 67,500.00 | 51,750.00 | 50,197.50 | 1,575.00 | 15,727.50 | -1,552.50 | -3.00 |
| Operaciones | Transporte | 63,000.00 | 47,250.00 | 45,832.50 | 1,575.00 | 15,592.50 | -1,417.50 | -3.00 |
| Tecnología | Licencias | 90,000.00 | 67,500.00 | 65,475.00 | 2,250.00 | 22,275.00 | -2,025.00 | -3.00 |
| Tecnología | PRY-310 | 108,000.00 | 81,000.00 | 78,570.00 | 2,700.00 | 26,730.00 | -2,430.00 | -3.00 |
| Personal | Nómina | 360,000.00 | 270,000.00 | 270,000.00 | 9,000.00 | 81,000.00 | 0.00 | 0.00 |

Todo lo que llegó se procesó. El reporte completo, tal como lo escribió el motor, está en `estado-finanzas/1790000001001-comercial-control/presupuesto/2026/reporte-variance-report.md`.

Queda abierto un compromiso del acta 06 (2026-09-10): que Administración revise el contrato de vigilancia antes del próximo comité. Está en la ficha, sin evidencia, y este comando no lo marca como señal.

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La corrida quedó registrada como `2026-10-06-budget-setup-1`.