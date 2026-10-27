# /criterio-legal:legal-setup legal/20790000014-comercial-control-sur

La instalación de Fidel quedó lista para Comercial Control Sur (RUC 20790000014). Procesé los 6 contratos y el calendario salió sin nada abierto que atender.

**Lo que había en la carpeta**
- Hay 6 contratos (CTR-901 a CTR-906), el registro de contratos y la matriz de atribuciones, y nada fuera de la estructura recomendada.
- También hay carpetas de políticas, normativa, canal de denuncias y cumplimiento de 2026-07 a 2026-09. Esas son de Constanza, no las toqué.

**Las preguntas**
Nadie contestó, así que tomé la respuesta sugerida a partir de los documentos:
- **Entidad:** Comercial Control Sur, país PE, moneda PEN (los contratos dicen PEN).
- **Avisos:** 60 días para vencimientos y 30 para preavisos, los de `config.example.json`.
- **Certificado de la contraparte:** antigüedad máxima de 30 días, también del ejemplo.
- **Estado:** `estado-legal/20790000014-comercial-control-sur`, fuera de los documentos.
- **Feriados:** lista vacía; no inventé los de Perú.
- **Marca `_CRITERIO_LEGAL.txt`:** no la dejé, porque nadie autorizó escribir dentro de los documentos.

**Los términos**
Los mostré tal cual (v1.2) y quedaron aceptados a nombre de José Francisco Ñáñez el 2026-10-06. El comprobante, en Markdown y PDF, está en `.criterio/terminos/aceptacion-criterio-legal-0.10.0-2026-10-06.md` y `.pdf`.

**Los contratos**
La configuración validó sin problemas y las 6 fichas no traen `record_issues`. El cálculo no dio ninguna señal.

**El calendario (corte 2026-10-06)**
Estas son las fechas que muestra el reporte:

| Fecha | Contrato | Qué | Días | Evidencia |
|---|---|---|---|---|
| 2026-09-30 | CTR-901 | Obligación OBL-3, reporte de operaciones al oficial de cumplimiento | -6 | entregada el 2026-09-30 |
| 2026-11-20 | CTR-905 | Terminación y obligación OBL-2 (informe final y acta de liquidación) | 45 | ninguna |
| 2026-12-31 | CTR-903 | Terminación y obligación OBL-2 (informe final y acta de liquidación) | 86 | ninguna |

El reporte completo está en `estado-legal/20790000014-comercial-control-sur/contratos/reporte-obligations-calendar.md`.

**Una dificultad**
En CTR-906 la cláusula 5 dice «el de agosto, a más tardar el 2026-07-06». Registré la fecha tal como está escrita; la dejo como duda para una persona.

**Lo que no revisé**
No corrí authority-check ni contract-execution. Las facultades de firma y los pagos contra lo pactado quedan pendientes de esos comandos.

La corrida quedó registrada como `2026-10-06-legal-setup-1`, con la salida en `estado-legal/20790000014-comercial-control-sur/corridas/salida-legal-setup.md`.