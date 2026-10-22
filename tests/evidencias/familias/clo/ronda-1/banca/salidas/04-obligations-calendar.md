# /criterio-legal:obligations-calendar 

Los términos (v1.2) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva. El comando `terminos` no pidió nada más. Dos puntos de CTR-104 piden atención antes de que corra el plazo.

# Vencimientos, preavisos y obligaciones · Banco Andino · al 2026-10-06

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-06 · **Procesado:** 2026-10-06 · **Agente:** Fidel, versión 0.7.0 · **Comando:** `obligations-calendar`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación del contrato pasó su fecha sin evidencia (`contract_obligation_overdue`) | CTR-104 · OBL-1 · Informe mensual de ejecución: venció el 2026-09-05 y no hay evidencia en 40-ejecucion/ | — | Licencias del Norte S.A.S. | 31 | `contratos/CTR-104-licencias-del-norte-s-a-s/10-contrato/contrato.md, cláusula 5` |
| 2 | La fecha límite del preaviso de no renovación de un contrato con renovación automática cae dentro de los días configurados (`notice_deadline_near`) | CTR-104: el preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie decidió | — | — | 26 | `contratos/CTR-104-licencias-del-norte-s-a-s/10-contrato/contrato.md` |

## El resultado

| Fecha | Contrato | Qué | Días | Evidencia |
|---|---|---|---|---|
| 2026-09-30 | CTR-101 | obligación OBL-3 · Reporte de operaciones al oficial de cumplimiento | -6 | `contratos/CTR-101-soluciones-andinas-s-a-s/40-ejecucion/OBL-3_reporte-de-operaciones-al-oficial-de-cum.md` |
| 2026-11-01 | CTR-104 | límite del preaviso | 26 | — |
| 2026-11-20 | CTR-105 | terminación | 45 | — |
| 2026-11-20 | CTR-105 | obligación OBL-2 · Informe final y acta de liquidación (a la terminación) | 45 | — |
| 2026-12-31 | CTR-103 | terminación | 86 | — |
| 2026-12-31 | CTR-103 | obligación OBL-2 · Informe final y acta de liquidación (a la terminación) | 86 | — |
| 2026-12-31 | CTR-104 | terminación | 86 | — |
| 2026-12-31 | CTR-104 | obligación OBL-2 · Informe final y acta de liquidación (a la terminación) | 86 | — |

Entre 30 días atrás y 90 adelante. La decisión de renovar o terminar es de una persona.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `contratos/CTR-104-licencias-del-norte-s-a-s/10-contrato/contrato.md`
- `contratos/CTR-104-licencias-del-norte-s-a-s/10-contrato/contrato.md, cláusula 5`

La corrida quedó registrada como `2026-10-06-obligations-calendar-1`, con 5 hallazgos. El texto mostrado está guardado en `estado-legal/900123456-banco-andino/corridas/salida-obligations-calendar.md`.