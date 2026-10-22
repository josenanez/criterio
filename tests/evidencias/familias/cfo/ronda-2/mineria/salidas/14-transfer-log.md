# /criterio-budget:transfer-log 

Las tres actas de `40-actas/` ya estaban registradas en la ficha, así que no había nada nuevo que agregar. De los cuatro cambios entre la versión 1 y la 2 del presupuesto, dos tienen acta y dos no. Ninguna acta quedó sin cambio aplicado.

# Traslados y sus actas · Minera Cóndor · presupuesto 2026, corte 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09 · **Procesado:** 2026-10-06 · **Agente:** Tomás, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `transfer-log`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Operaciones · Transporte: cambió 9,600.00 entre la versión 1 y la 2 sin acta que lo apruebe | 9,600.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |
| 2 | Un traslado o una modificación no tiene el acta que lo aprueba (`transfer_without_approval`) | Tecnología · Licencias: cambió -9,600.00 entre la versión 1 y la 2 sin acta que lo apruebe | -9,600.00 | — | — | `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` · `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv` |

## El resultado

| Versión | Área | Línea | Valor | Tipo | Acta | Estado |
|---|---|---|---|---|---|---|
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Eventos | 6,000.00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Comercial | Publicidad | -6,000.00 | traslado | `presupuesto-2026/40-actas/acta-05-traslado.md` | con acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Operaciones | Transporte | 9,600.00 | traslado | — | sin acta |
| `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv` | Tecnología | Licencias | -9,600.00 | traslado | — | sin acta |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la versión aprobada y con qué acta? → La 1, acta 01 del 2026-01-20; la versión 2 no tiene acta que la apruebe como versión (el acta 05 solo aprueba el traslado Publicidad a Eventos)
- ¿Fechas del comité de presupuesto? → No hay fechas en los documentos; queda vacío

## Fuentes

- `presupuesto-2026/10-aprobado/presupuesto-2026-v1-2026-01-15.csv`
- `presupuesto-2026/10-aprobado/presupuesto-2026-v2-2026-06-30.csv`

La corrida quedó registrada como `2026-10-06-transfer-log-1`, con 4 hallazgos. Lo mostrado está guardado en `estado-finanzas/0990054321001-minera-condor/corridas/salida-transfer-log.md`. El reporte del motor está en `estado-finanzas/0990054321001-minera-condor/presupuesto/2026/reporte-transfer-log.md`; no lo abrí para confirmarlo.

Los términos ya estaban vigentes con la aceptación de José Francisco Ñáñez del 2026-10-06, así que no hizo falta registrarla de nuevo.