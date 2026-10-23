# /criterio-compliance:compliance-setup legal/900123456-banco-andino

Constanza quedó instalada sobre Banco Andino (NIT 900123456) y el primer estado es el del periodo 2026-09. Hay 10 obligaciones en la matriz y 60 documentos en la carpeta; todos están en su lugar y ninguno es ilegible. En esta prueba nadie respondió: las tres preguntas que hice las contesté con la respuesta sugerida por los documentos.

El informe del 2026-10-05 declara el periodo como **cumplido** (línea 5), y el motor encuentra 5 señales abiertas que ese estado no explica. El avance con evidencia es 72,73 %, ponderado por criticidad.

- **OB-09, Reporte mensual de quejas:** venció el 2026-10-05 sin evidencia. La responsable es Diana Cruz.
- **OB-12, Registro de conflictos de interés:** la matriz no le asigna responsable, aunque sí tiene evidencia.
- **CTR-101, OBL-3:** el contrato tiene una obligación de cumplimiento (reporte de operaciones al oficial de cumplimiento) que la matriz no incluye.
- **Declarado contra evidenciado:** hay una señal propia por declarar «cumplido» con las otras señales abiertas.
- **Norma sin evaluar:** hay una norma nueva (`regulatory_change_unassessed`) que no aparece en la tabla del reporte. Quedó contada como quinta señal, y la detalla `/regulatory-watch`.

**Lo que escribí:**
- La configuración de Constanza, en `.criterio/cumplimiento/900123456-banco-andino/config.json`. Ya existía una de Fidel en `.criterio/legal/`, pero el motor pedía una propia. Usé periodo 2026-09, plazo del canal de 15 días, 30 días para evaluar una norma y las fichas de Fidel en `estado-legal/900123456-banco-andino/contratos`.
- Los términos quedaron aceptados a nombre de José Francisco Ñáñez el 2026-10-06, con comprobante en `.criterio/terminos/`.
- El archivo `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Lo tomé de la respuesta sugerida, que era sí.
- La ficha del periodo, con lo declarado y las tres preguntas, en `estado-legal/900123456-banco-andino/cumplimiento/2026-09/ficha.json`.
- El reporte, en `estado-legal/900123456-banco-andino/cumplimiento/2026-09/reporte-compliance-status.md`, y la corrida registrada como `2026-10-06-compliance-setup-1`.

No moví ni renombré ningún documento.