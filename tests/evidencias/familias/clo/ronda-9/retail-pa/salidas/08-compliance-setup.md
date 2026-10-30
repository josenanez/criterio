# /criterio-compliance:compliance-setup legal/155791002-2-2017-almacenes-del-canal

Constanza quedó instalada sobre Almacenes del Canal para el periodo 2026-09, y el motor encontró 5 señales. El reporte solo muestra 3 en «Lo que hay que atender». Las otras dos están en `cumplimiento/2026-09/resultados.json`; no las abrí, así que no sé su detalle.

**Lo que dejé hecho**
- **Configuración:** `.criterio/cumplimiento/155791002-2-2017/config.json`. La validé y salió sin problemas. Los umbrales son los del ejemplo (15 días para el canal de denuncias, 30 para evaluar normas) y la lista de feriados quedó vacía.
- **Términos:** versión 1.3, aceptada a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante está en `.criterio/terminos/`, en Markdown y PDF.
- **Ficha del periodo:** `cumplimiento/2026-09/ficha.json`. El informe del 2026-10-05 declara «con observaciones».
- **Corrida:** `2026-10-06-compliance-setup-1`, con 5 hallazgos.
- **Fichas de Fidel:** están en `estado-legal/155791002-2-2017-almacenes-del-canal/contratos`; las comprobé en disco.

**Lo que no hice**
- No dejé la marca `_CRITERIO_LEGAL.txt` en la carpeta de documentos, porque nadie podía autorizarla en esta prueba. La pregunta quedó en la ficha como sin respuesta.

**Lo que mostró el estado**
- **Avance con evidencia:** 72.73 % ponderado por criticidad. De las 10 obligaciones, 7 están cumplidas con evidencia, 2 en plazo y 1 vencida.
- **OB-09, reporte mensual de quejas:** venció el 2026-10-05 sin evidencia. Responsable: Abdiel Moreno.
- **CTR-3001, OBL-3:** el contrato exige un reporte de operaciones al oficial de cumplimiento, y la matriz no lo tiene.
- **OB-12, registro de conflictos de interés:** no tiene responsable en la matriz. Aun así tiene evidencia en el periodo.
- **OB-07:** quedó contada como cumplida con una evidencia de 2026-07, dentro de su ventana semestral.

El reporte completo está en `estado-legal/155791002-2-2017-almacenes-del-canal/cumplimiento/2026-09/reporte-compliance-status.md`. Lo que mostré en esta sesión quedó guardado en `corridas/salida-compliance-setup.md`.