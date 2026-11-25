# /criterio-remediation:remediation-scan 

Desde la corrida anterior no llegó ni cambió ningún documento. La ficha ya tenía la evidencia de H-20, la explicación del atraso de H-03 y el hallazgo RF-01 del revisor fiscal, cada uno con su cita, y no hubo que agregarle nada. El inventario marca `informe_revisor_fiscal_2026.pdf` y `riesgos_aceptados.xlsx` como fuera de lugar. Según la estructura recomendada, los dos van en `30-seguimiento/`, así que no los moví. Lo que sigue es del responsable de auditoría.

# Qué cambió en el seguimiento · Seguradora Atlântica Sintética · periodo 2026-11

**Entidad:** Seguradora Atlântica Sintética (31452078000190) · **Fecha de corte:** 2026-11-24 · **Procesado:** 2026-11-24 · **Agente:** Remedios, versión 0.1.0 · **Comando:** `remediation-scan`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Un plan se dio por cerrado sin la evidencia de su implementación o sin la validación de auditoría (norma 15.2) (`closure_without_evidence`) | H-21 · Conciliaciones bancarias sin firma del revisor: cerrado el 2025-10-20 sin la evidencia de su implementación (norma 15.2) | — | Tesorería | — | `30-seguimiento/registro_hallazgos.xlsx` fila 6 |
| 2 | La gerencia aceptó un riesgo por encima del apetito y no hay constancia de que se discutiera con la alta dirección o, sin resolverse, de que llegara al consejo (norma 11.5) (`risk_accepted_not_escalated`) | RA-01 · Sistema central sin soporte del fabricante: aceptado por encima del apetito el 2026-06-01; no hay constancia de que se discutiera con la alta dirección (norma 11.5) | — | — | — | `30-seguimiento/riesgos_aceptados.xlsx` fila 2 |
| 3 | La fecha de un plan se corrió más veces de las que permite la metodología (`due_date_extended_repeatedly`) | H-03 · Cuentas privilegiadas sin revisión trimestral: su fecha se corrió 3 veces y la metodología permite 2 | — | Gerencia de tecnología | — | `30-seguimiento/registro_hallazgos.xlsx` fila 5 |

## El resultado

**Hallazgos en el registro:** 6 · **Abiertos:** 4 · **Evidencias en la ficha:** 1.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `30-seguimiento/registro_hallazgos.xlsx`
- `30-seguimiento/riesgos_aceptados.xlsx`
- Fuentes técnicas: F-01 (families/criterio-cae/FUENTES.es.md)

---

La aceptación de los términos ya estaba registrada a nombre de José Francisco Ñáñez con fecha 2026-11-24. La corrida quedó registrada como `2026-11-24-remediation-scan-1`.