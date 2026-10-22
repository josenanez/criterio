# /criterio-budget:variance-report 

Términos vigentes y aceptados (versión 1.2). Hay dos señales: Administración se declaró dentro del presupuesto y Servicios públicos no lo sostiene, y esa misma línea supera el umbral de desviación.

# Ejecución contra aprobado · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.7.0 · **Aprueba:** Contralor · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 4.050.000,00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %) | 4.050.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01 a 2026-09

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Servicios públicos | 36.000.000,00 | 27.000.000,00 | 31.050.000,00 | 900.000,00 | 4.050.000,00 | 4.050.000,00 | 15,00 |
| Administración | Mantenimiento | 24.000.000,00 | 18.000.000,00 | 17.460.000,00 | 600.000,00 | 5.940.000,00 | -540.000,00 | -3,00 |
| Comercial | Eventos | 21.000.000,00 | 15.000.000,00 | 14.550.000,00 | 600.000,00 | 5.850.000,00 | -450.000,00 | -3,00 |
| Comercial | Publicidad | 45.000.000,00 | 34.500.000,00 | 33.465.000,00 | 1.050.000,00 | 10.485.000,00 | -1.035.000,00 | -3,00 |
| Operaciones | Transporte | 46.800.000,00 | 33.900.000,00 | 32.883.000,00 | 1.290.000,00 | 12.627.000,00 | -1.017.000,00 | -3,00 |
| Tecnología | Licencias | 55.200.000,00 | 42.600.000,00 | 41.322.000,00 | 1.260.000,00 | 12.618.000,00 | -1.278.000,00 | -3,00 |
| Tecnología | PRY-310 | 72.000.000,00 | 54.000.000,00 | 52.380.000,00 | 1.800.000,00 | 17.820.000,00 | -1.620.000,00 | -3,00 |
| Personal | Nómina | 240.000.000,00 | 180.000.000,00 | 180.000.000,00 | 6.000.000,00 | 54.000.000,00 | 0,00 | 0,00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada y su acta? → Sesión sin interfaz: respuesta sugerida. Acta 01 (2026-01-20) aprueba la versión 1; el acta 05 (2026-06-28) aprueba un traslado y existe la versión 2 del 2026-06-30. Ningún acta dice que apruebe la versión 2 como tal.

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-variance-report-1`. Lo mostrado está guardado en `estado-finanzas/900123456-banco-andino/corridas/salida-variance-report.md`.