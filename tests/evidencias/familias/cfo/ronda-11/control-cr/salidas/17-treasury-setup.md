# /criterio-treasury:treasury-setup finanzas/3101733015-comercial-control-de-costa-rica

Áurea quedó instalada sobre Comercial Control de Costa Rica (3101733015), y la caja de las dos cuentas está por encima de su mínimo en septiembre de 2026. El motor no marcó ninguna señal.

- **Carpeta:** usé la del argumento, `finanzas/3101733015-comercial-control-de-costa-rica`. No corrí `buscar-raiz`.
- **Lo que hay:** 2 cuentas con extracto, el programa de pagos, la política de tesorería y el registro de deuda. También están la matriz de firmas y los covenants.
- **Configuración:** quedó en `.criterio/tesoreria/3101733015/config.json`, en la misma carpeta de estado que usan Clara y Tomás. La entidad, el periodo y la moneda funcional (CRC) vienen de la configuración de Clara. No declaré cuentas en otra moneda y puse los umbrales de `config.example.json`: 10 % de desviación, 30 días de vencimiento y 10 % de margen del covenant. Pasa la validación.
- **Términos:** los mostré tal cual y registré la aceptación de José Francisco Ñáñez, con fecha 2026-10-06, para la versión 1.0.0 (términos 1.3). El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-1.0.0-2026-10-06.md`, con su PDF.

Las cifras son las del reporte `cash-position`:

| Cuenta | Saldo | Mínimo | Proyectado | Desviación |
|---|---|---|---|---|
| andino-10701 | 4.124.700,00 | 1.462.350,00 | 4.124.700,00 | 0,00 % |
| pacifico-10702 | 18.000.000,00 | 8.400.000,00 | 18.000.000,00 | 0,00 % |

La caja consolidada es 22.124.700,00 CRC.

No hice ninguna pregunta, porque no había quien contestara. El reporte quedó en `estado-finanzas/3101733015-comercial-control-de-costa-rica/tesoreria/2026-09/reporte-cash-position.md`.

La corrida quedó registrada como `2026-10-06-treasury-setup-1`, con lo que le mostré en `corridas/salida-treasury-setup.md`.

No marqué la raíz con `marcar-raiz`: no hacía falta porque la carpeta ya tiene la estructura de Clara y Tomás, y en esta sesión nadie lo autorizó. No moví ni creé nada dentro de la carpeta de documentos.