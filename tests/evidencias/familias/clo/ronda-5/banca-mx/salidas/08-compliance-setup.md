# /criterio-compliance:compliance-setup legal/BVA150301K21-banco-valle-de-anahuac

Constanza quedó instalada sobre Banco Valle de Anáhuac (BVA150301K21) y revisó las 10 obligaciones de la matriz contra su evidencia del periodo 2026-09. El motor encontró 5 señales.

El informe de septiembre declara el periodo **cumplido** (2026-10-05), pero el avance con evidencia es de 72.73 %, ponderado por criticidad. El motor lo marca como declarado contra evidenciado.

Las 5 señales:
1. **OB-09, Reporte mensual de quejas (Mónica Garza):** venció el 2026-10-05 y no tiene evidencia.
2. **Informe contra evidencia:** el informe declara cumplido y hay señales abiertas que ese estado no explica.
3. **Norma sin evaluar:** la Circular sintética 007 de 2026 (N-2026-07) llegó en el boletín de agosto y no está en el registro normativo.
4. **OBL-3 de CTR-1301:** es una obligación de cumplimiento del contrato (cláusula 7) que la matriz no tiene.
5. **OB-12, Registro de conflictos de interés:** no tiene responsable en la matriz.

La tabla «Lo que hay que atender» del reporte lista solo 4 de estas 5; la de la norma sin evaluar no aparece ahí, pero sí en `resultados.json`.

**Preguntas:** como no había nadie que contestara, usé la respuesta sugerida por los documentos en cada una:
- **Periodo:** 2026-09.
- **Plazos:** 15 días para el canal de denuncias y 30 para evaluar una norma, los valores por defecto.
- **Fichas de Fidel:** `estado-legal/BVA150301K21-banco-valle-de-anahuac/contratos`, carpeta que comprobé que existe.
- **Marca de la raíz:** dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos.
- **Sin respuesta:** quién responde por OB-12. Eso lo define la organización.

**Términos:** mostré los términos 1.2 y registré su aceptación a nombre de José Francisco Ñáñez (2026-10-06), con comprobante en Markdown y PDF.

**Archivos** (el estado está en `estado-legal/BVA150301K21-banco-valle-de-anahuac/`):
- **Configuración:** `.criterio/cumplimiento/BVA150301K21/config.json`
- **Ficha del periodo:** `cumplimiento/2026-09/ficha.json`
- **Reporte del motor:** `cumplimiento/2026-09/reporte-compliance-status.md`
- **Salida de la corrida:** `corridas/salida-compliance-setup.md`
- **Corrida registrada:** `2026-10-06-compliance-setup-1`