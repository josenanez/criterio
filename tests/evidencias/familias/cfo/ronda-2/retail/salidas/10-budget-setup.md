# /criterio-budget:budget-setup finanzas/900765432-almacenes-caribe

## Listo — Almacenes Caribe (900765432) · presupuesto 2026

**Lo que miré:** 2 versiones (v1 del 2026-01-15 y v2 del 2026-06-30), contabilidad de 2026-01 a 2026-09 y 3 actas.

**Versión aprobada:** la 2, `presupuesto-2026-v2-2026-06-30.csv`.
- La propuse porque su cambio coincide con el traslado del acta 05 (2026-06-28), que pasa 2.400.000 de Publicidad a Eventos.
- Ningún acta dice «versión 2»: el acta 01 (2026-01-20) aprueba solo la versión 1. Hay que confirmarlo con quien aprueba.

**Términos:** aceptados para la versión 0.8.0 (términos 1.2) por José Francisco Ñáñez, 2026-10-06. Los comprobantes están en `.criterio/terminos/aceptacion-criterio-budget-0.8.0-2026-10-06.md` y `.pdf`.

**Configuración:**
- Config: `.criterio/presupuesto/900765432/config.json`.
- Estado: `estado-finanzas/900765432-almacenes-caribe`.
- Fichas PMO: `estado-pmo/records`, donde está `PRY-310.json`.
- Gasto: cuentas con prefijo 51.
- Umbrales del ejemplo: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días. Son configuración, no norma.
- Fechas de comité: ninguna, porque el acta 06 no la trae.

**Preguntas sin quien contestara:** tomé la respuesta sugerida en cada una. Versión aprobada: la 2. Cuentas de gasto: 51. Fechas del comité: no encontrado. Fichas PMO: `estado-pmo/records`. No dejé la marca `_CRITERIO_FINANZAS.txt` porque nadie autorizó escribir en los documentos.

**Además de lo que trae el reporte:**
- **Proyección sobre lo aprobado:** el cálculo levantó una señal que el reporte no lista. En Tecnología · PRY-310, la proyección al cierre del área es 63.360.000,00 contra 57.600.000,00 aprobados (está en `resultados.json`).
- **Compromiso abierto del acta 06:** Administración revisa el contrato de vigilancia antes del próximo comité.

El reporte lo escribió el motor. Queda en `estado-finanzas/900765432-almacenes-caribe/presupuesto/2026/reporte-variance-report.md`.

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

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

**Cuándo vuelvo:** cuando llegue la contabilidad de un mes nuevo, antes de cada comité y una vez por semana por los compromisos.

La salida completa quedó en `estado-finanzas/900765432-almacenes-caribe/corridas/salida-budget-setup.md` y la corrida está registrada como `2026-10-06-budget-setup-1`.