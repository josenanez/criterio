# /criterio-legal:contract-scan 

Se procesaron los 6 contratos de la carpeta, todos nuevos en esta corrida. Las fichas ya existían y coinciden con sus documentos, y no quedaron `record_issues`. El motor marcó 5 señales.

Los términos 1.3 ya estaban aceptados por José Francisco Ñáñez el 2026-10-06, así que no hizo falta volver a registrarlos. Ninguna pregunta quedó abierta.

| # | Contrato | Señal | Detalle |
|---|---|---|---|
| 1 | CTR-4501 | Firma sin facultad | Celeste Villalba firmó por 2.640.000.000 y la matriz de atribuciones no le da facultad para ese tipo y monto (`matriz-atribuciones.csv`, fila 2). |
| 2 | CTR-4503 | Vence sin decisión | Vence el 2026-11-25, en 50 días, y no hay decisión de renovar o terminar. |
| 3 | CTR-4506 | Pago posterior a la terminación | Hay 1 pago de 82.500.000 después de la terminación del 2026-07-31 (`pagos-2026-09-30.csv`, fila 20). |
| 4 | CTR-4501 | Póliza que vence antes de lo exigido | La póliza vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31 (61 días de diferencia). |
| 5 | CTR-4509 | Registro sin documento | Está en el registro (`registro-contratos.csv`, fila 8) y no hay documento en `contratos/CTR-4509…/10-contrato/`. |

No califiqué la validez de ninguna firma ni recomendé renovar o terminar. Eso queda para la persona.

La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 5 hallazgos. La salida completa está en `salida-contract-scan.md`, dentro de la carpeta `corridas` del estado, y el reporte del motor en `contratos/reporte-contract-scan.md`.