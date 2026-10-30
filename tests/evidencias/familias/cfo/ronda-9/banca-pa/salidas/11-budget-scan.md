# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (65 documentos). Las tres actas de `40-actas/` ya estaban en la ficha con su cita. El cálculo da 4 señales.

# Qué cambió en el presupuesto · Banco Istmeño · presupuesto 2026, corte 2026-09

**Entidad:** Banco Istmeño (155731001-2-2016) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.0.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 8,100.00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 9,600.00 entre la versión 1 y la 2 sin acta que lo apruebe | 9,600.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -9,600.00 entre la versión 1 y la 2 sin acta que lo apruebe | -9,600.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 62,100.00 contra 54,000.00 aprobado al corte (+15.0 %) | 8,100.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx` fila 2 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 2 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La vigente es la más reciente de 10-aprobado/ (v2, 2026-06-30); la v1 la aprueba el acta 01 del 2026-01-20 y el acta 05 del 2026-06-28 respalda el traslado Publicidad → Eventos. No se fijó approved_version.
- ¿Qué cuentas son gasto? → Prefijo 51, según mapeo-presupuesto.csv (5135, 5145, 5195).
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días.
- ¿Fechas del comité de presupuesto? → No encontrada en los documentos; se deja vacía.
- ¿Dónde están las fichas PMO? → estado-pmo/records (contiene PRY-310.json).
- ¿Dónde se guarda el estado? → estado-finanzas/155731001-2-2016-banco-istmeno (fuera de la carpeta de documentos).

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.xlsx`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-budget-scan-1`, con 4 hallazgos. El texto mostrado está en `<espacio>/estado-finanzas/155731001-2-2016-banco-istmeno/corridas/salida-budget-scan.md`.

Los términos ya estaban vigentes (versión 1.3, aceptada a nombre de José Francisco Ñáñez el 2026-10-06), así que no hizo falta registrarlos otra vez.