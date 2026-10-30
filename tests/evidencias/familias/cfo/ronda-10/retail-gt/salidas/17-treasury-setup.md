# /criterio-treasury:treasury-setup finanzas/87145200-almacenes-del-altiplano

Áurea quedó instalada para Almacenes del Altiplano (periodo 2026-09), con los términos aceptados y la primera posición de caja calculada.

**Lo que se hizo**
- **Carpeta:** `finanzas/87145200-almacenes-del-altiplano`, la única candidata. No la marqué con `_CRITERIO_FINANZAS.txt` porque nadie lo autorizó.
- **Inventario:** 2 cuentas con extracto (andino-8701 y pacifico-8702), y la carpeta trae el programa de pagos, la política, el registro de deuda y los covenants.
- **Configuración:** `.criterio/tesoreria/87145200-almacenes-del-altiplano/config.json`. La entidad, la moneda funcional (GTQ) y la aprobadora (Sofía León) salen de la configuración de Clara. Los umbrales son los de `config.example.json` (10 %, 30 días, 10 %), que son configuración y no norma. La moneda de pacifico-8702 la tomó el motor del extracto, así que no declaré cuentas en otra moneda.
- **Términos:** versión 1.0.0, aceptados a nombre de José Francisco Ñáñez con fecha 2026-10-06. Los comprobantes en Markdown y PDF están en `.criterio/terminos/`.
- **Estado:** `estado-finanzas/87145200-almacenes-del-altiplano`. La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con la salida en `corridas/salida-treasury-setup.md`.

**La caja (cifras del motor)**
- La caja consolidada es 3,000,278.40.
- andino-8701 tiene 228,278.40 GTQ contra un mínimo de 102,139.20.
- pacifico-8702 tiene 360,000.00 USD contra un mínimo de 168,000.00.
- Las dos cuentas coinciden con su proyección (desviación 0.00 %).
- La posición en USD equivale a 2,772,000.00 GTQ con la tasa de la política, sobre el límite de 1,386,000.00. Es la señal `fx_exposure_over_limit` (exposición en otra moneda sobre su límite) y es la única que muestra el reporte de posición de caja.

El cálculo completo dio 3 señales. Las otras dos son un pago sin aprobación (`payment_without_approval`) y un vencimiento cercano (`maturity_near`). Quedaron en `tesoreria/2026-09/resultados.json` y las verás con los comandos de pagos y de deuda.

El reporte completo está en `estado-finanzas/87145200-almacenes-del-altiplano/tesoreria/2026-09/reporte-cash-position.md`.