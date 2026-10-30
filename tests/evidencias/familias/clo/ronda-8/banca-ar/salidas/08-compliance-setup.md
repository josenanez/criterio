# /criterio-compliance:compliance-setup legal/30718174607-banco-del-rio-de-la-plata-sintetico

Constanza quedó instalada sobre Banco del Río de la Plata (sintético), CUIT 30718174607. El motor revisó las 10 obligaciones de la matriz del periodo 2026-09, con un avance con evidencia de 72,73 % (ponderado por criticidad). La corrida quedó registrada con 5 señales.

**Lo que dejé escrito**
- La configuración está en `.criterio/cumplimiento/30718174607/config.json` y el motor la validó sin problemas.
- Los términos quedaron aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes están en `.criterio/terminos/` (Markdown y PDF).
- Puse la marca `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Lo tomé como respuesta sugerida, porque en esta sesión nadie podía autorizarlo.
- Registré el informe de septiembre en `cumplimiento/2026-09/ficha.json`. Declara «cumplido» (línea 5).
- El reporte del motor está en `estado-legal/30718174607-banco-del-rio-de-la-plata-sintetico/cumplimiento/2026-09/reporte-compliance-status.md`.
- Lo que te mostré quedó en `corridas/salida-compliance-setup.md`.

**Preguntas** (nadie respondió; tomé lo sugerido por los documentos)
- Periodo evaluado: 2026-09.
- Fichas de Fidel: `estado-legal/30718174607-banco-del-rio-de-la-plata-sintetico/contratos`. La carpeta existe.
- Plazo del canal de denuncias: 15 días. Días para evaluar una norma nueva: 30. Son los valores por defecto de la configuración de ejemplo, no algo que digan los documentos.

**Señales**
1. OB-09 (reporte mensual de quejas) venció el 2026-10-05 sin evidencia. El responsable es Santiago Ferreyra.
2. El informe declara el periodo «cumplido», pero hay señales abiertas que ese estado no explica.
3. La cláusula 7 del contrato CTR-2501 trae la obligación OBL-3, que la matriz no tiene.
4. OB-12 (registro de conflictos de interés) no tiene responsable.
5. Hay una norma sin evaluar (`regulatory_change_unassessed`). El reporte no la detalla en su tabla de atención.

No interpreté ninguna cláusula ni norma, y no recomendé nada. Si OBL-3 pasa a la matriz o quién responde por OB-12 es decisión de la organización.

Glob no estaba disponible en esta sesión, así que usé `find` para buscar las fichas de Fidel.