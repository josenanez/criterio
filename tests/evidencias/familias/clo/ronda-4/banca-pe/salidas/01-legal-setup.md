# /criterio-legal:legal-setup legal/20710000019-banco-ribera

Fidel quedó instalado sobre Banco Ribera (RUC 20710000019, Perú, soles). Procesó los 6 contratos (CTR-701 a CTR-706) sin preguntar nada, y `compute` no dejó `record_issues`.

- **Documentos:** están la matriz de atribuciones y el registro de contratos, y nada quedó fuera de la estructura.
- **Configuración:** quedó en `.criterio/legal/20710000019/config.json`, con los umbrales de `config.example.json`: 60 días para vencimientos, 30 para preavisos y 30 de antigüedad máxima del certificado. El estado se guarda en `estado-legal/20710000019-banco-ribera`.
- **Términos:** la versión 1.2 quedó aceptada a nombre de José Francisco Ñáñez, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt`, porque nadie podía autorizarla en esta prueba.

El motor detectó 5 señales:

1. **Firma sin facultad:** 1. El motor no dice cuál es en la salida que vi; el detalle sale con `authority-check`.
2. **Obligación vencida (CTR-704):** el informe de agosto venció el 2026-09-05 y no hay evidencia en `40-ejecucion/`.
3. **Preaviso (CTR-704):** el límite para avisar la no renovación es el 2026-11-01, en 26 días, y nadie ha decidido.
4. **Garantía faltante:** 1. Tampoco sé cuál es; el detalle sale con `contract-execution`.
5. **Registro distinto del contrato:** 1. El detalle sale con `contract-register`.

Por mi cuenta, en la ficha de CTR-702 puse el informe final y el acta de liquidación el 2027-12-31, la terminación que fija el otrosí OT-1. El contrato dice solo "a la terminación".

Sobre CTR-705: un acta de comité del 2026-09-18 decide renovarlo. Esa decisión está en su ficha; no la tomé yo.

El calendario completo está en `estado-legal/20710000019-banco-ribera/contratos/reporte-obligations-calendar.md`. Lo que te mostré quedó guardado en `estado-legal/20710000019-banco-ribera/corridas/salida-legal-setup.md`, y la corrida quedó registrada como `2026-10-06-legal-setup-1`.