# /criterio-legal:contract-scan 

Corrí `contract-scan` sobre los seis contratos del banco, que el inventario marcó como nuevos. El motor encontró cinco señales y ningún problema de ficha (`record_issues` vacío). Dejé la corrida registrada.

Las fichas de `estado-legal/…/contratos/` ya existían, porque las armó `legal-setup`. Las contrasté con los documentos y coincidían, así que no las modifiqué. Los términos 1.3 estaban vigentes con la aceptación de José Francisco Ñáñez del 2026-10-06. No hubo preguntas que responder.

Las cinco señales, con las cifras tal como las dio el motor:

| # | Contrato | Señal |
|---|---|---|
| 1 | CTR-3302 | José Pablo Cifuentes firmó el otrosí OT-1 (3,150,000.00) sin facultad para ese monto según la matriz de atribuciones. El contrato queda en 4,950,000.00 con el otrosí. |
| 2 | CTR-3302 | Lo pagado, 5,247,000.00, supera el valor con otrosíes en 297,000.00 (filas 6 y 7 del archivo de pagos). |
| 3 | CTR-3304 | La obligación OBL-1 (informe mensual) venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`. Lleva 31 días vencida. |
| 4 | CTR-3304 | El preaviso de no renovación vence el 2026-11-01, en 26 días, y nadie ha decidido. |
| 5 | CTR-3303 | El contrato exige garantía de calidad y no hay póliza aportada en `20-garantias/`. |

- **Reporte:** el reporte del motor está en `estado-legal/48712035-banco-del-altiplano-sintetico/contratos/reporte-contract-scan.md`.
- **Salida de la corrida:** la salida completa que te mostré está en `estado-legal/48712035-banco-del-altiplano-sintetico/corridas/salida-contract-scan.md`.
- **Registro:** quedó como `2026-10-06-contract-scan-1`.

No califiqué ninguna firma ni recomendé renovar o terminar. Esas decisiones quedan para una persona.