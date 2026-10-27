# /criterio-legal:legal-setup legal/76097001-8-comercial-control-andes

Fidel quedó instalado sobre Comercial Control Andes (RUT 76097001-8, Chile, CLP) y procesó los 6 contratos. El motor no encontró señales nuevas al 2026-10-06.

- **Carpeta:** usé `legal/76097001-8-comercial-control-andes`, que venía como argumento. Tiene los 6 contratos (CTR-1201 a CTR-1206), el registro y la matriz de atribuciones, y nada fuera de lugar. También hay políticas, normativa, canal y 3 periodos de cumplimiento, que son de Constanza.
- **Preguntas:** no hice ninguna a la persona. Tomé seis respuestas de los documentos y de `config.example.json`: entidad, matriz de atribuciones, umbrales de aviso, certificado, carpeta de estado y la marca de la carpeta. La configuración validó sin problemas.
- **Términos:** versión 1.2, aceptada por José Francisco Ñáñez el 2026-10-06. Los comprobantes están en `.criterio/terminos/` en Markdown y PDF.
- **Marca:** dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos, como autorizó José Francisco Ñáñez.
- **Fichas:** 6 fichas en `estado-legal/76097001-8-comercial-control-andes/contratos/`, sin `record_issues`. Dos puntos de la extracción:
  - CTR-1202: el contrato termina el 2027-06-30 y el otrosí OT-1 lo mueve al 2027-12-31. Su informe final vence en la fecha nueva.
  - CTR-1205: la ficha registra la decisión de renovar, tomada por el acta del comité del 2026-09-18.
- **Calendario:** el reporte no marca nada abierto. Lista cinco filas, que el motor calcula contra el 2026-10-06:

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-1201 | OBL-3, reporte al oficial de cumplimiento | -6 (con evidencia) |
| 2026-11-20 | CTR-1205 | terminación y acta de liquidación | 45 |
| 2026-12-31 | CTR-1203 | terminación y acta de liquidación | 86 |

- **Corrida:** quedó registrada como `2026-10-06-legal-setup-1`, con 0 hallazgos, y lo mostrado está en `estado-legal/76097001-8-comercial-control-andes/corridas/salida-legal-setup.md`.

Las comprobaciones de facultades y de pagos son comandos aparte (`authority-check`, `contract-execution`); no las corrí aquí.

Me quedó una duda por resolver: el contrato CTR-1206 dice «el de agosto» para un informe con fecha 2026-07-06. La ficha registra la fecha tal como está escrita.