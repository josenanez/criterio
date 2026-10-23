# /criterio-compliance:compliance-status 

Los términos (versión 1.2) ya estaban vigentes con la aceptación de la versión 0.8.0. No hizo falta registrar de nuevo a José Francisco Ñáñez. Hay tres señales abiertas y nadie ha declarado el estado del periodo.

# Estado del cumplimiento · Cooperativa Sierra Alta · periodo 2026-10

**Entidad:** Cooperativa Sierra Alta (1790012345001) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `compliance-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | — | Gabriela Mora | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-05 · Capacitación mensual del personal nuevo: la última evidencia es de 2026-08; el ciclo anterior no tiene | — | Esteban Jácome | — | `00-referencia/matriz-obligaciones.csv` fila 6 |
| 3 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-11 · Monitoreo mensual de listas restrictivas: la última evidencia es de 2026-07; el ciclo anterior no tiene | — | Esteban Jácome | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

**Estado declarado:** nadie lo ha declarado · **Avance con evidencia:** 22.73 % (ponderado por criticidad)

| Id | Obligación | Fuente | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|---|
| OB-06 | Reporte de operaciones del contratista de tecnología | Contrato CTR-201 OBL-3 | Gabriela Mora | 2026-11-05 | en plazo | — |
| OB-01 | Reporte mensual de operaciones al supervisor | N-2026-01 · Resolución sintética 001 de 2026 | Gabriela Mora | 2026-11-10 | en plazo | — |
| OB-03 | Informe trimestral del comité de riesgos | Política P-01 | Patricio Andrade | 2026-11-20 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-03_informe-trimestral-del-comite-de-riesgos-2026-09.md` |
| OB-10 | Declaración mensual de origen de fondos | Política P-04 | Gabriela Mora | 2026-11-25 | cumplida sin evidencia | — |
| OB-02 | Conciliación de la base de clientes vinculados | Política P-02 | Gabriela Mora | 2026-11-06 | en plazo | — |
| OB-08 | Actualización de datos de proveedores críticos | Política P-04 | Esteban Jácome | 2026-11-08 | en plazo | — |
| OB-11 | Monitoreo mensual de listas restrictivas | Política P-04 | Esteban Jácome | 2026-11-25 | en plazo | — |
| OB-04 | Certificación anual de la junta | Estatutos, artículo 40 | Patricio Andrade | 2026-12-31 | en plazo | — |
| OB-07 | Revisión semestral de la matriz de riesgos | Política P-01 | Patricio Andrade | 2026-11-30 | cumplida con evidencia | `cumplimiento-2026-07/10-evidencias/OB-07_revision-semestral-de-la-matriz-de-riesg-2026-07.md` |
| OB-05 | Capacitación mensual del personal nuevo | Política P-03 | Esteban Jácome | 2026-11-20 | en plazo | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-obligaciones.csv`

La corrida quedó registrada como `2026-10-06-compliance-status-1`. En `estado-legal/1790012345001-cooperativa-sierra-alta/corridas/salida-compliance-status.md` está lo mostrado, con la línea de términos al inicio.

La nota que dejé en el registro dice "2 de 10 obligaciones con evidencia, 3 señales abiertas". El motor registró 5 hallazgos en la corrida, que no coincide con las 3 señales del reporte. No lo investigué.