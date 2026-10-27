# /criterio-legal:legal-setup legal/20790000014-comercial-control-sur

Fidel quedó instalado sobre Comercial Control Sur (RUC 20790000014, Perú, PEN), con las 6 fichas de contrato escritas y la corrida registrada. No hubo preguntas a la persona. En las que no se podían contestar desde los documentos tomé la respuesta sugerida.

- **Carpeta:** usé la que llegó como argumento, `legal/20790000014-comercial-control-sur`. Tiene 6 contratos, el registro y la matriz de atribuciones, y nada fuera de la estructura recomendada.
- **Entidad y umbrales:** el nombre, el RUC y el país salen de los contratos. Los umbrales son los de `config.example.json`: aviso de vencimiento a 60 días, de preaviso a 30 y certificado de máximo 30 días. No cargué feriados, porque los del ejemplo son de Colombia.
- **Dónde quedó:** la configuración está en `.criterio/legal/20790000014/config.json`. El estado está en `estado-legal/20790000014-comercial-control-sur`, fuera de los documentos.
- **Términos:** mostré el resumen de la versión 1.2 y registré la aceptación de José Francisco Ñáñez con fecha 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Nadie la autorizó y es lo único que se escribiría ahí.
- **Fichas:** los 6 contratos (CTR-901 a CTR-906) se convirtieron y quedaron en fichas, cada dato con su fuente. El cálculo no dio `record_issues` ni señales.

**Calendario al 2026-10-06** (entre 30 días atrás y 90 adelante):

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-901 | Reporte de operaciones al oficial de cumplimiento (con evidencia) | -6 |
| 2026-11-20 | CTR-905 | Terminación e informe final y acta de liquidación (sin evidencia) | 45 |
| 2026-12-31 | CTR-903 | Terminación e informe final y acta de liquidación (sin evidencia) | 86 |

Para CTR-905, un acta del 2026-09-18 registra la decisión de renovar. La ficha la guarda como decisión de quien la tomó, no como recomendación mía.

El reporte dice "Nada abierto" y el cálculo no dio señales, así que no pasé a revisar facultades ni pagos: el setup solo pide el calendario.

El reporte completo está en `estado-legal/20790000014-comercial-control-sur/contratos/reporte-obligations-calendar.md`. Lo que te mostré quedó en `estado-legal/20790000014-comercial-control-sur/corridas/salida-legal-setup.md`, y la corrida se registró como `2026-10-06-legal-setup-1` sin hallazgos.