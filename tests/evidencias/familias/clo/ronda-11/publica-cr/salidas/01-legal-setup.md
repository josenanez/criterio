# /criterio-legal:legal-setup legal/3101399101-instituto-publico-de-la-meseta

La instalación para el Instituto Público de la Meseta quedó terminada y la corrida está registrada. Procesé los 6 contratos y no encontré fichas con problemas.

- **Configuración:** quedó en `.criterio/legal/3101399101-instituto-publico-de-la-meseta/config.json`. El motor la validó. Los términos 1.3 quedaron aceptados a nombre de José Francisco Ñáñez el 2026-10-06, con su comprobante en `.criterio/terminos/`.
- **Calendario de vencimientos al 2026-10-06:**
  - CTR-3905 termina el 2026-11-20, a 45 días. Su informe final y acta de liquidación vencen ese mismo día, sin evidencia todavía.
  - CTR-3903 termina el 2026-12-31, a 86 días. Su informe final y acta de liquidación también vencen ese día, sin evidencia todavía.
  - El reporte al oficial de cumplimiento de CTR-3901 venció el 2026-09-30 y sí tiene evidencia entregada.
- **Garantías:** salieron 3 señales.
  - CTR-3901: la garantía es de 3.600.000 y la ley pide al menos 6.000.000.
  - CTR-3903: la garantía es de 2.700.000 y la ley pide al menos 4.500.000.
  - CTR-3906: la garantía es de 9.000.000 y la ley la limita a 7.500.000, sin justificación en el contrato.
  - Tu orden era dejar fuera todo criterio jurídico, así que no califiqué estas señales.
- **Facultades y pagos:** todavía no los corrí. Esos chequeos son de `/authority-check` y `/contract-execution`.

Valores que puse porque nadie respondió, para que los revises:
- **Umbral de garantía:** `public_procurement.guarantee_threshold` quedó en `null`, porque el umbral solo se pide para Ecuador y Chile.
- **Feriados:** la lista de Costa Rica quedó vacía. No los tengo y no quise inventarlos.
- **Marca de la carpeta:** no dejé `_CRITERIO_LEGAL.txt` en los documentos, porque nadie lo autorizó.
- **Otros valores:** los días de aviso (60 de vencimiento y 30 de preaviso), la antigüedad máxima del certificado (30 días) y el resto vienen de `config.example.json`.

Archivos, bajo `estado-legal/3101399101-instituto-publico-de-la-meseta/`:
- `contratos/reporte-obligations-calendar.md`
- `corridas/salida-legal-setup.md`