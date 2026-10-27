# /criterio-legal:contract-scan 

Ya terminé el escaneo de contratos y la corrida quedó registrada. Esto es lo que mostré:

Se procesaron los 6 contratos (CTR-701 a CTR-706). Sus fichas pasaron la validación sin observaciones y el motor marcó 5 señales.

# Qué cambió en los contratos · Banco Ribera · al 2026-10-06

**Fecha de corte:** 2026-10-06 · **Agente:** Fidel, versión 0.10.0 · **Comando:** `contract-scan`

## Lo que hay que atender

| # | Señal | Qué | Cita |
|---|---|---|---|
| 1 | `signed_without_authority` | CTR-701: Claudia Salinas firmó por 480,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto | `contratos/CTR-701-…/10-contrato/contrato.md` · `00-referencia/matriz-atribuciones.csv` fila 2 |
| 2 | `contract_obligation_overdue` | CTR-704 · OBL-1 · Informe mensual de ejecución (el de agosto): venció el 2026-09-05, hace 31 días, y no hay evidencia en `40-ejecucion/`. Responsable: Licencias Andinas S.A.C. | `contratos/CTR-704-…/10-contrato/contrato.md, cláusula 5` |
| 3 | `notice_deadline_near` | CTR-704: el preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie decidió | `contratos/CTR-704-…/10-contrato/contrato.md` |
| 4 | `guarantee_missing` | CTR-703: el contrato exige la garantía de calidad y no hay póliza aportada en `20-garantias/` | `contratos/CTR-703-…/10-contrato/contrato.md, cláusula 9` |
| 5 | `register_differs_from_contract` | CTR-702: el registro dice 360,000.00 y el documento 300,000.00 | `10-registro/registro-contratos.csv` fila 3 · `contratos/CTR-702-…/10-contrato/contrato.md` |

## El resultado

Esta sección salió vacía en el reporte del motor.

## Lo que no se pudo procesar

Todo lo que llegó se procesó.

## Las preguntas que hizo

Ninguna en esta corrida.

## Fuentes

- `00-referencia/matriz-atribuciones.csv`
- `10-registro/registro-contratos.csv`
- `contratos/CTR-701-…/10-contrato/contrato.md`
- `contratos/CTR-702-…/10-contrato/contrato.md`
- `contratos/CTR-703-…/10-contrato/contrato.md, cláusula 9`
- `contratos/CTR-704-…/10-contrato/contrato.md` (también la cláusula 5)

Todo está en `estado-legal/20710000019-banco-ribera/`:
- **Reporte:** `contratos/reporte-contract-scan.md`.
- **Salida de la corrida:** `corridas/salida-contract-scan.md`.
- **Corrida registrada:** `2026-10-06-contract-scan-1`, con 5 hallazgos.

Los términos ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-06, así que no hizo falta registrar la aceptación otra vez. No hubo preguntas que responder.

En CTR-702 (que tiene otrosí), la fecha de OBL-2 (informe final y acta de liquidación) es 2027-12-31. Es la terminación nueva del otrosí, porque el contrato dice "a la terminación".