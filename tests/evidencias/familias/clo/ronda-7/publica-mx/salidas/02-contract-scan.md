# /criterio-legal:contract-scan 

Los seis contratos de la carpeta llegaron como nuevos. Sus fichas ya existían de `legal-setup` y coinciden con los documentos, así que no hice extracción nueva. `compute` no devolvió `record_issues` y todo se procesó.

El motor marca tres señales del mismo tipo, `public_guarantee_late`. La garantía de cumplimiento se entregó después del plazo que el motor aplica (10 días naturales después de la firma) en tres contratos:

| Contrato | Entregada | Límite | Días |
|---|---|---|---|
| CTR-2302 | 2025-07-12 | 2025-07-06 | 6 |
| CTR-2304 | 2026-03-12 | 2026-03-06 | 6 |
| CTR-2306 | 2025-10-12 | 2025-10-06 | 6 |

Qué significa esa fuera de plazo es una pregunta para una persona; no la interpreto.

- **Términos:** ya estaban vigentes, con aceptación de José Francisco Ñáñez del 2026-10-06. No hubo que registrar nada.
- **Fuera de lugar:** `00-referencia/politica-contratacion.md` iría en `20-politicas/`; no lo moví.
- **Registro de la corrida:** `2026-10-06-contract-scan-1`, con el informe completo en `estado-legal/OPB150301AB9-organismo-publico-del-bajio/corridas/salida-contract-scan.md`.
- **Fecha:** pasé `--today 2026-10-06` en cada llamada que la acepta.