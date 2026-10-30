# /criterio-legal:contract-scan 

Corrí `contract-scan` sobre los 6 contratos de Empresa Pública Paulista, con fecha 2026-10-06. Salieron 4 señales, y todo lo que llegó se procesó (`record_issues` vacío).

Los términos ya estaban vigentes, con la aceptación de José Francisco Ñáñez registrada, así que no hubo que registrarla de nuevo.

Las fichas de los seis contratos ya existían en el estado. Solo comprobé a mano la de CTR-2401 contra su contrato, y coincide. Las otras cinco las dejé como estaban, porque el motor las validó sin observaciones.

Las 4 señales:
- **CTR-2402, publicación:** no hay constancia de publicación en PNCP. La ley pedía publicar a más tardar el 2025-07-24, así que van 439 días.
- **CTR-2404, publicación:** se publicó en PNCP el 2026-03-13, y el plazo era el 2026-03-10, 3 días después.
- **CTR-2403, garantía:** la exigida es de 72.000,00 y el tope de la ley es 45.000,00, sin justificación (exceso de 27.000,00).
- **CTR-2406, garantía:** la exigida es de 60.000,00 y el tope es 37.500,00, sin justificación (exceso de 22.500,00).

En el reporte, la sección «El resultado» salió vacía; es tal como la generó el motor.

La corrida quedó registrada como `2026-10-06-contract-scan-1`, con 4 hallazgos. El reporte está en `estado-legal/45678912000155-empresa-publica-paulista/contratos/reporte-contract-scan.md`, y la salida mostrada en `corridas/salida-contract-scan.md` de esa misma carpeta de estado.