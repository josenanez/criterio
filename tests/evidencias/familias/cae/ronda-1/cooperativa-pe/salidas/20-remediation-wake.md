# /criterio-remediation:remediation-wake 

Hoy solo tocaba la revisión semanal del seguimiento (`remediation-scan`). No había peticiones en Rostrum, los términos están vigentes y no llegó ningún documento nuevo ni cambiado. La ficha ya tenía las dos evidencias y los dos hallazgos del revisor fiscal, así que no la cambié.

Hay una inconsistencia que no corregí: el inventario dice que el informe del revisor fiscal debería ir en `20-trabajos/` y los riesgos aceptados en `10-plan/`, pero la estructura recomendada pone los dos en `30-seguimiento/`. No moví nada.

# Qué cambió en el seguimiento · Cooperativa de Ahorro Altiplano Sintética · periodo 2026-11

**Entidad:** Cooperativa de Ahorro Altiplano Sintética (20601777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `remediation-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) | — | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 2 | Un hallazgo comunicado no tiene plan de acción, responsable o fecha (norma 15.1) (`action_plan_missing`) | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable (norma 15.1) | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |
| 3 | Un hallazgo del revisor fiscal, del auditor externo o del supervisor no está en el registro con su plan (`external_finding_untracked`) | RF-02 · Caja menor sin arqueo en el trimestre: hallazgo de Revisor fiscal que no está en el registro con su plan | — | — | — | `30-seguimiento/informe_revisor_fiscal_2026.pdf` |
| 4 | La misma condición, en el mismo proceso, vuelve a aparecer después de que su hallazgo se cerró (`finding_repeated`) | H-01: la misma condición que H-20 en Crédito, que se cerró el 2025-09-15 | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 3 · `30-seguimiento/registro_hallazgos.xlsx` fila 2 |

## El resultado

**Hallazgos en el registro:** 6 · **Abiertos:** 4 · **Evidencias en la ficha:** 2.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/informe_revisor_fiscal_2026.pdf`
- `30-seguimiento/registro_hallazgos.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

Quedaron registradas las dos corridas, `remediation-scan` y `remediation-wake`, con el caso 2026-11. Lo que se concluya de estas señales le corresponde al responsable de auditoría.