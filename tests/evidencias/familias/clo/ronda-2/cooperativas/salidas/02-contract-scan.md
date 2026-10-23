# /criterio-legal:contract-scan 

Se procesaron los 7 contratos (CTR-201 a CTR-207) y salieron 4 señales. Las fichas ya existían desde `legal-setup` y coinciden con los documentos, así que no las reescribí. El motor no reportó campos faltantes ni archivos sin procesar.

| # | Contrato | Señal | Detalle |
|---|---|---|---|
| 1 | CTR-202 | Lo pagado supera el valor del contrato más sus otrosíes | 105,999.99 pagados contra 100,000.00; exceso de 5,999.99. |
| 2 | CTR-203 | El registro lo reporta vigente y ya terminó | Terminó el 2026-08-31. |
| 3 | CTR-207 | Está en la carpeta pero no en el registro | — |
| 4 | CTR-204 | Certificado de la contraparte antiguo al firmar | Tenía 75 días cuando se firmó. |

El reporte completo está en `estado-legal/1790012345001-cooperativa-sierra-alta/contratos/reporte-contract-scan.md`. Lo que te mostré quedó guardado en `corridas/salida-contract-scan.md` y la corrida quedó registrada como `2026-10-06-contract-scan-1`.

- **Términos:** ya estaban vigentes (versión 1.2, aceptados por José Francisco Ñáñez el 2026-10-06), así que no hubo que registrarlos de nuevo.
- **Fecha:** usé `--today 2026-10-06` en cada llamada que la acepta.
- **Preguntas:** no hubo ninguna.