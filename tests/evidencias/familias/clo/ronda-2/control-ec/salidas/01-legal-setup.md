# /criterio-legal:legal-setup legal/1790000001001-comercial-control

Fidel quedó instalado sobre Comercial Control (RUC 1790000001001, Ecuador, USD). Procesó los 6 contratos y el calendario no marca nada abierto.

**Instalación**
- **Carpeta y configuración:** usé la carpeta del argumento. La configuración está en `.criterio/legal/1790000001001/config.json` y el motor la validó sin problemas.
- **Documentos:** estaban el registro y la matriz de atribuciones, y no había nada fuera de la estructura.
- **Preguntas:** nadie respondió, así que tomé las respuestas sugeridas: avisos de 60 y 30 días y certificado de máximo 30 días (los de `config.example.json`), y el estado en `estado-legal/1790000001001-comercial-control`.
- **Marca de la raíz:** no escribí `_CRITERIO_LEGAL.txt`, porque nadie dio permiso. No toqué nada dentro de los documentos.
- **Feriados:** la lista quedó vacía; el feriado del ejemplo era de Colombia.
- **Términos:** versión 1.2, aceptada a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante está en `.criterio/terminos/` (`.md` y `.pdf`).

**Lo que encontró**
- **Fichas:** convertí 30 documentos (0 ilegibles) y armé las 6 fichas en `estado-legal/1790000001001-comercial-control/contratos/`. El motor no reportó `record_issues`.
- **Señales:** `compute` devolvió 0, así que no hay firmas sin facultad ni pagos por fuera de lo pactado que marcar. No hay exportación de pagos cargada en este comando.
- **CTR-601:** su reporte al oficial de cumplimiento vencía el 2026-09-30 y ya tiene evidencia entregada ese día.
- **CTR-604:** el límite de su preaviso es el 2026-11-01, a 26 días. El comité decidió renovarlo el 2026-09-25.
- **Terminaciones en 90 días:** CTR-605 el 2026-11-20, y CTR-603 y CTR-604 el 2026-12-31. Cada una trae su informe final y acta de liquidación sin evidencia todavía.

**Para revisar**
- **Fuentes del calendario:** el reporte del motor dice «Sin documentos citados» en Fuentes, aunque las fichas sí traen sus citas. Es un comportamiento del motor y lo dejo así.
- **Valores en CTR-602:** la ficha toma el valor del contrato (60.000) más el otrosí (15.000), que suman los 75.000 del registro. Esto lo calcula el motor; no lo concilié a mano.

La corrida quedó registrada como `2026-10-06-legal-setup-1`, con lo mostrado en `estado-legal/1790000001001-comercial-control/corridas/salida-legal-setup.md`. El reporte del calendario está en `estado-legal/1790000001001-comercial-control/contratos/reporte-obligations-calendar.md`.