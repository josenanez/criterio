# /criterio-budget:budget-scan 

Nada nuevo en la carpeta desde la corrida anterior: son 63 archivos, sin nuevos ni cambiados. Las 3 actas de `40-actas/` ya estaban en la ficha, así que no la modifiqué. Quedan 4 señales abiertas, todas en el reporte.

# Qué cambió en el presupuesto · Minera Cóndor · presupuesto 2026, corte 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Operaciones · Transporte: ejecutado 77,970.00 contra 67,800.00 aprobado al corte (+15.0 %) | 10,170.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 8 · `2026-01/10-contabilidad/libro-mayor.csv` fila 14 · `2026-02/10-contabilidad/libro-mayor.csv` fila 14 |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 9,600.00 entre la versión 1 y la 2 sin acta que lo apruebe | 9,600.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -9,600.00 entre la versión 1 y la 2 sin acta que lo apruebe | -9,600.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96.0 % de lo aprobado en el año | -1,900.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.csv` fila 4 · `2026-02/10-contabilidad/libro-mayor.csv` fila 4 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Entidad y año presupuestal? → Minera Cóndor (RUC 0990054321001), presupuesto 2026, corte 2026-09 (propuesto desde la carpeta)
- ¿Cuál es la versión aprobada? → No se fijó por cuenta propia: rige la más reciente de 10-aprobado (v2, 2026-06-30). El acta 01 aprueba la v1.
- ¿Áreas y responsables? → Áreas tomadas del mapeo: Administración, Comercial, Tecnología, Operaciones, Personal. Responsables: no encontrado en los documentos.
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma).
- ¿Fechas del comité? → No encontrado: el acta 06 dice «próximo comité» sin fecha; se deja vacío.
- ¿Fichas PMO? → Se encontró estado-pmo/records/PRY-310.json; se usa esa ruta.
- ¿Dónde guardo lo que encuentro? → estado-finanzas/0990054321001-minera-condor, fuera de la carpeta de documentos.
- ¿Términos? → Aceptados por José Francisco Ñáñez, 2026-10-06 (indicado en el argumento de la prueba).

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 4 hallazgos. La salida está en `estado-finanzas/0990054321001-minera-condor/corridas/salida-budget-scan.md`.