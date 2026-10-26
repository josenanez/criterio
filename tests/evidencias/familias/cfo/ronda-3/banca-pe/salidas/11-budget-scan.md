# /criterio-budget:budget-scan 

Corrida de `budget-scan` para Banco Ribera (corte 2026-09): sin archivos nuevos ni cambiados, y el motor encontró 4 señales. Los términos (v1.2) ya estaban vigentes a nombre de José Francisco Ñáñez, así que no hizo falta aceptarlos de nuevo.

Las tres actas de `40-actas/` y el correo de Administración ya estaban en la ficha con su cita, y coinciden con los documentos. No la modifiqué. Al calcular, `record_issues` salió vacío y no quedó nada sin procesar.

# Qué cambió en el presupuesto · Banco Ribera · presupuesto 2026, corte 2026-09

**Entidad:** Banco Ribera (20710000019) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.9.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 16,200.00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 19,200.00 entre la versión 1 y la 2 sin acta que lo apruebe | 19,200.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -19,200.00 entre la versión 1 y la 2 sin acta que lo apruebe | -19,200.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 124,200.00 contra 108,000.00 aprobado al corte (+15.0 %) | 16,200.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 2 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → La 1, acta 01 del 2026-01-20; no fijé approved_version, rige la más reciente de 10-aprobado/
- ¿Fechas del comité de presupuesto? → No encontradas en los documentos; el acta 06 no trae la del próximo comité

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

Esto es lo que se ve en el reporte:
- **Administración:** dice que va dentro del presupuesto (correo del 2026-10-01), pero Servicios públicos supera lo aprobado al corte en 15.0 %.
- **Versión 2 del presupuesto (2026-06-30):** movió 19,200.00 de Tecnología · Licencias a Operaciones · Transporte, y ninguna acta lo aprueba. El único traslado con acta es el del acta 05, de 12,000.00 de Comercial · Publicidad a Eventos.
- **Compromiso abierto del acta 06:** Administración debe revisar el contrato de vigilancia antes del próximo comité. El acta no da fecha de ese comité.

La corrida quedó registrada con el id `2026-10-06-budget-scan-3` y 4 hallazgos. La salida está guardada en `estado-finanzas/20710000019-banco-ribera/corridas/salida-budget-scan.md`.