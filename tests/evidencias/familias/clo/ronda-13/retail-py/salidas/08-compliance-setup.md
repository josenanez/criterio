# /criterio-compliance:compliance-setup legal/88612904-4-distribuidora-del-ybytyruzu-sintetica

La instalación de Constanza sobre Distribuidora del Ybytyruzú Sintética (RUC 88612904-4) quedó lista, con el primer estado del periodo 2026-09 y la corrida registrada. Nadie respondió preguntas, así que todas las respuestas salieron de los documentos.

- **Configuración:** está en `.criterio/cumplimiento/88612904-4/config.json` y el motor la validó sin problemas. Usé PY y PYG, el periodo 2026-09 y los umbrales del ejemplo. Las fichas de Fidel están en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/contratos`, que comprobé con Glob.
- **Términos 1.3:** mostré el texto corto tal cual y registré la aceptación a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Marca de la raíz:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarlo.
- **Estado declarado:** el informe de septiembre dice «con observaciones» (2026-10-05, Osvaldo Ramírez). Lo registré en `cumplimiento/2026-09/ficha.json`. No había normas nuevas ni preguntas que anotar.

El reporte de estado, escrito por el motor, da un avance con evidencia de 76,19 % (ponderado por criticidad). Marca dos cosas para atender:
- **OB-10** (Declaración mensual de origen de fondos) figura cumplida en la matriz, pero no hay evidencia que empiece por OB-10.
- **OB-13** (Reporte de regalos e invitaciones) no cita la norma, el contrato o la política de la que sale.

El motor calculó cinco señales en total. Las otras tres no salen en este reporte: un caso del canal de denuncias vencido, una norma que aplica sin obligación en la matriz y una política con la revisión vencida. Las muestran `reports-cases`, `regulatory-watch` y `policy-review`.

La corrida quedó registrada como `2026-10-06-compliance-setup-1`, con 5 hallazgos. Lo que te mostré está en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-compliance-setup.md`. El reporte completo está en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/cumplimiento/2026-09/reporte-compliance-status.md`.