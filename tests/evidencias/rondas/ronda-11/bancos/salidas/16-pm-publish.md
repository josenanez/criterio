# /criterio-project:pm-publish confirmar

Publiqué la ficha de PRY-206 en `/tmp/claude-0/-home-claude/692b0e4d-0e89-5e8d-a391-2cabbf233557/scratchpad/r11/bancos/espacio/documentos/proyectos/PRY-206-billetera-y-qr/00-gobierno/ficha-pm.json`, con corte al 2026-10-23.

Es una copia exacta de `records/PRY-206.json`, y la carpeta de gobierno ya existía. Los términos (v1.2) ya estaban vigentes, aceptados por José Francisco Ñáñez el 2026-10-23, así que no volví a registrarlos.

**Lleva:** 65 campos con dato · 7 sin decir en ninguna parte · declara **verde** al 2026-10-20.

Los 7 sin decir son `identity.authority`, `identity.phase`, `vendors[1].invoiced`, los responsables de los 3 riesgos (`raid.risks[0..2].owner`) y el de la incidencia (`raid.issues[0].owner`).

**Lo más viejo que va ahí:** la identidad del proyecto y el presupuesto aprobado, del 2026-04-12 (acta de constitución). No pasa de un año.

**Fecha de cierre:** `plan.end_date` es 2027-01-25. Coincide con la línea base y con el único cronograma que hay (v1), así que no corregí nada.

**Lo que la PMO va a ver:** la ficha marca el «verde» como declarado por ti, no como dictamen. Los datos recalculados lo contradicen en cuatro señales:
- Compromisos vencidos y reprogramados.
- Dos hitos dados por cumplidos sin evidencia: «Ambiente de pruebas certificado» e «Integración con el core».
- Entregables de proveedor atrasados.

La corrida quedó registrada como `2026-10-23-pm-publish-1`, con lo anterior guardado en `estado/PRY-206-billetera-y-qr/corridas/salida-pm-publish.md`.