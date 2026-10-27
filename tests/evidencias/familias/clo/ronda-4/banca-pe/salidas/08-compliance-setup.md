# /criterio-compliance:compliance-setup legal/20710000019-banco-ribera

Constanza quedó instalada sobre Banco Ribera (20710000019, Perú, PEN). Revisó las 10 obligaciones del periodo 2026-09 y encontró 5 señales abiertas. El informe de septiembre declara el periodo «cumplido», pero con evidencia solo hay 72,73 % de avance (ponderado por criticidad).

- **Configuración:** `.criterio/cumplimiento/20710000019/config.json`. Pasó la validación sin problemas.
- **Términos:** José Francisco Ñáñez los aceptó el 2026-10-06, como indicaste. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Carpeta de documentos:** no la marqué con `_CRITERIO_LEGAL.txt`, porque nadie lo autorizó. La pregunta queda sin respuesta en la ficha del periodo.
- **Preguntas:** hice 3, todas con respuesta sugerida a partir de los documentos. Eran el periodo, la ruta de las fichas de Fidel y la marca de la carpeta.

Las señales abiertas son:
1. **OB-09 (Reporte mensual de quejas):** venció el 2026-10-05 y no tiene evidencia. El responsable es Claudia Salinas.
2. **Declarado contra evidenciado:** el informe declara «cumplido», pero hay señales abiertas que ese estado no explica.
3. **CTR-701, OBL-3 (Reporte de operaciones al oficial de cumplimiento):** es una obligación del contrato que la matriz no tiene.
4. **OB-12 (Registro de conflictos de interés):** no tiene responsable en la matriz.
5. **Una norma sin evaluar:** el motor la cuenta, pero el reporte no la lista en «lo que hay que atender». Se revisa con `regulatory-watch`.

El reporte completo está en `estado-legal/20710000019-banco-ribera/cumplimiento/2026-09/reporte-compliance-status.md`. La corrida quedó registrada como `2026-10-06-compliance-setup-1`.