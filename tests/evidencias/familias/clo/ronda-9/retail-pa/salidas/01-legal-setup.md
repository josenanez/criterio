# /criterio-legal:legal-setup legal/155791002-2-2017-almacenes-del-canal

Fidel quedó instalado sobre Almacenes del Canal (RUC 155791002-2-2017, Panamá, USD). Procesó los 7 contratos y registró la corrida (`2026-10-06-legal-setup-1`).

**Qué se hizo**
- Nadie respondió preguntas, así que tomé cada respuesta de los documentos o de los valores de `config.example.json`.
- La configuración quedó en `.criterio/legal/155791002-2-2017/config.json` y el motor la validó sin problemas.
- José Francisco Ñáñez aceptó los términos (versión 1.3) con fecha 2026-10-06. Los comprobantes están en `.criterio/terminos/`.
- El estado quedó en `estado-legal/155791002-2-2017-almacenes-del-canal`, fuera de la carpeta de documentos.
- Dejé la lista de feriados vacía, porque el ejemplo trae uno de Colombia. No dejé la marca `_CRITERIO_LEGAL.txt`, porque nadie pudo autorizarla.
- No moví ni creé nada dentro de los documentos.

**Lo que encontró (5 señales)**
- **Firma sin facultad:** en CTR-3001, Abdiel Moreno firmó por 360,000.00 y la matriz de atribuciones no le da facultad para ese tipo y monto.
- **Vencimiento:** CTR-3003 vence el 2026-11-25, en 50 días, sin decisión de renovar o terminar. Es la única señal que sale en el calendario.
- **Póliza corta:** en CTR-3001, la póliza de cumplimiento vence el 2027-05-31 y el contrato la exige hasta el 2027-07-31.
- **Fuera del registro:** CTR-3007 está en la carpeta pero no en el registro.
- **Valor distinto:** CTR-3002 figura con 270,000.00 en el registro y 225,000.00 en el documento.

El reporte del calendario es `estado-legal/155791002-2-2017-almacenes-del-canal/contratos/reporte-obligations-calendar.md`. Lo que le mostré a la persona queda en `corridas/salida-legal-setup.md`.

**Pendiente:** el cruce de pagos contra lo pactado no se hizo en este comando. Corresponde a `contract-execution`, con el archivo `10-registro/pagos-2026-09-30.csv`.