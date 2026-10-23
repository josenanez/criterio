# /criterio-compliance:compliance-status 

Los términos (versión 1.2) están vigentes. Hay tres señales abiertas, y solo 2 de las 10 obligaciones tienen evidencia dentro de su ventana: OB-03 y OB-07.

# Estado del cumplimiento · Almacenes Caribe · periodo 2026-10

**Entidad:** Almacenes Caribe (900765432) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 0.8.0 · **Comando:** `compliance-status`

## Lo que hay que atender

| # | Señal | Qué | Monto | Responsable | Días | Cita |
|---|---|---|---|---|---|---|
| 1 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-05 · Capacitación mensual del personal nuevo: la última evidencia es de 2026-08; el ciclo anterior no tiene | — | Felipe Arango | — | `00-referencia/matriz-obligaciones.csv` fila 6 |
| 2 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-09 · Reporte mensual de quejas: la última evidencia es de 2026-08; el ciclo anterior no tiene | — | Felipe Arango | — | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 3 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | — | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

**Estado declarado:** nadie lo ha declarado · **Avance con evidencia:** 22,73 % (ponderado por criticidad)

| Id | Obligación | Fuente | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|---|
| OB-06 | Reporte de operaciones del contratista de tecnología | Contrato CTR-301 OBL-3 | Lucía Ortega | 2026-11-05 | en plazo | — |
| OB-09 | Reporte mensual de quejas | Política P-02 | Felipe Arango | 2026-11-05 | en plazo | — |
| OB-01 | Reporte mensual de operaciones al supervisor | N-2026-01 · Resolución sintética 001 de 2026 | Lucía Ortega | 2026-11-10 | en plazo | — |
| OB-03 | Informe trimestral del comité de riesgos | Política P-01 | Carlos Benítez | 2026-11-20 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-03_informe-trimestral-del-comite-de-riesgos-2026-09.md` |
| OB-02 | Conciliación de la base de clientes vinculados | Política P-02 | Lucía Ortega | 2026-11-06 | en plazo | — |
| OB-08 | Actualización de datos de proveedores críticos | Política P-04 | Felipe Arango | 2026-11-08 | en plazo | — |
| OB-04 | Certificación anual de la junta | Estatutos, artículo 40 | Carlos Benítez | 2026-12-31 | en plazo | — |
| OB-07 | Revisión semestral de la matriz de riesgos | Política P-01 | Carlos Benítez | 2026-11-30 | cumplida con evidencia | `cumplimiento-2026-07/10-evidencias/OB-07_revision-semestral-de-la-matriz-de-riesg-2026-07.md` |
| OB-13 | Reporte de regalos e invitaciones | — | Felipe Arango | 2026-11-10 | en plazo | — |
| OB-05 | Capacitación mensual del personal nuevo | Política P-03 | Felipe Arango | 2026-11-20 | en plazo | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-obligaciones.csv`

---
La corrida quedó registrada como `2026-10-06-compliance-status-1`. La salida completa está en `estado-legal/900765432-almacenes-caribe/corridas/salida-compliance-status.md`.

Hubo un desvío del comando: la aceptación de los términos no la registré. El comando no tiene paso de registro, y `terminos` ya devolvió el estado como vigente, con la versión 0.8.0 aceptada. Por eso no escribí el nombre de José Francisco Ñáñez en ningún comprobante.