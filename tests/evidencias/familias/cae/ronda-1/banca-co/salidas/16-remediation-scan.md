# /criterio-remediation:remediation-scan 

No llegó ningún documento nuevo ni cambió ninguno desde la corrida anterior. La ficha del periodo ya tenía la evidencia de H-20 y los dos hallazgos del revisor fiscal, y el motor no encontró documentos que faltaran en ella. Según el inventario, hay dos archivos de `30-seguimiento/` en la carpeta equivocada: `informe_revisor_fiscal_2026.pdf` va en `20-trabajos/` y `riesgos_aceptados.xlsx` va en `10-plan/`. Los dos se procesaron igual, desde donde están.

# Qué cambió en el seguimiento · Banco Andino Sintético · periodo 2026-11

**Entidad:** Banco Andino Sintético (901777321) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `remediation-scan`

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

Lo que se mostró quedó guardado en `<espacio>/estado-auditoria/901777321-banco-andino-sintetico/corridas/salida-remediation-scan.md`, y la corrida quedó registrada como `2026-11-24-remediation-scan-1`.