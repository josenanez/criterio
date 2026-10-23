# /criterio-compliance:compliance-setup legal/0990054321001-minera-condor

Constanza quedó instalada sobre Minera Cóndor (EC) y ya corrió el primer estado del periodo 2026-09. El informe del periodo declara **con observaciones**, y la matriz muestra un **68.18 % de avance con evidencia** (ponderado por criticidad).

- **Configuración:** está en `.criterio/cumplimiento/0990054321001/config.json`, con el periodo 2026-09, el plazo del canal en 15 días y la evaluación de normas en 30.
- **Fichas de Fidel:** las encontré en `estado-legal/0990054321001-minera-condor/contratos`.
- **Marca de la carpeta:** ya tenía `_CRITERIO_LEGAL.txt`, así que no pregunté de nuevo.
- **Términos:** los de la versión 1.2 quedaron aceptados por José Francisco Ñáñez el 2026-10-06, con comprobante en `.criterio/terminos/`.
- **Preguntas:** hice dos, el periodo y la ruta de las fichas, y las respondí con los documentos.
- **Obligaciones:** revisé las 10 de la matriz.

Tres señales aparecen en el reporte:
- **OB-10** (Declaración mensual de origen de fondos) figura cumplida en la matriz, pero no hay evidencia que empiece por OB-10.
- **OBL-3 de CTR-401** (reporte de operaciones al oficial de cumplimiento) es una obligación del contrato 401 que la matriz no tiene.
- **OB-11** (Monitoreo mensual de listas restrictivas) tiene como última evidencia la de 2026-07, y el ciclo anterior no tiene.

El motor cuenta 5 señales, pero el reporte solo lista esas 3. Faltan por mostrar un caso del canal de denuncias vencido y una norma sin evaluar. Quedan en `estado-legal/0990054321001-minera-condor/cumplimiento/2026-09/resultados.json`. No sé por qué el reporte no las incluyó. Lo dejé anotado en la salida de la corrida.

El reporte está en `estado-legal/0990054321001-minera-condor/cumplimiento/2026-09/reporte-compliance-status.md`. Lo que te mostré quedó guardado en `estado-legal/0990054321001-minera-condor/corridas/salida-compliance-setup.md`, y la corrida quedó registrada como `2026-10-06-compliance-setup-1`.