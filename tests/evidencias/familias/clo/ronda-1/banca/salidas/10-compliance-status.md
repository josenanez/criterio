# /criterio-compliance:compliance-status 

Los términos de la versión 0.7.0 ya estaban vigentes, así que no hubo que registrar una aceptación nueva. Nadie ha declarado el estado del periodo; lo que sigue es lo evidenciado.

# Estado del cumplimiento · Banco Andino · periodo 2026-10

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.7.0 · **Comando:** `compliance-status`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Obligación de un contrato que no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-101 · OBL-3 · Reporte de operaciones al oficial de cumplimiento | — | `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md, cláusula 7` |
| 2 | Evidencia más reciente anterior a la ventana (`compliance_evidence_stale`) | OB-05 · Capacitación mensual del personal nuevo: la última evidencia es de 2026-08; el ciclo anterior no tiene | Diana Cruz | `00-referencia/matriz-obligaciones.csv` fila 6 |
| 3 | Evidencia más reciente anterior a la ventana (`compliance_evidence_stale`) | OB-09 · Reporte mensual de quejas: la última evidencia es de 2026-08; el ciclo anterior no tiene | Diana Cruz | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Obligación sin responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

**Estado declarado:** nadie lo ha declarado · **Avance con evidencia:** 22,73 % (ponderado por criticidad)

| Id | Obligación | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|
| OB-06 | Reporte de operaciones del contratista de tecnología | Andrés Vela | 2026-11-05 | en plazo | — |
| OB-09 | Reporte mensual de quejas | Diana Cruz | 2026-11-05 | en plazo | — |
| OB-01 | Reporte mensual de operaciones al supervisor | Andrés Vela | 2026-11-10 | en plazo | — |
| OB-03 | Informe trimestral del comité de riesgos | Marta Ríos | 2026-11-20 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-03_…-2026-09.md` |
| OB-02 | Conciliación de la base de clientes vinculados | Andrés Vela | 2026-11-06 | en plazo | — |
| OB-08 | Actualización de datos de proveedores críticos | Diana Cruz | 2026-11-08 | en plazo | — |
| OB-04 | Certificación anual de la junta | Marta Ríos | 2026-12-31 | en plazo | — |
| OB-07 | Revisión semestral de la matriz de riesgos | Marta Ríos | 2026-11-30 | cumplida con evidencia | `cumplimiento-2026-07/10-evidencias/OB-07_…-2026-07.md` |
| OB-12 | Registro de conflictos de interés | — | 2026-11-10 | en plazo | — |
| OB-05 | Capacitación mensual del personal nuevo | Diana Cruz | 2026-11-20 | en plazo | — |

**Lo que no se pudo procesar:** nada, todo se procesó. **Preguntas que hizo:** ninguna.

**Fuentes:** `00-referencia/matriz-obligaciones.csv`; `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md`, cláusula 7.

La salida quedó en `estado-legal/900123456-banco-andino/corridas/salida-compliance-status.md` y la corrida se registró como `2026-10-06-compliance-status-2`.