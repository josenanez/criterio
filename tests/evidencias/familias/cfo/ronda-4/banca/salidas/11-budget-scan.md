# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (63 documentos en el inventario). Las tres actas de `40-actas/` ya estaban en la ficha, con su cita, y el cálculo da cinco señales.

# Qué cambió en el presupuesto · Banco Andino · presupuesto 2026, corte 2026-09

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.10.0 · **Aprueba:** Sofía León · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 4.050.000,00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | 4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -4.800.000,00 entre la versión 1 y la 2 sin acta que lo apruebe | -4.800.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 31.050.000,00 contra 27.000.000,00 aprobado al corte (+15,0 %) | 4.050.000,00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.csv` fila 2 · `2026-02/10-contabilidad/libro-mayor.csv` fila 2 |
| 5 | El presupuesto de un proyecto en su ficha no es el que tiene asignado el área (`project_budget_mismatch`) | PRY-310: la ficha del proyecto dice 64.800.000,00 y el área tiene asignado 72.000.000,00 | -7.200.000,00 | — | — | `PRY-310.json` · `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 7 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Rige la v2 (la más reciente de 10-aprobado/). El acta 01 aprueba la v1; el acta 05 respalda solo el traslado Publicidad a Eventos.
- ¿Umbrales y fechas del comité? → Los del ejemplo: desviación 10 %, comprometido 95 %, proyección vencida 45 días; comité 2026-10-15.
- ¿Dónde están las fichas PMO? → estado-pmo/records (existe PRY-310.json).

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.csv`
- `2026-02/10-contabilidad/libro-mayor.csv`
- `PRY-310.json`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-budget-scan-1` con 5 hallazgos.

Los términos (versión 1.2) ya estaban vigentes y aceptados para la versión 0.10.0 del plugin. No tuve que registrar la aceptación a nombre de José Francisco Ñáñez ni mostrar el texto de los términos. Pasé `--today 2026-10-06` en cada llamada al motor que lo acepta.

La sección «El resultado» salió vacía en el reporte del motor, y la dejé tal cual.