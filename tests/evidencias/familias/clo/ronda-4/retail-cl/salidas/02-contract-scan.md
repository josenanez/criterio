# /criterio-legal:contract-scan 

Las seis fichas de contrato ya existían y coinciden con los documentos, así que no cambié ninguna. El inventario marcó todo como nuevo porque era la primera lectura. Los términos ya estaban vigentes, así que no los registré de nuevo. No hubo preguntas en esta corrida.

# Qué cambió en los contratos · Tiendas Pacífico · al 2026-10-06

El motor calculó 5 señales:

| # | Señal | Detalle | Monto |
|---|---|---|---|
| 1 | Firma sin facultad (`signed_without_authority`) | CTR-1002, OT-1: Tomás Contreras firmó el otrosí que lleva el contrato a 132.000.000,00 sin facultad para ese monto, según la matriz de atribuciones. | 84.000.000,00 |
| 2 | Contrato por vencer sin decisión (`contract_expiring`) | CTR-1003 vence el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar. | 72.000.000,00 |
| 3 | Pago posterior a la terminación (`payment_after_termination`) | CTR-1006: 1 pago después de la terminación del 2026-07-31 (`10-registro/pagos-2026-09-30.csv`, fila 20). | 3.000.000,00 |
| 4 | Póliza vence antes de lo exigido (`guarantee_expires_early`) | CTR-1001: la póliza vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 (61 días de diferencia). | — |
| 5 | Contrato en el registro sin documento (`register_mismatch`) | CTR-1009 está en el registro (fila 8) y no hay documento en `contratos/CTR-1009…/10-contrato/`. | — |

Todo lo que llegó se procesó.

Los archivos quedaron en estos lugares:
- **Reporte del motor:** `estado-legal/76083001-1-tiendas-pacifico/contratos/reporte-contract-scan.md`. No abrí ese archivo; lo que muestro arriba es la salida del comando `reporte`.
- **Salida de la corrida:** `estado-legal/76083001-1-tiendas-pacifico/corridas/salida-contract-scan.md`.
- **Corrida registrada:** `2026-10-06-contract-scan-1`, con 5 hallazgos.

Si la señal 1 es un problema real o si hay que renovar CTR-1003 lo decide una persona; no emito opinión jurídica.