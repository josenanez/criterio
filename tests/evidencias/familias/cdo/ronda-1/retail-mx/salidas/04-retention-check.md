# /criterio-data-governance:retention-check 

Los términos ya estaban vigentes (versión 1.6), así que no registré ninguna aceptación. El reporte encontró una política de datos vencida.

**Política vencida:** la política de datos debía revisarse el 2025-06-30 y no hay una versión posterior. Han pasado 513 días. La política de conservación está al día (revisión el 2027-09-01).

**Plazos de conservación:** el reporte da, para cada conjunto, la fecha antes de la cual vence lo conservado.

| Conjunto | Tipo | Plazo | Registro más antiguo | Vence antes del |
|---|---|---|---|---|
| DS-01 | Clientes | 120 meses | 2018-03-01 | 2016-11-25 |
| DS-02 | Transaccional | 120 meses | 2017-01-01 | 2016-11-25 |
| DS-03 | Proveedores | 60 meses | 2023-01-01 | 2021-11-25 |
| DS-04 | Candidatos | 24 meses | 2025-01-01 | 2024-11-25 |
| DS-05 | Transaccional | 120 meses | 2020-01-01 | 2016-11-25 |

El reporte no marca ningún conjunto como pasado de plazo; decidir qué se archiva o se borra le toca al dueño de cada dato.

**Corrida:** quedó registrada con el id `2026-11-25-retention-check-1`. El motor la contó con 4 hallazgos, aunque el reporte lista una sola señal. No sé de dónde sale esa diferencia.

Archivos, en `estado-datos/rcm190305ab1-retail-central-sintetico/`:
- `gobierno/2026-11/reporte-retention-check.md`
- `corridas/salida-retention-check.md`