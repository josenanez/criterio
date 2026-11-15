# /criterio-budget:variance-report 

Hay una señal para atender: gasto de la cuenta 5135 en el centro ZZZ sin línea presupuestal. Ninguna línea supera el umbral de desviación del 10 %.

# Ejecución contra aprobado · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01 a 2026-09

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 432,000.00 | 324,000.00 | 349,200.00 | 10,800.00 | 72,000.00 | 25,200.00 | 7.78 |
| Administración | Servicios públicos | 648,000.00 | 486,000.00 | 471,420.00 | 16,200.00 | 160,380.00 | -14,580.00 | -3.00 |
| Comercial | Eventos | 378,000.00 | 270,000.00 | 261,900.00 | 10,800.00 | 105,300.00 | -8,100.00 | -3.00 |
| Operaciones | Transporte | 756,000.00 | 567,000.00 | 549,990.00 | 18,900.00 | 187,110.00 | -17,010.00 | -3.00 |
| Tecnología | Licencias | 1,080,000.00 | 810,000.00 | 785,700.00 | 27,000.00 | 267,300.00 | -24,300.00 | -3.00 |
| Tecnología | PRY-310 | 1,296,000.00 | 972,000.00 | 942,840.00 | 32,400.00 | 320,760.00 | -29,160.00 | -3.00 |
| Comercial | Publicidad | 810,000.00 | 621,000.00 | 605,070.00 | 18,900.00 | 186,030.00 | -15,930.00 | -2.57 |
| Personal | Nómina | 4,320,000.00 | 3,240,000.00 | 3,240,000.00 | 108,000.00 | 972,000.00 | 0.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Distribuidora del Noroeste (DNO190402B43), 2026; tomado de la configuración y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → Rige la más reciente de 10-aprobado/: versión 2 (2026-06-30), que nace del traslado del acta 05 sobre la versión 1 aprobada en el acta 01 del 2026-01-20
- ¿Áreas y su responsable? → Áreas: Administración, Comercial, Tecnología, Operaciones, Personal. Responsables: no encontrados en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Desviación 10 %, comprometido 95 %, proyección vencida a los 45 días; configuración, no norma
- ¿Fechas del comité? → No encontradas; el acta 06 menciona un próximo comité sin fecha
- ¿Fichas PMO? → estado-pmo/records (PRY-310.json)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

La corrida quedó registrada como `2026-10-06-variance-report-1` (1 hallazgo), con la salida en `corridas/salida-variance-report.md`.

Dos cosas que debes saber sobre lo que te muestro:
- Acorté la línea de periodos procesados a "2026-01 a 2026-09"; el motor los lista uno por uno.
- Quité de las preguntas la frase "de la familia" y la referencia a `config.example.json`. Son retoques de redacción. El archivo guardado en `corridas/salida-variance-report.md` lleva el reporte del motor completo y sin esos cambios.