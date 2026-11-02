# /criterio-legal:legal-setup legal/88612904-4-distribuidora-del-ybytyruzu-sintetica

Fidel quedó instalado sobre Distribuidora del Ybytyruzú Sintética (RUC 88612904-4, Paraguay, PYG). Procesó los 6 contratos y registró la corrida con 5 señales.

**Qué quedó hecho**
- **Carpeta:** el inventario encontró 6 contratos, el registro y la matriz de atribuciones. Nada estaba fuera de la estructura.
- **Configuración:** está en `.criterio/legal/88612904-4/config.json` y el motor la validó sin problemas.
- **Términos:** acepté los términos 1.3 a nombre de José Francisco Ñáñez, con fecha 2026-10-06. Los comprobantes quedaron en `.criterio/terminos/`.
- **Fichas:** escribí las 6 fichas en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/contratos/`. `compute` no reportó `record_issues`.

**Lo que la sesión sin interfaz decidió por la persona**
- Tomé los umbrales de `config.example.json` (60, 30 y 30 días).
- Marqué la entidad como no pública.
- Dejé la lista de feriados vacía, porque el feriado del ejemplo es de Colombia.
- No marqué la carpeta raíz con `_CRITERIO_LEGAL.txt`, porque nadie contestó la pregunta.

**Calendario (al 2026-10-06)**
- **CTR-4503** vence el 2026-11-25, en 50 días, y no tiene decisión de renovar o terminar. Es la única señal que muestra el reporte.
- **CTR-4505** termina el 2026-11-20, en 45 días. Un acta del 2026-09-18 ya decidió renovarlo.
- **CTR-4501:** el reporte al oficial de cumplimiento (OBL-3) se entregó el 2026-09-30, y el calendario lo muestra con la evidencia del documento.

**Las 5 señales**
El motor las contó, pero no escribió su detalle. La salida solo trae los totales, y el detalle está en `contratos/resultados.json`, que no abrí:
- una firma sin facultad
- un contrato por vencer
- un pago después de la terminación
- una garantía que vence antes de lo exigido
- un registro que no cuadra

El reporte `obligations-calendar` solo muestra los vencimientos. Para ver las otras cuatro señales, corre `authority-check`, `contract-execution` y `contract-register`.

El texto que te mostré quedó en `estado-legal/88612904-4-distribuidora-del-ybytyruzu-sintetica/corridas/salida-legal-setup.md`, y la corrida es `2026-10-06-legal-setup-1`.