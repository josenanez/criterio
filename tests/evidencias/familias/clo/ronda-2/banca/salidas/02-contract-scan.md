# /criterio-legal:contract-scan 

Las seis fichas ya existían de la configuración inicial. Las contrasté con los documentos y corregí una: la terminación original de CTR-102 estaba en 2026-06-30 y la cláusula 3 dice 2027-06-30.

Los términos ya estaban vigentes (v1.2, aceptados por José Francisco Ñáñez el 2026-10-06), así que no hubo que registrar nada.

El inventario trajo 60 documentos nuevos y ninguno cambiado. De ellos, 28 son de contratos y se convirtieron sin fallos; el resto es de otras familias.

Esto es el reporte del motor (`<espacio>/estado-legal/900123456-banco-andino/contratos/reporte-contract-scan.md`). Salieron cinco señales:

| # | Contrato | Señal |
|---|---|---|
| 1 | CTR-101 | Diana Cruz firmó por 400.000.000,00 y la matriz de atribuciones no le da facultad para ese tipo y monto (fila 2 de la matriz). |
| 2 | CTR-104 | El informe mensual de agosto (OBL-1) venció el 2026-09-05, hace 31 días, y no hay evidencia en `40-ejecucion/`. |
| 3 | CTR-104 | El preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie ha decidido. |
| 4 | CTR-103 | El contrato exige garantía de calidad y no hay póliza aportada. |
| 5 | CTR-102 | El registro dice 300.000.000,00 y el documento 250.000.000,00. |

Todo lo que llegó se procesó y el motor no hizo preguntas. Las fichas no tienen campos pendientes (`record_issues` vacío).

No interpreté ninguna cláusula ni califiqué ninguna firma. Dejé a la persona dos puntos:
- CTR-105: el acta del comité decide renovar, pero el contrato dice que no se prorroga automáticamente.
- Las obligaciones de informe final y liquidación de las fichas usan la fecha de terminación como vencimiento, porque la cláusula 6 dice "a la terminación". En CTR-102 es la del otrosí, 2027-12-31.

La salida quedó en `<espacio>/estado-legal/900123456-banco-andino/corridas/salida-contract-scan.md` y la corrida quedó registrada como `2026-10-06-contract-scan-1`.