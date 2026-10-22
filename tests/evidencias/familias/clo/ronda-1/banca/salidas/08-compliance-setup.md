# /criterio-compliance:compliance-setup legal/900123456-banco-andino

Constanza quedó instalada sobre Banco Andino (NIT 900123456), con el primer estado de 2026-09 y la corrida registrada. Se revisaron las 10 obligaciones de la matriz contra su evidencia, y el motor levantó 4 señales.

**Lo que encontró**
- **OB-09, Reporte mensual de quejas** (Diana Cruz): venció el 2026-10-05 y no hay evidencia. Está vencida hace 1 día.
- **Informe declarado contra evidencia:** el informe del 2026-10-05, que presenta Andrés Vela, declara el periodo «cumplido». Pero hay señales abiertas que ese estado no explica.
- **OB-12, Registro de conflictos de interés:** no tiene responsable en la matriz. Tiene evidencia, pero la fila queda incompleta.
- **Norma N-2026-05 sin evaluar:** es la cuarta señal (`regulatory_change_unassessed`). El reporte de estado no la detalla; sale en `/regulatory-watch`.
- **Avance con evidencia:** 72,73 % ponderado por criticidad.

**Lo que hice**
- **Preguntas:** hice 2, sin interfaz y con la respuesta sugerida por los documentos. El periodo es 2026-09 (el último con informe) y puse la marca `_CRITERIO_LEGAL.txt` en la carpeta.
- **Términos:** aceptados a nombre de José Francisco Ñáñez, 2026-10-06 (versión 1.2 de los términos, familia 0.7.0). El texto corto está en la salida registrada y los comprobantes están en `.criterio/terminos/`.
- **Configuración:** `legal.py config` no crea el archivo, solo lo valida, y el comando pedía que el setup lo dejara escrito. Escribí yo `.criterio/cumplimiento/900123456/config.json`. Tomé los plazos de la configuración de Fidel: 15 días para el canal de denuncias y 30 para evaluar una norma.

**Archivos**
- **Reporte:** `estado-legal/900123456-banco-andino/cumplimiento/2026-09/reporte-compliance-status.md`
- **Ficha del periodo:** `estado-legal/900123456-banco-andino/cumplimiento/2026-09/ficha.json`
- **Salida de la corrida:** `estado-legal/900123456-banco-andino/corridas/salida-compliance-setup.md`