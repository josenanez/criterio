# /criterio-compliance:compliance-setup legal/48712035-banco-del-altiplano-sintetico

Constanza quedó instalada sobre Banco del Altiplano Sintético (48712035, GT) y revisó las 10 obligaciones de la matriz contra su evidencia. El motor encontró 5 señales, y la más importante es que el informe de septiembre declara «cumplido» pese a ellas.

**Lo que dejé hecho**
- **Configuración:** `.criterio/cumplimiento/48712035/config.json`, validada sin problemas. Evalúa el periodo 2026-09 y apunta a las fichas de Fidel en `estado-legal/48712035-banco-del-altiplano-sintetico/contratos`, que comprobé en disco.
- **Términos:** José Francisco Ñáñez los aceptó, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/` en Markdown y PDF.
- **Ficha del periodo:** registré el estado que declara el informe del 2026-10-05, «cumplido». No había normas nuevas que registrar.
- **Corrida:** quedó registrada como `2026-10-06-compliance-setup-1`.
- **Reporte:** `estado-legal/48712035-banco-del-altiplano-sintetico/cumplimiento/2026-09/reporte-compliance-status.md`.

**Lo que encontró el motor** (el avance con evidencia es del 65.22 %, ponderado por criticidad):
1. **OB-09, reporte mensual de quejas:** venció el 2026-10-05 y no tiene evidencia. El responsable es María Fernanda Barrios.
2. **Declarado contra evidenciado:** el informe declara el periodo cumplido, pero el reporte cuenta 4 señales abiertas que ese estado no explica.
3. **OBL-3 de CTR-3301**, reporte de operaciones al oficial de cumplimiento: es una obligación del contrato que la matriz no tiene.
4. **OB-11, monitoreo de listas restrictivas:** su última evidencia es de 2026-07, y el ciclo anterior no tiene.
5. **Norma N-2026-05:** está por evaluar. Esta quinta señal la contó el motor, pero el reporte no la muestra en su tabla.

**Pendiente para una persona**
- La matriz salta de OB-09 a OB-11. No sé si OB-10 se retiró o falta; lo decide quien mantiene la matriz.
- No dejé la marca `_CRITERIO_LEGAL.txt` en la carpeta raíz. Nadie podía autorizarla en esta sesión sin interfaz, así que la omití en vez de suponer el sí.
- Las dos preguntas que tomé con respuesta sugerida (el periodo y la ruta de las fichas de Fidel) quedaron en la ficha y en el reporte. Conviene confirmarlas.