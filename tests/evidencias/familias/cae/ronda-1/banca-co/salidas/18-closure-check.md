# /criterio-remediation:closure-check 

Los términos de la versión 1.6 ya estaban vigentes (aceptación 0.1.0), así que no hizo falta registrar de nuevo la aceptación de José Francisco Ñáñez. El reporte de closure-check de 2026-11 queda abajo tal cual, con dos señales por atender.

# Cada cierre contra su evidencia · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `closure-check`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan se dio por cerrado sin la evidencia de su implementación o sin la validación de auditoría (norma 15.2) (`closure_without_evidence`) | H-21 · Conciliaciones bancarias sin firma del revisor: cerrado el 2025-10-20 sin la evidencia de su implementación (norma 15.2) | — | Tesorería | — | `30-seguimiento/registro_hallazgos.xlsx` fila 6 |
| 2 | La misma condición, en el mismo proceso, vuelve a aparecer después de que su hallazgo se cerró (`finding_repeated`) | H-01: la misma condición que H-20 en Crédito, que se cerró el 2025-09-15 | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 3 · `30-seguimiento/registro_hallazgos.xlsx` fila 2 |

## El resultado

| Hallazgo | Proceso | Estado | Evidencias |
|---|---|---|---|
| H-20 | Crédito | Cerrado | 1 |
| H-21 | Tesorería | Cerrado | 0 |

| Vuelve | Antes | Proceso |
|---|---|---|
| H-01 | H-20 | Crédito |

El cierre lo valida el auditor: aquí se dice cuál no tiene con qué sostenerse.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/registro_hallazgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

La corrida quedó registrada como `2026-11-24-closure-check-1`. La salida está en `estado-auditoria/901777321-banco-andino-sintetico/corridas/salida-closure-check.md`.