# /criterio-finance:audit-pack 

De los cinco requerimientos del índice, dos están respondidos con soporte; R-05 está vencido y R-03 se respondió sin soporte. No había requerimientos fuera de la tabla, así que no hubo nada que convertir.

# Paquete del auditor · Cooperativa Sierra Alta · periodo 2026-09

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-09-30 · **Procesado:** 2026-10-06 · **Agente:** Clara, versión 0.8.0 · **Aprueba:** Sofía León · **Comando:** `audit-pack`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-05 · Contratos de los proveedores principales: vencido, venció el 2026-10-02 | — | Jorge Vela | 4 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 6 |
| 2 | Un requerimiento del auditor no tiene respuesta con soporte (`audit_request_unanswered`) | R-03 · Detalle de facturas emitidas: respondido sin soporte, venció el 2026-10-03 | — | Lucía Mora | 3 | `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv` fila 4 |

## El resultado

| Requerimiento | Solicitud | Responsable | Vence | Estado | Respuesta |
|---|---|---|---|---|---|
| R-01 | Conciliaciones bancarias de septiembre | Andrés Paz | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-01-respuesta.md` |
| R-02 | Auxiliar de cartera con antigüedad | Marta Ríos | 2026-10-03 | respondido con soporte | `2026-09/50-auditoria/respuestas/R-02-respuesta.md` |
| R-03 | Detalle de facturas emitidas | Lucía Mora | 2026-10-03 | respondido sin soporte | — |
| R-04 | Actas del comité de presupuesto | Sofía León | 2026-10-09 | sin responder | — |
| R-05 | Contratos de los proveedores principales | Jorge Vela | 2026-10-02 | vencido | — |

El índice no mueve ni copia archivos: cita dónde está cada uno.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

- ¿Cuál es la entidad, su RUC, país y moneda? → Cooperativa Sierra Alta, RUC 1790012345001, Ecuador, USD (por el nombre de la carpeta y las facturas del SRI)
- ¿Qué marco contable aplica? → NIIF para PYMES, por confirmar: ningún documento lo dice
- ¿Cuál es el periodo que se está cerrando? → 2026-09, el último con 10-contabilidad/
- ¿Qué cuentas cruzan las facturas? → Ventas 41, compras 5135/5145/5195, IVA 2408 (del balance de comprobación)
- ¿Qué cuentas se concilian contra auxiliar y qué bancos se esperan? → 1305 y 2205 (los auxiliares que hay); bancos andino-2301 y pacifico-2302
- ¿Qué checklist se usa? → El de la organización, 00-referencia/checklist-cierre.csv; sin aprobación registrada
- ¿Quién aprueba el cierre? → Sofía León, responsable de C-09 en el checklist
- ¿Hay festivos del calendario? → No encontrado: ningún documento los trae

## Fuentes

- `2026-09/50-auditoria/requerimientos/pbc-2026-09.csv`

La corrida quedó registrada como `2026-10-06-audit-pack-1`.