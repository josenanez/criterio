# /criterio-legal:contract-scan 

Las siete fichas de contratos ya existían de la corrida anterior (`legal-setup`) y coinciden con los documentos, así que no corregí ninguna. El motor no devolvió `record_issues` y procesó todo lo que llegó. Las cinco señales son las mismas que dejó esa corrida. Todo se calculó con `--today 2026-10-06`, y los términos ya estaban vigentes con la aceptación de José Francisco Ñáñez.

El inventario marcó como "nuevos" los 66 archivos de la carpeta. De ellos 33 son documentos de contratos, y los 33 se convirtieron sin errores.

Estas son las señales:

| # | Señal | Contrato | Qué dice el reporte |
|---|---|---|---|
| 1 | `signed_without_authority` | CTR-3702 | Andrea Jiménez firmó el otrosí OT-1 (154.000.000,00) sin facultad para ese monto según la matriz de atribuciones. |
| 2 | `contract_expiring` | CTR-3703 | Vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar. |
| 3 | `guarantee_missing` | CTR-3703 | El contrato exige la garantía de calidad y no hay póliza aportada en `20-garantias/`. |
| 4 | `register_mismatch` | CTR-3707 | El contrato está en la carpeta y no en el registro. |
| 5 | `register_differs_from_contract` | CTR-3702 | El registro dice 132.000.000,00 y el documento 242.000.000,00. |

El reporte quedó en `contratos/reporte-contract-scan.md` y la salida mostrada en `corridas/salida-contract-scan.md`. La corrida está registrada como `2026-10-06-contract-scan-1`, con 5 hallazgos, y no hice ninguna pregunta.

Todas las rutas son relativas a `estado-legal/3101612904-almacenes-de-la-meseta/`.