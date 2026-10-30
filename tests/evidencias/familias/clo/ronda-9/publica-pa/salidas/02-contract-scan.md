# /criterio-legal:contract-scan 

Corrida registrada: procesé los seis contratos y el motor dejó 4 señales. Ya terminé; solo queda este resumen.

Todos los contratos (CTR-3201 a CTR-3206) eran nuevos, y no hubo cambiados ni ilegibles. Armé una ficha por contrato y el motor no dejó `record_issues`.

Las 4 señales vienen de dos contratos, CTR-3201 y CTR-3203:

- **Sin póliza:** el contrato exige garantía de cumplimiento (cláusula 9) y no hay póliza en `20-garantias/`.
- **Bajo el mínimo de ley:** son contratos públicos de 200,000 USD y 150,000 USD, y la ley exige la garantía por encima de 50,000. El motor las marca por no tener garantía.

- **Sección «El resultado»:** el reporte del motor la trae vacía, y la dejé así.
- **Archivo fuera de lugar:** `00-referencia/politica-contratacion.md` iría en `20-politicas/`.
- **Términos:** el motor los dio por vigentes (versión 1.3, aceptados por José Francisco Ñáñez el 2026-10-06), así que no repetí el registro.

Pasé `--today 2026-10-06` en cada llamada que lo acepta.

Archivos en `<espacio>/estado-legal/155699101-2-2021-autoridad-publica-del-istmo/`:
- `contratos/CTR-3201.json` a `contratos/CTR-3206.json` (las fichas)
- `corridas/salida-contract-scan.md` (lo mostrado, entero)
- `contratos/reporte-contract-scan.md` (lo escribió el motor)