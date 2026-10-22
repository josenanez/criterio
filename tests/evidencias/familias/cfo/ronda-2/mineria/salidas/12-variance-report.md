# /criterio-budget:variance-report 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Corte 2026-09, fecha de prueba 2026-10-06.

Ojo con la versión: el reporte usa la versión 2 del presupuesto. La versión aprobada con acta es la 1 (acta 01 del 2026-01-20). La versión 2 no tiene acta que la apruebe como versión. El acta 05 solo aprueba el traslado de Publicidad a Eventos.

# Ejecución contra aprobado · Minera Cóndor · presupuesto 2026, corte 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Operaciones · Transporte: ejecutado 77,970.00 contra 67,800.00 aprobado al corte (+15.0 %) | 10,170.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 8 · `2026-01/10-contabilidad/libro-mayor.csv` fila 14 · `2026-02/10-contabilidad/libro-mayor.csv` fila 14 |
| 2 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -1,900.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 3 · `2026-01/10-contabilidad/libro-mayor.csv` fila 4 · `2026-02/10-contabilidad/libro-mayor.csv` fila 4 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01 a 2026-09

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Operaciones | Transporte | 93,600.00 | 67,800.00 | 77,970.00 | 2,580.00 | 13,050.00 | 10,170.00 | 15.00 |
| Administración | Mantenimiento | 48,000.00 | 36,000.00 | 34,920.00 | 11,180.00 | 1,900.00 | -1,080.00 | -3.00 |
| Administración | Servicios públicos | 72,000.00 | 54,000.00 | 52,380.00 | 1,800.00 | 17,820.00 | -1,620.00 | -3.00 |
| Comercial | Eventos | 42,000.00 | 30,000.00 | 29,100.00 | 1,200.00 | 11,700.00 | -900.00 | -3.00 |
| Comercial | Publicidad | 90,000.00 | 69,000.00 | 66,930.00 | 2,100.00 | 20,970.00 | -2,070.00 | -3.00 |
| Tecnología | Licencias | 110,400.00 | 85,200.00 | 82,644.00 | 2,520.00 | 25,236.00 | -2,556.00 | -3.00 |
| Tecnología | PRY-310 | 144,000.00 | 108,000.00 | 104,760.00 | 3,600.00 | 35,640.00 | -3,240.00 | -3.00 |
| Personal | Nómina | 480,000.00 | 360,000.00 | 360,000.00 | 12,000.00 | 108,000.00 | 0.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada y con qué acta? → La 1, acta 01 del 2026-01-20; la versión 2 no tiene acta que la apruebe como versión (el acta 05 solo aprueba el traslado Publicidad a Eventos)
- ¿Fechas del comité de presupuesto? → No hay fechas en los documentos; queda vacío

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

**Corrida registrada:** `2026-10-06-variance-report-1`, con 4 hallazgos. Guardé la salida en `estado-finanzas/0990054321001-minera-condor/corridas/salida-variance-report.md`.