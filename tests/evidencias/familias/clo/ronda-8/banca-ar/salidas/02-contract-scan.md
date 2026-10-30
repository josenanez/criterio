# /criterio-legal:contract-scan 

Corrí el escaneo de los 6 contratos. Salieron 5 señales y no hubo nada sin procesar ni `record_issues`.

Los términos de la versión 1.3 ya estaban vigentes y aceptados por José Francisco Ñáñez el 2026-10-06, así que no hizo falta registrarlos de nuevo. Las seis fichas ya existían, hechas por `legal-setup`. Las comparé con los documentos y coinciden, por eso no las rehíce.

Todo el inventario figura como nuevo, sin cambios ni borrados.

Esto es lo que trae el reporte del motor, que quedó en `contratos/reporte-contract-scan.md`:

| # | Señal | Detalle |
|---|---|---|
| 1 | Firma sin facultad | CTR-2501: Santiago Ferreyra firmó por 72.000.000,00 y la matriz de atribuciones no le da facultad para ese tipo y monto. |
| 2 | Obligación vencida sin evidencia | CTR-2504 · OBL-1, informe mensual: venció el 2026-09-05, hace 31 días, y no hay evidencia en `40-ejecucion/`. |
| 3 | Preaviso de no renovación cercano | CTR-2504: vence el 2026-11-01, en 26 días, y nadie decidió. |
| 4 | Garantía faltante | CTR-2503: el contrato exige la garantía de calidad y no hay póliza aportada en `20-garantias/`. |
| 5 | Registro distinto del contrato | CTR-2502: el registro dice 54.000.000,00 y el documento dice 45.000.000,00. |

La sección «El resultado» del reporte salió vacía. La dejé tal cual, sin agregarle nada.

Dejé la salida completa en `corridas/salida-contract-scan.md` y registré la corrida como `2026-10-06-contract-scan-1`.