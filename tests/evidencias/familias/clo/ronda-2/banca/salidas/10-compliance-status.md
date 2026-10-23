# /criterio-compliance:compliance-status 

Los términos de la versión 1.2 ya estaban vigentes, así que no hizo falta registrar una aceptación nueva.

Hay cuatro señales abiertas, y nadie ha declarado el estado del cumplimiento del periodo.

# Estado del cumplimiento · Banco Andino · periodo 2026-10

**Entidad:** Banco Andino (900123456) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `compliance-status`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Una obligación de un contrato no está en la matriz (`contract_obligation_not_in_matrix`) | CTR-101 · OBL-3 · Reporte de operaciones del periodo al oficial de cumplimiento | — | `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md, cláusula 7` |
| 2 | La evidencia más reciente es de antes de su ventana (`compliance_evidence_stale`) | OB-05 · Capacitación mensual del personal nuevo: la última evidencia es de 2026-08; el ciclo anterior no tiene | Diana Cruz | `00-referencia/matriz-obligaciones.csv` fila 6 |
| 3 | La evidencia más reciente es de antes de su ventana (`compliance_evidence_stale`) | OB-09 · Reporte mensual de quejas: la última evidencia es de 2026-08; el ciclo anterior no tiene | Diana Cruz | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 4 | Una obligación de la matriz no tiene responsable (`obligation_without_owner`) | OB-12 · Registro de conflictos de interés | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

**Estado declarado:** nadie lo ha declarado · **Avance con evidencia:** 22,73 % (ponderado por criticidad)

| Id | Obligación | Fuente | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|---|
| OB-06 | Reporte de operaciones del contratista de tecnología | Política P-01 | Andrés Vela | 2026-11-05 | en plazo | — |
| OB-09 | Reporte mensual de quejas | Política P-02 | Diana Cruz | 2026-11-05 | en plazo | — |
| OB-01 | Reporte mensual de operaciones al supervisor | N-2026-01 · Resolución sintética 001 de 2026 | Andrés Vela | 2026-11-10 | en plazo | — |
| OB-03 | Informe trimestral del comité de riesgos | Política P-01 | Marta Ríos | 2026-11-20 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-03_informe-trimestral-del-comite-de-riesgos-2026-09.md` |
| OB-02 | Conciliación de la base de clientes vinculados | Política P-02 | Andrés Vela | 2026-11-06 | en plazo | — |
| OB-08 | Actualización de datos de proveedores críticos | Política P-04 | Diana Cruz | 2026-11-08 | en plazo | — |
| OB-04 | Certificación anual de la junta | Estatutos, artículo 40 | Marta Ríos | 2026-12-31 | en plazo | — |
| OB-07 | Revisión semestral de la matriz de riesgos | Política P-01 | Marta Ríos | 2026-11-30 | cumplida con evidencia | `cumplimiento-2026-07/10-evidencias/OB-07_revision-semestral-de-la-matriz-de-riesg-2026-07.md` |
| OB-12 | Registro de conflictos de interés | Política P-03 | — | 2026-11-10 | en plazo | — |
| OB-05 | Capacitación mensual del personal nuevo | Política P-03 | Diana Cruz | 2026-11-20 | en plazo | — |

## Lo que no se pudo procesar
Todo lo que llegó se procesó.

## Las preguntas que hizo
Ninguna en esta corrida.

## Fuentes
- `00-referencia/matriz-obligaciones.csv`
- `contratos/CTR-101-soluciones-andinas-s-a-s/10-contrato/contrato.md, cláusula 7`

La corrida quedó registrada como `2026-10-06-compliance-status-1`, con la nota "2 obligaciones con evidencia sobre 10, 4 señales abiertas". La salida completa está en `estado-legal/900123456-banco-andino/corridas/salida-compliance-status.md`.

El motor reportó 5 hallazgos al registrar la corrida, pero el reporte muestra 4 señales. No averigüé de dónde sale la diferencia.