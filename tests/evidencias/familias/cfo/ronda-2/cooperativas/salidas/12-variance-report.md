# /criterio-budget:variance-report 

Términos vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06). Corte 2026-09, versión 2 del presupuesto. Hay una señal por atender, en Tecnología · Licencias.

# Ejecución contra aprobado · Cooperativa Sierra Alta · presupuesto 2026, corte 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Comité de presupuesto · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Tecnología · Licencias: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -2,390.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 6 · `2026-01/10-contabilidad/libro-mayor.csv` fila 10 · `2026-02/10-contabilidad/libro-mayor.csv` fila 10 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01, 2026-02, 2026-03, 2026-04, 2026-05, 2026-06, 2026-07, 2026-08, 2026-09

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 24,000.00 | 18,000.00 | 17,460.00 | 600.00 | 5,940.00 | -540.00 | -3.00 |
| Administración | Servicios públicos | 36,000.00 | 27,000.00 | 26,190.00 | 900.00 | 8,910.00 | -810.00 | -3.00 |
| Comercial | Eventos | 21,000.00 | 15,000.00 | 14,550.00 | 600.00 | 5,850.00 | -450.00 | -3.00 |
| Comercial | Publicidad | 45,000.00 | 34,500.00 | 33,465.00 | 1,050.00 | 10,485.00 | -1,035.00 | -3.00 |
| Operaciones | Transporte | 42,000.00 | 31,500.00 | 30,555.00 | 1,050.00 | 10,395.00 | -945.00 | -3.00 |
| Tecnología | Licencias | 60,000.00 | 45,000.00 | 43,650.00 | 13,960.00 | 2,390.00 | -1,350.00 | -3.00 |
| Tecnología | PRY-310 | 72,000.00 | 54,000.00 | 52,380.00 | 1,800.00 | 17,820.00 | -1,620.00 | -3.00 |
| Personal | Nómina | 240,000.00 | 180,000.00 | 180,000.00 | 6,000.00 | 54,000.00 | 0.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Cooperativa Sierra Alta (RUC 1790012345001), presupuesto 2026; tomado del nombre de la carpeta y de presupuesto-2026/
- ¿Cuál es la versión aprobada y su acta? → El acta 01 (2026-01-20) aprueba la versión 1; el acta 05 (2026-06-28) aprueba un traslado de 3,000.00 que coincide con la versión 2 (2026-06-30), pero ningún acta nombra esa versión. Se registró lo que dicen las actas.
- ¿Áreas y responsables? → No encontrado: ningún documento nombra a los responsables de las áreas. Áreas tomadas del mapeo: Administración, Comercial, Tecnología, Operaciones, Personal.
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité? → No encontrado en los documentos; quedó vacío
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Dónde se guarda lo que se encuentra? → estado-finanzas/1790012345001-cooperativa-sierra-alta, fuera de la carpeta de documentos
- ¿Términos? → Aceptados por José Francisco Ñáñez, 2026-10-06, versión 1.2

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-variance-report-1`.