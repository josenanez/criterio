# /criterio-compliance:compliance-setup legal/76089001-4-minera-atacama-norte

Constanza quedó instalada sobre Minera Atacama Norte (76089001-4). El reporte del periodo 2026-09 dejó tres cosas por atender.

Ya había una configuración de Fidel para esta entidad. Dejé la de Constanza aparte, en `.criterio/cumplimiento/76089001-4/config.json`. Dato interno: el motor contó 5 señales en `compute`. El reporte de estado muestra 3. Las otras 2 son un caso del canal vencido y una norma sin evaluar, que corresponden a los reportes de casos y de normativa.

**Lo que hice**
- **Carpeta:** usé la del argumento, `legal/76089001-4-minera-atacama-norte`, sin buscarla. El inventario dio 59 documentos, 6 contratos y 3 periodos, sin nada fuera de lugar ni ilegible.
- **Configuración:** el periodo es 2026-09 y el resto son los plazos por defecto (canal de denuncias 15 días, normas nuevas 30 días). Las fichas de Fidel las tomé de `estado-legal/76089001-4-minera-atacama-norte/contratos`.
- **Términos:** quedaron aceptados por José Francisco Ñáñez el 2026-10-06 (versión 1.2), con el comprobante en `.criterio/terminos/`.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en los documentos, porque nadie respondió esa pregunta. Quedó registrada sin respuesta.
- **Estado declarado:** el informe del 2026-10-05 dice «con observaciones». Lo anoté en la ficha del periodo, en `estado-legal/76089001-4-minera-atacama-norte/cumplimiento/2026-09/ficha.json`.

**Lo que hay que atender**
1. **OB-10** (Declaración mensual de origen de fondos): la matriz la marca como cumplida, pero no hay ningún archivo que empiece por OB-10. Responsable: Daniela Fuentes.
2. **CTR-1101, OBL-3** (Reporte de operaciones al oficial de cumplimiento): el contrato la exige en la cláusula 7 y la matriz no la tiene.
3. **OB-11** (Monitoreo mensual de listas restrictivas): la última evidencia es de 2026-07. Responsable: Ignacio Pizarro.

El avance con evidencia, ponderado por criticidad, es 68,18 %. De las 10 obligaciones, 6 están cumplidas con evidencia, 3 están en plazo y 1 está cumplida sin evidencia (OB-10).

En la matriz, OB-02 tiene el límite escrito como «D+5», distinto del formato «día N» de las demás, y no existe OB-09. No corregí ninguna de las dos cosas.

La corrida quedó registrada como `2026-10-06-compliance-setup-1`.

Archivos en `estado-legal/76089001-4-minera-atacama-norte/`:
- `cumplimiento/2026-09/reporte-compliance-status.md`
- `corridas/salida-compliance-setup.md`