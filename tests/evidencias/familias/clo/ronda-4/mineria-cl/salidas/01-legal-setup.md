# /criterio-legal:legal-setup legal/76089001-4-minera-atacama-norte

La instalación sobre Minera Atacama Norte está terminada y la corrida quedó registrada como `2026-10-06-legal-setup-1`. Se procesaron los 6 contratos, sin errores de ficha.

**Qué quedó escrito**
- **Configuración:** `.criterio/legal/76089001-4/config.json`. Es Chile, en CLP, con avisos de 60 días para vencimientos y 30 para preavisos, certificado de máximo 30 días, y estado en `estado-legal/76089001-4-minera-atacama-norte`.
- **Términos:** la versión 1.2 quedó aceptada a nombre de José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/`, en Markdown y PDF.
- **Fichas:** una por contrato, de CTR-1101 a CTR-1106, en `estado-legal/76089001-4-minera-atacama-norte/contratos/`.
- **Salida de la corrida:** `estado-legal/76089001-4-minera-atacama-norte/corridas/salida-legal-setup.md`.

**Lo que encontró el motor**
- **Señales:** 4 en total. Son 1 firma sin facultad, 1 preaviso vencido, 1 contrato sin la firma de las dos partes y 1 garantía faltante.
- **Calendario:** solo muestra la del preaviso. El preaviso de CTR-1101 venció el 2026-10-01 sin decisión registrada, y el contrato se prorroga el 2026-10-31.
- **Las otras tres:** el motor no las desglosó por contrato. Para verlas hay que correr `authority-check` y `contract-execution`.
- **Decisión de renovar:** la ficha de CTR-1105 recoge la decisión del acta del 2026-09-18, que dice renovarlo. Lo dice el acta, no yo.

**Para que lo sepas**
- La nota de la corrida dice "9 preguntas respondidas con la propuesta", pero fueron 6 preguntas, más la de la marca de la raíz, que dejé sin hacer. El conteo está mal y no lo corregí.
- No dejé el archivo `_CRITERIO_LEGAL.txt` en la carpeta de documentos, porque nadie podía autorizarlo en esta sesión.
- En CTR-1106 el contrato dice "el [informe] de agosto" con fecha límite 2026-07-06. Lo registré tal cual y no lo interpreté.