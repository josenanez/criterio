# /criterio-budget:budget-scan 

Sin archivos nuevos ni cambiados desde la corrida anterior (66 en el inventario). Leí las tres actas y la ficha ya las recoge. Salieron 4 señales.

# Qué cambió en el presupuesto · Banco de Occidente Sintético · presupuesto 2026, corte 2026-09

**Entidad:** Banco de Occidente Sintético (08010004578120) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 1.1.0 · **Aprueba:** Contralor · **Comando:** `budget-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | El área se reporta dentro del presupuesto y los números no lo sostienen (`declared_vs_evidence`) | Administración se reporta dentro del presupuesto (presupuesto-2026/30-proyecciones/correo-administracion.md) y 1 línea(s) no lo sostienen: Servicios públicos | 202,500.00 | — | — | `presupuesto-2026/30-proyecciones/correo-administracion.md` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 240,000.00 entre la versión 1 y la 2 sin acta que lo apruebe | 240,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 3 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -240,000.00 entre la versión 1 y la 2 sin acta que lo apruebe | -240,000.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx` |
| 4 | Lo ejecutado al corte se aparta del presupuesto más del porcentaje configurado (`variance_over_threshold`) | Administración · Servicios públicos: ejecutado 1,552,500.00 contra 1,350,000.00 aprobado al corte (+15.0 %) | 202,500.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` fila 2 · `2026-01/10-contabilidad/libro-mayor.xlsx` fila 2 · `2026-02/10-contabilidad/libro-mayor.xlsx` fila 2 |

## El resultado

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada? → Rige la más reciente de 10-aprobado/ (v2, 2026-06-30); el acta 01 (2026-01-20) aprueba la v1 y el acta 05 (2026-06-28) aprueba el traslado de Publicidad a Eventos
- ¿Cuáles son las fechas del comité de presupuesto? → No encontrado en los documentos; se deja vacío (el acta 06 es del 2026-09-10 y no fija el siguiente)
- ¿Dónde están las fichas PMO? → estado-pmo/records (PRY-310.json)
- ¿Umbrales? → Los de config.example.json: desviación 10 %, comprometido 95 %, proyección vencida 45 días

## Fuentes

- `2026-01/10-contabilidad/libro-mayor.xlsx`
- `2026-02/10-contabilidad/libro-mayor.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.xlsx`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`
- `presupuesto-2026/30-proyecciones/correo-administracion.md`

La corrida quedó registrada como `2026-10-06-budget-scan-1`. El texto de arriba está guardado en `corridas/salida-budget-scan.md`.