# /criterio-legal:contract-scan 

Corrí `contract-scan` sobre Almacenes del Plata, fecha 2026-10-06. Los seis contratos estaban en las fichas que dejó `legal-setup` y coinciden con sus documentos. El motor no devolvió `record_issues`. Todo lo que llegó se procesó.

Los términos ya estaban vigentes (versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-06), así que no hubo que registrarlos de nuevo. No hubo preguntas para la persona.

**Lo que hay que atender (5 señales):**

| # | Contrato | Señal | Monto | Cita |
|---|---|---|---|---|
| 1 | CTR-2602 | Martín Acosta firmó el otrosí OT-1 sin facultad para ese monto según la matriz de atribuciones (`signed_without_authority`). El otrosí lleva el contrato a 77.000.000,00. | 49.000.000,00 | `…/CTR-2602-…/10-contrato/otrosi-1.md` |
| 2 | CTR-2603 | Vence el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar (`contract_expiring`). | 42.000.000,00 | `…/CTR-2603-…/10-contrato/contrato.md` |
| 3 | CTR-2606 | Hay 1 pago posterior a la terminación del 2026-07-31 (`payment_after_termination`). | 1.750.000,00 | `10-registro/pagos-2026-09-30.csv`, fila 20 |
| 4 | CTR-2601 | La póliza vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 (`guarantee_expires_early`), 61 días antes. | — | `…/CTR-2601-…/20-garantias/poliza-cumplimiento.md` |
| 5 | CTR-2609 | Está en el registro y no hay documento en `contratos/CTR-2609…/10-contrato/` (`register_mismatch`). | — | `10-registro/registro-contratos.csv`, fila 8 |

El reporte completo está en `estado-legal/30714520780-almacenes-del-plata/contratos/reporte-contract-scan.md`. Lo que le mostré a la persona quedó en `corridas/salida-contract-scan.md`. La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 5 hallazgos.

No interpreté ninguna cláusula ni opiné sobre validez o renovación. Las cinco señales quedan para que las revise una persona.