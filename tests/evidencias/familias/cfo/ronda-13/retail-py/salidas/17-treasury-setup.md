# /criterio-treasury:treasury-setup finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica

Áurea queda instalada para tesorería 2026-09 y la corrida está registrada. La primera posición de caja encontró una cuenta bajo su mínimo.

**Lo que miré:** 2 cuentas con extracto (andino-13701, pacifico-13702). También hay programa de pagos, política y registro de deuda.

**Términos:** José Francisco Ñáñez los aceptó para la versión 1.2.0, con fecha 2026-10-06. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.2.0-2026-10-06.md` y en `.pdf`.

**Caja consolidada:** 379.900.000,00 PYG.

| Cuenta | Saldo | Mínimo | Proyectado | Desviación % |
|---|---|---|---|---|
| andino-13701 | 79.900.000,00 | 105.880.000,00 | 79.900.000,00 | 0,00 |
| pacifico-13702 | 300.000.000,00 | 140.000.000,00 | 300.000.000,00 | 0,00 |

**Lo que hay que atender:** andino-13701 queda 25.980.000,00 por debajo del mínimo de la política (`2026-09/20-bancos/andino-13701/extracto.pdf`, fila 16).

El cálculo también marcó un pago sin aprobación y una obligación con vencimiento cercano. No los detallé porque no hacen parte del reporte de posición de caja. Se ven con `payment-check` y `debt-watch`.

Como nadie podía contestar en esta prueba, tomé estas decisiones:
- **Carpeta raíz:** la del argumento. No la marqué con `_CRITERIO_FINANZAS.txt` porque no hubo un sí.
- **Estado:** `estado-finanzas/88612904-4-distribuidora-del-ybytyruzu-sintetica`.
- **Otras monedas:** ninguna cuenta. El extracto de pacifico-13702 trae PYG, y el de andino-13701 es un PDF que no verifiqué.
- **Umbrales:** los de `config.example.json` (10 % de desviación, 30 días de vencimiento, 10 % de margen de covenant).

El reporte está en `estado-finanzas/…/tesoreria/2026-09/reporte-cash-position.md`. La configuración está en `.criterio/tesoreria/88612904-4/config.json`.

Áurea vuelve cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.