# /criterio-compliance:compliance-setup legal/155831003-2-2013-comercial-control-del-istmo

La instalación de Constanza quedó lista para Comercial Control del Istmo. Revisé las 8 obligaciones de la matriz contra su evidencia del periodo 2026-09, y el informe de ese periodo declara «cumplido».

- **Obligaciones:** 6 tienen evidencia. OB-04 y OB-05 están en plazo y aún sin evidencia. El motor da un avance con evidencia de 83,33 %, ponderado por criticidad, y no levantó señales abiertas.
- **OB-07:** su evidencia es del periodo 2026-07, porque la revisión es semestral.
- **Norma por evaluar:** el boletín de septiembre trae la Circular sintética 009 de 2026 (N-2026-09), que el registro normativo todavía no tiene. La dejé en la ficha como «por evaluar», como la dice el boletín.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Nadie autorizó escribir ahí, así que queda para cuando una persona lo confirme.

Como nadie podía responder, tomé las respuestas sugeridas por los documentos. Para el plazo del canal de denuncias (15 días) y la evaluación de normas nuevas (30 días) usé los valores por defecto del ejemplo de configuración, porque ningún documento fija otros. Cambian en `thresholds` de la configuración.

Archivos principales (relativos a la carpeta de la sesión):
- La configuración, validada sin problemas, está en `.criterio/cumplimiento/155831003-2-2013/config.json`.
- La ficha del periodo está en `estado-legal/155831003-2-2013-comercial-control-del-istmo/cumplimiento/2026-09/ficha.json`.
- El reporte completo está en `estado-legal/155831003-2-2013-comercial-control-del-istmo/cumplimiento/2026-09/reporte-compliance-status.md`.
- Lo que te mostré en esta corrida, entero, está en `estado-legal/155831003-2-2013-comercial-control-del-istmo/corridas/salida-compliance-setup.md`. La corrida quedó registrada como `2026-10-06-compliance-setup-1`.