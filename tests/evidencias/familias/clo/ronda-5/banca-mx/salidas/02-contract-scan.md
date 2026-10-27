# /criterio-legal:contract-scan 

Procesé los 6 contratos (CTR-1301 a CTR-1306). Todos llegaron como nuevos y ya tienen su ficha. El motor encontró 5 señales y la corrida quedó registrada como `2026-10-06-contract-scan-1`. Los términos v1.2 ya estaban vigentes con la aceptación de José Francisco Ñáñez del 2026-10-06, así que no hizo falta registrarlos de nuevo.

| # | Contrato | Señal | Dato del motor |
|---|---|---|---|
| 1 | CTR-1301 | Mónica Garza firmó por la entidad un contrato de 2,400,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto. | `matriz-atribuciones.csv`, fila 2 |
| 2 | CTR-1302 | Lo pagado, 1,590,000.00, supera en 90,000.00 el valor con otrosíes, 1,500,000.00. | `pagos-2026-09-30.csv`, filas 6 y 7 |
| 3 | CTR-1303 | Vence el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar. | Contrato, cláusula 3 |
| 4 | CTR-1301 | La póliza vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31. | Póliza de cumplimiento |
| 5 | CTR-1304 | El informe mensual de agosto (OBL-1) venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`. | Contrato, cláusula 5 |

- **Fichas:** quedaron en `estado-legal/BVA150301K21-banco-valle-de-anahuac/contratos/`, una por contrato. `record_issues` salió vacío y no hubo documentos sin procesar. Del acta del 2026-09-18 registré la decisión de renovar el CTR-1305.
- **Registro, pagos y matriz:** no los extraje; los procesó el motor.
- **Preguntas:** no hice ninguna en esta corrida.
- **Reporte:** el motor lo dejó en `contratos/reporte-contract-scan.md`, dentro de la carpeta de estado. La sección «El resultado» salió vacía; la copié tal cual.
- **Salida de la corrida:** la guardé en `corridas/salida-contract-scan.md`.

Todo esto describe lo que muestran los documentos; no valoré la validez de las firmas ni de las pólizas.