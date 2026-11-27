# /criterio-remediation:remediation-wake 

Hoy solo tocaba la revisión semanal (`remediation-scan`) de Seguradora Atlântica Sintética. No había peticiones de Rostrum y los términos ya estaban vigentes. No llegaron documentos nuevos, cambiados ni borrados desde la corrida anterior, y el motor no encontró documentos fuera de la ficha del periodo, así que no hubo nada que agregarle. Este es el reporte del motor:

# Qué cambió en el seguimiento · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.2.2 · **Comando:** `remediation-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan se dio por cerrado sin la evidencia de su implementación o sin la validación de auditoría (norma 15.2) (`closure_without_evidence`) | H-21 · Conciliaciones bancarias sin firma del revisor: cerrado el 2025-10-20 sin la evidencia de su implementación (norma 15.2) | — | Tesorería | — | `30-seguimiento/registro_hallazgos.xlsx` fila 6 |
| 2 | La gerencia aceptó un riesgo por encima del apetito y no hay constancia de que se discutiera con la alta dirección o, sin resolverse, de que llegara al consejo (norma 11.5) (`risk_accepted_not_escalated`) | RA-01 · Sistema central sin soporte del fabricante: aceptado por encima del apetito el 2026-06-01; no hay constancia de que se discutiera con la alta dirección (norma 11.5) | — | — | — | `30-seguimiento/riesgos_aceptados.xlsx` fila 2 |
| 3 | Un plan de acción pasó su fecha sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) (`action_plan_overdue`) | H-03 · Cuentas privilegiadas sin revisión trimestral: venció el 2026-09-30 sin la evidencia de su implementación ni la explicación documentada del atraso (norma 15.2) | — | Gerencia de tecnología | 55 | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |
| 4 | Un hallazgo comunicado no tiene plan de acción, responsable o fecha (norma 15.1) (`action_plan_missing`) | H-02 · Avalúos con más de tres años sin actualizar: comunicado el 2026-04-30 y sin responsable (norma 15.1) | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 4 |
| 5 | Un hallazgo del revisor fiscal, del auditor externo o del supervisor no está en el registro con su plan (`external_finding_untracked`) | RF-02 · Caja menor sin arqueo en el trimestre: hallazgo de Revisor fiscal que no está en el registro con su plan | — | — | — | `30-seguimiento/informe_revisor_fiscal_2026.pdf` |
| 6 | La misma condición, en el mismo proceso, vuelve a aparecer después de que su hallazgo se cerró (`finding_repeated`) | H-01: la misma condición que H-20 en Crédito, que se cerró el 2025-09-15 | — | — | — | `30-seguimiento/registro_hallazgos.xlsx` fila 3 · `30-seguimiento/registro_hallazgos.xlsx` fila 2 |
| 7 | La fecha de un plan se corrió más veces de las que permite la metodología (`due_date_extended_repeatedly`) | H-03 · Cuentas privilegiadas sin revisión trimestral: su fecha se corrió 3 veces y la metodología permite 2 | — | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Hallazgos en el registro:** 6 · **Abiertos:** 4 · **Evidencias en la ficha:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/informe_revisor_fiscal_2026.pdf`
- `30-seguimiento/registro_hallazgos.xlsx`
- `30-seguimiento/riesgos_aceptados.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

Quedan registradas dos corridas: `2026-11-24-remediation-scan-2` y `2026-11-24-remediation-wake-1`. Cerrar, validar o escalar cualquiera de estas siete señales le toca a quien es responsable de auditoría.