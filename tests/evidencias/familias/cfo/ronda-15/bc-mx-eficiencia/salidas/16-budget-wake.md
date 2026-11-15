# /criterio-budget:budget-wake 

Esta corrida tenía trabajo porque llegó contabilidad nueva de enero a agosto de 2026. Revisé las carpetas: hay 62 documentos y ninguno es nuevo, cambió o no se pudo leer. Luego saqué la ejecución contra el presupuesto aprobado y la proyección al cierre del año, con corte a 2026-09. No había peticiones abiertas. Los términos ya estaban aceptados a nombre de José Francisco Ñáñez con fecha 2026-10-06, así que no hubo que registrarlos de nuevo.

Hay una sola cosa que atender: un gasto en la cuenta 5135, centro de costo ZZZ, que no tiene línea en el presupuesto.

---

# Ejecución contra aprobado · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `variance-report`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

Versión vigente: **2** (`presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`) · periodos procesados: 2026-01, 2026-02, 2026-03, 2026-04, 2026-05, 2026-06, 2026-07, 2026-08, 2026-09

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

- ¿Entidad y año presupuestal? → Distribuidora del Noroeste (DNO190402B43), 2026; tomado de la configuración de la familia y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → Rige la más reciente de 10-aprobado/: versión 2 (2026-06-30), que nace del traslado del acta 05 sobre la versión 1 aprobada en el acta 01 del 2026-01-20
- ¿Áreas y su responsable? → Áreas del presupuesto: Administración, Comercial, Tecnología, Operaciones, Personal. Responsables: no encontrados en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días; configuración, no norma
- ¿Fechas del comité? → No encontradas; el acta 06 menciona un próximo comité sin fecha
- ¿Fichas PMO? → estado-pmo/records (PRY-310.json)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste, el que ya fijó la familia

## Fuentes

- `2026-08/10-contabilidad/libro-mayor.csv`

---

# Proyección al cierre del año · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `forecast`

## Lo que hay que atender

Nada abierto en lo que procesa este comando.

## El resultado

| Área | Línea | Aprobado | Proyección del área | Al ritmo | Al plan |
|---|---|---|---|---|---|
| Administración | Mantenimiento | 432,000.00 | 423,360.00 (2026-09-30) | 465,600.00 | 457,200.00 |
| Administración | Servicios públicos | 648,000.00 | 635,040.00 (2026-09-30) | 628,560.00 | 633,420.00 |
| Comercial | Eventos | 378,000.00 | 370,440.00 (2026-09-30) | 349,200.00 | 369,900.00 |
| Comercial | Publicidad | 810,000.00 | 793,800.00 (2026-09-30) | 806,760.00 | 794,070.00 |
| Operaciones | Transporte | 756,000.00 | 740,880.00 (2026-09-30) | 733,320.00 | 738,990.00 |
| Personal | Nómina | 4,320,000.00 | 4,320,000.00 (2026-09-30) | 4,320,000.00 | 4,320,000.00 |
| Tecnología | Licencias | 1,080,000.00 | 1,058,400.00 (2026-09-30) | 1,047,600.00 | 1,055,700.00 |
| Tecnología | PRY-310 | 1,296,000.00 | 1,270,080.00 (2026-09-30) | 1,257,120.00 | 1,266,840.00 |

**Al ritmo:** el ejecutado más el mayor entre el promedio mensual por los meses que faltan y lo comprometido. **Al plan:** el ejecutado más lo que falta del aprobado según su distribución mensual.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Distribuidora del Noroeste (DNO190402B43), 2026; tomado de la configuración de la familia y de presupuesto-2026/
- ¿Cuál es la versión aprobada? → Rige la más reciente de 10-aprobado/: versión 2 (2026-06-30), que nace del traslado del acta 05 sobre la versión 1 aprobada en el acta 01 del 2026-01-20
- ¿Áreas y su responsable? → Áreas del presupuesto: Administración, Comercial, Tecnología, Operaciones, Personal. Responsables: no encontrados en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida a los 45 días; configuración, no norma
- ¿Fechas del comité? → No encontradas; el acta 06 menciona un próximo comité sin fecha
- ¿Fichas PMO? → estado-pmo/records (PRY-310.json)
- ¿Dónde guardo el estado? → estado-finanzas/DNO190402B43-distribuidora-del-noroeste, el que ya fijó la familia

## Fuentes

- Sin documentos citados.

---

La corrida quedó registrada con caso 2026-09, junto con el barrido, la ejecución y la proyección. Lo que se mostró quedó en `<espacio>/estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-budget-wake.md`.