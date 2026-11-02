# /criterio-compliance:compliance-setup legal/88457812-7-banco-del-tebicuary-sintetico

La instalación para Banco del Tebicuary Sintético (88457812-7) quedó lista, con el periodo 2026-09 evaluado contra la matriz de 10 obligaciones. El informe de cumplimiento declara el periodo «cumplido», pero la evidencia no lo respalda: hay 5 señales abiertas y el avance con evidencia es 65,22 % (ponderado por criticidad).

**Señales del motor**
1. **OB-09, Reporte mensual de quejas:** está vencida desde el 2026-10-05 y no tiene evidencia. La responsable es Rossana Giménez.
2. **Declarado contra evidenciado:** el informe de Hugo Duarte declara el periodo «cumplido», pero las otras 4 señales siguen abiertas.
3. **CTR-4401, obligación OBL-3:** el contrato exige un reporte de operaciones al oficial de cumplimiento (cláusula 7) y la matriz no lo tiene.
4. **OB-11, Monitoreo mensual de listas restrictivas:** su última evidencia es de 2026-07 y no hay evidencia del ciclo anterior.
5. **N-2026-05, Circular sintética 005 de 2026:** está «por evaluar» y no tiene fecha de evaluación en el registro normativo. Esta señal no aparece en la tabla del reporte, que muestra solo 4 filas, aunque el motor contó 5.

**Lo que hice**
- **Configuración:** quedó en `.criterio/cumplimiento/88457812-7/config.json`. Usé los plazos del ejemplo y apunté a las fichas de Fidel (6 contratos).
- **Marca de la carpeta:** dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos. Tomé el sí sugerido porque nadie podía responder.
- **Términos:** quedaron aceptados a nombre de José Francisco Ñáñez. Mi primera llamada a `aceptar` salió sin `--today` y dejó un comprobante con fecha 2026-11-02. La repetí con 2026-10-06; el comprobante de 2026-11-02 sigue en `.criterio/terminos/` y en el registro de aceptaciones.
- **Ficha del periodo:** `estado-legal/88457812-7-banco-del-tebicuary-sintetico/cumplimiento/2026-09/ficha.json` registra el estado declarado y las 2 preguntas que tomé como respondidas.
- **Reporte:** el motor escribió `cumplimiento/2026-09/reporte-compliance-status.md` en esa misma carpeta de estado, y es el que está al final de `corridas/salida-compliance-setup.md`.
- **Corrida:** quedó registrada como `2026-10-06-compliance-setup-1`.

No interpreté ninguna norma ni califiqué el informe.