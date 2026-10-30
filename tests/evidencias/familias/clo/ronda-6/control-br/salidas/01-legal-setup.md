# /criterio-legal:legal-setup legal/40217355000151-comercial-controle-paulista

Fidel quedó instalado sobre Comercial Controle Paulista (CNPJ 40217355000151, BR, BRL). Procesé los 6 contratos, CTR-1801 a CTR-1806. El calendario no tiene nada abierto con corte al 2026-10-06.

**Qué quedó hecho**
- **Inventario:** están el registro y la matriz de atribuciones, y nada está fuera de la estructura recomendada.
- **Configuración:** la escribí con las respuestas sugeridas por los documentos, sin preguntar a nadie:
  - avisos de 60 días para el vencimiento y de 30 para el preaviso;
  - certificado de la contraparte con máximo 30 días de antigüedad;
  - estado en `estado-legal/40217355000151-comercial-controle-paulista`.
- **Términos:** versión 1.3, aceptada por José Francisco Ñáñez el 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Raíz sin marcar:** no dejé `_CRITERIO_LEGAL.txt` en la carpeta de documentos, porque en esta prueba nadie lo autorizó.
- **Fichas:** las 6 pasaron la validación sin `record_issues`.
- **Corrida:** quedó registrada como `2026-10-06-legal-setup-1`, con 0 hallazgos. Lo que te mostré está en `corridas/salida-legal-setup.md`.

**Calendario (entre 30 días atrás y 90 adelante)**

| Fecha | Contrato | Qué | Días |
|---|---|---|---|
| 2026-09-30 | CTR-1801 | OBL-3, relatório de operações al responsable de compliance | -6 (ya hay evidencia entregada) |
| 2026-11-20 | CTR-1805 | terminación y OBL-2, relatório final | 45 |
| 2026-12-31 | CTR-1803 | terminación y OBL-2, relatório final | 86 |

La decisión de renovar o terminar es de una persona. En CTR-1805 hay un acta del comité del 2026-09-18 que decidió renovarlo.

Este comando no cruzó firmas contra la matriz de atribuciones ni pagos contra lo pactado. Eso lo hacen `/authority-check` y `/contract-execution`.