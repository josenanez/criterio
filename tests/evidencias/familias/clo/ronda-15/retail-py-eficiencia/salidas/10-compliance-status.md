# /criterio-compliance:compliance-status 

Los términos (versión 1.5) ya estaban vigentes y aceptados, así que no registré ninguna aceptación nueva. Corrí el reporte de 2026-10 con `--today 2026-10-06` y dejé la corrida registrada.

Hay tres señales abiertas. De las 10 obligaciones de la matriz, solo 2 tienen evidencia.

# Estado del cumplimiento · Distribuidora del Ybytyruzú Sintética · periodo 2026-10

**Entidad:** Distribuidora del Ybytyruzú Sintética (88612904-4) · **Fecha de corte:** 2026-10-31 · **Procesado:** 2026-10-06 · **Agente:** Constanza, versión 1.6.3 · **Comando:** `compliance-status`

## Lo que hay que atender

| # | Señal | Qué | Responsable | Cita |
|---|---|---|---|---|
| 1 | Una obligación figura cumplida y ninguna evidencia la sostiene (`compliance_done_without_evidence`) | OB-10 · Declaración mensual de origen de fondos: figura cumplida y no hay evidencia que empiece por OB-10 | Osvaldo Ramírez | `00-referencia/matriz-obligaciones.csv` fila 10 |
| 2 | La evidencia más reciente de una obligación periódica es de antes de su ventana (`compliance_evidence_stale`) | OB-05 · Capacitación mensual del personal nuevo: la última evidencia es de 2026-08; el ciclo anterior no tiene | Celeste Villalba | `00-referencia/matriz-obligaciones.csv` fila 6 |
| 3 | Una obligación de la matriz no cita la norma, el contrato o la política de la que sale (`obligation_without_source`) | OB-13 · Reporte de regalos e invitaciones: no cita la norma, el contrato o la política de la que sale | — | `00-referencia/matriz-obligaciones.csv` fila 11 |

## El resultado

**Estado declarado:** nadie lo ha declarado · **Avance con evidencia:** 23,81 % (ponderado por criticidad)

| Id | Obligación | Fuente | Responsable | Vence | Estado | Evidencia |
|---|---|---|---|---|---|---|
| OB-06 | Reporte de operaciones del contratista de tecnología | Contrato CTR-4501 OBL-3 | Osvaldo Ramírez | 2026-11-05 | en plazo | — |
| OB-01 | Reporte mensual de operaciones al supervisor | N-2026-01 · Resolución sintética 001 de 2026 | Osvaldo Ramírez | 2026-11-10 | en plazo | — |
| OB-03 | Informe trimestral del comité de riesgos | Política P-01 | Fátima Ayala | 2026-11-20 | cumplida con evidencia | `cumplimiento-2026-09/10-evidencias/OB-03_informe-trimestral-del-comite-de-riesgos-2026-09.md` |
| OB-10 | Declaración mensual de origen de fondos | Política P-04 | Osvaldo Ramírez | 2026-11-25 | cumplida sin evidencia | — |
| OB-02 | Conciliación de la base de clientes vinculados | Política P-02 | Osvaldo Ramírez | 2026-11-06 | en plazo | — |
| OB-08 | Actualización de datos de proveedores críticos | Política P-04 | Celeste Villalba | 2026-11-08 | en plazo | — |
| OB-04 | Certificación anual de la junta | Estatutos, artículo 40 | Fátima Ayala | 2026-12-31 | en plazo | — |
| OB-07 | Revisión semestral de la matriz de riesgos | Política P-01 | Fátima Ayala | 2026-11-30 | cumplida con evidencia | `cumplimiento-2026-07/10-evidencias/OB-07_revision-semestral-de-la-matriz-de-riesg-2026-07.md` |
| OB-13 | Reporte de regalos e invitaciones | — | Celeste Villalba | 2026-11-10 | en plazo | — |
| OB-05 | Capacitación mensual del personal nuevo | Política P-03 | Celeste Villalba | 2026-11-20 | en plazo | — |

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-obligaciones.csv`

Guardé lo mostrado en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-compliance-status.md`. El motor registró la corrida como `2026-10-06-compliance-status-1`.