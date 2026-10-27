# /criterio-treasury:treasury-setup finanzas/BVA150301K21-banco-valle-de-anahuac

## Listo — Banco Valle de Anáhuac (BVA150301K21) · tesorería 2026-09

**Lo que miré:** 2 cuentas con extracto (andino-1301, pacifico-1302). Hay programa de pagos, política y registro de deuda.
**Términos:** José Francisco Ñáñez los aceptó para la versión 0.11.0, con fecha 2026-10-06. Los tomé de tu argumento, sin preguntar. El comprobante está en `.criterio/terminos/aceptacion-criterio-treasury-0.11.0-2026-10-06.md`.

La configuración quedó en `.criterio/tesoreria/BVA150301K21/config.json` y el motor la validó sin problemas. Asumí lo siguiente por falta de respuestas:
- **Moneda:** pacifico-1302 en USD, porque su extracto trae esa columna.
- **Umbrales:** los de `config.example.json`, que son configuración y no norma.
- **Estado:** `estado-finanzas/BVA150301K21-banco-valle-de-anahuac`, el mismo de Clara y Tomás.

**Primera posición de caja (corte 2026-09-30):**
- **Caja consolidada:** 11,341,552.00.
- **andino-1301 (MXN):** saldo 241,552.00, sobre su mínimo de 100,776.00 y igual a lo proyectado.
- **pacifico-1302 (USD):** saldo 600,000.00, sobre su mínimo de 280,000.00, pero 180,000.00 por debajo de los 780,000.00 proyectados (-23.08%, sobre el umbral del 10%).
- **Exposición en USD:** equivale a 11,100,000.00 MXN con la tasa de la política y supera el límite de 5,550,000.00.

El motor también detectó 1 señal de pago sin aprobación (`payment_without_approval`). No está en este reporte; la detalla `/payment-check`.

**Archivos:**
- El reporte está en `estado-finanzas/BVA150301K21-banco-valle-de-anahuac/tesoreria/2026-09/reporte-cash-position.md`.
- Lo que te mostré, completo, está en `corridas/salida-treasury-setup.md`, en la misma carpeta de estado.
- La corrida quedó registrada como `2026-10-06-treasury-setup-1`.

**Cuándo vuelvo:** cuando haya pagos programados en los próximos días, cuando una obligación entre en su ventana de vencimiento y una vez por semana.