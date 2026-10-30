# /criterio-treasury:treasury-setup finanzas/155791002-2-2017-almacenes-del-canal

## Listo — Almacenes del Canal · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-7901 y pacifico-7902). Hay programa de pagos, política de tesorería y registro de deuda.
**Términos:** José Francisco Ñáñez los aceptó para la versión 1.0.0 (términos 1.3). Los comprobantes quedaron en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md` y `.pdf`.

Usé la entidad, la moneda funcional (USD), el periodo y el estado de la configuración de Clara. No declaré cuentas en otra moneda. Los umbrales son los de `config.example.json`: 10 % de desviación, 30 días y 10 % de margen del covenant. Son configuración, no norma. No marqué la raíz con `_CRITERIO_FINANZAS.txt`, porque nadie lo autorizó.

### La posición de caja (corte 2026-09-30)

**Caja consolidada:** 45,859.50 USD

| Cuenta | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|
| andino-7901 | 859.50 | -1,070.25 | 859.50 | 0.00 |
| pacifico-7902 | 45,000.00 | 21,000.00 | 58,500.00 | -23.08 |

**Lo que hay que atender:** pacifico-7902 quedó 13,500.00 por debajo de la proyección, un 23.08 %, más que el umbral del 10 %. Las citas están en `2026-09/20-bancos/pacifico-7902/extracto.xlsx` (fila 3) y `2026-09/60-tesoreria/flujo-proyectado.xlsx` (fila 3).

El cálculo del periodo registró dos señales más: un pago sin aprobación (`payment_without_approval`) y una obligación cerca de su vencimiento (`maturity_near`). El reporte de caja no las detalla. Se ven con `/payment-check` y `/debt-watch`.

Todo lo que llegó se procesó. No hice preguntas en esta corrida.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.

Lo que está en disco:
- **Configuración:** `.criterio/tesoreria/155791002-2-2017/config.json`.
- **Reporte:** `estado-finanzas/155791002-2-2017-almacenes-del-canal/tesoreria/2026-09/reporte-cash-position.md`.
- **Salida de esta corrida:** `estado-finanzas/155791002-2-2017-almacenes-del-canal/corridas/salida-treasury-setup.md`.
- **Corrida registrada:** `2026-10-06-treasury-setup-1`.