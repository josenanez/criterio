# /criterio-compliance:compliance-setup legal/900000001-distribuidora-control

No pude dejar instalada la configuración de Constanza, y paro aquí como pediste. No inventé el archivo de configuración.

- **Qué falta:** el motor no creó `.criterio/cumplimiento/900000001/config.json`. El paso 4 corrió `init --state estado-legal/900000001-distribuidora-control` y respondió `{"listo": true}`, pero no escribió ninguna configuración. El comando `config` tampoco la crea: exige `--config` y respondió «`.criterio/cumplimiento/900000001/config.json` no existe: corre el setup del agente». Ningún comando del motor escribe ese archivo. Por eso `aceptar`, `convertir`, `compute`, `reporte` y `corrida` no tienen sobre qué correr, y no los ejecuté.
- **Lo que sí hay:** la carpeta `legal/900000001-distribuidora-control` tiene 57 documentos, sin cambios, borrados ni archivos fuera de lugar. Son 6 contratos (CTR-501 a CTR-506), 3 periodos de cumplimiento (2026-07, 2026-08 y 2026-09), las políticas, la normativa y el canal de denuncias. La matriz tiene 8 obligaciones, OB-01 a OB-08. Cada una trae fuente, responsable, periodicidad, fecha límite, evidencia y criticidad.
- **Lo que no llegué a hacer:**
  - Las preguntas del paso 3, incluida la aceptación de términos a nombre de José Francisco Ñáñez.
  - La marca `_CRITERIO_LEGAL.txt`.
  - El primer estado y el reporte `compliance-status`.
  - El registro de la corrida, que también exige la configuración.
- **Ya existía antes:** la configuración de Fidel (`.criterio/legal/900000001/config.json`) con los términos de esa familia aceptados el 2026-10-06. No sirve para Constanza: es otro plugin y otra ruta.
- **Qué se necesita:** que el plugin `criterio-compliance` traiga un comando que cree la configuración, o que alguien con acceso al motor la genere. Con ese archivo, repito el flujo desde el paso 4.