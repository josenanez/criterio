# /criterio-budget:variance-report 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Año y corte salen de la configuración: 2026, corte 2026-09. Como no hay nadie que conteste, las preguntas se resolvieron con la respuesta que sugieren los documentos, y el reporte las deja escritas.

# Ejecución contra aprobado · Almacenes Caribe · presupuesto 2026, corte 2026-09

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 560.000,00 en 2026-08 sin línea presupuestal | 560.000,00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01 a 2026-09

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 19.200.000,00 | 14.400.000,00 | 15.520.000,00 | 480.000,00 | 3.200.000,00 | 1.120.000,00 | 7,78 |
| Administración | Servicios públicos | 28.800.000,00 | 21.600.000,00 | 20.952.000,00 | 720.000,00 | 7.128.000,00 | -648.000,00 | -3,00 |
| Comercial | Eventos | 16.800.000,00 | 12.000.000,00 | 11.640.000,00 | 480.000,00 | 4.680.000,00 | -360.000,00 | -3,00 |
| Operaciones | Transporte | 33.600.000,00 | 25.200.000,00 | 24.444.000,00 | 840.000,00 | 8.316.000,00 | -756.000,00 | -3,00 |
| Tecnología | Licencias | 48.000.000,00 | 36.000.000,00 | 34.920.000,00 | 1.200.000,00 | 11.880.000,00 | -1.080.000,00 | -3,00 |
| Tecnología | PRY-310 | 57.600.000,00 | 43.200.000,00 | 41.904.000,00 | 1.440.000,00 | 14.256.000,00 | -1.296.000,00 | -3,00 |
| Comercial | Publicidad | 36.000.000,00 | 27.600.000,00 | 26.892.000,00 | 840.000,00 | 8.268.000,00 | -708.000,00 | -2,57 |
| Personal | Nómina | 192.000.000,00 | 144.000.000,00 | 144.000.000,00 | 4.800.000,00 | 43.200.000,00 | 0,00 | 0,00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- **Versión aprobada:** se propone la 2 (`presupuesto-2026-v2-2026-06-30.csv`). Su cambio coincide con el traslado del acta 05 del 2026-06-28. El acta 01 aprueba solo la versión 1 y ningún acta dice "versión 2".
- **Cuentas de gasto:** prefijo 51 (5105, 5135, 5145, 5195), el del mapeo de presupuesto.
- **Fechas del comité:** no encontradas. El acta 06 no fija la del próximo comité.
- **Fichas PMO:** `estado-pmo/records` (contiene `PRY-310.json`).
- **Marca `_CRITERIO_FINANZAS.txt` en la carpeta de documentos:** no se deja, porque nadie autorizó escribir ahí.

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

La salida quedó en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-variance-report.md`. La corrida quedó registrada como `2026-10-06-variance-report-1` (el motor contó 2 hallazgos).

Dos cosas que el reporte no resuelve:
- **Mantenimiento:** es la única línea con desviación positiva (7,78 %), por debajo del umbral de 10 %.
- **Versión 2:** la elegí por coincidencia con el traslado del acta 05, no porque un acta la apruebe. Conviene que Sofía León lo confirme.