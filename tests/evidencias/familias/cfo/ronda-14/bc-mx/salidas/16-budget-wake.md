# /criterio-budget:budget-wake 

Esta corrida tenía trabajo pendiente porque había contabilidad nueva de 2026-01 a 2026-08, y nadie dejó peticiones en Rostrum. Revisé la carpeta: hay 62 archivos y ninguno es nuevo, cambió ni está fuera de lugar. Abajo van la ejecución y la proyección con corte a 2026-08, tal como las escribió el motor.

---

# Ejecución contra aprobado · Distribuidora del Noroeste · presupuesto 2026, corte 2026-08

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-08 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01, 2026-02, 2026-03, 2026-04, 2026-05, 2026-06, 2026-07, 2026-08

| Área | Línea | Aprobado | Al corte | Ejecutado | Comprometido | Disponible | Desviación | % |
|---|---|---|---|---|---|---|---|---|
| Administración | Mantenimiento | 432,000.00 | 288,000.00 | 279,360.00 | 10,800.00 | 141,840.00 | -8,640.00 | -3.00 |
| Administración | Servicios públicos | 648,000.00 | 432,000.00 | 419,040.00 | 16,200.00 | 212,760.00 | -12,960.00 | -3.00 |
| Comercial | Eventos | 378,000.00 | 234,000.00 | 226,980.00 | 10,800.00 | 140,220.00 | -7,020.00 | -3.00 |
| Comercial | Publicidad | 810,000.00 | 558,000.00 | 541,260.00 | 18,900.00 | 249,840.00 | -16,740.00 | -3.00 |
| Operaciones | Transporte | 756,000.00 | 504,000.00 | 488,880.00 | 18,900.00 | 248,220.00 | -15,120.00 | -3.00 |
| Tecnología | Licencias | 1,080,000.00 | 720,000.00 | 698,400.00 | 27,000.00 | 354,600.00 | -21,600.00 | -3.00 |
| Tecnología | PRY-310 | 1,296,000.00 | 864,000.00 | 838,080.00 | 32,400.00 | 425,520.00 | -25,920.00 | -3.00 |
| Personal | Nómina | 4,320,000.00 | 2,880,000.00 | 2,880,000.00 | 108,000.00 | 1,332,000.00 | 0.00 | 0.00 |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Distribuidora del Noroeste (RFC DNO190402B43), 2026 — tomado de la configuración de Clara y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → La vigente es la 2 (la más reciente de 10-aprobado/); la 1 la aprueba el acta 01 del 2026-01-20 y la 2 nace del traslado del acta 05
- ¿Quién responde por cada área? → No sé — ningún documento lo dice
- ¿Umbrales? → Los propuestos: desviación 10 %, comprometido 95 %, proyección vencida a 45 días
- ¿Fechas del comité de presupuesto? → Ninguna fijada en los documentos
- ¿Dónde están las fichas PMO? → estado-pmo/records (PRY-310)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste, el mismo que usa Clara

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

---

# Proyección al cierre del año · Distribuidora del Noroeste · presupuesto 2026, corte 2026-08

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-08 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `forecast`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 432,000.00 | 423,360.00 (2026-09-30) | 419,040.00 | 423,360.00 |
| Administración | Servicios públicos | 648,000.00 | 635,040.00 (2026-09-30) | 628,560.00 | 635,040.00 |
| Comercial | Eventos | 378,000.00 | 370,440.00 (2026-09-30) | 340,470.00 | 370,980.00 |
| Comercial | Publicidad | 810,000.00 | 793,800.00 (2026-09-30) | 811,890.00 | 793,260.00 |
| Operaciones | Transporte | 756,000.00 | 740,880.00 (2026-09-30) | 733,320.00 | 740,880.00 |
| Personal | Nómina | 4,320,000.00 | 4,320,000.00 (2026-09-30) | 4,320,000.00 | 4,320,000.00 |
| Tecnología | Licencias | 1,080,000.00 | 1,058,400.00 (2026-09-30) | 1,047,600.00 | 1,058,400.00 |
| Tecnología | PRY-310 | 1,296,000.00 | 1,270,080.00 (2026-09-30) | 1,257,120.00 | 1,270,080.00 |

**Al ritmo:** el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan:** el ejecutado más lo que falta del aprobado según su distribución mensual.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Distribuidora del Noroeste (RFC DNO190402B43), 2026 — tomado de la configuración de Clara y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → La vigente es la 2 (la más reciente de 10-aprobado/); la 1 la aprueba el acta 01 del 2026-01-20 y la 2 nace del traslado del acta 05
- ¿Quién responde por cada área? → No sé — ningún documento lo dice
- ¿Umbrales? → Los propuestos: desviación 10 %, comprometido 95 %, proyección vencida a 45 días
- ¿Fechas del comité de presupuesto? → Ninguna fijada en los documentos
- ¿Dónde están las fichas PMO? → estado-pmo/records (PRY-310)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste, el mismo que usa Clara

## Fuentes

- Sin documentos citados.

---

Registré las cuatro corridas con caso 2026-08: `budget-scan-2`, `variance-report-2`, `forecast-2` y `budget-wake-1`. Lo que se mostró está en `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-budget-wake.md`. Los términos ya estaban vigentes (versión 1.5.4), así que no hizo falta volver a registrar la aceptación.