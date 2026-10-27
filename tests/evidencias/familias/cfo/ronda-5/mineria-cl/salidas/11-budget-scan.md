# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior. Las tres actas de `40-actas/` ya estaban en la ficha y coinciden con ella, así que no la modifiqué. Aparecen dos señales.

# Qué cambió en el presupuesto · Minera Atacama Norte · presupuesto 2026, corte 2026-09

**Entidad:** Minera Atacama Norte (76089001-4) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Operaciones · Transporte: ejecutado 21.735.000,00 contra 18.900.000,00 aprobado al corte (+15,0 %) | 2.835.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 8 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 14 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 14 |
| 2 | Ejecutado más comprometido se acerca a lo aprobado sin holgura (`committed_near_approved`) | Administración · Mantenimiento: ejecutado más comprometido es 96,0 % de lo aprobado en el año | -570.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 3 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 4 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 4 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad y el año presupuestal? → Minera Atacama Norte (76089001-4), presupuesto 2026, corte 2026-09 (tomado de la carpeta y de la configuración de cierre existente)
- ¿Cuál es la versión aprobada y su acta? → La vigente es la más reciente de 10-aprobado/ (v2, 2026-06-30), nacida del traslado del acta 05; la v1 la aprueba el acta 01 del 2026-01-20
- ¿Áreas y responsables? → Las que trae el presupuesto y el mapeo; responsables no se encontraron en los documentos
- ¿Mapeo de cuentas a líneas? → 00-referencia/mapeo-presupuesto.csv
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días (configuración, no norma)
- ¿Fechas del comité? → No hay fecha futura en los documentos; el acta 06 es del 2026-09-10; se deja vacío
- ¿Fichas PMO? → estado-pmo/records (existe PRY-310.json)
- ¿Dónde guardo lo que encuentro? → estado-finanzas/76089001-4-minera-atacama-norte

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`

La corrida quedó registrada como `2026-10-06-budget-scan-1` con 2 hallazgos. La salida está en `estado-finanzas/76089001-4-minera-atacama-norte/corridas/salida-budget-scan.md`.

Dos cosas sobre cómo corrió:
- Los términos ya estaban vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06), así que no hubo que registrar nada.
- El reporte salió por pantalla y no confirmé que el motor lo guardara también en `reporte-budget-scan.md`. Lo que quedó en disco es la copia que escribí a mano en `salida-budget-scan.md`, con una línea de introducción antes del encabezado.