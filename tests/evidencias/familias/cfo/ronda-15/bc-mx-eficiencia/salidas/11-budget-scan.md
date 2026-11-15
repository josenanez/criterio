# /criterio-budget:budget-scan 

No files are new, changed or deleted since the last run: all 62 documents are the same. The budget record already holds the 3 minutes in `40-actas/`, so there was nothing new to extract. The engine found one signal.

# Qué cambió en el presupuesto · Distribuidora del Noroeste · presupuesto 2026, corte 2026-09

**Entidad:** Distribuidora del Noroeste (DNO190402B43) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.5.4 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Hay gasto en una cuenta o centro de costo sin línea presupuestal (`spend_without_budget_line`) | cuenta 5135 · centro ZZZ: 12,600.00 en 2026-08 sin línea presupuestal | 12,600.00 | — | — | `2026-08/10-contabilidad/libro-mayor.csv` fila 18 |

## El resultado

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

I saved the output to `estado-finanzas/DNO190402B43-distribuidora-del-noroeste/corridas/salida-budget-scan.md` and registered the run as `2026-10-06-budget-scan-1`. The terms were already in effect (accepted 2026-10-06 by José Francisco Ñáñez), so nothing needed to be recorded. The engine left the report's "El resultado" section empty, and I'm showing it as it came out.