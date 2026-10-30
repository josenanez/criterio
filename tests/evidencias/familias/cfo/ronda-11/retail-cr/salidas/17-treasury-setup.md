# /criterio-treasury:treasury-setup finanzas/3101612904-almacenes-de-la-meseta

## Listo — Almacenes de la Meseta (3101612904) · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-10301, pacifico-10302). También encontré el programa de pagos, la política de tesorería y el registro de deuda. No hice preguntas: usé los documentos y la configuración de Clara (CRC, NIIF).
**Términos:** José Francisco Ñáñez los aceptó el 2026-10-06 para la versión 1.0.0. El comprobante quedó en `.criterio/terminos/`.
**Configuración:** `.criterio/tesoreria/3101612904/config.json`. Usé los umbrales de ejemplo (10 % de desviación, 30 días de vencimiento, 10 % de margen del covenant). El estado quedó en `estado-finanzas/3101612904-almacenes-de-la-meseta`.

**Posición de caja al 2026-09-30:**

| Cuenta | Saldo | Mínimo de la política |
|---|---|---|
| andino-10301 | 18.942.750,00 CRC | 23.481.300,00 CRC |
| pacifico-10302 | 22.500.000,00 CRC | 10.500.000,00 CRC |

- **Caja consolidada:** 41.442.750,00 CRC.
- **Alerta:** andino-10301 está 4.538.550,00 CRC por debajo del mínimo que fija la política. Su saldo coincide con lo proyectado.
- **Otras señales:** el motor encontró 3 en total. Además de la caja, hay un pago sin aprobación y un vencimiento cercano. El reporte de caja solo detalla la primera; las otras dos las detallan `payment-check` y `debt-watch`.

**Lo que no hice:**
- No marqué la carpeta raíz con `_CRITERIO_FINANZAS.txt`. Eso necesita que alguien lo autorice y nadie podía contestar.
- No hay cuentas en otra moneda: los extractos traen la columna de moneda.

El reporte completo está en `estado-finanzas/3101612904-almacenes-de-la-meseta/tesoreria/2026-09/reporte-cash-position.md`. La salida de esta corrida está en `corridas/salida-treasury-setup.md` y la corrida quedó registrada como `2026-10-06-treasury-setup-1`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.