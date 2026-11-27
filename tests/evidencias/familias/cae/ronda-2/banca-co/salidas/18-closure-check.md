# /criterio-remediation:closure-check 

Dos señales abiertas en este cierre: un plan cerrado sin la evidencia de su implementación y una condición que vuelve en el mismo proceso. Lo que se concluye es del responsable de auditoría.

# Cada cierre contra su evidencia · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `closure-check`

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

La corrida quedó registrada con el id `2026-11-24-closure-check-1`. La salida completa está en `corridas/salida-closure-check.md`, dentro de la carpeta de estado. Los términos ya estaban vigentes (versión 1.6), así que no hubo nada que registrar.