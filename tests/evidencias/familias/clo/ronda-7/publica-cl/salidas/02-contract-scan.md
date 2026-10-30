# /criterio-legal:contract-scan 

Corrí el escaneo de contratos de Servicio Público del Maipo con fecha 2026-10-06 y salieron tres señales. Las seis fichas ya existían (de `legal-setup`) y coinciden con sus documentos, así que no las cambié. El motor no dio `record_issues` y procesó todo.

- **Términos:** ya estaban vigentes y aceptados a nombre de José Francisco Ñáñez (versión 1.3, 2026-10-06), así que no registré nada nuevo.
- **Inventario:** 64 documentos, todos nuevos. Hay uno fuera de lugar: `00-referencia/politica-contratacion.md` iría en `20-politicas/`.

Las tres señales del reporte:

1. **CTR-2201:** la garantía de cumplimiento es de 6.000.000,00 y la ley pide al menos el 5 % del valor, 10.000.000,00. Faltan 4.000.000,00.
2. **CTR-2203:** la garantía es de 4.500.000,00 y la ley pide 7.500.000,00. Faltan 3.000.000,00.
3. **CTR-2205:** se publicó en Mercado Público el 2026-01-30, y el plazo legal vencía el 2026-01-28. Son 2 días de retraso.

La sección «El resultado» del reporte sale vacía. Es lo que generó el motor y no la completé.

La salida está en `corridas/salida-contract-scan.md`. La corrida quedó registrada como `2026-10-06-contract-scan-1`.