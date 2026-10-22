# /criterio-finance:audit-pack 

Seis requerimientos en el índice: tres respondidos con soporte, uno vencido (R-05) y dos sin responder que vencen el 2026-10-09 (R-04 y R-09). R-09 venía en la carta del auditor, no en la tabla, y ya estaba registrado en la ficha con su cita.

# Paquete del auditor · Minera Cóndor · periodo 2026-09

**Entidad:** Minera Cóndor (0990054321001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `audit-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 6 |

## El resultado

| Requerimiento | Solicitud | Responsable | Vence | Estado | Respuesta |
|---|---|---|---|---|---|
| R-01 | Conciliaciones bancarias de septiembre | Andrés Paz | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-01-respuesta.md` |
| R-02 | Auxiliar de cartera con antigüedad | Marta Ríos | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-02-respuesta.md` |
| R-03 | Detalle de facturas emitidas | Lucía Mora | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-03-respuesta.md` |
| R-04 | Actas del comité de presupuesto | Sofía León | 2026-10-09 | sin responder | — |
| R-05 | Contratos de los proveedores principales | Jorge Vela | 2026-10-02 | vencido | — |
| R-09 | Detalle de las partidas conciliatorias de más de 90 días | Andrés Paz | 2026-10-09 | sin responder | — |

El índice no mueve ni copia archivos: cita dónde está cada uno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la carpeta raíz de documentos? → finanzas/0990054321001-minera-condor (la del argumento)
- ¿Entidad, país y moneda? → Minera Cóndor, RUC 0990054321001, Ecuador, USD (por el RUC de las facturas y la carpeta)
- ¿Qué marco contable aplica? → No indicado en los documentos; queda registrado así
- ¿Qué periodo se está cerrando? → 2026-09 (el último con 10-contabilidad/)
- ¿Qué cuentas cruzan las facturas? → Ventas 41; compras 14/51/52/61; IVA 2408 (los del balance de comprobación)
- ¿Qué cuentas se concilian y qué bancos se esperan? → 1305 y 2205 (tienen auxiliar); andino-4101 y pacifico-4102 (carpetas de 20-bancos)
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin constancia de aprobación, queda como no aprobado
- ¿Quién aprueba el cierre? → Sofía León (responsable de C-09 en el checklist)
- ¿Festivos? → Ninguno a mano; la lista queda vacía

## Fuentes

- `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv`

La corrida quedó registrada como `2026-10-06-audit-pack-1`. El motor la cuenta con 7 hallazgos, aunque el reporte de arriba solo lista una señal. Esa diferencia no la investigué.